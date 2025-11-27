# scripts/setup/transfer_100m_to_claim_and_vault.py
# Script para transferir 100M tokens para Claim e 100M para Vault
# Executa ambas as transferências em sequência

from ape import accounts, project
import os

def main():
    acct = accounts.load("neoflow-admin")
    
    # Ler endereços dos arquivos
    token_file = "artifacts/addresses/.token_address.txt"
    claim_file = "artifacts/addresses/.claim_address.txt"
    vault_file = "artifacts/addresses/.vault_address.txt"
    
    for file_path in [token_file, claim_file, vault_file]:
        if not os.path.exists(file_path):
            raise ValueError(f"Arquivo {file_path} não encontrado!")
    
    with open(token_file, "r") as f:
        token_address = f.read().strip()
    
    with open(claim_file, "r") as f:
        claim_address = f.read().strip()
    
    with open(vault_file, "r") as f:
        vault_address = f.read().strip()
    
    print("=" * 70)
    print("💰 DISTRIBUIÇÃO DE TOKENS - CLAIM E VAULT")
    print("=" * 70)
    print()
    print(f"📊 Token: {token_address}")
    print(f"🎁 Claim: {claim_address}")
    print(f"🏦 Vault: {vault_address}")
    print()
    
    # Obter instâncias dos contratos
    token = project.NeoFlowToken.at(token_address)
    
    # Verificar saldo atual
    owner_balance = token.balanceOf(acct.address)
    claim_balance = token.balanceOf(claim_address)
    vault_balance = token.balanceOf(vault_address)
    
    print(f"💰 Saldo atual na wallet: {owner_balance / 10**18:,.2f} NEOFLW")
    print(f"🎁 Saldo atual do Claim: {claim_balance / 10**18:,.2f} NEOFLW")
    print(f"🏦 Saldo atual do Vault: {vault_balance / 10**18:,.2f} NEOFLW")
    print()
    
    # Quantidade a transferir (100M para cada)
    amount_to_transfer = 100_000_000 * 10**18  # 100M tokens
    
    total_needed = amount_to_transfer * 2  # 200M total
    
    if owner_balance < total_needed:
        raise ValueError(
            f"❌ Saldo insuficiente! Você tem {owner_balance / 10**18:,.2f} NEOFLW, "
            f"mas precisa de {total_needed / 10**18:,.0f} NEOFLW (100M para Claim + 100M para Vault)"
        )
    
    print("=" * 70)
    print("📤 TRANSFERÊNCIAS PLANEJADAS:")
    print("=" * 70)
    print(f"1. Claim: {amount_to_transfer / 10**18:,.0f}M NEOFLW (10% do total supply)")
    print(f"2. Vault: {amount_to_transfer / 10**18:,.0f}M NEOFLW (10% do total supply)")
    print(f"Total: {total_needed / 10**18:,.0f}M NEOFLW (20% do total supply)")
    print()
    print("⚠️  ATENÇÃO: Você precisará confirmar cada transação e digitar a senha da wallet")
    print()
    
    # Transferir para Claim
    print("=" * 70)
    print("📤 TRANSFERINDO PARA CLAIM...")
    print("=" * 70)
    print(f"Quantidade: {amount_to_transfer / 10**18:,.0f}M NEOFLW")
    print()
    token.transfer(claim_address, amount_to_transfer, sender=acct, auto_confirm=True)
    
    # Verificar após primeira transferência
    new_claim_balance = token.balanceOf(claim_address)
    print(f"✅ Transferência para Claim concluída!")
    print(f"   Saldo do Claim agora: {new_claim_balance / 10**18:,.2f}M NEOFLW")
    print()
    
    # Transferir para Vault
    print("=" * 70)
    print("📤 TRANSFERINDO PARA VAULT...")
    print("=" * 70)
    print(f"Quantidade: {amount_to_transfer / 10**18:,.0f}M NEOFLW")
    print()
    token.transfer(vault_address, amount_to_transfer, sender=acct, auto_confirm=True)
    
    # Verificar após segunda transferência
    new_vault_balance = token.balanceOf(vault_address)
    print(f"✅ Transferência para Vault concluída!")
    print(f"   Saldo do Vault agora: {new_vault_balance / 10**18:,.2f}M NEOFLW")
    print()
    
    # Resumo final
    print("=" * 70)
    print("✅ DISTRIBUIÇÃO CONCLUÍDA!")
    print("=" * 70)
    print()
    
    final_owner_balance = token.balanceOf(acct.address)
    final_claim_balance = token.balanceOf(claim_address)
    final_vault_balance = token.balanceOf(vault_address)
    
    print(f"💰 Saldo final na wallet: {final_owner_balance / 10**18:,.2f}M NEOFLW")
    print(f"🎁 Saldo final do Claim: {final_claim_balance / 10**18:,.2f}M NEOFLW")
    print(f"🏦 Saldo final do Vault: {final_vault_balance / 10**18:,.2f}M NEOFLW")
    print()
    print("📋 Próximos passos:")
    print("   1. Configurar whitelist no NeoFlowClaim")
    print("   2. Usuários podem fazer stake no StakingVault")
    print("   3. Após 6 meses de lock, receberão 10% APY em rewards")
    print()

