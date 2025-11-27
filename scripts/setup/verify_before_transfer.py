# scripts/setup/verify_before_transfer.py
# Script para verificar tudo antes de transferir tokens
# Valida endereços, saldos, contratos e configurações

from ape import accounts, networks
import os
import sys

def main():
    # Garantir que estamos em Polygon Mainnet
    if not networks.active_provider:
        with networks.polygon.mainnet.use_provider("alchemy"):
            return _verify()
    else:
        return _verify()

def _verify():
    print("=" * 70)
    print("🔍 VERIFICAÇÃO PRÉ-TRANSFERÊNCIA DE TOKENS")
    print("=" * 70)
    print()
    
    # 1. Verificar network
    print("1️⃣  VERIFICANDO NETWORK...")
    print("-" * 70)
    if not networks.active_provider:
        print("❌ Nenhum provider ativo!")
        print("   Execute com: APE_NETWORK=polygon:mainnet")
        return False
    
    current_network = networks.active_provider.network.name
    ecosystem = networks.active_provider.network.ecosystem.name if hasattr(networks.active_provider.network, 'ecosystem') else None
    chain_id = networks.active_provider.chain_id if hasattr(networks.active_provider, 'chain_id') else None
    
    print(f"   Network: {current_network}")
    print(f"   Ecosystem: {ecosystem}")
    print(f"   Chain ID: {chain_id}")
    
    is_polygon = ecosystem == "polygon" or chain_id == 137
    if not is_polygon:
        print("⚠️  ATENÇÃO: Não está em Polygon Mainnet!")
        print("   Certifique-se de usar: --network polygon:mainnet")
    else:
        print("✅ Network: Polygon Mainnet")
    print()
    
    # 2. Verificar wallet
    print("2️⃣  VERIFICANDO WALLET...")
    print("-" * 70)
    try:
        acct = accounts.load("neoflow-admin")
        print(f"✅ Wallet carregada: {acct.address}")
        print(f"   Label: neoflow-admin")
    except Exception as e:
        print(f"❌ Erro ao carregar wallet: {e}")
        return False
    print()
    
    # 3. Verificar arquivos de endereços
    print("3️⃣  VERIFICANDO ARQUIVOS DE ENDEREÇOS...")
    print("-" * 70)
    
    token_file = "artifacts/addresses/.token_address.txt"
    claim_file = "artifacts/addresses/.claim_address.txt"
    vault_file = "artifacts/addresses/.vault_address.txt"
    
    files_status = {}
    for name, file_path in [("Token", token_file), ("Claim", claim_file), ("Vault", vault_file)]:
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                address = f.read().strip()
            files_status[name] = {"exists": True, "address": address}
            print(f"✅ {name}: {address}")
        else:
            files_status[name] = {"exists": False, "address": None}
            print(f"❌ {name}: Arquivo não encontrado ({file_path})")
    
    if not all(f["exists"] for f in files_status.values()):
        print()
        print("❌ Alguns arquivos de endereços estão faltando!")
        return False
    print()
    
    # 4. Verificar se endereços são válidos
    print("4️⃣  VERIFICANDO FORMATO DOS ENDEREÇOS...")
    print("-" * 70)
    
    token_address = files_status["Token"]["address"]
    claim_address = files_status["Claim"]["address"]
    vault_address = files_status["Vault"]["address"]
    
    def is_valid_address(addr):
        return addr.startswith("0x") and len(addr) == 42
    
    addresses_valid = True
    for name, addr in [("Token", token_address), ("Claim", claim_address), ("Vault", vault_address)]:
        if is_valid_address(addr):
            print(f"✅ {name}: Formato válido")
        else:
            print(f"❌ {name}: Formato inválido ({addr})")
            addresses_valid = False
    
    if not addresses_valid:
        return False
    print()
    
    # 5. Verificar se contratos existem na blockchain
    print("5️⃣  VERIFICANDO CONTRATOS NA BLOCKCHAIN...")
    print("-" * 70)
    
    try:
        from ape import Contract
        
        # ABI mínimo para verificar se é contrato
        minimal_abi = [
            {
                "constant": True,
                "inputs": [],
                "name": "totalSupply",
                "outputs": [{"name": "", "type": "uint256"}],
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
        
        # Verificar Token
        try:
            token = Contract(token_address, abi=minimal_abi)
            total_supply = token.totalSupply()
            print(f"✅ Token existe na blockchain")
            print(f"   Total Supply: {total_supply / 10**18:,.0f} NEOFLW")
        except Exception as e:
            print(f"⚠️  Token: Erro ao verificar ({type(e).__name__})")
            print(f"   Pode ser que o contrato não esteja verificado ainda")
            print(f"   Tentando verificar saldo diretamente...")
        
        # Verificar Claim e Vault (tentando ler código)
        try:
            claim_code = networks.active_provider.get_code(claim_address)
            if claim_code and len(claim_code) > 2:
                print(f"✅ Claim existe na blockchain (código encontrado)")
            else:
                print(f"⚠️  Claim: Código não encontrado - pode não estar deployado")
        except Exception as e:
            print(f"⚠️  Claim: Erro ao verificar ({type(e).__name__})")
        
        try:
            vault_code = networks.active_provider.get_code(vault_address)
            if vault_code and len(vault_code) > 2:
                print(f"✅ Vault existe na blockchain (código encontrado)")
            else:
                print(f"⚠️  Vault: Código não encontrado - pode não estar deployado")
        except Exception as e:
            print(f"⚠️  Vault: Erro ao verificar ({type(e).__name__})")
            
    except Exception as e:
        print(f"⚠️  Erro ao verificar contratos: {e}")
        print(f"   Continuando com verificação de saldos...")
    print()
    
    # 6. Verificar saldos
    print("6️⃣  VERIFICANDO SALDOS...")
    print("-" * 70)
    
    try:
        # Usar provider direto para balanceOf
        from ape.types import AddressType
        
        # Verificar saldo de POL na wallet
        pol_balance = networks.active_provider.get_balance(acct.address)
        print(f"💰 Saldo de POL na wallet: {pol_balance / 10**18:.4f} POL")
        
        if pol_balance < 0.01 * 10**18:  # Menos de 0.01 POL
            print("⚠️  ATENÇÃO: Saldo de POL muito baixo!")
            print("   Pode não ter gas suficiente para as transferências")
        else:
            print("✅ Saldo de POL suficiente")
        
        # Tentar verificar saldo de tokens
        try:
            # Usar call direto
            from eth_abi import encode, decode
            from eth_utils import to_checksum_address
            
            # balanceOf(address) selector: 0x70a08231
            balance_selector = "0x70a08231"
            encoded_address = encode(['address'], [to_checksum_address(acct.address)])
            data = balance_selector + encoded_address.hex()[2:]
            
            result = networks.active_provider.web3.eth.call({
                'to': to_checksum_address(token_address),
                'data': data
            })
            
            owner_balance = int(result.hex(), 16)
            print(f"💰 Saldo de tokens na wallet: {owner_balance / 10**18:,.2f} NEOFLW")
            
            # Verificar saldo do Claim
            encoded_claim = encode(['address'], [to_checksum_address(claim_address)])
            data_claim = balance_selector + encoded_claim.hex()[2:]
            result_claim = networks.active_provider.web3.eth.call({
                'to': to_checksum_address(token_address),
                'data': data_claim
            })
            claim_balance = int(result_claim.hex(), 16)
            print(f"🎁 Saldo de tokens no Claim: {claim_balance / 10**18:,.2f} NEOFLW")
            
            # Verificar saldo do Vault
            encoded_vault = encode(['address'], [to_checksum_address(vault_address)])
            data_vault = balance_selector + encoded_vault.hex()[2:]
            result_vault = networks.active_provider.web3.eth.call({
                'to': to_checksum_address(token_address),
                'data': data_vault
            })
            vault_balance = int(result_vault.hex(), 16)
            print(f"🏦 Saldo de tokens no Vault: {vault_balance / 10**18:,.2f} NEOFLW")
            
            # Verificar se tem saldo suficiente
            amount_needed = 200_000_000 * 10**18  # 200M total
            if owner_balance >= amount_needed:
                print()
                print("✅ Saldo suficiente para transferências (200M tokens)")
            else:
                print()
                print(f"❌ Saldo insuficiente!")
                print(f"   Necessário: {amount_needed / 10**18:,.0f}M NEOFLW")
                print(f"   Disponível: {owner_balance / 10**18:,.2f}M NEOFLW")
                return False
                
        except Exception as e:
            print(f"⚠️  Erro ao verificar saldo de tokens: {e}")
            print(f"   Tipo: {type(e).__name__}")
            print(f"   Continuando...")
            
    except Exception as e:
        print(f"⚠️  Erro ao verificar saldos: {e}")
    print()
    
    # 7. Resumo e recomendações
    print("=" * 70)
    print("📋 RESUMO DA VERIFICAÇÃO")
    print("=" * 70)
    print()
    print("✅ Verificações básicas concluídas")
    print()
    print("📝 Endereços dos contratos:")
    print(f"   Token:  {token_address}")
    print(f"   Claim:  {claim_address}")
    print(f"   Vault:  {vault_address}")
    print()
    print("🔗 Links Polygonscan:")
    print(f"   Token:  https://polygonscan.com/address/{token_address}")
    print(f"   Claim:  https://polygonscan.com/address/{claim_address}")
    print(f"   Vault:  https://polygonscan.com/address/{vault_address}")
    print()
    print("📋 Próximos passos:")
    print("   1. Verificar manualmente os links acima")
    print("   2. Confirmar que os endereços estão corretos")
    print("   3. Se tudo estiver OK, executar transferências")
    print()
    
    return True

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Verificação cancelada pelo usuário")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Erro durante verificação: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

