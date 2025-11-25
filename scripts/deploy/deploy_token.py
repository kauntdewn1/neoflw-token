# scripts/deploy_token.py
from ape import accounts, project, networks

def main():
    acct = accounts.load("neoflow-admin")
    initial_supply = 1_000_000_000 * 10**18  # 1 bilhão com 18 decimais
    
    print(f"🚀 Deploying NeoFlowToken...")
    print(f"📊 From: {acct.address}")
    print(f"💰 Initial Supply: {initial_supply / 10**18:,.0f} NEOFLW")
    if networks.active_provider:
        print(f"🌐 Provider: {networks.active_provider.name}")
    print("")
    
    # Deploy com confirmação automática
    token = project.NeoFlowToken.deploy(initial_supply, sender=acct, auto_confirm=True)
    
    print("")
    print("=" * 60)
    print(f"✅ NEOFLW Token deployed at: {token.address}")
    print("=" * 60)
    print("")
    
    # Detectar rede e explorer (apenas mainnet)
    if networks.active_provider:
        # Verificar ecosystem (mais confiável que network.name)
        ecosystem = networks.active_provider.network.ecosystem.name if hasattr(networks.active_provider.network, 'ecosystem') else None
        chain_id = networks.active_provider.chain_id if hasattr(networks.active_provider, 'chain_id') else None
        
        # Polygon mainnet (137) ou ecosystem "polygon"
        is_polygon = ecosystem == "polygon" or chain_id == 137
        
        if is_polygon:
            explorer_url = "https://polygonscan.com"
        else:
            # Ethereum mainnet ou outras redes
            explorer_url = "https://etherscan.io"
    else:
        # Fallback padrão para Polygon
        explorer_url = "https://polygonscan.com"
    
    print(f"🔗 Ver no Explorer:")
    print(f"   {explorer_url}/address/{token.address}")
    print("")
    
    # Salvar endereço
    with open(".token_address.txt", "w") as f:
        f.write(token.address)
    
    return token.address

