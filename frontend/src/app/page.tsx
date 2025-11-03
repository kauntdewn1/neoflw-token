// src/app/page.tsx
'use client';

import { useState, useEffect } from 'react';
import { useAccount, useConnect, useDisconnect } from 'wagmi';
import { TokenCard } from '../components/TokenCard';
import { StakingCard } from '../components/StakingCard';
import { ClaimCard } from '../components/ClaimCard';
import { TOKEN_CONFIG } from '../config/token';

export default function Home() {
  const [mounted, setMounted] = useState(false);
  const { address, isConnected } = useAccount();
  const { connect, connectors, isPending } = useConnect();
  const { disconnect } = useDisconnect();

  // Prevenir erro de hidratação - só renderizar após montagem no cliente
  useEffect(() => {
    setMounted(true);
  }, []);

  // Evitar erro de hidratação - mostrar loading até montar no cliente
  if (!mounted) {
    return (
      <main className="container">
        <header>
          <h1>NEOFLW Protocol</h1>
          <p>Tokenização com propósito</p>
          <div className="wallet-section">
            <p>Carregando...</p>
          </div>
        </header>
      </main>
    );
  }

  return (
    <main className="container">
      <header>
        <h1>NEOFLW Protocol</h1>
        <p>Tokenização com propósito</p>
        
        {!isConnected ? (
          <div className="wallet-section">
            <p>Conecte sua wallet para começar</p>
            {connectors.map((connector) => (
              <button
                key={connector.uid}
                onClick={() => connect({ connector })}
                disabled={isPending}
              >
                Conectar {connector.name}
              </button>
            ))}
          </div>
        ) : (
          <div className="wallet-section">
            <p>Conectado: {address}</p>
            <button onClick={() => disconnect()}>Desconectar</button>
          </div>
        )}
      </header>

      {isConnected && (
        <div className="cards-grid">
          <TokenCard />
          <StakingCard />
          <ClaimCard />
        </div>
      )}

      <footer>
        <p>
          Token: <strong>{TOKEN_CONFIG.name}</strong> ({TOKEN_CONFIG.symbol}) | 
          Rede: {TOKEN_CONFIG.network.name}
        </p>
        <a 
          href={`${TOKEN_CONFIG.network.explorer}/token/${TOKEN_CONFIG.address}`}
          target="_blank"
          rel="noopener noreferrer"
        >
          Ver no Explorer
        </a>
      </footer>
    </main>
  );
}

