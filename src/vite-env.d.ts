/// <reference types="svelte" />
/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_RECAPTCHA_ENTERPRISE_CHECKBOX_SITE_KEY: string;
  readonly VITE_SALES_REQUEST_URL?: string;
}

interface Window {
  grecaptcha?: {
    enterprise?: {
      ready(callback: () => void): void;
      render(
        container: HTMLElement,
        options: {
          sitekey: string;
          action: string;
          callback: (token: string) => void;
          "expired-callback"?: () => void;
          "error-callback"?: () => void;
        },
      ): number;
      reset(widgetId?: number): void;
    };
  };
}
