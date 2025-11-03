// src/app/providers.tsx
'use client';

import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { WagmiProvider } from 'wagmi';
import { createConfig, http } from 'wagmi';
import { sepolia } from 'wagmi/chains';
import { injected, metaMask } from 'wagmi/connectors';
import { TOKEN_CONFIG } from '../config/token';

const queryClient = new QueryClient();

const config = createConfig({
  chains: [sepolia],
  connectors: [
    injected(), // MetaMask e outras wallets injetadas
    metaMask(), // MetaMask específico
  ],
  transports: {
    [sepolia.id]: http(TOKEN_CONFIG.network.rpcUrls[0]),
  },
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

