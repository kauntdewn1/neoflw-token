# scripts/setup_claim.py
# Script auxiliar para configurar o contrato de claim:
# 1. Transferir tokens para o contrato
# 2. Configurar whitelist de endereços elegíveis

from ape import accounts, project
import os
import sys

def main():
    acct = accounts.load("neoflow-admin")
    
    # Ler endereços dos arquivos
    token_address = None
    claim_address = None
    
    if os.path.exists(".token_address.txt"):
        with open(".token_address.txt", "r") as f:
            token_address = f.read().strip()
    
    if os.path.exists(".claim_address.txt"):
        with open(".claim_address.txt", "r") as f:
            claim_address = f.read().strip()
    
    # Permitir override via argumentos CLI
    if len(sys.argv) > 1:
        token_address = sys.argv[1]
    if len(sys.argv) > 2:
        claim_address = sys.argv[2]
    
    if not token_address or token_address == "0x...":
        raise ValueError("Token address required!")
    
    if not claim_address or claim_address == "0x...":
        raise ValueError("Claim contract address required!")
    
    # Validar formatos
    if not token_address.startswith("0x") or len(token_address) != 42:
        raise ValueError(f"Invalid token address format: {token_address}")
    if not claim_address.startswith("0x") or len(claim_address) != 42:
        raise ValueError(f"Invalid claim address format: {claim_address}")
    
    print(f"🔗 Token address: {token_address}")
    print(f"🔗 Claim contract address: {claim_address}")
    print("")
    
    # Obter instâncias dos contratos
    token = project.NeoFlowToken.at(token_address)
    claim = project.NeoFlowClaim.at(claim_address)
    
    # Verificar saldo atual do contrato
    claim_balance = token.balanceOf(claim_address)
    print(f"💰 Saldo atual do contrato de claim: {claim_balance / 10**18:.2f} NEOFLW")
    print("")
    
    # Perguntar se deseja transferir tokens
    print("=" * 60)
    print("OPÇÃO 1: Transferir tokens para o contrato")
    print("=" * 60)
    print(f"Exemplo: token.transfer({claim_address}, 50_000_000 * 10**18)")
    print("Execute manualmente ou modifique este script para automatizar.")
    print("")
    
    # Perguntar se deseja configurar whitelist
    print("=" * 60)
    print("OPÇÃO 2: Configurar whitelist")
    print("=" * 60)
    print("Exemplo de uso:")
    print("  claim.setWhitelist([user1, user2], [amount1, amount2], sender=acct)")
    print("")
    print("Ou use a função updateClaimableAmount para um usuário:")
    print("  claim.updateClaimableAmount(user_address, amount, sender=acct)")
    print("")
    
    # Exemplo prático
    print("=" * 60)
    print("EXEMPLO COMPLETO:")
    print("=" * 60)
    print("""
# 1. Transferir tokens para o contrato
amount_to_transfer = 50_000_000 * 10**18  # 50M tokens
token.transfer(claim_address, amount_to_transfer, sender=acct)

# 2. Configurar whitelist
users = ["0x...", "0x...", "0x..."]
amounts = [1000 * 10**18, 2000 * 10**18, 3000 * 10**18]
claim.setWhitelist(users, amounts, sender=acct)
""")
    
    return {
        "token": token,
        "claim": claim,
        "token_address": token_address,
        "claim_address": claim_address
    }

