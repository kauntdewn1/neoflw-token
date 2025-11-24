// src/hooks/useThirdweb.ts
'use client';

import { useThirdwebContext } from '@thirdweb-dev/react';
import { THIRDWEB_CONFIG } from '../config/thirdweb';

/**
 * Hook para usar funcionalidades do Thirdweb
 * @returns Thirdweb context e configurações
 */
export function useThirdweb() {
  const thirdweb = useThirdwebContext();

  return {
    // Context do Thirdweb
    thirdweb,
    
    // Configurações
    clientId: THIRDWEB_CONFIG.clientId,
    walletAddress: THIRDWEB_CONFIG.walletAddress,
    walletLabel: THIRDWEB_CONFIG.walletLabel,
    
    // Status
    isConfigured: !!THIRDWEB_CONFIG.clientId,
    isConnected: !!thirdweb?.wallet,
  };
}

