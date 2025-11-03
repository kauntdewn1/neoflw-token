// src/components/TokenCard.tsx
'use client';

import { useNeoflow } from '../hooks/useNeoflow';
import { useState } from 'react';

export function TokenCard() {
  const { balance, totalSupply, burn, isBurning, isBurnSuccess } = useNeoflow();
  const [burnAmount, setBurnAmount] = useState('');

  const handleBurn = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!burnAmount || parseFloat(burnAmount) <= 0) return;
    
    try {
      await burn(burnAmount);
      setBurnAmount('');
    } catch (error) {
      console.error('Erro ao queimar tokens:', error);
    }
  };

  return (
    <div className="card">
      <h2>Token NEOFLW</h2>
      
      <div className="info">
        <div>
          <span>Seu Saldo:</span>
          <strong>{parseFloat(balance).toLocaleString()} NEOFLW</strong>
        </div>
        <div>
          <span>Total Supply:</span>
          <strong>{parseFloat(totalSupply).toLocaleString()} NEOFLW</strong>
        </div>
      </div>

      <form onSubmit={handleBurn} className="burn-form">
        <h3>Queimar Tokens</h3>
        <input
          type="number"
          step="0.000001"
          placeholder="Quantidade"
          value={burnAmount}
          onChange={(e) => setBurnAmount(e.target.value)}
          disabled={isBurning}
        />
        <button type="submit" disabled={isBurning || !burnAmount}>
          {isBurning ? 'Queimando...' : 'Queimar'}
        </button>
        {isBurnSuccess && (
          <p className="success">Tokens queimados com sucesso!</p>
        )}
      </form>
    </div>
  );
}

