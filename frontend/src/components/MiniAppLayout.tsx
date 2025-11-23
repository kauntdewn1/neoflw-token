// src/components/MiniAppLayout.tsx
'use client';

import { useTelegram } from '../hooks/useTelegram';
import { useFarcaster } from '../hooks/useFarcaster';
import { getPlatform } from '../utils/miniapp';

interface MiniAppLayoutProps {
  children: React.ReactNode;
}

export function MiniAppLayout({ children }: MiniAppLayoutProps) {
  const { isTelegram, webApp, theme, isReady } = useTelegram();
  const { isFrame } = useFarcaster();
  
  const platform = getPlatform();
  
  // Aplicar tema do Telegram se disponível
  const style: React.CSSProperties = {};
  if (isTelegram && theme && isReady) {
    style.backgroundColor = theme.bg_color || '#ffffff';
    style.color = theme.text_color || '#000000';
    if (webApp?.viewportHeight) {
      style.minHeight = `${webApp.viewportHeight}px`;
    }
  }
  
  return (
    <div 
      className={`miniapp-container ${platform}`}
      style={style}
    >
      {children}
    </div>
  );
}

