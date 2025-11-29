// src/app/providers.tsx
'use client';

import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { WagmiProvider } from 'wagmi';
import { createConfig, http } from 'wagmi';
import { polygon } from 'wagmi/chains';
import { injected, metaMask, walletConnect } from 'wagmi/connectors';
import { ThirdwebProvider } from '@thirdweb-dev/react';
import { TOKEN_CONFIG } from '../config/token';
import { THIRDWEB_CONFIG, isThirdwebConfigured } from '../config/thirdweb';

const queryClient = new QueryClient();

// Usar apenas Polygon Mainnet (testnets já não são necessárias)
const currentChain = polygon;
// Thirdweb espera um identificador de chain (slug, id ou objeto próprio)
const thirdwebActiveChain = 'polygon';

// Configuração para suportar MiniApps (Telegram/Farcaster)
const config = createConfig({
  chains: [polygon],
  connectors: [
    injected(), // MetaMask e outras wallets injetadas
    metaMask(), // MetaMask específico
    // WalletConnect para suporte a mais wallets (incluindo mobile)
    walletConnect({
      projectId: process.env.NEXT_PUBLIC_WALLETCONNECT_PROJECT_ID || '',
      showQrModal: true,
    }),
  ],
  transports: {
    [polygon.id]: http(TOKEN_CONFIG.network.rpcUrls[0]),
  },
  // Configurações para melhor suporte mobile
  ssr: true, // Suporte SSR para Next.js
});

export function Providers({ children }: { children: React.ReactNode }) {
  // Se Thirdweb estiver configurado, usar como provider principal
  if (isThirdwebConfigured()) {
    return (
      <ThirdwebProvider
        clientId={THIRDWEB_CONFIG.clientId}
        activeChain={thirdwebActiveChain}
      >
        <WagmiProvider config={config}>
          <QueryClientProvider client={queryClient}>
            {children}
          </QueryClientProvider>
        </WagmiProvider>
      </ThirdwebProvider>
    );
  }

  // Fallback para apenas Wagmi se Thirdweb não estiver configurado
  return (
    <WagmiProvider config={config}>
      <QueryClientProvider client={queryClient}>
        {children}
      </QueryClientProvider>
    </WagmiProvider>
  );
}

