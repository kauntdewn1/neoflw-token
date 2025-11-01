# scripts/add_whitelist.py
# Script para adicionar endereços específicos na whitelist do Claim

from ape import accounts, project
import os

def main():
    acct = accounts.load("neoflow-admin")
    
    # Ler endereço do Claim
    if not os.path.exists(".claim_address.txt"):
        raise ValueError("Arquivo .claim_address.txt não encontrado!")
    
    with open(".claim_address.txt", "r") as f:
        claim_address = f.read().strip()
    
    claim = project.NeoFlowClaim.at(claim_address)
    
    print("=" * 60)
    print("📝 Adicionando Endereços na Whitelist")
    print("=" * 60)
    print()
    print(f"🎁 Contrato de Claim: {claim_address}")
    print()
    
    # Endereços a adicionar
    users = [
        "0xc8b6c6cf88ece28efdede72ed625b95b73cb649f",
        "0x025d20c85bca82a614466429a8c7806e25e99408",
        "0xece5867f7c82e34a7273c2361cdf5ffa01fdf5a3",
    ]
    
    # Quantidades para cada endereço (MODIFIQUE AQUI SE PRECISAR)
    # Exemplo: 1000 tokens para cada
    amounts = [
        1000 * 10**18,  # 1000 tokens para primeiro endereço
        1000 * 10**18,  # 1000 tokens para segundo endereço
        1000 * 10**18,  # 1000 tokens para terceiro endereço
    ]
    
    print("📋 Endereços a adicionar:")
    for i, (user, amount) in enumerate(zip(users, amounts), 1):
        print(f"  {i}. {user}")
        print(f"     Quantidade: {amount / 10**18:,.0f} NEOFLW")
    print()
    
    # Verificar saldo disponível
    claim_balance = claim.contractBalance()
    total_needed = sum(amounts)
    
    print(f"💰 Saldo disponível no Claim: {claim_balance / 10**18:,.2f} NEOFLW")
    print(f"📤 Total necessário: {total_needed / 10**18:,.2f} NEOFLW")
    print()
    
    if claim_balance < total_needed:
        raise ValueError(
            f"Saldo insuficiente! Claim tem {claim_balance / 10**18:,.2f} NEOFLW, "
            f"mas precisa de {total_needed / 10**18:,.2f} NEOFLW"
        )
    
    # Verificar se algum endereço já está na whitelist
    print("🔍 Verificando endereços existentes...")
    for user in users:
        current_amount = claim.claimableAmount(user)
        has_claimed = claim.hasClaimed(user)
        
        if current_amount > 0:
            print(f"  ⚠️  {user[:10]}... já tem {current_amount / 10**18:,.0f} tokens configurados")
            if has_claimed:
                print(f"     ⚠️  ATENÇÃO: Este endereço já fez claim!")
        else:
            print(f"  ✅ {user[:10]}... não está na whitelist ainda")
    print()
    
    # Confirmar antes de adicionar
    print("=" * 60)
    print("⚠️  ATENÇÃO:")
    print("  - Se algum endereço já tem tokens configurados, será SOBRESCRITO")
    print("  - Se algum endereço já fez claim, não pode ser modificado")
    print("=" * 60)
    print()
    
    # Adicionar na whitelist
    print("⏳ Adicionando na whitelist...")
    claim.setWhitelist(users, amounts, sender=acct)
    
    print()
    print("=" * 60)
    print("✅ Whitelist configurada com sucesso!")
    print("=" * 60)
    print()
    
    # Verificar resultado
    print("📊 Verificação final:")
    for i, user in enumerate(users, 1):
        amount = claim.claimableAmount(user)
        has_claimed = claim.hasClaimed(user)
        status = "✅" if amount > 0 else "❌"
        claimed_status = " (já fez claim)" if has_claimed else ""
        
        print(f"{status} {i}. {user}")
        print(f"   Amount: {amount / 10**18:,.0f} NEOFLW{claimed_status}")
    print()
    
    print("🎉 Agora esses endereços podem fazer claim!")
    print("   Eles precisarão pagar o próprio gas para fazer claim.")

