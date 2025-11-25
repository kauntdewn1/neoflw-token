# scripts/setup/distribute_initial_tokens.py
# Script para distribuir tokens iniciais conforme TOKENOMICS NEOFLW
#
# TOKENOMICS - Distribuição Total: 1,000,000,000 NEOFLW (100%)
#
# Após deploy, TODOS os tokens ficam na wallet de deploy (neoflow-admin)
# Este script distribui conforme a estratégia de tokenomics:
#
# ├─ 🎮 Gamificação & Rewards: 400M (40%)
# │  ├─ Quest Rewards: 200M (20%) → GamificationController (quando deployado)
# │  ├─ Staking Rewards: 100M (10%) → StakingVault
# │  ├─ Referral Program: 50M (5%) → GamificationController
# │  └─ Badges & Achievements: 50M (5%) → GamificationController
# │
# ├─ 👥 Comunidade & Airdrop: 250M (25%)
# │  ├─ Initial Airdrop: 100M (10%) → NeoFlowClaim
# │  ├─ Community Rewards: 75M (7.5%) → Manter na wallet (distribuir gradualmente)
# │  ├─ Early Adopters: 50M (5%) → Manter na wallet (distribuir gradualmente)
# │  └─ Marketing & Partnerships: 25M (2.5%) → Manter na wallet
# │
# ├─ 🏛️ Governança DAO: 150M (15%)
# │  ├─ Treasury: 100M (10%) → Manter na wallet (ou transferir para DAO quando criado)
# │  ├─ Voting Rewards: 30M (3%) → Manter na wallet
# │  └─ Proposals Fund: 20M (2%) → Manter na wallet
# │
# ├─ 👨‍💼 Equipe & Desenvolvimento: 100M (10%)
# │  ├─ Team: 60M (6%) → Manter na wallet (vesting será implementado)
# │  ├─ Development: 25M (2.5%) → Manter na wallet
# │  └─ Advisors: 15M (1.5%) → Manter na wallet (vesting será implementado)
# │
# ├─ 💼 Reserva Estratégica: 50M (5%)
# │  └─ Future Partnerships → Manter na wallet
# │
# └─ 🔥 Liquidity & Exchange: 50M (5%)
#    ├─ DEX Liquidity: 30M (3%) → Manter na wallet (para criar pools depois)
#    └─ CEX Listing: 20M (2%) → Manter na wallet
#
# ESTRATÉGIA DE DISTRIBUIÇÃO:
# 1. Transferir para contratos deployados (Claim, Vault, Gamification)
# 2. Manter o restante na wallet de deploy para distribuição gradual
# 3. Criar multi-sig wallet para treasury no futuro

from ape import accounts, project
import os
import sys

