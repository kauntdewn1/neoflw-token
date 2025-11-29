#!/usr/bin/env python3
"""
Script para deploy do GamificationController em Polygon
"""

from ape import accounts, project, networks

def main():
    # Obter conta
    deployer = accounts.load("neoflow-admin")
    
    # Obter endereço do token (deve ser deployado primeiro)
    # Prioridade: .token_address.txt -> env -> erro explícito
    token_address = None
    try:
        with open(".token_address.txt", "r") as f:
            token_address = f.read().strip()
    except FileNotFoundError:
        token_address = None

    if not token_address:
        import os

        token_address = os.getenv("TOKEN_ADDRESS", "").strip()

    if not token_address or not token_address.startswith("0x") or len(token_address) != 42:
        raise ValueError(
            "Token address is required and must be set in .token_address.txt "
            "or in TOKEN_ADDRESS env var"
        )
    
    print(f"\n🚀 Deploying GamificationController...")
    print(f"📝 Token Address: {token_address}")
    print(f"👤 Deployer: {deployer.address}")
    
    # Deploy
    gamification = project.GamificationController.deploy(
        token_address,
        sender=deployer,
        auto_confirm=True,
    )
    
    print(f"\n✅ GamificationController deployed!")
    print(f"📍 Address: {gamification.address}")
    print(f"\n📋 Next steps:")
    print(f"1. Transfer tokens to contract for rewards")
    print(f"2. Update frontend .env with address")
    print(f"3. Verify contract on Polygonscan")

    # Salvar endereço em arquivo auxiliar
    with open(".gamification_address.txt", "w") as f:
        f.write(gamification.address)

    return gamification.address

