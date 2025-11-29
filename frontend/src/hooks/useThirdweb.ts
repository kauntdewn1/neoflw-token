// src/hooks/useThirdweb.ts
'use client';

import { useCreateAccount } from '@thirdweb-dev/react'; 
import { THIRDWEB_CONFIG } from '../config/thirdweb';

/**
 * Hook para usar funcionalidades do Thirdweb
 * @returns Thirdweb context e configurações
 */
export function useThirdweb() {
  // Fix: Import actual ThirdwebClient class and use correctly
  // Import should be: import { ThirdwebClient } from 'thirdweb';
  const thirdwebClient = new (require('thirdweb').ThirdwebClient)(THIRDWEB_CONFIG.clientId);
  const createAccount = useCreateAccount(thirdwebClient);
  return {
    // Estado da wallet/account
    wallet: createAccount,
    account: createAccount,
    
    // Configurações
    clientId: THIRDWEB_CONFIG.clientId,
    walletAddress: THIRDWEB_CONFIG.walletAddress,
    walletLabel: THIRDWEB_CONFIG.walletLabel,
    
    // Status
    isConfigured: !!THIRDWEB_CONFIG.clientId,
    isConnected: !!createAccount,
  };
}

