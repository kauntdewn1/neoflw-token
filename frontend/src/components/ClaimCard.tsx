// src/components/ClaimCard.tsx
'use client';

import { useClaim } from '../hooks/useClaim';

export function ClaimCard() {
  const {
    claimableAmount,
    hasClaimed,
    contractBalance,
    isLoading,
    isClaiming,
    isClaimSuccess,
    claim,
  } = useClaim();

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
      <h2>Claim de Tokens</h2>
      
      <div className="info">
        <div>
          <span>Saldo do Contrato:</span>
          <strong>{parseFloat(contractBalance).toLocaleString()} NEOFLW</strong>
        </div>
        <div>
          <span>Disponível para Claim:</span>
          <strong>{parseFloat(claimableAmount).toLocaleString()} NEOFLW</strong>
        </div>
      </div>

      {hasClaimed ? (
        <p>Você já reivindicou seus tokens.</p>
      ) : parseFloat(claimableAmount) > 0 ? (
        <div>
          <button onClick={handleClaim} disabled={isClaiming}>
            {isClaiming ? 'Reivindicando...' : 'Reivindicar Tokens'}
          </button>
          {isClaimSuccess && (
            <p className="success">Tokens reivindicados com sucesso!</p>
          )}
        </div>
      ) : (
        <p>Você não é elegível para claim.</p>
      )}
    </div>
  );
}

