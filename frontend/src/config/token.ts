// src/config/token.ts
export const TOKEN_CONFIG = {
  // Polygon Mainnet (ou Mumbai testnet durante desenvolvimento)
  address: process.env.NEXT_PUBLIC_TOKEN_ADDRESS || "",
  name: "NeoFlowOFF",
  symbol: "NEOFLW",
  decimals: 18,
  
  // Network - POLYGON MAINNET
  network: {
    name: "Polygon",
    chainId: 137, // Polygon mainnet (80001 para Mumbai testnet)
    rpcUrls: [
      process.env.NEXT_PUBLIC_ALCHEMY_API_KEY
        ? `https://polygon-mainnet.g.alchemy.com/v2/${process.env.NEXT_PUBLIC_ALCHEMY_API_KEY}`
        : "https://polygon-rpc.com",
      "https://rpc.ankr.com/polygon",
      "https://polygon-rpc.com",
    ],
    explorer: "https://polygonscan.com",
    nativeCurrency: {
      name: "MATIC",
      symbol: "MATIC",
      decimals: 18,
    },
  },
  
  // Para desenvolvimento/testnet, usar Mumbai:
  // chainId: 80001,
  // explorer: "https://mumbai.polygonscan.com",
  
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
};

export function getTokenLogoUrl(size: string = 'default'): string {
  const cid = TOKEN_CONFIG.logo.ipfsCid;
  return `${TOKEN_CONFIG.logo.gateways[0]}/${cid}`;
}

