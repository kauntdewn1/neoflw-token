# scripts/deploy_vault.py
from ape import accounts, project, networks
import os
import sys

def main():
    acct = accounts.load("neoflow-admin")
    
    # Tentar ler de arquivo primeiro
    token_address = None
    if os.path.exists(".token_address.txt"):
        with open(".token_address.txt", "r") as f:
            token_address = f.read().strip()
    
    # Se não existir, tentar argumento CLI
    if not token_address or token_address == "0x...":
        if len(sys.argv) > 1:
            token_address = sys.argv[1]
    
    if not token_address or token_address == "0x...":
        raise ValueError(
            "Token address required!\n"
            "Opções:\n"
            "  1. Passar como argumento: ape run deploy_vault -- <token_address>\n"
            "  2. Criar arquivo .token_address.txt com o endereço do token"
        )
    
    # Validar formato de endereço básico
    if not token_address.startswith("0x") or len(token_address) != 42:
        raise ValueError(f"Invalid token address format: {token_address}")
    
    print(f"🔗 Token address: {token_address}")
    print("📦 Deploying StakingVault...")
    if networks.active_provider:
        print(f"🌐 Provider: {networks.active_provider.name}")
    print("")
    
    vault = project.StakingVault.deploy(token_address, sender=acct, auto_confirm=True)
    
    print("")
    print("=" * 60)
    print(f"✅ StakingVault deployed at: {vault.address}")
    print(f"🔗 Token address: {token_address}")
    print("=" * 60)
    print("")
    print(f"🔗 Ver no Polygonscan:")
    print(f"   https://polygonscan.com/address/{vault.address}")
    print("")
    
    # Salvar endereço do vault
    with open(".vault_address.txt", "w") as f:
        f.write(vault.address)
    
    return vault.address

