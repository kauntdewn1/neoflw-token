# scripts/deploy/deploy_claim.py
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
            "  1. Passar como argumento: ape run deploy_claim -- <token_address>\n"
            "  2. Criar arquivo .token_address.txt com o endereço do token"
        )
    
    # Validar formato de endereço básico
    if not token_address.startswith("0x") or len(token_address) != 42:
        raise ValueError(f"Invalid token address format: {token_address}")
    
    print(f"🔗 Token address: {token_address}")
    print("📦 Deploying NeoFlowClaim...")
    if networks.active_provider:
        print(f"🌐 Provider: {networks.active_provider.name}")
    print("")
    
    # Obter instância do contrato de token para passar como parâmetro
    # O contrato espera IERC20, mas podemos passar o endereço diretamente
    token_contract = project.NeoFlowToken.at(token_address)
    
    # Deploy do contrato de claim passando a interface IERC20
    claim_contract = project.NeoFlowClaim.deploy(token_contract, sender=acct, auto_confirm=True)
    
    print("")
    print("=" * 60)
    print(f"✅ NeoFlowClaim deployed at: {claim_contract.address}")
    print(f"🔗 Token address: {token_address}")
    print("=" * 60)
    print("")
    print(f"🔗 Ver no Polygonscan:")
    print(f"   https://polygonscan.com/address/{claim_contract.address}")
    print("")
    print("⚠️  IMPORTANTE: Lembre-se de transferir tokens para o contrato!")
    print(f"   Transferir tokens via: token.transfer({claim_contract.address}, amount)")
    print("")
    
    # Salvar endereço do claim contract
    with open(".claim_address.txt", "w") as f:
        f.write(claim_contract.address)
    
    return claim_contract.address

