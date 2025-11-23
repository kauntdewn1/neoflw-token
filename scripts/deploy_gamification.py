#!/usr/bin/env python3
"""
Script para deploy do GamificationController em Polygon
"""

from ape import accounts, project, networks

def main():
    # Obter conta
    deployer = accounts.load("neoflow-admin")
    
    # Obter endereço do token (deve ser deployado primeiro)
    token_address = input("Enter NEOFLW Token address: ").strip()
    if not token_address or token_address == "":
        raise ValueError("Token address is required")
    
    print(f"\n🚀 Deploying GamificationController...")
    print(f"📝 Token Address: {token_address}")
    print(f"👤 Deployer: {deployer.address}")
    
    # Deploy
    gamification = project.GamificationController.deploy(
        token_address,
        sender=deployer
    )
    
    print(f"\n✅ GamificationController deployed!")
    print(f"📍 Address: {gamification.address}")
    print(f"\n📋 Next steps:")
    print(f"1. Transfer tokens to contract for rewards")
    print(f"2. Update frontend .env with address")
    print(f"3. Verify contract on Polygonscan")
    
    return gamification.address

