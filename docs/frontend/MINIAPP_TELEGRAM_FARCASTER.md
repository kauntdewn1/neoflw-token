# 📱 MiniApp NEOFLW - Telegram & Farcaster

## 🎯 Visão Geral

O DApp NEOFLW será deployado como **MiniApp** no Telegram e **Frame** no Farcaster, permitindo acesso direto dentro dessas plataformas sociais.

---

## 📊 Por Que MiniApp?

### **Telegram Mini Apps (TMA)**

- ✅ **1B+ usuários** no Telegram
- ✅ **Acesso nativo** dentro do app
- ✅ **TON Wallet** integrado
- ✅ **Web3 nativo** no Telegram
- ✅ **Viralização** fácil (compartilhar links)

### **Farcaster Frames**

- ✅ **Comunidade Web3 nativa**
- ✅ **On-chain social** (verificável)
- ✅ **Frames** = apps dentro de posts
- ✅ **Crypto-native** audience
- ✅ **Engagement alto**

---

## 🔧 Ajustes Necessários

### **1. Frontend - Suporte MiniApp**

#### **1.1. Detecção de Ambiente**

```typescript
// src/utils/miniapp.ts
export function isTelegramWebApp(): boolean {
  if (typeof window === 'undefined') return false;
  return window.Telegram?.WebApp !== undefined;
}

export function isFarcasterFrame(): boolean {
  if (typeof window === 'undefined') return false;
  // Farcaster frames são detectados via meta tags
  return document.querySelector('meta[name="farcaster:frame"]') !== null;
}

export function getPlatform(): 'telegram' | 'farcaster' | 'web' {
  if (isTelegramWebApp()) return 'telegram';
  if (isFarcasterFrame()) return 'farcaster';
  return 'web';
}
```

#### **1.2. Telegram WebApp SDK**

```typescript
// src/hooks/useTelegram.ts
import { useEffect, useState } from 'react';

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
        BackButton: {
          isVisible: boolean;
          onClick: (callback: () => void) => void;
          show: () => void;
          hide: () => void;
        };
        MainButton: {
          text: string;
          color: string;
          textColor: string;
          isVisible: boolean;
          isActive: boolean;
          isProgressVisible: boolean;
          setText: (text: string) => void;
          onClick: (callback: () => void) => void;
          show: () => void;
          hide: () => void;
          enable: () => void;
          disable: () => void;
          showProgress: (leaveActive?: boolean) => void;
          hideProgress: () => void;
        };
        ready: () => void;
        expand: () => void;
        close: () => void;
        sendData: (data: string) => void;
        openLink: (url: string, options?: { try_instant_view?: boolean }) => void;
        openTelegramLink: (url: string) => void;
        openInvoice: (url: string, callback?: (status: string) => void) => void;
        showPopup: (params: {
          title?: string;
          message: string;
          buttons?: Array<{
            id?: string;
            type?: 'default' | 'ok' | 'close' | 'cancel' | 'destructive';
            text?: string;
          }>;
        }, callback?: (id: string) => void) => void;
        showAlert: (message: string, callback?: () => void) => void;
        showConfirm: (message: string, callback?: (confirmed: boolean) => void) => void;
        showScanQrPopup: (params: {
          text?: string;
        }, callback?: (data: string) => void) => void;
        closeScanQrPopup: () => void;
        readTextFromClipboard: (callback?: (text: string) => void) => void;
        requestWriteAccess: (callback?: (granted: boolean) => void) => void;
        requestContact: (callback?: (granted: boolean) => void) => void;
      };
    };
  }
}

export function useTelegram() {
  const [webApp, setWebApp] = useState<Window['Telegram']['WebApp'] | null>(null);
  const [user, setUser] = useState<any>(null);

  useEffect(() => {
    if (typeof window !== 'undefined' && window.Telegram?.WebApp) {
      const tg = window.Telegram.WebApp;
      tg.ready();
      tg.expand();
      setWebApp(tg);
      setUser(tg.initDataUnsafe.user);
    }
  }, []);

  return { webApp, user, isTelegram: !!webApp };
}
```

#### **1.3. Farcaster Frame Support**

