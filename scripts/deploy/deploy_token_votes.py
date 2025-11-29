# scripts/deploy_token_votes.py
from ape import accounts, project, networks


def main():
    """
    Deploy do NeoFlowTokenVotes (token de governança com ERC20Votes + ContractMetadata)
    - Mesma supply do NeoFlowToken: 1 bilhão de tokens com 18 decimais
    - Rede alvo: Polygon Mainnet
    """
    acct = accounts.load("neoflow-admin")
    initial_supply = 1_000_000_000 * 10**18  # 1 bilhão com 18 decimais

    print("🚀 Deploying NeoFlowTokenVotes...")
    print(f"📊 From: {acct.address}")
    print(f"💰 Initial Supply: {initial_supply / 10**18:,.0f} NEOFLW (votes)")
    if networks.active_provider:
        print(f"🌐 Provider: {networks.active_provider.name}")
    print("")

    # Deploy com confirmação automática
    token_votes = project.NeoFlowTokenVotes.deploy(
        initial_supply,
        sender=acct,
        auto_confirm=True,
    )

    print("")
    print("=" * 60)
    print(f"✅ NeoFlowTokenVotes deployed at: {token_votes.address}")
    print("=" * 60)
    print("")

    # Detectar rede e explorer (Polygon vs outras)
    if networks.active_provider:
        ecosystem = (
            networks.active_provider.network.ecosystem.name
            if hasattr(networks.active_provider.network, "ecosystem")
            else None
        )
        chain_id = (
            networks.active_provider.chain_id
            if hasattr(networks.active_provider, "chain_id")
            else None
        )

        is_polygon = ecosystem == "polygon" or chain_id == 137

        if is_polygon:
            explorer_url = "https://polygonscan.com"
        else:
            explorer_url = "https://etherscan.io"
    else:
        explorer_url = "https://polygonscan.com"

    print("🔗 Ver no Explorer:")
    print(f"   {explorer_url}/address/{token_votes.address}")
    print("")

    # Salvar endereço
    with open(".token_votes_address.txt", "w") as f:
        f.write(token_votes.address)

    return token_votes.address


