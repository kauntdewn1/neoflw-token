// src/app/providers.tsx
'use client';

import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { WagmiProvider } from 'wagmi';
import { createConfig, http } from 'wagmi';
import { polygon, polygonMumbai } from 'wagmi/chains';
import { injected, metaMask, walletConnect } from 'wagmi/connectors';
import { TOKEN_CONFIG } from '../config/token';

const queryClient = new QueryClient();

// Usar Polygon Mainnet em produção, Mumbai em desenvolvimento
const isDevelopment = process.env.NODE_ENV === 'development';
const chains = isDevelopment ? [polygonMumbai] : [polygon];
const currentChain = isDevelopment ? polygonMumbai : polygon;

// Configuração para suportar MiniApps (Telegram/Farcaster)
const config = createConfig({
  chains,
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
    [currentChain.id]: http(TOKEN_CONFIG.network.rpcUrls[0]),
  },
  // Configurações para melhor suporte mobile
  ssr: true, // Suporte SSR para Next.js
});

export function Providers({ children }: { children: React.ReactNode }) {
  return (
    <WagmiProvider config={config}>
      <QueryClientProvider client={queryClient}>
        {children}
      </QueryClientProvider>
    </WagmiProvider>
  );
}

