<script>
  const ongoingStudies = [
    {
      organization: "Fundación Universitaria del Área Andina",
      status: "EN CURSO · 10.º SEMESTRE",
      title: "Ingeniería de Sistemas",
      detail: "Facultad de Ingeniería de Sistemas y Ciencias Básicas",
    },
    {
      organization: "Fundación Universitaria del Área Andina",
      status: "EN CURSO · 2 MÓDULOS",
      title: "Diplomado en Social Media Management",
    },
  ];

  const education = [
    {
      year: "2016",
      organization: "SENA",
      type: "TÍTULO",
      title: "Cultura de Paz",
    },
    {
      year: "2016",
      organization: "SENA",
      type: "TÉCNICO",
      title: "Mantenimiento de Equipos de Cómputo",
    },
    {
      year: "2016",
      organization: "SENA",
      type: "CURSO ESPECIAL",
      title: "Identificación de Ideas y Formulación de Planes de Negocio",
    },
    {
      year: "2022",
      organization: "Universidad de Caldas · Misión TIC",
      type: "DIPLOMA",
      title: "Programador de Aplicaciones Móviles Java",
    },
    {
      year: "2023",
      organization: "SENA",
      type: "TÍTULO",
      title: "Introducción a la Inteligencia Artificial desde el Enfoque Académico",
    },
    {
      year: "2025",
      organization: "Politécnico de Colombia",
      type: "DIPLOMA",
      title: "Aprendizaje Basado en Proyectos",
    },
  ];

  const certificates = [
    "Unreal Engine Blueprint Game",
    "Make Arcade React System",
    "Unreal VideoGames",
    "Google Certified: Foundations of Project Management · Coursera",
  ];

  const googleBadges = [
    {
      title: "Exploring Data Transformation with Google Cloud",
      date: "1 jun 2026",
      url: "https://www.skills.google/public_profiles/efb60a19-0e77-4cea-ace6-363bc02e924c/badges/24604339",
    },
    {
      title: "Google Workspace User and Resource Management",
      date: "30 may 2026",
      url: "https://www.skills.google/public_profiles/efb60a19-0e77-4cea-ace6-363bc02e924c/badges/24553259",
    },
    {
      title: "Introduction to Large Language Models",
      date: "26 may 2026",
      url: "https://www.skills.google/public_profiles/efb60a19-0e77-4cea-ace6-363bc02e924c/badges/24451110",
    },
    {
      title: "Build Agents with Agent Development Kit (ADK)",
      date: "26 may 2026",
      url: "https://www.skills.google/public_profiles/efb60a19-0e77-4cea-ace6-363bc02e924c/badges/24451029",
    },
    {
      title: "Create Generative AI Apps on Google Cloud",
      date: "25 may 2026",
      url: "https://www.skills.google/public_profiles/efb60a19-0e77-4cea-ace6-363bc02e924c/badges/24416858",
    },
    {
      title: "Machine Learning Operations (MLOps) for Generative AI",
      date: "10 abr 2026",
      url: "https://www.skills.google/public_profiles/efb60a19-0e77-4cea-ace6-363bc02e924c/badges/23541833",
    },
    {
      title: "Google Cloud Computing Foundations: Infrastructure in Google Cloud",
      date: "10 abr 2026",
      url: "https://www.skills.google/public_profiles/efb60a19-0e77-4cea-ace6-363bc02e924c/badges/23540147",
    },
    {
      title: "Google DeepMind: Train A Small Language Model",
      date: "10 abr 2026",
      url: "https://www.skills.google/public_profiles/efb60a19-0e77-4cea-ace6-363bc02e924c/badges/23539362",
    },
    {
      title: "AI Boost Bites: AI Power-Ups for Google Workspace",
      date: "9 abr 2026",
      url: "https://www.skills.google/public_profiles/efb60a19-0e77-4cea-ace6-363bc02e924c/badges/23524487",
      deprecated: true,
    },
    {
      title: "AI Boost Bites: Your Personal Feedback Agent",
      date: "9 abr 2026",
      url: "https://www.skills.google/public_profiles/efb60a19-0e77-4cea-ace6-363bc02e924c/badges/23524460",
    },
    {
      title: "Gemini for Application Developers",
      date: "9 abr 2026",
      url: "https://www.skills.google/public_profiles/efb60a19-0e77-4cea-ace6-363bc02e924c/badges/23523987",
      deprecated: true,
    },
    {
      title: "Google Cloud Computing Foundations: Cloud Computing Fundamentals",
      date: "9 abr 2026",
      url: "https://www.skills.google/public_profiles/efb60a19-0e77-4cea-ace6-363bc02e924c/badges/23516575",
    },
    {
      title: "Gemini for end-to-end SDLC",
      date: "8 abr 2026",
      url: "https://www.skills.google/public_profiles/efb60a19-0e77-4cea-ace6-363bc02e924c/badges/23506116",
      deprecated: true,
    },
  ];
