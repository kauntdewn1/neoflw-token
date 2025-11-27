# scripts/setup/transfer_to_vault_only.py
# Script para transferir apenas para o Vault (caso a transferência para Claim já tenha sido feita)

from ape import accounts, networks, Contract
import os

def main():
    with networks.polygon.mainnet.use_provider("alchemy"):
        acct = accounts.load("neoflow-admin")
        
        # Ler endereços
        token_file = "artifacts/addresses/.token_address.txt"
        vault_file = "artifacts/addresses/.vault_address.txt"
        
        with open(token_file, "r") as f:
            token_address = f.read().strip()
        
        with open(vault_file, "r") as f:
            vault_address = f.read().strip()
        
        print("=" * 70)
        print("💰 TRANSFERINDO PARA VAULT")
        print("=" * 70)
        print(f"📊 Token: {token_address}")
        print(f"🏦 Vault: {vault_address}")
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
            }
        ]
        
        token = Contract(token_address, abi=erc20_abi)
        amount_to_transfer = 100_000_000 * 10**18  # 100M tokens
        
        print(f"📤 Transferindo: {amount_to_transfer / 10**18:,.0f}M NEOFLW")
        print()
        print("⚠️  Você precisará confirmar a transação e digitar a senha da wallet")
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
        
        print()
        print("✅ Transferência para Vault concluída!")
        print()

if __name__ == "__main__":
    main()

