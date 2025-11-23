// src/utils/miniapp.ts
/**
 * Utilitários para detecção e integração com MiniApps
 * Suporta Telegram Mini Apps e Farcaster Frames
 */

// Telegram WebApp types
declare global {
  interface Window {
    Telegram?: {
      WebApp: {
        initData: string;
        initDataUnsafe: {
          user?: {
            id: number;
            first_name: string;
            last_name?: string;
            username?: string;
            language_code?: string;
          };
          auth_date: number;
          hash: string;
        };
        version: string;
        platform: string;
        colorScheme: 'light' | 'dark';
        themeParams: {
          bg_color?: string;
          text_color?: string;
          hint_color?: string;
          link_color?: string;
          button_color?: string;
          button_text_color?: string;
        };
        isExpanded: boolean;
        viewportHeight: number;
        viewportStableHeight: number;
        headerColor: string;
        backgroundColor: string;
        ready: () => void;
        expand: () => void;
        close: () => void;
        sendData: (data: string) => void;
        openLink: (url: string, options?: { try_instant_view?: boolean }) => void;
        openTelegramLink: (url: string) => void;
      };
    };
  }
}

export type Platform = 'telegram' | 'farcaster' | 'web';

/**
 * Detecta se está rodando no Telegram WebApp
 */
export function isTelegramWebApp(): boolean {
  if (typeof window === 'undefined') return false;
  return window.Telegram?.WebApp !== undefined;
}

/**
 * Detecta se está rodando em um Farcaster Frame
 */
export function isFarcasterFrame(): boolean {
  if (typeof window === 'undefined') return false;
  // Farcaster frames são detectados via meta tags ou user agent
  const frameMeta = document.querySelector('meta[name="farcaster:frame"]');
  const userAgent = navigator.userAgent.toLowerCase();
  return frameMeta !== null || userAgent.includes('farcaster');
}

/**
 * Retorna a plataforma atual
 */
export function getPlatform(): Platform {
  if (isTelegramWebApp()) return 'telegram';
  if (isFarcasterFrame()) return 'farcaster';
  return 'web';
}

/**
 * Obtém dados do usuário do Telegram (se disponível)
 */
export function getTelegramUser() {
  if (!isTelegramWebApp()) return null;
  return window.Telegram?.WebApp.initDataUnsafe.user || null;
}

/**
 * Obtém tema do Telegram (para aplicar cores)
 */
export function getTelegramTheme() {
  if (!isTelegramWebApp()) return null;
  return window.Telegram?.WebApp.themeParams || null;
}

/**
 * Inicializa Telegram WebApp (chama ready() e expand())
 */
export function initTelegramWebApp() {
  if (!isTelegramWebApp()) return;
  
  const tg = window.Telegram?.WebApp;
  if (tg) {
    tg.ready();
    tg.expand();
  }
}

/**
 * Verifica se deve usar layout compacto (para frames)
 */
export function useCompactLayout(): boolean {
  return isFarcasterFrame();
}

/**
 * Obtém altura do viewport (especialmente útil para Telegram)
 */
export function getViewportHeight(): number {
  if (isTelegramWebApp()) {
    return window.Telegram?.WebApp.viewportHeight || window.innerHeight;
  }
  return window.innerHeight;
}