def main():
    acct = accounts.load("neoflow-admin")
    
    # Ler endereços dos arquivos
    if not os.path.exists(".token_address.txt"):
        raise ValueError("Arquivo .token_address.txt não encontrado!")
    
    with open(".token_address.txt", "r") as f:
        token_address = f.read().strip()
    
    print("=" * 70)
    print("💰 DISTRIBUIÇÃO INICIAL DE TOKENS - TOKENOMICS NEOFLW")
    print("=" * 70)
    print()
    print("📊 Total Supply: 1,000,000,000 NEOFLW (100%)")
    print(f"📊 Token: {token_address}")
    print(f"👤 Wallet de Deploy: {acct.address}")
    print()
    
    # Obter instância do token
    token = project.NeoFlowToken.at(token_address)
    
    # Verificar saldo atual (deve ser 1B se ainda não distribuiu)
    owner_balance = token.balanceOf(acct.address)
    print(f"💰 Saldo atual na wallet de deploy: {owner_balance / 10**18:,.0f} NEOFLW")
    print()
    
    if owner_balance < 1_000_000_000 * 10**18:
        print("⚠️  ATENÇÃO: Saldo menor que 1B tokens!")
        print("   Alguns tokens já podem ter sido distribuídos.")
        print()
    
    # Definir distribuições conforme tokenomics
    distributions = {
        "claim": {
            "name": "NeoFlowClaim - Initial Airdrop",
            "amount": 100_000_000 * 10**18,  # 100M (10%)
            "file": ".claim_address.txt",
            "description": "Initial Airdrop para comunidade"
        },
        "vault": {
            "name": "StakingVault - Staking Rewards",
            "amount": 100_000_000 * 10**18,  # 100M (10%)
            "file": ".vault_address.txt",
            "description": "Rewards pool para staking (10% APY)"
        },
        # Gamification será adicionado quando deployado
        # "gamification": {
        #     "name": "GamificationController - Quest & Referral Rewards",
        #     "amount": 300_000_000 * 10**18,  # 300M (30%)
        #     "file": ".gamification_address.txt",
        #     "description": "Quest Rewards (200M) + Referral (50M) + Badges (50M)"
        # }
    }
    
    print("📋 DISTRIBUIÇÕES PLANEJADAS:")
    print("-" * 70)
    
    total_to_distribute = 0
    available_contracts = []
    
    for key, dist in distributions.items():
        if os.path.exists(dist["file"]):
            with open(dist["file"], "r") as f:
                contract_address = f.read().strip()
            
            available_contracts.append({
                "key": key,
                "name": dist["name"],
                "address": contract_address,
                "amount": dist["amount"],
                "description": dist["description"]
            })
            total_to_distribute += dist["amount"]
            
            print(f"✅ {dist['name']}")
            print(f"   Endereço: {contract_address}")
            print(f"   Quantidade: {dist['amount'] / 10**18:,.0f}M NEOFLW ({dist['amount'] / 10**18 / 10:,.1f}%)")
            print(f"   Descrição: {dist['description']}")
            print()
        else:
            print(f"⏸️  {dist['name']}")
            print(f"   Arquivo {dist['file']} não encontrado - contrato ainda não deployado")
            print()
    
    # Calcular o que fica na wallet
    remaining_in_wallet = owner_balance - total_to_distribute
    
    print("-" * 70)
    print(f"📤 Total a distribuir para contratos: {total_to_distribute / 10**18:,.0f}M NEOFLW")
    print(f"💼 Restante na wallet de deploy: {remaining_in_wallet / 10**18:,.0f}M NEOFLW ({remaining_in_wallet / 10**18 / 10:,.1f}%)")
    print()
    print("💼 O restante na wallet inclui:")
    print("   - Community Rewards: 75M (7.5%)")
    print("   - Early Adopters: 50M (5%)")
    print("   - Marketing & Partnerships: 25M (2.5%)")
    print("   - DAO Treasury: 100M (10%)")
    print("   - Voting Rewards: 30M (3%)")
    print("   - Proposals Fund: 20M (2%)")
    print("   - Team: 60M (6%) - Vesting")
    print("   - Development: 25M (2.5%)")
    print("   - Advisors: 15M (1.5%) - Vesting")
    print("   - Reserva Estratégica: 50M (5%)")
    print("   - DEX Liquidity: 30M (3%)")
    print("   - CEX Listing: 20M (2%)")
    print()
    
    if not available_contracts:
        print("⚠️  Nenhum contrato disponível para distribuição!")
        print("   Deploy os contratos primeiro (Claim, Vault, etc.)")
        return
    
    # Confirmar antes de distribuir
    print("=" * 70)
    print("⚠️  CONFIRMAÇÃO NECESSÁRIA")
    print("=" * 70)
    print("Você está prestes a distribuir tokens para os contratos deployados.")
    print("Certifique-se de que esta é a estratégia correta!")
    print()
    
    # Executar distribuições
    for contract in available_contracts:
        print(f"📤 Transferindo para {contract['name']}...")
        print(f"   Endereço: {contract['address']}")
        print(f"   Quantidade: {contract['amount'] / 10**18:,.0f}M NEOFLW")
        print()
        
        # Verificar saldo antes
        current_balance = token.balanceOf(acct.address)
        if current_balance < contract['amount']:
            print(f"❌ Saldo insuficiente! Você tem {current_balance / 10**18:,.2f}M, mas precisa de {contract['amount'] / 10**18:,.0f}M")
            continue
        
        # Transferir
        print("⏳ Transferindo...")
        print("⚠️  Você precisará confirmar a transação e digitar a senha da wallet")
        print()
        
        token.transfer(contract['address'], contract['amount'], sender=acct, auto_confirm=True)
        
        # Verificar após transferência
        new_balance = token.balanceOf(contract['address'])
        print(f"✅ Transferência concluída!")
        print(f"   Saldo do contrato agora: {new_balance / 10**18:,.2f}M NEOFLW")
        print()
    
    # Resumo final
    print("=" * 70)
    print("✅ DISTRIBUIÇÃO CONCLUÍDA!")
    print("=" * 70)
    print()
    
    final_owner_balance = token.balanceOf(acct.address)
    print(f"💰 Saldo final na wallet de deploy: {final_owner_balance / 10**18:,.0f}M NEOFLW")
    print()
    
    for contract in available_contracts:
        contract_balance = token.balanceOf(contract['address'])
        print(f"📊 {contract['name']}: {contract_balance / 10**18:,.2f}M NEOFLW")
    
    print()
    print("📋 Próximos passos:")
    print("   1. Configurar whitelist no NeoFlowClaim")
    print("   2. Depositar rewards no StakingVault (quando necessário)")
    print("   3. Deploy GamificationController e transferir 300M tokens")
    print("   4. Criar multi-sig wallet para treasury")
    print()

