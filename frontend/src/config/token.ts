// src/config/token.ts
export const TOKEN_CONFIG = {
  // Sepolia Testnet
  address: process.env.NEXT_PUBLIC_TOKEN_ADDRESS || "0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87",
  name: "NeoFlowOFF",
  symbol: "NEOFLW",
  decimals: 18,
  
  // Network
  network: {
    name: "Sepolia",
    chainId: 11155111,
    rpcUrls: [
      "https://rpc.sepolia.org",
      "https://rpc.sepolia.online",
    ],
    explorer: "https://sepolia.etherscan.io",
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
};

export function getTokenLogoUrl(size: string = 'default'): string {
  const cid = TOKEN_CONFIG.logo.ipfsCid;
  return `${TOKEN_CONFIG.logo.gateways[0]}/${cid}`;
}

