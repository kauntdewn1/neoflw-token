# scripts/transfer_to_claim.py
# Script para transferir tokens para o contrato de Claim
#
# TOKENOMICS NEOFLW - Distribuição:
# Total Supply: 1,000,000,000 NEOFLW (100%)
#
# Comunidade & Airdrop: 250M (25%)
#   ├─ Initial Airdrop: 100M (10%) → NeoFlowClaim
#   ├─ Community Rewards: 75M (7.5%)
#   ├─ Early Adopters: 50M (5%)
#   └─ Marketing & Partnerships: 25M (2.5%)
#
# ESTRATÉGIA:
# - Initial Airdrop (100M): Transferir para NeoFlowClaim
# - Pode ser transferido gradualmente conforme necessidade
# - Recomendado: Transferir 100M inicialmente ou conforme whitelist cresce

from ape import accounts, project
import os
import sys

def main():
    acct = accounts.load("neoflow-admin")
    
    # Ler endereços dos arquivos
    if not os.path.exists(".token_address.txt"):
        raise ValueError("Arquivo .token_address.txt não encontrado!")
    
    if not os.path.exists(".claim_address.txt"):
        raise ValueError("Arquivo .claim_address.txt não encontrado!")
    
    with open(".token_address.txt", "r") as f:
        token_address = f.read().strip()
    
    with open(".claim_address.txt", "r") as f:
        claim_address = f.read().strip()
    
    print("=" * 60)
    print("💰 Transferindo Tokens para o Contrato de Claim")
    print("=" * 60)
    print()
    print("📊 TOKENOMICS:")
    print("   Initial Airdrop: 100M NEOFLW (10% do total supply)")
    print("   Comunidade & Airdrop: 250M NEOFLW (25% do total supply)")
    print()
    print(f"📊 Token: {token_address}")
    print(f"🎁 Claim: {claim_address}")
    print()
    
    # Obter instâncias dos contratos
    token = project.NeoFlowToken.at(token_address)
    claim = project.NeoFlowClaim.at(claim_address)
    
    # Verificar saldo atual
    owner_balance = token.balanceOf(acct.address)
    claim_balance = token.balanceOf(claim_address)
    
    print(f"💰 Seu saldo atual: {owner_balance / 10**18:,.2f} NEOFLW")
    print(f"🎁 Saldo atual do Claim: {claim_balance / 10**18:,.2f} NEOFLW")
    print()
    
    # Quantidade a transferir (padrão: 100M conforme tokenomics)
    # Pode ser sobrescrito via argumento CLI: ape run transfer_to_claim -- <amount_in_millions>
    if len(sys.argv) > 1:
        try:
            amount_millions = float(sys.argv[1])
            amount_to_transfer = int(amount_millions * 1_000_000 * 10**18)
            print(f"📝 Quantidade customizada: {amount_millions}M NEOFLW")
        except ValueError:
            print(f"⚠️  Argumento inválido '{sys.argv[1]}', usando padrão de 100M")
            amount_to_transfer = 100_000_000 * 10**18
    else:
        # Padrão: 100M conforme tokenomics (Initial Airdrop)
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
    print("⚠️  ATENÇÃO: Você está prestes a transferir tokens para o contrato de Claim")
    print("   Certifique-se de que esta é a quantidade correta conforme sua estratégia!")
    print()
    
    # Transferir tokens
    print("⏳ Transferindo tokens...")
    print("⚠️  Você precisará confirmar a transação e digitar a senha da wallet")
    print()
    token.transfer(claim_address, amount_to_transfer, sender=acct, auto_confirm=True)
    
    print()
    print("=" * 60)
    print("✅ Transferência concluída com sucesso!")
    print("=" * 60)
    print()
    
    # Verificar saldo final
    new_owner_balance = token.balanceOf(acct.address)
    new_claim_balance = token.balanceOf(claim_address)
    
    print(f"💰 Seu saldo agora: {new_owner_balance / 10**18:,.2f} NEOFLW")
    print(f"🎁 Saldo do Claim agora: {new_claim_balance / 10**18:,.2f} NEOFLW")
    print()
    print("📋 Próximos passos:")
    print("   1. Configurar whitelist de endereços elegíveis")
    print("      Use: ape run scripts/setup/setup_whitelist --network polygon:mainnet")
    print("   2. Ou configurar manualmente via: claim.setWhitelist([users], [amounts])")
    print()
    print("📚 Documentação completa: docs/deploy/CLAIM_SETUP.md")
    print()

