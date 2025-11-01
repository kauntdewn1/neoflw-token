# 🎨 Guia de Desenvolvimento Frontend - Token NEOFLW

## 📋 Informações do Token

```javascript
const TOKEN_INFO = {
  address: "0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87",
  name: "NeoFlowOFF",
  symbol: "NEOFLW",
  decimals: 18,
  network: "Ethereum Sepolia (Testnet)",
  chainId: 11155111,
  logoUrl: "https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i",
  metadataUrl: "./metadata/token-metadata.json"
};
```

---

## 🖼️ 1. Exibindo o Logo do Token

### **Opção 1: URL Direta do IPFS (Recomendado)**

```jsx
// React/Next.js
import Image from 'next/image';

const TokenLogo = () => {
  const logoUrl = "https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i";
  
  return (
    <Image
      src={logoUrl}
      alt="NEOFLW Token Logo"
      width={64}
      height={64}
      className="rounded-full"
      onError={(e) => {
        // Fallback se o gateway falhar
        e.target.src = "https://ipfs.io/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i";
      }}
    />
  );
};
```

```javascript
// Vanilla JS / Vue
const logoUrl = "https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i";

function createTokenLogo(container) {
  const img = document.createElement('img');
  img.src = logoUrl;
  img.alt = "NEOFLW Token Logo";
  img.style.width = '64px';
  img.style.height = '64px';
  img.style.borderRadius = '50%';
  
  // Fallback para outro gateway se falhar
  img.onerror = function() {
    this.src = "https://ipfs.io/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i";
  };
  
  container.appendChild(img);
}
```

### **Opção 2: Com Fallback Inteligente (Mais Robusto)**

```javascript
// utils/ipfs.js - Utilitário para gateways IPFS com fallback
const IPFS_CID = "bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i";

const IPFS_GATEWAYS = [
  `https://gateway.lighthouse.storage/ipfs/${IPFS_CID}`,
  `https://ipfs.io/ipfs/${IPFS_CID}`,
  `https://cloudflare-ipfs.com/ipfs/${IPFS_CID}`,
  `https://gateway.pinata.cloud/ipfs/${IPFS_CID}`,
];

/**
 * Tenta carregar imagem IPFS com fallback automático
 */
async function loadIPFSImage(cid, fallbackUrl = null) {
  for (const gatewayUrl of IPFS_GATEWAYS) {
    try {
      const response = await fetch(gatewayUrl, { method: 'HEAD' });
      if (response.ok) {
        return gatewayUrl;
      }
    } catch (error) {
      console.warn(`Gateway falhou: ${gatewayUrl}`, error);
      continue;
    }
  }
  
  // Se todos falharem, retorna fallback
  return fallbackUrl || IPFS_GATEWAYS[0];
}

// React Hook
import { useState, useEffect } from 'react';

function useIPFSImage(cid, fallbackUrl = null) {
  const [imageUrl, setImageUrl] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    loadIPFSImage(cid, fallbackUrl)
      .then(url => {
        setImageUrl(url);
        setIsLoading(false);
      })
      .catch(err => {
        setError(err);
        setIsLoading(false);
        setImageUrl(fallbackUrl);
      });
  }, [cid, fallbackUrl]);

  return { imageUrl, isLoading, error };
}

// Uso no componente
function TokenLogo() {
  const { imageUrl, isLoading, error } = useIPFSImage(
    "bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i",
    "/images/avatar_neoflow.png" // Fallback local
  );

  if (isLoading) return <div>Carregando...</div>;
  if (error) return <div>Erro ao carregar logo</div>;

  return <img src={imageUrl} alt="NEOFLW Logo" />;
}
```

---

## 📄 2. Carregando Metadados do Token

### **Opção 1: Arquivo JSON Local**

```javascript
// Carregar metadados do arquivo local
async function loadTokenMetadata() {
  try {
    const response = await fetch('/metadata/token-metadata.json');
    const metadata = await response.json();
    
    return {
      name: metadata.name,
      symbol: metadata.symbol,
      decimals: metadata.decimals,
      logoUrl: metadata.image || metadata.logo,
      description: metadata.description,
      website: metadata.website,
      social: metadata.social
    };
  } catch (error) {
    console.error('Erro ao carregar metadados:', error);
    // Retornar valores padrão
    return {
      name: "NeoFlowOFF",
      symbol: "NEOFLW",
      decimals: 18,
      logoUrl: "https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i"
    };
  }
}
```

### **Opção 2: React Hook para Metadados**

```jsx
// hooks/useTokenMetadata.js
import { useState, useEffect } from 'react';

