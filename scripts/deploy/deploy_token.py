# scripts/deploy_token.py
from ape import accounts, project

def main():
    acct = accounts.load("neoflow-admin")
    initial_supply = 1_000_000_000 * 10**18  # 1 bilhão com 18 decimais
    
    print(f"🚀 Deploying NeoFlowToken...")
    print(f"📊 From: {acct.address}")
    print(f"💰 Initial Supply: {initial_supply / 10**18:,.0f} NEOFLW")
    print("")
    
    token = project.NeoFlowToken.deploy(initial_supply, sender=acct, auto_confirm=True)
    
    print("")
    print("=" * 60)
    print(f"✅ NEOFLW Token deployed at: {token.address}")
    print("=" * 60)
    print("")
    # Detectar rede
    network = acct.network.name if hasattr(acct, 'network') else 'mainnet'
    explorer_url = "https://etherscan.io" if network == "mainnet" else f"https://{network}.etherscan.io"
    
    print(f"🔗 Ver no Etherscan:")
    print(f"   {explorer_url}/address/{token.address}")
    print("")
    
    # Salvar endereço
    with open(".token_address.txt", "w") as f:
        f.write(token.address)
    
    return token.address

