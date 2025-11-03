// src/components/StakingCard.tsx
'use client';

import { useStakingVault } from '../hooks/useStakingVault';
import { useState } from 'react';

export function StakingCard() {
  const {
    stakeInfo,
    timeLeft,
    totalStaked,
    balance,
    isLoading,
    isStaking,
    isStakeSuccess,
    isClaiming,
    isClaimSuccess,
    isApproving,
    isApproveSuccess,
    approve,
    stake,
    claim,
  } = useStakingVault();
  
  const [stakeAmount, setStakeAmount] = useState('');
  const [needsApproval, setNeedsApproval] = useState(true);

  const formatTime = (seconds: number) => {
    if (seconds === 0) return 'Pronto para claim!';
    const days = Math.floor(seconds / 86400);
    const hours = Math.floor((seconds % 86400) / 3600);
    return `${days}d ${hours}h`;
  };

  const handleApprove = async () => {
    try {
      await approve(stakeAmount);
      setNeedsApproval(false);
    } catch (error) {
      console.error('Erro ao aprovar:', error);
    }
  };

  const handleStake = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!stakeAmount || parseFloat(stakeAmount) <= 0) return;
    
    try {
      if (needsApproval) {
        await handleApprove();
        return;
      }
      await stake(stakeAmount);
      setStakeAmount('');
    } catch (error) {
      console.error('Erro ao fazer stake:', error);
    }
  };

  const handleClaim = async () => {
    try {
      await claim();
    } catch (error) {
      console.error('Erro ao reivindicar:', error);
    }
  };

  if (isLoading) {
    return <div className="card">Carregando...</div>;
  }

  return (
    <div className="card">
      <h2>Staking Vault</h2>
      
      <div className="info">
        <div>
          <span>Total Staked:</span>
          <strong>{parseFloat(totalStaked).toLocaleString()} NEOFLW</strong>
        </div>
        {stakeInfo && (
          <>
            <div>
              <span>Seu Stake:</span>
              <strong>{parseFloat(stakeInfo.amount).toLocaleString()} NEOFLW</strong>
            </div>
            <div>
              <span>Tempo Restante:</span>
              <strong>{formatTime(timeLeft)}</strong>
            </div>
          </>
        )}
      </div>

      {!stakeInfo ? (
        <form onSubmit={handleStake} className="stake-form">
          <h3>Fazer Stake (Lock 6 meses, 10% reward)</h3>
          <input
            type="number"
            step="0.000001"
            placeholder="Quantidade"
            value={stakeAmount}
            onChange={(e) => setStakeAmount(e.target.value)}
            disabled={isStaking || isApproving}
            max={balance}
          />
          <div className="balance-info">
            Disponível: {parseFloat(balance).toLocaleString()} NEOFLW
          </div>
          {needsApproval && !isApproveSuccess ? (
            <button type="button" onClick={handleApprove} disabled={isApproving}>
              {isApproving ? 'Aprovando...' : 'Aprovar Tokens'}
            </button>
          ) : (
            <button type="submit" disabled={isStaking || !stakeAmount}>
              {isStaking ? 'Fazendo Stake...' : 'Fazer Stake'}
            </button>
          )}
          {isStakeSuccess && (
            <p className="success">Stake realizado com sucesso!</p>
          )}
        </form>
      ) : (
        <div className="claim-section">
          {stakeInfo.claimed ? (
            <p>Você já reivindicou seus tokens.</p>
          ) : timeLeft > 0 ? (
            <p>Aguarde o período de lock: {formatTime(timeLeft)}</p>
          ) : (
            <div>
              <p>Pronto para reivindicar!</p>
              <button onClick={handleClaim} disabled={isClaiming}>
                {isClaiming ? 'Reivindicando...' : 'Reivindicar Tokens + Reward'}
              </button>
              {isClaimSuccess && (
                <p className="success">Tokens reivindicados com sucesso!</p>
              )}
            </div>
          )}
        </div>
      )}
    </div>
  );
}