```typescript
// src/hooks/useFarcaster.ts
import { useEffect, useState } from 'react';

export function useFarcaster() {
  const [isFrame, setIsFrame] = useState(false);
  const [frameData, setFrameData] = useState<any>(null);

  useEffect(() => {
    if (typeof window !== 'undefined') {
      // Detectar se está em um frame
      const frameMeta = document.querySelector('meta[name="farcaster:frame"]');
      if (frameMeta) {
        setIsFrame(true);
        // Ler dados do frame se disponíveis
        const frameUrl = frameMeta.getAttribute('content');
        setFrameData({ frameUrl });
      }
    }
  }, []);

  return { isFrame, frameData };
}
```

---

### **2. Wallet Integration para MiniApps**

#### **2.1. Thirdweb (Recomendado para MiniApps)**

**Por que Thirdweb:**

- ✅ Suporte nativo para Telegram
- ✅ Embed wallet (sem necessidade de extensão)
- ✅ Social login (Google, Twitter, etc)
- ✅ Farcaster integration
- ✅ Mobile-first

**Instalação:**
```bash
cd frontend
npm install @thirdweb-dev/react @thirdweb-dev/sdk
```

**Configuração:**

```typescript
// src/app/providers.tsx
'use client';

import { ThirdwebProvider } from '@thirdweb-dev/react';
import { polygon } from '@thirdweb-dev/chains';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';

const queryClient = new QueryClient();

export function Providers({ children }: { children: React.ReactNode }) {
  return (
    <ThirdwebProvider
      activeChain={polygon}
      clientId={process.env.NEXT_PUBLIC_THIRDWEB_CLIENT_ID}
      supportedWallets={[
        // Embed wallet (para Telegram/Farcaster)
        'embedded',
        // MetaMask (fallback)
        'metamask',
        // WalletConnect (fallback)
        'walletConnect',
      ]}
    >
      <QueryClientProvider client={queryClient}>
        {children}
      </QueryClientProvider>
    </ThirdwebProvider>
  );
}
```

#### **2.2. TON Wallet (Telegram)**

Para suporte completo ao Telegram, pode adicionar TON wallet:

```typescript
// src/hooks/useTONWallet.ts
export function useTONWallet() {
  const [tonWallet, setTonWallet] = useState<any>(null);

  useEffect(() => {
    if (isTelegramWebApp()) {
      // Telegram tem TON wallet nativo
      // Pode usar window.Telegram.WebApp.openTelegramLink para abrir TON wallet
    }
  }, []);

  return { tonWallet };
}
```

---

### **3. Responsividade Mobile-First**

#### **3.1. Viewport para Telegram**

```typescript
// src/app/layout.tsx
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="pt-BR">
      <head>
        {/* Telegram MiniApp viewport */}
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
        <meta name="telegram-web-app" content="true" />
        {/* Farcaster Frame */}
        <meta name="farcaster:frame" content="https://neoflowoff.eth" />
      </head>
      <body>{children}</body>
    </html>
  );
}
```

#### **3.2. CSS Mobile-First**

```css
/* src/app/globals.css */
/* Base mobile (320px+) - Telegram/Farcaster */
.container {
  width: 100%;
  max-width: 100%;
  padding: 1rem;
  margin: 0;
}

/* Telegram specific */
@media (max-width: 640px) {
  .cards-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }
  
  /* Usar altura do viewport do Telegram */
  .main-content {
    min-height: var(--tg-viewport-height, 100vh);
  }
}

/* Farcaster Frame (compacto) */
.farcaster-frame {
  max-width: 100%;
  padding: 0.5rem;
}
```

---

### **4. Configuração Next.js para MiniApp**

#### **4.1. next.config.js**

```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  
  // Para Telegram/Farcaster - permitir iframes
  headers: async () => {
    return [
      {
        source: '/:path*',
        headers: [
          {
            key: 'X-Frame-Options',
            value: 'ALLOWALL', // Permitir embed em Telegram/Farcaster
          },
          {
            key: 'Content-Security-Policy',
            value: "frame-ancestors 'self' https://*.telegram.org https://*.farcaster.xyz;",
          },
        ],
      },
    ];
  },
  
  // Output estático para IPFS (opcional)
  output: 'export', // Para deploy em IPFS
  
  images: {
    unoptimized: true, // Para IPFS
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'gateway.lighthouse.storage',
        pathname: '/ipfs/**',
      },
      {
        protocol: 'https',
        hostname: 'ipfs.io',
        pathname: '/ipfs/**',
      },
    ],
  },
};

module.exports = nextConfig;
```

