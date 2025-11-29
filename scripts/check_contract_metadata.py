#!/usr/bin/env python3
"""
Script para verificar se um contrato deployado já tem suporte a ContractMetadata
(verifica se a função contractURI() existe on-chain)
"""

from ape import project, networks
import sys

def check_contract_metadata(contract_address: str):
    """
    Verifica se o contrato no endereço especificado tem a função contractURI()
    
    Args:
        contract_address: Endereço do contrato a verificar
    """
    print("=" * 60)
    print("🔍 Verificando suporte a ContractMetadata")
    print("=" * 60)
    print(f"\n📋 Endereço do contrato: {contract_address}")
    
    if not networks.active_provider:
        print("\n❌ Erro: Nenhuma rede conectada!")
        print("💡 Execute: ape run scripts/check_contract_metadata --network polygon:mainnet")
        return False
    
    print(f"🌐 Rede: {networks.active_provider.name}")
    print(f"🔗 Chain ID: {networks.active_provider.chain_id}")
    print()
    
    try:
        # Tentar obter instância do contrato
        # Usamos o contrato compilado como referência
        token = project.NeoFlowToken.at(contract_address)
        
        print("✅ Contrato encontrado on-chain")
        print()
        
        # Verificar se tem a função contractURI()
        print("🔎 Verificando função contractURI()...")
        try:
            # Tentar chamar contractURI() - se existir, retorna string (pode ser vazia)
            uri = token.contractURI()
            print(f"✅ Função contractURI() encontrada!")
            print(f"📄 Valor atual: '{uri}'")
            print()
            
            # Verificar se tem setContractURI()
            print("🔎 Verificando função setContractURI()...")
            try:
                # Verificar se a função existe no ABI
                if hasattr(token, 'setContractURI'):
                    print("✅ Função setContractURI() encontrada!")
                    print()
                    print("=" * 60)
                    print("✅ RESULTADO: Contrato JÁ TEM ContractMetadata!")
                    print("=" * 60)
                    print()
                    print("💡 Próximos passos:")
                    print("   1. Você pode configurar contractURI usando:")
                    print("      token.setContractURI('https://...', sender=acct)")
                    print("   2. NÃO precisa fazer novo deploy!")
                    print("   3. Basta verificar o contrato no PolygonScan")
                    return True
                else:
                    print("❌ Função setContractURI() NÃO encontrada")
            except Exception as e:
                print(f"❌ Erro ao verificar setContractURI(): {e}")
                
        except Exception as e:
            error_msg = str(e).lower()
            if "function" in error_msg and "not found" in error_msg:
                print("❌ Função contractURI() NÃO encontrada no contrato")
            elif "execution reverted" in error_msg:
                # Pode ser que a função existe mas reverte (comportamento esperado se não configurado)
                print("⚠️  Função contractURI() pode existir mas reverteu")
                print("   (Isso pode indicar que a função existe mas não está configurada)")
            else:
                print(f"❌ Erro ao chamar contractURI(): {e}")
        
        print()
        print("=" * 60)
        print("❌ RESULTADO: Contrato NÃO tem ContractMetadata")
        print("=" * 60)
        print()
        print("💡 Próximos passos:")
        print("   1. Você precisa fazer NOVO deploy do contrato")
        print("   2. O código atual JÁ tem ContractMetadata implementado")
        print("   3. Use: ape run scripts/deploy/deploy_token --network polygon:mainnet")
        return False
        
    except Exception as e:
        print(f"❌ Erro ao acessar contrato: {e}")
        print()
        print("💡 Possíveis causas:")
        print("   - Contrato não existe neste endereço")
        print("   - Rede incorreta (verifique se está na rede correta)")
        print("   - Problema de conexão RPC")
        return False

def main(contract_address: str = None):
    """Função principal"""
    # Prioridade 1: Parâmetro passado diretamente
    if contract_address and contract_address.startswith("0x") and len(contract_address) == 42:
        pass  # Usar o endereço fornecido
    # Prioridade 2: Tentar ler do arquivo .token_address.txt
    else:
        try:
            with open(".token_address.txt", "r") as f:
                contract_address = f.read().strip()
            print(f"📁 Endereço lido de .token_address.txt")
        except FileNotFoundError:
            # Prioridade 3: Tentar sys.argv (mas validar que é um endereço válido)
            if len(sys.argv) > 1:
                potential_address = sys.argv[1]
                # Validar se é um endereço válido (ignorar "run" e outros comandos do Ape)
                if potential_address.startswith("0x") and len(potential_address) == 42:
                    contract_address = potential_address
                    print(f"📋 Endereço recebido como argumento")
                else:
                    # Não é um endereço válido, tentar arquivo alternativo
                    try:
                        with open("artifacts/addresses/.token_address.txt", "r") as f:
                            contract_address = f.read().strip()
                        print(f"📁 Endereço lido de artifacts/addresses/.token_address.txt")
                    except FileNotFoundError:
                        print("❌ Erro: Endereço do contrato não fornecido!")
                        print()
                        print("💡 Uso:")
                        print("   # Criar arquivo com endereço:")
                        print("   echo '0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87' > .token_address.txt")
                        print()
                        print("   # Executar script:")
                        print("   ape run check_contract_metadata --network polygon:mainnet")
                        sys.exit(1)
    
    # Validar formato do endereço
    if not contract_address or not contract_address.startswith("0x") or len(contract_address) != 42:
        print(f"❌ Erro: Endereço inválido: {contract_address}")
        print()
        print("💡 Certifique-se de que o arquivo .token_address.txt contém um endereço válido:")
        print("   echo '0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87' > .token_address.txt")
        sys.exit(1)
    
    # Verificar
    has_metadata = check_contract_metadata(contract_address)
    
    # Retornar código de saída apropriado
    sys.exit(0 if has_metadata else 1)

if __name__ == "__main__":
    main()

