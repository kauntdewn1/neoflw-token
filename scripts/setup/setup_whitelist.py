# scripts/setup_whitelist.py
# Script para configurar whitelist de endereços elegíveis no Claim

from ape import accounts, project
import os

def main():
    acct = accounts.load("neoflow-admin")
    
    # Ler endereços
    if not os.path.exists(".claim_address.txt"):
        raise ValueError("Arquivo .claim_address.txt não encontrado!")
    
    with open(".claim_address.txt", "r") as f:
        claim_address = f.read().strip()
    
    claim = project.NeoFlowClaim.at(claim_address)
    
    print("=" * 60)
    print("📝 Configurar Whitelist - NeoFlowClaim")
    print("=" * 60)
    print()
    print(f"🎁 Contrato de Claim: {claim_address}")
    print()
    
    # Exemplo de configuração
    print("📋 Exemplo de configuração:")
    print()
    print("users = [")
    print('    "0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb",')
    print('    "0x8ba1f109551bD432803012645Hac136c22C2bF5c",')
    print('    "0x1234567890123456789012345678901234567890",')
    print("]")
    print()
    print("amounts = [")
    print("    1000 * 10**18,  # 1000 tokens")
    print("    2000 * 10**18,  # 2000 tokens")
    print("    5000 * 10**18,  # 5000 tokens")
    print("]")
    print()
    print("claim.setWhitelist(users, amounts, sender=acct)")
    print()
    print("=" * 60)
    print("💡 Para configurar agora, modifique este script ou use:")
    print("   ape console --network ethereum:sepolia")
    print("=" * 60)
    print()
    
    # Verificar saldo do contrato
    claim_balance = claim.contractBalance()
    print(f"💰 Saldo disponível no Claim: {claim_balance / 10**18:,.2f} NEOFLW")
    print()
    
    return {
        "claim": claim,
        "claim_address": claim_address,
        "available_balance": claim_balance
    }

