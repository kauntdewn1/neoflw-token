// src/hooks/useClaim.ts
import { useAccount, useReadContract, useWriteContract, useWaitForTransactionReceipt } from 'wagmi';
import { CONTRACT_ADDRESSES, CLAIM_ABI } from '../config/contracts';
import { formatUnits } from 'viem';

/**
 * Hook para interagir com o contrato de Claim
 * @returns claimable amount, claim function e loading states
 */
export function useClaim() {
  const { address } = useAccount();

  // Ler amount disponível para claim
  const claimableQuery = useReadContract({
    address: CONTRACT_ADDRESSES.claim as `0x${string}`,
    abi: CLAIM_ABI,
    functionName: 'claimableAmount',
    args: address ? [address] : undefined,
    query: {
      enabled: !!address && !!CONTRACT_ADDRESSES.claim,
    },
  });

  // Verificar se já fez claim
  const hasClaimedQuery = useReadContract({
    address: CONTRACT_ADDRESSES.claim as `0x${string}`,
    abi: CLAIM_ABI,
    functionName: 'hasClaimed',
    args: address ? [address] : undefined,
    query: {
      enabled: !!address && !!CONTRACT_ADDRESSES.claim,
    },
  });

  // Saldo do contrato
  const contractBalanceQuery = useReadContract({
    address: CONTRACT_ADDRESSES.claim as `0x${string}`,
    abi: CLAIM_ABI,
    functionName: 'contractBalance',
    query: {
      enabled: !!CONTRACT_ADDRESSES.claim,
    },
  });

  // Escrever (claim)
  const { writeContract: claimTokens, data: claimHash, isPending: isClaiming } = useWriteContract();
  const { isLoading: isConfirming, isSuccess: isClaimSuccess } = 
    useWaitForTransactionReceipt({ hash: claimHash });

  /**
   * Reivindica tokens elegíveis
   */
  const handleClaim = async () => {
    if (!address || !CONTRACT_ADDRESSES.claim) throw new Error('Configuração inválida');
    
    await claimTokens({
      address: CONTRACT_ADDRESSES.claim as `0x${string}`,
      abi: CLAIM_ABI,
      functionName: 'claimTokens',
      args: [],
    });
  };

  return {
    // Dados
    claimableAmount: claimableQuery.data ? formatUnits(claimableQuery.data, 18) : '0',
    hasClaimed: hasClaimedQuery.data || false,
    contractBalance: contractBalanceQuery.data ? formatUnits(contractBalanceQuery.data, 18) : '0',
    
    // Estados
    isLoading: claimableQuery.isLoading || hasClaimedQuery.isLoading,
    isClaiming: isClaiming || isConfirming,
    isClaimSuccess,
    
    // Funções
    claim: handleClaim,
    refetch: claimableQuery.refetch,
  };
}

