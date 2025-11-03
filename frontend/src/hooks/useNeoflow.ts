// src/hooks/useNeoflow.ts
import { useAccount, useReadContract, useWriteContract, useWaitForTransactionReceipt } from 'wagmi';
import { CONTRACT_ADDRESSES, TOKEN_ABI } from '../config/contracts';
import { formatUnits, parseUnits } from 'viem';

/**
 * Hook para interagir com o token NEOFLW
 * @returns balance, totalSupply, burn function e loading states
 */
export function useNeoflow() {
  const { address } = useAccount();

  // Ler balance do usuário
  const { data: balance, isLoading: balanceLoading, refetch: refetchBalance } = useReadContract({
    address: CONTRACT_ADDRESSES.token as `0x${string}`,
    abi: TOKEN_ABI,
    functionName: 'balanceOf',
    args: address ? [address] : undefined,
    query: {
      enabled: !!address,
    },
  });

  // Ler total supply
  const { data: totalSupply, isLoading: supplyLoading } = useReadContract({
    address: CONTRACT_ADDRESSES.token as `0x${string}`,
    abi: TOKEN_ABI,
    functionName: 'totalSupply',
  });

  // Escrever (burn)
  const { 
    writeContract: burn, 
    data: burnHash, 
    isPending: isBurning 
  } = useWriteContract();

  const { isLoading: isConfirming, isSuccess: isBurnSuccess } = 
    useWaitForTransactionReceipt({
      hash: burnHash,
    });

  /**
   * Queima tokens
   * @param amount Quantidade em formato humano (ex: "100.5")
   */
  const handleBurn = async (amount: string) => {
    if (!address) throw new Error('Conecte sua wallet');
    
    const amountWei = parseUnits(amount, 18);
    
    await burn({
      address: CONTRACT_ADDRESSES.token as `0x${string}`,
      abi: TOKEN_ABI,
      functionName: 'burn',
      args: [amountWei],
    });
  };

  return {
    // Dados
    balance: balance ? formatUnits(balance, 18) : '0',
    totalSupply: totalSupply ? formatUnits(totalSupply, 18) : '0',
    
    // Estados
    balanceLoading,
    supplyLoading,
    isBurning: isBurning || isConfirming,
    isBurnSuccess,
    
    // Funções
    burn: handleBurn,
    refetchBalance,
  };
}

