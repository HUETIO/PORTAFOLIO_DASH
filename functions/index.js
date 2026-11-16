const { RecaptchaEnterpriseServiceClient } = require("@google-cloud/recaptcha-enterprise");
const { onRequest } = require("firebase-functions/v2/https");
const { defineSecret, defineString } = require("firebase-functions/params");

const emailjsPrivateKey = defineSecret("EMAILJS_PRIVATE_KEY");
const projectId = defineString("RECAPTCHA_PROJECT_ID", {
  default: "portafoliodash",
});
const siteKey = defineString("RECAPTCHA_ENTERPRISE_CHECKBOX_SITE_KEY", {
  default: "",
});
const emailjsServiceId = defineString("EMAILJS_SERVICE_ID");
const emailjsTemplateId = defineString("EMAILJS_TEMPLATE_ID");
const emailjsPublicKey = defineString("EMAILJS_PUBLIC_KEY");
const allowedOrigins = defineString("SALES_ALLOWED_ORIGINS", {
  default:
    "http://localhost:5173,http://localhost:5174,http://127.0.0.1:5173,http://127.0.0.1:5174",
});
const minimumScore = defineString("RECAPTCHA_MINIMUM_SCORE", {
  default: "0.5",
});

const expectedAction = "SALES_REQUEST";
const allowedServices = new Set([
  "Gestión documental",
  "Desarrollo de software",
  "Inteligencia artificial y machine learning",
  "Blockchain",
  "Operación de minería",
  "Transferencia verificable con hash",
  "Ciberseguridad y control de acceso",
  "Analítica y automatización",
]);
const recaptchaClient = new RecaptchaEnterpriseServiceClient();

function cleanText(value, maxLength) {
  if (typeof value !== "string") return "";
  return value.replace(/[\u0000-\u001f\u007f]/g, " ").trim().slice(0, maxLength);
}

function setCorsHeaders(req, res, allowedOriginList) {
  const origin = req.get("origin");
  if (origin && allowedOriginList.includes(origin)) {
    res.set("Access-Control-Allow-Origin", origin);
    res.set("Vary", "Origin");
  }
  return !origin || allowedOriginList.includes(origin);
}

function sendError(res, status, message) {
  return res.status(status).json({ error: message });
}

exports.submitSalesRequest = onRequest(
  {
    region: "us-central1",
    maxInstances: 3,
    secrets: [emailjsPrivateKey],
  },
  async (req, res) => {
    const originList = allowedOrigins
      .value()
      .split(",")
      .map((origin) => origin.trim())
      .filter(Boolean);

    if (!setCorsHeaders(req, res, originList)) {
      return sendError(res, 403, "Origen no autorizado.");
    }

    if (req.method === "OPTIONS") {
      res.set("Access-Control-Allow-Methods", "POST, OPTIONS");
      res.set("Access-Control-Allow-Headers", "Content-Type");
      return res.status(204).send("");
    }
    if (req.method !== "POST") {
      res.set("Allow", "POST, OPTIONS");
      return sendError(res, 405, "Método no permitido.");
    }
    if (!req.is("application/json") || req.rawBody.length > 12_000) {
      return sendError(res, 413, "Solicitud inválida o demasiado grande.");
    }

    const body = req.body;
    if (!body || typeof body !== "object" || Array.isArray(body)) {
      return sendError(res, 400, "Solicitud inválida.");
    }

    if (cleanText(body.website, 200)) {
      return sendError(res, 400, "No se pudo validar la solicitud.");
    }

    const name = cleanText(body.name, 120);
    const email = cleanText(body.email, 254);
    const phone = cleanText(body.phone, 24);
    const service = cleanText(body.service, 100);
    const message = cleanText(body.message, 3000);
    const token = cleanText(body.recaptchaToken, 4096);
    const validEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    const validPhone = /^[+0-9(). -]{7,24}$/.test(phone);

    if (
      name.length < 2 ||
      !validEmail ||
      !validPhone ||
      !allowedServices.has(service) ||
      body.consent !== true ||
      !token
    ) {
      return sendError(res, 400, "Revisa los datos obligatorios y el consentimiento.");
    }

    const scoreThreshold = Number(minimumScore.value());
    if (!Number.isFinite(scoreThreshold) || scoreThreshold < 0 || scoreThreshold > 1) {
      console.error("RECAPTCHA_MINIMUM_SCORE debe ser un número entre 0 y 1.");
      return sendError(res, 503, "El servicio de verificación no está configurado.");
    }

    const configuredSiteKey = siteKey.value();
    if (!configuredSiteKey) {
      console.error("Falta configurar RECAPTCHA_ENTERPRISE_CHECKBOX_SITE_KEY.");
      return sendError(res, 503, "El servicio de verificación no está configurado.");
    }

    try {
      const [assessment] = await recaptchaClient.createAssessment({
        parent: `projects/${projectId.value()}`,
        assessment: {
          event: {
            token,
            siteKey: configuredSiteKey,
            expectedAction,
            userAgent: req.get("user-agent") || undefined,
            userIpAddress: req.ip || undefined,
          },
        },
      });

      const tokenProperties = assessment.tokenProperties;
      const score = assessment.riskAnalysis?.score;
      if (
        !tokenProperties?.valid ||
        tokenProperties.action !== expectedAction ||
        typeof score !== "number" ||
        score < scoreThreshold
      ) {
        return sendError(
          res,
          403,
          "No se pudo validar la verificación anti-bots. Intenta nuevamente.",
        );
      }
    } catch (error) {
      console.error("No se pudo evaluar el token reCAPTCHA Enterprise.", error);
      return sendError(res, 503, "La verificación anti-bots no está disponible.");
    }

    const privateKey = emailjsPrivateKey.value();
    if (!privateKey) {
      console.error("Falta configurar el secreto EMAILJS_PRIVATE_KEY.");
      return sendError(res, 503, "El servicio de correo no está configurado.");
    }

    try {
      const emailResponse = await fetch("https://api.emailjs.com/api/v1.0/email/send", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        signal: AbortSignal.timeout(10_000),
        body: JSON.stringify({
          service_id: emailjsServiceId.value(),
          template_id: emailjsTemplateId.value(),
          user_id: emailjsPublicKey.value(),
          accessToken: privateKey,
          template_params: {
            customer_name: name,
            customer_email: email,
            customer_phone: phone,
            service_name: service,
            customer_message: message || "Sin comentarios adicionales.",
            submitted_at: new Date().toISOString(),
          },
        }),
      });

      if (!emailResponse.ok) {
        console.error("EmailJS rechazó la solicitud.", {
          status: emailResponse.status,
        });
        return sendError(res, 502, "No se pudo entregar la solicitud por correo.");
      }

      return res.status(200).json({ ok: true });
    } catch (error) {
      console.error("Error al comunicarse con EmailJS.", error);
      return sendError(res, 502, "No se pudo entregar la solicitud por correo.");
    }
  },
);
