# scripts/transfer_to_claim.py
# Script para transferir tokens para o contrato de Claim

from ape import accounts, project
import os

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
    
    # Quantidade a transferir (50M tokens)
    amount_to_transfer = 50_000_000 * 10**18
    
    print(f"📤 Transferindo: {amount_to_transfer / 10**18:,.0f} NEOFLW")
    print()
    
    # Verificar se tem saldo suficiente
    if owner_balance < amount_to_transfer:
        raise ValueError(
            f"Saldo insuficiente! Você tem {owner_balance / 10**18:,.2f} NEOFLW, "
            f"mas precisa de {amount_to_transfer / 10**18:,.0f} NEOFLW"
        )
    
    # Transferir tokens
    print("⏳ Transferindo tokens...")
    token.transfer(claim_address, amount_to_transfer, sender=acct)
    
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
    print("📋 Próximo passo: Configurar whitelist de endereços elegíveis")
    print("   Use: ape run setup_claim ou veja CLAIM_SETUP.md")
    print()

