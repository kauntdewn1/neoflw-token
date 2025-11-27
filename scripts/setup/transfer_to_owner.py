# scripts/setup/transfer_to_owner.py
# Script para transferir tokens para a wallet do owner

from ape import accounts, networks, Contract
import os
import sys

def main():
    # Wallet do owner
    owner_address = "0xe329ea473d4307b734487d2ab35281b4d2557cb7"
    
    with networks.polygon.mainnet.use_provider("alchemy"):
        acct = accounts.load("neoflow-admin")
        
        # Ler endereço do token
        token_file = "artifacts/addresses/.token_address.txt"
        
        if not os.path.exists(token_file):
            raise ValueError(f"Arquivo {token_file} não encontrado!")
        
        with open(token_file, "r") as f:
            token_address = f.read().strip()
        
        print("=" * 70)
        print("💰 TRANSFERINDO TOKENS PARA OWNER")
        print("=" * 70)
        print(f"📊 Token: {token_address}")
        print(f"👤 Owner: {owner_address}")
        print(f"📤 De: {acct.address}")
        print()
        
        # Interface ERC20
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
            },
            {
                "constant": True,
                "inputs": [{"name": "account", "type": "address"}],
                "name": "balanceOf",
                "outputs": [{"name": "", "type": "uint256"}],
                "type": "function"
            }
        ]
        
        token = Contract(token_address, abi=erc20_abi)
        
        # Verificar saldo atual
        try:
            owner_balance = token.balanceOf(acct.address)
            owner_wallet_balance = token.balanceOf(owner_address)
            
            print(f"💰 Saldo atual na wallet de deploy: {owner_balance / 10**18:,.2f} NEOFLW")
            print(f"👤 Saldo atual na wallet do owner: {owner_wallet_balance / 10**18:,.2f} NEOFLW")
            print()
        except Exception as e:
            print(f"⚠️  Não foi possível verificar saldos: {e}")
            print("   Continuando...")
            print()
        
        # Quantidade a transferir
        if len(sys.argv) > 1:
            try:
                amount_millions = float(sys.argv[1])
                amount_to_transfer = int(amount_millions * 1_000_000 * 10**18)
                print(f"📝 Quantidade customizada: {amount_millions}M NEOFLW")
            except ValueError:
                print(f"⚠️  Argumento inválido '{sys.argv[1]}', usando padrão")
                amount_to_transfer = 10_000_000 * 10**18  # 10M padrão
        else:
            # Padrão: 10M tokens (pode ser ajustado)
            amount_to_transfer = 10_000_000 * 10**18
            print("📝 Usando quantidade padrão (10M NEOFLW)")
            print("   Para customizar: python scripts/setup/transfer_to_owner.py <quantidade_em_milhoes>")
        
        print()
        print(f"📤 Transferindo: {amount_to_transfer / 10**18:,.0f} NEOFLW")
        print(f"   ({amount_to_transfer / 10**18 / 1_000_000:.1f}M tokens)")
        print()
        print("⚠️  Você precisará confirmar a transação e digitar a senha da wallet")
        print()
        
        # Transferir
        try:
            receipt = token.transfer(owner_address, amount_to_transfer, sender=acct, auto_confirm=True)
            print(f"✅ Transação enviada! Hash: {receipt.txn_hash}")
            print(f"   Ver no Polygonscan: https://polygonscan.com/tx/{receipt.txn_hash}")
        except Exception as e:
            if "TransactionNotFound" in str(type(e).__name__) or "TransactionNotFoundError" in str(type(e).__name__):
                print(f"⚠️  Transação enviada mas receipt não encontrado imediatamente")
                print(f"   Isso é normal - a transação pode estar sendo processada")
                print(f"   Verifique manualmente no Polygonscan:")
                print(f"   https://polygonscan.com/address/{owner_address}")
            else:
                raise
        
        print()
        print("✅ Transferência concluída!")
        print()
        print("📋 Verificar saldo do owner:")
        print(f"   https://polygonscan.com/address/{owner_address}")
        print()

if __name__ == "__main__":
    main()