---

### **5. Integração com Telegram Bot**

#### **5.1. Bot Setup**

```python
# bot/telegram_bot.py
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Criar botão para abrir MiniApp
    keyboard = [[
        InlineKeyboardButton(
            "🚀 Abrir NEOFLW",
            web_app=WebAppInfo(url="https://neoflowoff.eth")
        )
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "Bem-vindo ao NEOFLW!",
        reply_markup=reply_markup
    )

# Deploy bot
application = Application.builder().token("BOT_TOKEN").build()
application.add_handler(CommandHandler("start", start))
application.run_polling()
```

---

### **6. Integração com Farcaster**

#### **6.1. Frame Metadata**

```html
<!-- public/frame.html -->
<!DOCTYPE html>
<html>
<head>
  <meta property="fc:frame" content="vNext" />
  <meta property="fc:frame:image" content="https://neoflowoff.eth/og-image.png" />
  <meta property="fc:frame:button:1" content="Stake NEOFLW" />
  <meta property="fc:frame:button:1:action" content="link" />
  <meta property="fc:frame:button:1:target" content="https://neoflowoff.eth/stake" />
  <meta property="fc:frame:button:2" content="View Leaderboard" />
  <meta property="fc:frame:button:2:action" content="link" />
  <meta property="fc:frame:button:2:target" content="https://neoflowoff.eth/leaderboard" />
</head>
<body>
  <!-- Conteúdo do frame -->
</body>
</html>
```

---

## 📦 Dependências Necessárias

### **Frontend:**

```json
{
  "dependencies": {
    "@thirdweb-dev/react": "^5.0.0",
    "@thirdweb-dev/sdk": "^5.0.0",
    "@thirdweb-dev/chains": "^0.1.0",
    "wagmi": "^2.19.2",
    "viem": "^2.38.6"
  }
}
```

### **Backend (Opcional - para bot Telegram):**

```json
{
  "dependencies": {
    "node-telegram-bot-api": "^0.64.0"
  }
}
```

---

## 🔧 Configurações Específicas

### **Telegram MiniApp:**

#### **1. Configurar Bot no BotFather**

```
1. Criar bot: /newbot
2. Obter token
3. Configurar MiniApp: /newapp
4. Definir URL: https://neoflowoff.eth
5. Configurar permissões
```

#### **2. Variáveis de Ambiente**

```env
# Telegram
NEXT_PUBLIC_TELEGRAM_BOT_NAME=@neoflw_bot
TELEGRAM_BOT_TOKEN=seu-bot-token

# Thirdweb
NEXT_PUBLIC_THIRDWEB_CLIENT_ID=seu-client-id

# Polygon
NEXT_PUBLIC_TOKEN_ADDRESS=0x...
NEXT_PUBLIC_VAULT_ADDRESS=0x...
NEXT_PUBLIC_CLAIM_ADDRESS=0x...
NEXT_PUBLIC_GAMIFICATION_ADDRESS=0x...
```

---

### **Farcaster Frame:**

#### **1. Configurar Frame**

```typescript
// src/app/frame/route.ts
import { NextRequest, NextResponse } from 'next/server';

export async function GET(request: NextRequest) {
  return new NextResponse(`
    <!DOCTYPE html>
    <html>
      <head>
        <meta property="fc:frame" content="vNext" />
        <meta property="fc:frame:image" content="https://neoflowoff.eth/og-image.png" />
        <meta property="fc:frame:button:1" content="Stake" />
        <meta property="fc:frame:button:1:action" content="link" />
        <meta property="fc:frame:button:1:target" content="https://neoflowoff.eth" />
      </head>
      <body>
        <h1>NEOFLW Protocol</h1>
      </body>
    </html>
  `, {
    headers: {
      'Content-Type': 'text/html',
    },
  });
}
```

---

## 📱 Design Mobile-First

### **Princípios:**

