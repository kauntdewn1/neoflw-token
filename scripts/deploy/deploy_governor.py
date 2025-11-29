# scripts/deploy_governor.py
from ape import accounts, project, networks
from ape.api import ReceiptAPI

def main():
    """
    Deploy do sistema de DAO Governance
    
    Requisitos:
    1. Token com suporte a votação (NeoFlowTokenVotes) já deployado
    2. TimelockController já deployado (ou será criado aqui)
    """
    acct = accounts.load("neoflow-admin")
    
    print("🚀 Deploying DAO Governance System...")
    print(f"📊 From: {acct.address}")
    print("")
    
    # Parâmetros de governança
    VOTING_DELAY = 1  # 1 bloco de delay antes de votação começar
    VOTING_PERIOD = 50400  # ~7 dias em blocos (12s por bloco)
    PROPOSAL_THRESHOLD = 100_000 * 10**18  # 100k tokens mínimos para propor
    QUORUM_PERCENTAGE = 4  # 4% do supply precisa votar
    
    # 1. Deploy TimelockController (se não existir)
    print("1️⃣ Deploying TimelockController...")
    # Min delay: 1 dia (86400 segundos)
    MIN_DELAY = 86400
    timelock_proposers = [acct.address]  # Quem pode propor
    timelock_executors = [acct.address]   # Quem pode executar
    timelock_admin = acct.address        # Admin (será renunciado depois)
    
    # Usamos o wrapper local NeoFlowTimelockController para evitar conflito
    # de nome com o TimelockController da dependência OpenZeppelin.
    timelock = project.NeoFlowTimelockController.deploy(
        MIN_DELAY,
        timelock_proposers,
        timelock_executors,
        timelock_admin,
        sender=acct,
        auto_confirm=True
    )
    
    print(f"   ✅ TimelockController deployed: {timelock.address}")
    print("")
    
    # 2. Obter endereço do token (assumindo que já foi deployado)
    # Prioridade: .token_votes_address.txt -> env -> erro explícito
    token_address = None
    try:
        with open(".token_votes_address.txt", "r") as f:
            token_address = f.read().strip()
    except FileNotFoundError:
        token_address = None

    if not token_address:
        # Tentar via variável de ambiente
        import os

        token_address = os.getenv("TOKEN_VOTES_ADDRESS", "").strip()

    if not token_address or not token_address.startswith("0x") or len(token_address) != 42:
        raise ValueError(
            "Endereço do token de votos é obrigatório e deve estar em .token_votes_address.txt "
            "ou na variável de ambiente TOKEN_VOTES_ADDRESS"
        )
    
    token = project.NeoFlowTokenVotes.at(token_address)
    print(f"   📝 Token address: {token_address}")
    print("")
    
    # 3. Deploy Governor
    print("2️⃣ Deploying DaoGovernor...")
    governor = project.DaoGovernor.deploy(
        token,                    # ERC20Votes token
        timelock,                 # TimelockController
        VOTING_DELAY,
        VOTING_PERIOD,
        PROPOSAL_THRESHOLD,
        QUORUM_PERCENTAGE,
        sender=acct,
        auto_confirm=True
    )
    
    print(f"   ✅ DaoGovernor deployed: {governor.address}")
    print("")
    
    # 4. Configurar roles no Timelock
    print("3️⃣ Configurando roles no Timelock...")
    # O Governor precisa ser proposer e executor
    PROPOSER_ROLE = timelock.PROPOSER_ROLE()
    EXECUTOR_ROLE = timelock.EXECUTOR_ROLE()
    CANCELLER_ROLE = timelock.CANCELLER_ROLE()
    
    timelock.grantRole(PROPOSER_ROLE, governor.address, sender=acct)
    timelock.grantRole(EXECUTOR_ROLE, governor.address, sender=acct)
    timelock.grantRole(CANCELLER_ROLE, governor.address, sender=acct)
    
    print("   ✅ Roles configuradas")
    print("")
    
    # 5. Renunciar admin role (opcional - para descentralização)
    print("4️⃣ Renunciando admin role do Timelock...")
    ADMIN_ROLE = timelock.DEFAULT_ADMIN_ROLE()
    timelock.renounceRole(ADMIN_ROLE, acct.address, sender=acct)
    print("   ✅ Admin role renunciado (Timelock agora é controlado pelo Governor)")
    print("")
    
    # Salvar endereços
    with open(".governor_address.txt", "w") as f:
        f.write(governor.address)
    
    with open(".timelock_address.txt", "w") as f:
        f.write(timelock.address)
    
    print("=" * 60)
    print("✅ DAO Governance System deployado com sucesso!")
    print("=" * 60)
    print("")
    print("📋 Endereços:")
    print(f"   Governor:  {governor.address}")
    print(f"   Timelock: {timelock.address}")
    print(f"   Token:    {token_address}")
    print("")
    
    # Detectar rede para explorer (Polygon vs outras)
    explorer_url = "https://polygonscan.com"
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
        if not is_polygon:
            explorer_url = "https://etherscan.io"

    print("🔗 Ver no Explorer:")
    print(f"   Governor:  {explorer_url}/address/{governor.address}")
    print(f"   Timelock: {explorer_url}/address/{timelock.address}")
    print("")
    
    return {
        "governor": governor.address,
        "timelock": timelock.address,
        "token": token_address,
    }