export function useTokenMetadata(tokenAddress) {
  const [metadata, setMetadata] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchMetadata() {
      try {
        // Tenta carregar do arquivo local primeiro
        const response = await fetch('/metadata/token-metadata.json');
        if (response.ok) {
          const data = await response.json();
          setMetadata(data);
        } else {
          throw new Error('Metadata não encontrado');
        }
      } catch (err) {
        console.error('Erro ao carregar metadados:', err);
        setError(err);
        // Fallback para valores hardcoded
        setMetadata({
          name: "NeoFlowOFF",
          symbol: "NEOFLW",
          decimals: 18,
          image: "https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i"
        });
      } finally {
        setLoading(false);
      }
    }

    fetchMetadata();
  }, [tokenAddress]);

  return { metadata, loading, error };
}

// Uso
function TokenCard() {
  const { metadata, loading } = useTokenMetadata("0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87");

  if (loading) return <div>Carregando...</div>;

  return (
    <div>
      <img src={metadata.image} alt={metadata.name} />
      <h2>{metadata.name}</h2>
      <p>{metadata.symbol}</p>
      <p>{metadata.description}</p>
    </div>
  );
}
```

---

## 🔗 3. Integração com Wallets (MetaMask, WalletConnect, etc)

### **Ethers.js / viem**

```javascript
// utils/token.js
import { ethers } from 'ethers';

const TOKEN_ADDRESS = "0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87";
const TOKEN_ABI = [
  "function name() view returns (string)",
  "function symbol() view returns (string)",
  "function decimals() view returns (uint8)",
  "function totalSupply() view returns (uint256)",
  "function balanceOf(address) view returns (uint256)"
];

// Carregar informações do token do contrato
async function getTokenInfo(provider, address = TOKEN_ADDRESS) {
  const tokenContract = new ethers.Contract(address, TOKEN_ABI, provider);
  
  const [name, symbol, decimals, totalSupply] = await Promise.all([
    tokenContract.name(),
    tokenContract.symbol(),
    tokenContract.decimals(),
    tokenContract.totalSupply()
  ]);

  return {
    address,
    name,
    symbol,
    decimals,
    totalSupply: ethers.formatUnits(totalSupply, decimals),
    // Logo vem dos metadados, não do contrato
    logoUrl: "https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i"
  };
}

// Verificar saldo do usuário
async function getTokenBalance(provider, userAddress) {
  const tokenContract = new ethers.Contract(TOKEN_ADDRESS, TOKEN_ABI, provider);
  const balance = await tokenContract.balanceOf(userAddress);
  const decimals = await tokenContract.decimals();
  return ethers.formatUnits(balance, decimals);
}
```

### **React Hook para Wallet + Token**

```jsx
// hooks/useTokenBalance.js
import { useState, useEffect } from 'react';
import { ethers } from 'ethers';

