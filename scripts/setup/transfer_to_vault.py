# scripts/setup/transfer_to_vault.py
# Script para transferir tokens para o contrato de StakingVault
#
# TOKENOMICS NEOFLW - Distribuição:
# Total Supply: 1,000,000,000 NEOFLW (100%)
#
# Gamificação & Rewards: 400M (40%)
#   ├─ Staking Rewards: 100M (10%) → StakingVault
#
# ESTRATÉGIA:
# - Staking Rewards (100M): Transferir para StakingVault
# - Pool de rewards para staking (10% APY, 6 meses lock)

from ape import accounts, project
import os
import sys

def main():
    acct = accounts.load("neoflow-admin")
    
    # Ler endereços dos arquivos
    token_file = "artifacts/addresses/.token_address.txt"
    vault_file = "artifacts/addresses/.vault_address.txt"
    
    if not os.path.exists(token_file):
        raise ValueError(f"Arquivo {token_file} não encontrado!")
    
    if not os.path.exists(vault_file):
        raise ValueError(f"Arquivo {vault_file} não encontrado!")
    
    with open(token_file, "r") as f:
        token_address = f.read().strip()
    
    with open(vault_file, "r") as f:
        vault_address = f.read().strip()
    
    print("=" * 60)
    print("💰 Transferindo Tokens para o StakingVault")
    print("=" * 60)
    print()
    print("📊 TOKENOMICS:")
    print("   Staking Rewards: 100M NEOFLW (10% do total supply)")
    print("   Gamificação & Rewards: 400M NEOFLW (40% do total supply)")
    print()
    print(f"📊 Token: {token_address}")
    print(f"🏦 Vault: {vault_address}")
    print()
    
    # Obter instâncias dos contratos
    token = project.NeoFlowToken.at(token_address)
    vault = project.StakingVault.at(vault_address)
    
    # Verificar saldo atual
    owner_balance = token.balanceOf(acct.address)
    vault_balance = token.balanceOf(vault_address)
    
    print(f"💰 Seu saldo atual: {owner_balance / 10**18:,.2f} NEOFLW")
    print(f"🏦 Saldo atual do Vault: {vault_balance / 10**18:,.2f} NEOFLW")
    print()
    
    # Quantidade a transferir (padrão: 100M conforme tokenomics)
    if len(sys.argv) > 1:
        try:
            amount_millions = float(sys.argv[1])
            amount_to_transfer = int(amount_millions * 1_000_000 * 10**18)
            print(f"📝 Quantidade customizada: {amount_millions}M NEOFLW")
        except ValueError:
            print(f"⚠️  Argumento inválido '{sys.argv[1]}', usando padrão de 100M")
            amount_to_transfer = 100_000_000 * 10**18
    else:
        # Padrão: 100M conforme tokenomics (Staking Rewards)
        amount_to_transfer = 100_000_000 * 10**18
        print("📝 Usando quantidade padrão (100M conforme tokenomics)")
    
    print()
    print(f"📤 Transferindo: {amount_to_transfer / 10**18:,.0f} NEOFLW")
    print(f"   ({amount_to_transfer / 10**18 / 1_000_000:.1f}M tokens = {amount_to_transfer / 10**18 / 1_000_000_000 * 100:.1f}% do total supply)")
    print()
    
    # Verificar se tem saldo suficiente
    if owner_balance < amount_to_transfer:
        raise ValueError(
            f"❌ Saldo insuficiente! Você tem {owner_balance / 10**18:,.2f} NEOFLW, "
            f"mas precisa de {amount_to_transfer / 10**18:,.0f} NEOFLW"
        )
    
    # Confirmar antes de transferir
    print("⚠️  ATENÇÃO: Você está prestes a transferir tokens para o StakingVault")
    print("   Certifique-se de que esta é a quantidade correta conforme sua estratégia!")
    print()
    
    # Transferir tokens
    print("⏳ Transferindo tokens...")
    print("⚠️  Você precisará confirmar a transação e digitar a senha da wallet")
    print()
    token.transfer(vault_address, amount_to_transfer, sender=acct, auto_confirm=True)
    
    print()
    print("=" * 60)
    print("✅ Transferência concluída com sucesso!")
    print("=" * 60)
    print()
    
    # Verificar saldo final
    new_owner_balance = token.balanceOf(acct.address)
    new_vault_balance = token.balanceOf(vault_address)
    
    print(f"💰 Seu saldo agora: {new_owner_balance / 10**18:,.2f} NEOFLW")
    print(f"🏦 Saldo do Vault agora: {new_vault_balance / 10**18:,.2f} NEOFLW")
    print()
    print("📋 Próximos passos:")
    print("   1. Usuários podem fazer stake de tokens")
    print("   2. Após 6 meses de lock, receberão 10% APY em rewards")
    print("   3. Os rewards serão pagos do pool de 100M tokens")
    print()

