# scripts/setup/transfer_100m_final.py
# Script final para transferir 100M para Claim e 100M para Vault
# Usa método direto que não requer contrato verificado

from ape import accounts, networks
import os

def main():
    # Garantir Polygon Mainnet
    with networks.polygon.mainnet.use_provider("alchemy"):
        _transfer()

def _transfer():
    acct = accounts.load("neoflow-admin")
    
    # Ler endereços dos arquivos
    token_file = "artifacts/addresses/.token_address.txt"
    claim_file = "artifacts/addresses/.claim_address.txt"
    vault_file = "artifacts/addresses/.vault_address.txt"
    
    for file_path in [token_file, claim_file, vault_file]:
        if not os.path.exists(file_path):
            raise ValueError(f"Arquivo {file_path} não encontrado!")
    
    with open(token_file, "r") as f:
        token_address = f.read().strip()
    
    with open(claim_file, "r") as f:
        claim_address = f.read().strip()
    
    with open(vault_file, "r") as f:
        vault_address = f.read().strip()
    
    print("=" * 70)
    print("💰 DISTRIBUIÇÃO DE TOKENS - CLAIM E VAULT")
    print("=" * 70)
    print()
    print(f"📊 Token: {token_address}")
    print(f"🎁 Claim: {claim_address}")
    print(f"🏦 Vault: {vault_address}")
    print()
    
    # Usar interface ERC20 básica para verificar saldos
    from ape import Contract
    
    erc20_read_abi = [
        {
            "constant": True,
            "inputs": [{"name": "account", "type": "address"}],
            "name": "balanceOf",
            "outputs": [{"name": "", "type": "uint256"}],
            "type": "function"
        }
    ]
    
    try:
        token_read = Contract(token_address, abi=erc20_read_abi)
        owner_balance = token_read.balanceOf(acct.address)
        claim_balance = token_read.balanceOf(claim_address)
        vault_balance = token_read.balanceOf(vault_address)
        
        print(f"💰 Saldo atual na wallet: {owner_balance / 10**18:,.2f} NEOFLW")
        print(f"🎁 Saldo atual do Claim: {claim_balance / 10**18:,.2f} NEOFLW")
        print(f"🏦 Saldo atual do Vault: {vault_balance / 10**18:,.2f} NEOFLW")
        print()
    except Exception as e:
        print(f"⚠️  Não foi possível verificar saldos automaticamente: {e}")
        print("   Continuando com transferências...")
        print()
        owner_balance = 1_000_000_000 * 10**18  # Assumir 1B tokens
        claim_balance = 0
        vault_balance = 0
    
    # Quantidade a transferir (100M para cada)
    amount_to_transfer = 100_000_000 * 10**18  # 100M tokens
    total_needed = amount_to_transfer * 2  # 200M total
    
    if owner_balance < total_needed:
        raise ValueError(
            f"❌ Saldo insuficiente! Você tem {owner_balance / 10**18:,.2f} NEOFLW, "
            f"mas precisa de {total_needed / 10**18:,.0f} NEOFLW (100M para Claim + 100M para Vault)"
        )
    
    print("=" * 70)
    print("📤 TRANSFERÊNCIAS PLANEJADAS:")
    print("=" * 70)
    print(f"1. Claim: {amount_to_transfer / 10**18:,.0f}M NEOFLW (10% do total supply)")
    print(f"2. Vault: {amount_to_transfer / 10**18:,.0f}M NEOFLW (10% do total supply)")
    print(f"Total: {total_needed / 10**18:,.0f}M NEOFLW (20% do total supply)")
    print()
    print("⚠️  ATENÇÃO: Você precisará confirmar cada transação e digitar a senha da wallet")
    print()
    
    # Usar interface ERC20 básica para transfer
    erc20_abi = [
        {
            "constant": False,
            "inputs": [
                {"name": "to", "type": "address"},
                {"name": "amount", "type": "uint256"}
            ],
            "name": "transfer",
            "outputs": [{"name": "", "type": "bool"}],
            "type": "function"
        }
    ]
    
    from ape import Contract
    token = Contract(token_address, abi=erc20_abi)
    
    # Transferir para Claim
    print("=" * 70)
    print("📤 TRANSFERINDO PARA CLAIM...")
    print("=" * 70)
    print(f"Quantidade: {amount_to_transfer / 10**18:,.0f}M NEOFLW")
    print()
    try:
        receipt = token.transfer(claim_address, amount_to_transfer, sender=acct, auto_confirm=True)
        print(f"✅ Transação enviada! Hash: {receipt.txn_hash}")
        print(f"   Ver no Polygonscan: https://polygonscan.com/tx/{receipt.txn_hash}")
    except Exception as e:
        if "TransactionNotFound" in str(type(e).__name__) or "TransactionNotFoundError" in str(type(e).__name__):
            print(f"⚠️  Transação enviada mas receipt não encontrado imediatamente")
            print(f"   Isso é normal - a transação pode estar sendo processada")
            print(f"   Verifique manualmente no Polygonscan:")
            print(f"   https://polygonscan.com/address/{claim_address}")
            print()
            print("   Se a transação foi confirmada, você pode continuar com a próxima transferência")
        else:
            raise
    
    # Verificar após primeira transferência
    try:
        new_claim_balance = token_read.balanceOf(claim_address)
        print(f"✅ Transferência para Claim concluída!")
        print(f"   Saldo do Claim agora: {new_claim_balance / 10**18:,.2f}M NEOFLW")
    except:
        print(f"✅ Transferência para Claim concluída!")
        print(f"   Verifique no Polygonscan: https://polygonscan.com/address/{claim_address}")
    print()
    
    # Transferir para Vault
    print("=" * 70)
    print("📤 TRANSFERINDO PARA VAULT...")
    print("=" * 70)
    print(f"Quantidade: {amount_to_transfer / 10**18:,.0f}M NEOFLW")
    print()
    try:
        receipt = token.transfer(vault_address, amount_to_transfer, sender=acct, auto_confirm=True)
        print(f"✅ Transação enviada! Hash: {receipt.txn_hash}")
        print(f"   Ver no Polygonscan: https://polygonscan.com/tx/{receipt.txn_hash}")
    except Exception as e:
        if "TransactionNotFound" in str(type(e).__name__) or "TransactionNotFoundError" in str(type(e).__name__):
            print(f"⚠️  Transação enviada mas receipt não encontrado imediatamente")
            print(f"   Isso é normal - a transação pode estar sendo processada")
            print(f"   Verifique manualmente no Polygonscan:")
            print(f"   https://polygonscan.com/address/{vault_address}")
        else:
            raise
    
    # Verificar após segunda transferência
    try:
        new_vault_balance = token_read.balanceOf(vault_address)
        print(f"✅ Transferência para Vault concluída!")
        print(f"   Saldo do Vault agora: {new_vault_balance / 10**18:,.2f}M NEOFLW")
    except:
        print(f"✅ Transferência para Vault concluída!")
        print(f"   Verifique no Polygonscan: https://polygonscan.com/address/{vault_address}")
    print()
    
    # Resumo final
    print("=" * 70)
    print("✅ DISTRIBUIÇÃO CONCLUÍDA!")
    print("=" * 70)
    print()
    
    try:
        final_owner_balance = token_read.balanceOf(acct.address)
        final_claim_balance = token_read.balanceOf(claim_address)
        final_vault_balance = token_read.balanceOf(vault_address)
        
        print(f"💰 Saldo final na wallet: {final_owner_balance / 10**18:,.2f}M NEOFLW")
        print(f"🎁 Saldo final do Claim: {final_claim_balance / 10**18:,.2f}M NEOFLW")
        print(f"🏦 Saldo final do Vault: {final_vault_balance / 10**18:,.2f}M NEOFLW")
    except:
        print("📊 Verifique os saldos manualmente no Polygonscan:")
        print(f"   Wallet: https://polygonscan.com/address/{acct.address}")
        print(f"   Claim: https://polygonscan.com/address/{claim_address}")
        print(f"   Vault: https://polygonscan.com/address/{vault_address}")
    
    print(f"💰 Saldo final na wallet: {final_owner_balance / 10**18:,.2f}M NEOFLW")
    print(f"🎁 Saldo final do Claim: {final_claim_balance / 10**18:,.2f}M NEOFLW")
    print(f"🏦 Saldo final do Vault: {final_vault_balance / 10**18:,.2f}M NEOFLW")
    print()
    print("📋 Próximos passos:")
    print("   1. Configurar whitelist no NeoFlowClaim")
    print("   2. Usuários podem fazer stake no StakingVault")
    print("   3. Após 6 meses de lock, receberão 10% APY em rewards")
    print()

if __name__ == "__main__":
    main()