export function useTokenBalance(tokenAddress, userAddress) {
  const [balance, setBalance] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!userAddress || !window.ethereum) return;

    async function fetchBalance() {
      try {
        const provider = new ethers.BrowserProvider(window.ethereum);
        const tokenContract = new ethers.Contract(
          tokenAddress,
          [
            "function balanceOf(address) view returns (uint256)",
            "function decimals() view returns (uint8)"
          ],
          provider
        );

        const [balance, decimals] = await Promise.all([
          tokenContract.balanceOf(userAddress),
          tokenContract.decimals()
        ]);

        setBalance(ethers.formatUnits(balance, decimals));
      } catch (err) {
        setError(err);
        console.error('Erro ao buscar saldo:', err);
      } finally {
        setLoading(false);
      }
    }

    fetchBalance();
  }, [tokenAddress, userAddress]);

  return { balance, loading, error };
}
```

---

## ⚙️ 4. Configuração e Variáveis de Ambiente

### **`.env` ou `config.js`**

```javascript
// config/token.js
export const TOKEN_CONFIG = {
  // Sepolia Testnet
  address: import.meta.env.VITE_TOKEN_ADDRESS || "0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87",
  name: "NeoFlowOFF",
  symbol: "NEOFLW",
  decimals: 18,
  
  // Network
  network: {
    name: "Sepolia",
    chainId: 11155111,
    networkId: 11155111,
    // RPC público (sem necessidade de API key)
    rpcUrls: [
      "https://rpc.sepolia.org",
      "https://rpc.sepolia.online",
      "https://www.sepoliarpc.space",
      "https://rpc-sepolia.rockx.com",
      // Com API key (se tiver)
      import.meta.env.VITE_RPC_URL || "https://sepolia.infura.io/v3/YOUR_KEY"
    ],
    explorer: "https://sepolia.etherscan.io",
    explorerAlternatives: [
      "https://eth-sepolia.blockscout.com/",
      "https://sepolia.otterscan.io"
    ],
    faucets: [
      "https://sepoliafaucet.com/",
      "https://grabteeth.xyz",
      "https://faucet.quicknode.com/ethereum/sepolia"
    ],
    officialWebsite: "https://sepolia.ethpandaops.io/"
  },
  
  // Logo e Metadados
  logo: {
    ipfsCid: "bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i",
    gateways: [
      "https://gateway.lighthouse.storage/ipfs",
      "https://ipfs.io/ipfs",
      "https://cloudflare-ipfs.com/ipfs"
    ],
    fallback: "/images/avatar_neoflow.png"
  },
  
  // URLs
  metadataUrl: "/metadata/token-metadata.json",
  website: "neoflowoff.eth",
  
  // Social
  social: {
    twitter: "https://twitter.com/neoflw",
    discord: "https://discord.gg/neoflw",
    github: "https://github.com/neoflw"
  }
};

// Helper para URL do logo
export function getTokenLogoUrl(size = 'default') {
  const cid = TOKEN_CONFIG.logo.ipfsCid;
  // Você pode ter diferentes tamanhos se necessário
  return `${TOKEN_CONFIG.logo.gateways[0]}/${cid}`;
}
```

### **Vite/React `.env`**

```bash
# .env
VITE_TOKEN_ADDRESS=0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
VITE_NETWORK_CHAIN_ID=11155111
VITE_RPC_URL=https://sepolia.infura.io/v3/YOUR_KEY
VITE_IPFS_GATEWAY=https://gateway.lighthouse.storage/ipfs
```

---

## 🎯 5. Componente React Completo (Exemplo)

```jsx
// components/TokenDisplay.jsx
import { useState, useEffect } from 'react';
import { useTokenMetadata } from '../hooks/useTokenMetadata';
import { useTokenBalance } from '../hooks/useTokenBalance';
import { TOKEN_CONFIG } from '../config/token';

export function TokenDisplay({ userAddress }) {
  const { metadata, loading: metadataLoading } = useTokenMetadata(TOKEN_CONFIG.address);
  const { balance, loading: balanceLoading } = useTokenBalance(TOKEN_CONFIG.address, userAddress);
  
  const [logoUrl, setLogoUrl] = useState(null);
  const [logoError, setLogoError] = useState(false);

  useEffect(() => {
    // Tenta carregar logo com fallback
    if (metadata?.image) {
      setLogoUrl(metadata.image);
    } else {
      setLogoUrl(getTokenLogoUrl());
    }
  }, [metadata]);

  const handleLogoError = () => {
    if (!logoError) {
      // Tenta gateway alternativo
      const cid = TOKEN_CONFIG.logo.ipfsCid;
      const altGateway = TOKEN_CONFIG.logo.gateways[1];
      setLogoUrl(`${altGateway}/${cid}`);
      setLogoError(true);
    } else {
      // Fallback para imagem local
      setLogoUrl(TOKEN_CONFIG.logo.fallback);
    }
  };

  if (metadataLoading) {
    return <div className="token-loading">Carregando informações do token...</div>;
  }

  return (
    <div className="token-display">
      {/* Logo */}
      <div className="token-logo">
        {logoUrl && (
          <img
            src={logoUrl}
            alt={`${metadata.name} Logo`}
            onError={handleLogoError}
            className="token-logo-img"
          />
        )}
      </div>

      {/* Informações */}
      <div className="token-info">
        <h2 className="token-name">{metadata.name}</h2>
        <p className="token-symbol">{metadata.symbol}</p>
        {metadata.description && (
          <p className="token-description">{metadata.description}</p>
        )}
      </div>

      {/* Saldo (se usuário conectado) */}
      {userAddress && (
        <div className="token-balance">
          <h3>Seu Saldo</h3>
          {balanceLoading ? (
            <p>Carregando...</p>
          ) : (
            <p className="balance-amount">
              {parseFloat(balance || 0).toLocaleString()} {metadata.symbol}
            </p>
          )}
        </div>
      )}

      {/* Links */}
      <div className="token-links">
        <a
          href={`${TOKEN_CONFIG.network.explorer}/token/${TOKEN_CONFIG.address}`}
          target="_blank"
          rel="noopener noreferrer"
        >
          Ver no Explorer
        </a>
        {metadata.website && (
          <a href={metadata.website} target="_blank" rel="noopener noreferrer">
            Website
          </a>
        )}
      </div>

      {/* Social */}
      {metadata.social && (
        <div className="token-social">
          {metadata.social.twitter && (
            <a href={metadata.social.twitter} target="_blank" rel="noopener noreferrer">
              Twitter
            </a>
          )}
          {metadata.social.discord && (
            <a href={metadata.social.discord} target="_blank" rel="noopener noreferrer">
              Discord
            </a>
          )}
        </div>
      )}
    </div>
  );
}
```

---

## 🚀 6. Performance e Otimização

### **Lazy Loading de Imagens**

```jsx
import { lazy, Suspense } from 'react';

