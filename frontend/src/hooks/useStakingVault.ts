// src/hooks/useStakingVault.ts
import { useAccount, useReadContract, useWriteContract, useWaitForTransactionReceipt } from 'wagmi';
import { useReadContracts } from 'wagmi';
import { CONTRACT_ADDRESSES, VAULT_ABI, TOKEN_ABI } from '../config/contracts';
import { formatUnits, parseUnits } from 'viem';

/**
 * Hook para interagir com o StakingVault
 * @returns stake info, stake/claim functions e loading states
 */
export function useStakingVault() {
  const { address } = useAccount();

  // Ler informações do stake do usuário
  const stakeInfoQuery = useReadContract({
    address: CONTRACT_ADDRESSES.vault as `0x${string}`,
    abi: VAULT_ABI,
    functionName: 'stakes',
    args: address ? [address] : undefined,
    query: {
      enabled: !!address && !!CONTRACT_ADDRESSES.vault,
    },
  });

  // Ler tempo restante
  const timeLeftQuery = useReadContract({
    address: CONTRACT_ADDRESSES.vault as `0x${string}`,
    abi: VAULT_ABI,
    functionName: 'timeLeft',
    args: address ? [address] : undefined,
    query: {
      enabled: !!address && !!CONTRACT_ADDRESSES.vault,
    },
  });

  // Ler total staked
  const totalStakedQuery = useReadContract({
    address: CONTRACT_ADDRESSES.vault as `0x${string}`,
    abi: VAULT_ABI,
    functionName: 'getTotalStaked',
    query: {
      enabled: !!CONTRACT_ADDRESSES.vault,
    },
  });

  // Verificar aprovação necessária para stake
  const approvalQuery = useReadContract({
    address: CONTRACT_ADDRESSES.token as `0x${string}`,
    abi: TOKEN_ABI,
    functionName: 'balanceOf',
    args: address ? [address] : undefined,
    query: {
      enabled: !!address,
    },
  });

  // Escrever (stake)
  const { writeContract: stake, data: stakeHash, isPending: isStaking } = useWriteContract();
  const { isLoading: isStakeConfirming, isSuccess: isStakeSuccess } = 
    useWaitForTransactionReceipt({ hash: stakeHash });

  // Escrever (claim)
  const { writeContract: claim, data: claimHash, isPending: isClaiming } = useWriteContract();
  const { isLoading: isClaimConfirming, isSuccess: isClaimSuccess } = 
    useWaitForTransactionReceipt({ hash: claimHash });

  // Escrever (approve) - necessário antes de fazer stake
  const { writeContract: approve, data: approveHash, isPending: isApproving } = useWriteContract();
  const { isLoading: isApproveConfirming, isSuccess: isApproveSuccess } = 
    useWaitForTransactionReceipt({ hash: approveHash });

  /**
   * Aprova tokens para o vault (necessário antes de fazer stake)
   */
  const handleApprove = async (amount: string) => {
    if (!address || !CONTRACT_ADDRESSES.vault) throw new Error('Configuração inválida');
    
    const amountWei = parseUnits(amount, 18);
    
    await approve({
      address: CONTRACT_ADDRESSES.token as `0x${string}`,
      abi: TOKEN_ABI,
      functionName: 'approve',
      args: [CONTRACT_ADDRESSES.vault as `0x${string}`, amountWei],
    });
  };

  /**
   * Faz stake de tokens
   */
  const handleStake = async (amount: string) => {
    if (!address || !CONTRACT_ADDRESSES.vault) throw new Error('Configuração inválida');
    
    const amountWei = parseUnits(amount, 18);
    
    await stake({
      address: CONTRACT_ADDRESSES.vault as `0x${string}`,
      abi: VAULT_ABI,
      functionName: 'stake',
      args: [amountWei],
    });
  };

  /**
   * Reivindica tokens após período de lock
   */
  const handleClaim = async () => {
    if (!address || !CONTRACT_ADDRESSES.vault) throw new Error('Configuração inválida');
    
    await claim({
      address: CONTRACT_ADDRESSES.vault as `0x${string}`,
      abi: VAULT_ABI,
      functionName: 'claim',
      args: [],
    });
  };

  const stakeInfo = stakeInfoQuery.data as [bigint, bigint, boolean] | undefined;

  return {
    // Dados
    stakeInfo: stakeInfo ? {
      amount: formatUnits(stakeInfo[0], 18),
      startTime: Number(stakeInfo[1]),
      claimed: stakeInfo[2],
    } : null,
    timeLeft: timeLeftQuery.data ? Number(timeLeftQuery.data) : 0,
    totalStaked: totalStakedQuery.data ? formatUnits(totalStakedQuery.data, 18) : '0',
    balance: approvalQuery.data ? formatUnits(approvalQuery.data, 18) : '0',
    
    // Estados
    isLoading: stakeInfoQuery.isLoading || timeLeftQuery.isLoading,
    isStaking: isStaking || isStakeConfirming,
    isStakeSuccess,
    isClaiming: isClaiming || isClaimConfirming,
    isClaimSuccess,
    isApproving: isApproving || isApproveConfirming,
    isApproveSuccess,
    
    // Funções
    approve: handleApprove,
    stake: handleStake,
    claim: handleClaim,
    refetch: stakeInfoQuery.refetch,
  };
}