1. **Touch-Friendly**: Botões mínimo 44x44px
2. **Vertical Layout**: Otimizado para scroll vertical
3. **Compact UI**: Máximo de informação em pouco espaço
4. **Fast Loading**: < 2s para carregar
5. **Offline Support**: Service Worker para cache

### **Componentes Adaptados:**

```typescript
// src/components/MiniAppLayout.tsx
'use client';

import { useTelegram } from '../hooks/useTelegram';
import { useFarcaster } from '../hooks/useFarcaster';

export function MiniAppLayout({ children }: { children: React.ReactNode }) {
  const { isTelegram, webApp } = useTelegram();
  const { isFrame } = useFarcaster();
  
  const platform = isTelegram ? 'telegram' : isFrame ? 'farcaster' : 'web';
  
  return (
    <div 
      className={`miniapp-container ${platform}`}
      style={{
        backgroundColor: isTelegram ? webApp?.themeParams.bg_color : undefined,
        color: isTelegram ? webApp?.themeParams.text_color : undefined,
        minHeight: isTelegram ? `${webApp?.viewportHeight}px` : '100vh',
      }}
    >
      {children}
    </div>
  );
}
```

---

## 🚀 Deploy para MiniApps

### **Opção 1: IPFS (Recomendado)**

```bash
# Build estático
cd frontend
npm run build

# Deploy para IPFS (Pinata)
npx pinata-cli upload dist/

# Obter CID
# Configurar ENS: neoflowoff.eth → ipfs://CID
```

### **Opção 2: Vercel/Netlify**

```bash
# Deploy normal
vercel deploy

# Configurar custom domain
# neoflowoff.eth → vercel.app
```

### **Opção 3: Telegram Hosting (Nativo)**

```
1. Usar Telegram Bot API
2. Configurar webhook
3. Hosting gratuito do Telegram
```

---

## 📊 Custos e Limitações

### **Telegram MiniApp:**

| Aspecto | Detalhes |
|---------|----------|
| **Hosting** | Gratuito (via Telegram) ou IPFS |
| **Limite de tamanho** | ~50MB |
| **Usuários** | Ilimitado |
| **Gas fees** | Polygon = praticamente grátis |

### **Farcaster Frame:**

| Aspecto | Detalhes |
|---------|----------|
| **Hosting** | IPFS ou servidor próprio |
| **Limite** | Frame metadata < 4KB |
| **Usuários** | Ilimitado |
| **Gas fees** | Polygon = praticamente grátis |

---

## ✅ Checklist de Implementação

### **FASE 1: Configuração Base**

- [ ] Instalar Thirdweb SDK
- [ ] Configurar providers para Telegram/Farcaster
- [ ] Criar hooks de detecção de plataforma
- [ ] Ajustar CSS para mobile-first

### **FASE 2: Integração Telegram**

- [ ] Criar bot no BotFather
- [ ] Configurar MiniApp URL
- [ ] Testar em Telegram Desktop
- [ ] Testar em Telegram Mobile
- [ ] Integrar TON wallet (opcional)

### **FASE 3: Integração Farcaster**

- [ ] Criar frame metadata
- [ ] Configurar frame buttons
- [ ] Testar em Farcaster client
- [ ] Validar interações

### **FASE 4: Deploy**

- [ ] Build estático
- [ ] Deploy em IPFS
- [ ] Configurar ENS
- [ ] Testar em produção

---

## 🎯 Vantagens do Polygon para MiniApps

### **Telegram:**
- ✅ Gas fees baixos = viável para microtransações
- ✅ Confirmação rápida = melhor UX
- ✅ Escala ilimitada = suporta milhões de usuários

### **Farcaster:**
- ✅ On-chain actions = verificáveis
- ✅ Gas baixo = mais interações
- ✅ Polygon = padrão para social apps

---

## 📚 Recursos

- **Telegram Mini Apps Docs**: https://core.telegram.org/bots/webapps
- **Farcaster Frames**: https://warpcast.com/~/developers/frames
- **Thirdweb Docs**: https://portal.thirdweb.com/
- **Polygon Docs**: https://docs.polygon.technology/

---

**✅ MiniApp pronto para Telegram e Farcaster! 📱🚀**

*Última atualização: Após consideração de MiniApp requirements*