const TokenLogo = lazy(() => import('./TokenLogo'));

function TokenCard() {
  return (
    <Suspense fallback={<div>Carregando logo...</div>}>
      <TokenLogo />
    </Suspense>
  );
}
```

### **Otimização de Imagens (Next.js)**

```jsx
// next.config.js
module.exports = {
  images: {
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
```

### **Cache de Metadados**

```javascript
// utils/metadataCache.js
const METADATA_CACHE_KEY = 'neoflw_token_metadata';
const CACHE_DURATION = 24 * 60 * 60 * 1000; // 24 horas

export function getCachedMetadata() {
  const cached = localStorage.getItem(METADATA_CACHE_KEY);
  if (!cached) return null;

  const { data, timestamp } = JSON.parse(cached);
  const now = Date.now();

  if (now - timestamp > CACHE_DURATION) {
    localStorage.removeItem(METADATA_CACHE_KEY);
    return null;
  }

  return data;
}

export function setCachedMetadata(metadata) {
  localStorage.setItem(METADATA_CACHE_KEY, JSON.stringify({
    data: metadata,
    timestamp: Date.now()
  }));
}
```

---

## ⚠️ 7. Tratamento de Erros e Fallbacks

### **Estratégia de Fallback Completa**

```javascript
// utils/tokenHelpers.js
export async function getTokenLogoUrl(cid, fallbacks = []) {
  const gateways = [
    `https://gateway.lighthouse.storage/ipfs/${cid}`,
    `https://ipfs.io/ipfs/${cid}`,
    `https://cloudflare-ipfs.com/ipfs/${cid}`,
    `https://gateway.pinata.cloud/ipfs/${cid}`,
    ...fallbacks
  ];

  for (const url of gateways) {
    try {
      const response = await fetch(url, { method: 'HEAD' });
      if (response.ok) {
        return url;
      }
    } catch (error) {
      continue;
    }
  }

  // Último recurso: imagem placeholder
  return '/images/token-placeholder.png';
}

// Componente com tratamento robusto
function TokenLogoWithFallback({ cid, alt, className }) {
  const [src, setSrc] = useState(null);
  const [error, setError] = useState(false);

  useEffect(() => {
    getTokenLogoUrl(cid, ['/images/avatar_neoflow.png'])
      .then(url => setSrc(url))
      .catch(() => setError(true));
  }, [cid]);

  if (error || !src) {
    return (
      <div className={`token-placeholder ${className}`}>
        {alt?.[0] || '?'}
      </div>
    );
  }

  return (
    <img
      src={src}
      alt={alt}
      className={className}
      onError={() => setError(true)}
    />
  );
}
```

---

## 📱 8. Responsividade e Acessibilidade

```css
/* token.css */
.token-logo-img {
  width: 64px;
  height: 64px;
  border-radius: 50%;
  object-fit: cover;
  background: #f0f0f0;
  /* Fallback visual enquanto carrega */
}

.token-placeholder {
  width: 64px;
  height: 64px;
  border-radius: 50%;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: bold;
  font-size: 24px;
}

/* Mobile */
@media (max-width: 768px) {
  .token-logo-img {
    width: 48px;
    height: 48px;
  }
}

/* Dark mode */
@media (prefers-color-scheme: dark) {
  .token-logo-img {
    background: #2a2a2a;
  }
}

/* Loading state */
.token-loading {
  display: flex;
  align-items: center;
  gap: 12px;
}

.token-loading::before {
  content: '';
  width: 20px;
  height: 20px;
  border: 2px solid #f3f3f3;
  border-top: 2px solid #667eea;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

---

## ✅ 9. Checklist de Desenvolvimento Frontend

### **Essencial:**
- [ ] Logo do token carrega corretamente
- [ ] Fallback para gateway alternativo se principal falhar
- [ ] Fallback para imagem local se IPFS falhar
- [ ] Metadados do token carregam corretamente
- [ ] Tratamento de erros implementado
- [ ] Loading states visíveis
- [ ] Funciona offline (com cache)

### **Recomendado:**
- [ ] Cache de metadados (localStorage)
- [ ] Lazy loading de imagens
- [ ] Otimização de imagens (Next.js Image, etc)
- [ ] Acessibilidade (alt text, ARIA labels)
- [ ] Responsividade mobile
- [ ] Dark mode support
- [ ] Integração com wallets
- [ ] Verificação de rede (Sepolia vs Mainnet)

### **Avançado:**
- [ ] Service Worker para cache offline
- [ ] Preload de imagens críticas
- [ ] Skeleton loading states
- [ ] Error boundaries (React)
- [ ] Analytics de carregamento de imagens
- [ ] A/B testing de gateways IPFS

---

## 🔗 10. Links e Recursos

### **URLs Importantes do Token:**
- Logo IPFS: `https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i`
- Metadados: `/metadata/token-metadata.json`
- Token Explorer: `https://sepolia.etherscan.io/token/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87`

### **Sepolia Testnet - Recursos Oficiais:**

**Website Oficial:**
- https://sepolia.ethpandaops.io/ - Portal oficial do Sepolia Testnet

**Block Explorers:**
- https://sepolia.etherscan.io - Etherscan (oficial)
- https://eth-sepolia.blockscout.com/ - Blockscout (alternativa)
- https://sepolia.otterscan.io - Otterscan (open-source)
- https://sepolia.beaconcha.in - Beaconchain explorer

**RPC Endpoints (Públicos):**
- https://rpc.sepolia.online
- https://www.sepoliarpc.space
- https://rpc.sepolia.org (status: https://status.sepolia.org)
- https://rpc-sepolia.rockx.com
- https://rpc.bordel.wtf/sepolia
- https://rpc.sepolia.ethpandaops.io

**Faucets (ETH de Teste):**
- https://grabteeth.xyz
- https://sepolia-faucet.pk910.de/ (PoW powered)
- https://faucet-sepolia.rockx.com/
- https://faucet.quicknode.com/ethereum/sepolia
- https://sepoliafaucet.com/ (Alchemy)
- https://learnweb3.io/faucets/sepolia (LearnWeb3)
- https://infura.io/faucet
- https://unitap.app/gastap

**Status e Monitoramento:**
- https://stats.noderpc.xyz - Status Dashboard
- https://status.sepolia.org - Status do RPC Sepolia

**Informações Técnicas:**
- Chain ID: `11155111`
- Network ID: `11155111`
- GitHub: https://github.com/eth-clients/sepolia

### **Documentação de Desenvolvimento:**
- Ethers.js: https://docs.ethers.org/
- viem: https://viem.sh/
- Next.js Image: https://nextjs.org/docs/app/api-reference/components/image
- IPFS Gateways: https://docs.ipfs.io/how-to/address-ipfs-on-web/

---

## 💡 Dicas Finais

1. **Sempre use fallbacks** - Gateways IPFS podem estar offline
2. **Cache metadados** - Evite requisições desnecessárias
3. **Otimize imagens** - Use formato WebP quando possível
4. **Teste em diferentes redes** - Sepolia para dev, Mainnet para prod
5. **Monitore erros** - Track falhas de carregamento de logo
6. **Use TypeScript** - Para type safety nas informações do token

---

**Pronto!** Você tem tudo para desenvolver um frontend robusto com o token NEOFLW! 🚀

