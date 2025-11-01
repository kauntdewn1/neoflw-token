# scripts/deploy_token_direct.py
# Deploy direto usando Web3 (bypassa problemas de RPC alternativo)

from ape import accounts, project
from ape.api.networks import NetworkAPI

def main():
    print("🚀 Deploy direto do token NEOFLW...")
    print("")
    
    # Carregar conta
    acct = accounts.load("neoflow-admin")
    print(f"✅ Conta carregada: {acct.address}")
    
    # Garantir que está usando Alchemy
    print("🔗 Conectando via Alchemy RPC...")
    
    initial_supply = 1_000_000_000 * 10**18  # 1 bilhão com 18 decimais
    
    try:
        print("📦 Fazendo deploy do contrato...")
        token = project.NeoFlowToken.deploy(initial_supply, sender=acct)
        print("")
        print("=" * 60)
        print(f"✅ NEOFLW Token deployed at: {token.address}")
        print("=" * 60)
        print("")
        print(f"🔗 Ver no Etherscan:")
        print(f"   https://sepolia.etherscan.io/address/{token.address}")
        print("")
        
        # Salvar endereço para uso futuro
        with open(".token_address.txt", "w") as f:
            f.write(token.address)
        
        return token.address
        
    except Exception as e:
        print(f"❌ Erro no deploy: {e}")
        print("")
        print("💡 Tente novamente em alguns minutos (rate limiting)")
        raise

