// src/hooks/useTelegram.ts
'use client';

import { useEffect, useState } from 'react';
import { isTelegramWebApp, getTelegramUser, getTelegramTheme, initTelegramWebApp } from '../utils/miniapp';

export function useTelegram() {
  const [webApp, setWebApp] = useState<any>(null);
  const [user, setUser] = useState<any>(null);
  const [theme, setTheme] = useState<any>(null);
  const [isReady, setIsReady] = useState(false);

  useEffect(() => {
    if (isTelegramWebApp()) {
      const tg = window.Telegram?.WebApp;
      if (tg) {
        // Inicializar
        initTelegramWebApp();
        
        setWebApp(tg);
        setUser(getTelegramUser());
        setTheme(getTelegramTheme());
        setIsReady(true);
      }
    }
  }, []);

  return {
    webApp,
    user,
    theme,
    isTelegram: !!webApp,
    isReady,
  };
}

