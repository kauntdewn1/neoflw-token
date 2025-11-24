// src/config/thirdweb.ts
/**
 * Configuração do Thirdweb
 * Usa variáveis de ambiente do .env
 */

export const THIRDWEB_CONFIG = {
  clientId: process.env.NEXT_PUBLIC_THIRDWEB_CLIENT_ID || '',
  secretKey: process.env.NEXT_PUBLIC_THIRDWEB_SECRET_KEY || '',
  walletAddress: process.env.TOKEN_NEOFLW_WALLET_ADDRESS || '',
  walletLabel: process.env.TOKEN_NEOFLW_WALLET_LABEL || 'Token NEOFLW Wallet',
};

// Verificar se as configurações essenciais estão presentes
export const isThirdwebConfigured = () => {
  return !!THIRDWEB_CONFIG.clientId;
};