</script>

<section class="training-section" aria-labelledby="training-title">
  <div class="training-inner">
    <header class="training-heading">
      <p class="eyebrow"><span aria-hidden="true">✦</span> TRAYECTORIA ACADÉMICA Y TÉCNICA</p>
      <h2 id="training-title">Formación para seguir creando</h2>
      <p class="intro">
        Educación profesional, formación técnica y certificados en tecnología,
        inteligencia artificial y gestión.
      </p>
    </header>

    <section class="training-block" aria-labelledby="ongoing-title">
      <h3 class="credential-group-title" id="ongoing-title">Estudios en curso</h3>
      <div class="study-grid">
        {#each ongoingStudies as study}
          <article class="study-card">
            <p class="credential-meta">{study.organization}</p>
            <h4>{study.title}</h4>
            {#if study.detail}<p class="study-detail">{study.detail}</p>{/if}
            <span class="study-status">{study.status}</span>
          </article>
        {/each}
      </div>
    </section>

    <section class="training-block" aria-labelledby="education-title">
      <h3 class="credential-group-title" id="education-title">Educación y formación técnica</h3>
      <ul class="credential-list">
        {#each education as credential}
          <li>
            <div class="credential-info">
              <p class="credential-meta">{credential.organization} <span>·</span> {credential.type}</p>
              <h4>{credential.title}</h4>
            </div>
            <span class="credential-year">{credential.year}</span>
          </li>
        {/each}
      </ul>
    </section>

    <section class="training-block" aria-labelledby="certificates-title">
      <h3 class="credential-group-title" id="certificates-title">Certificados y aprendizaje continuo</h3>
      <ul class="certificate-grid">
        {#each certificates as certificate}
          <li>{certificate}</li>
        {/each}
      </ul>

      <details class="badge-details">
        <summary>Insignias de Google Cloud y Google Skills <span>13 certificados</span></summary>
        <ul class="badge-list">
          {#each googleBadges as badge}
            <li>
              <a href={badge.url} target="_blank" rel="noopener noreferrer">
                <span>{badge.title}</span>
                <span class="badge-meta">
                  {badge.date}{badge.deprecated ? " · programa descontinuado" : ""}
                </span>
              </a>
            </li>
          {/each}
        </ul>
      </details>
    </section>

    <aside class="soft-skills" aria-label="Habilidades blandas">
      <span>HABILIDADES BLANDAS</span>
      <p>Inteligencia emocional</p>
    </aside>
  </div>
</section>

<style>
  .training-section {
    padding: clamp(3rem, 7vw, 5.5rem) 1.25rem;
    color: #f5f4ff;
    background:
      radial-gradient(ellipse at 85% 20%, rgba(166, 135, 255, 0.075), transparent 28rem),
      linear-gradient(145deg, rgba(17, 15, 29, 0.78), rgba(11, 12, 20, 0.74));
  }

  .training-inner {
    width: min(1120px, 100%);
    margin: 0 auto;
  }

  .training-heading {
    max-width: 700px;
    margin-bottom: 2rem;
  }

  .eyebrow {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin: 0 0 1rem;
    color: #c3adff;
    font-size: 0.64rem;
    font-weight: 750;
    letter-spacing: 0.14em;
  }

  .eyebrow span {
    font-size: 1rem;
  }

  h2 {
    margin: 0;
    font-size: clamp(1.8rem, 4vw, 2.8rem);
    letter-spacing: -0.05em;
    line-height: 1.1;
  }

  .training-block {
    margin-top: clamp(2rem, 5vw, 3.5rem);
  }

  .intro {
    margin: 0.85rem 0 0;
    color: #b9b6c8;
    font-size: 0.92rem;
    line-height: 1.7;
  }

  .credential-group-title {
    margin: 0 0 1rem;
    color: #f5f4ff;
    font-size: 1.15rem;
  }

  .study-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }

  .study-card {
    padding: 1.25rem;
    border: 1px solid rgba(195, 173, 255, 0.25);
    border-radius: 18px;
    background: linear-gradient(135deg, rgba(166, 135, 255, 0.11), rgba(255, 255, 255, 0.025));
  }

  .study-card h4 {
    margin: 0.35rem 0 0.25rem;
    font-size: 1.05rem;
  }

  .study-detail {
    margin: 0 0 1rem;
    color: #b9b6c8;
    font-size: 0.82rem;
  }

  .study-status {
    display: inline-flex;
    padding: 0.3rem 0.65rem;
    border: 1px solid rgba(0, 245, 212, 0.25);
    border-radius: 999px;
    color: #7cebd9;
    background: rgba(0, 245, 212, 0.06);
    font-size: 0.65rem;
    font-weight: 750;
    letter-spacing: 0.08em;
  }

  .credential-list {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 0 1.5rem;
    margin: 0;
    padding: 0;
    list-style: none;
  }

  .credential-list li {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 1rem;
    padding: 1rem 0;
    border-bottom: 1px solid rgba(255, 255, 255, 0.13);
  }

  .credential-meta {
    margin: 0 0 0.35rem;
    color: #c3adff;
    font-size: 0.67rem;
    font-weight: 750;
    letter-spacing: 0.06em;
  }

  .credential-meta span {
    padding: 0 0.2rem;
    color: #796e91;
  }

  .credential-info h4 {
    margin: 0;
    font-size: 0.9rem;
    font-weight: 650;
    line-height: 1.5;
  }

  .credential-year {
    flex: 0 0 auto;
    padding: 0.15rem 0.5rem;
    border-radius: 999px;
    color: #b9b6c8;
    background: rgba(255, 255, 255, 0.06);
    font-size: 0.72rem;
    font-variant-numeric: tabular-nums;
  }

  .certificate-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 0.75rem;
    margin: 0;
    padding: 0;
    list-style: none;
  }

  .certificate-grid li {
    padding: 0.9rem 1rem;
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 14px;
    color: #e5e2ef;
    background: rgba(255, 255, 255, 0.035);
    font-size: 0.84rem;
  }

  .badge-details {
    margin-top: 1rem;
    border: 1px solid rgba(195, 173, 255, 0.2);
    border-radius: 16px;
    background: rgba(166, 135, 255, 0.045);
  }

  .badge-details summary {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    padding: 1rem 1.1rem;
    color: #e8e2ff;
    cursor: pointer;
    font-size: 0.88rem;
    font-weight: 700;
    list-style-position: inside;
  }

  .badge-details summary span {
    flex: 0 0 auto;
    color: #b9b6c8;
    font-size: 0.72rem;
    font-weight: 500;
  }

  .badge-list {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 0.6rem;
    margin: 0;
    padding: 0 1rem 1rem;
    list-style: none;
  }

  .badge-list a {
    display: flex;
    height: 100%;
    flex-direction: column;
    justify-content: space-between;
    gap: 0.5rem;
    padding: 0.85rem;
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    color: #e5e2ef;
    background: rgba(255, 255, 255, 0.035);
    font-size: 0.8rem;
    line-height: 1.5;
    text-decoration: none;
    transition: border-color 180ms ease, background 180ms ease;
  }

  .badge-list a:hover {
    border-color: rgba(0, 245, 212, 0.45);
    background: rgba(0, 245, 212, 0.06);
  }

  .badge-list a:focus-visible {
    outline: 2px solid #00f5d4;
    outline-offset: 2px;
  }

  .badge-meta {
    color: #a9a4b8;
    font-size: 0.68rem;
  }

  .soft-skills {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 0.6rem 1rem;
    margin-top: 2rem;
    padding-top: 1.25rem;
    border-top: 1px solid rgba(255, 255, 255, 0.13);
  }

  .soft-skills span {
    color: #c3adff;
    font-size: 0.65rem;
    font-weight: 750;
    letter-spacing: 0.12em;
  }

  .soft-skills p {
    margin: 0;
    color: #e5e2ef;
    font-size: 0.85rem;
  }

  @media (max-width: 640px) {
    .study-grid,
    .credential-list,
    .certificate-grid,
    .badge-list {
      grid-template-columns: 1fr;
    }

    .badge-details summary {
      align-items: flex-start;
      flex-direction: column;
      gap: 0.25rem;
    }
  }

  @media (prefers-reduced-motion: reduce) {
    .badge-list a {
      transition: none;
    }
  }
</style>
