#!/usr/bin/env python3
"""
Script para obter o ABI do contrato InterboxCoin (BOX Token) do BSCScan
Usa a API V2 do Etherscan (V1 está depreciada desde agosto 2025)
"""
import os
import sys
import json
import requests
from pathlib import Path

# Tenta importar dotenv para carregar .env automaticamente
try:
    from dotenv import load_dotenv
    # Carrega .env do projeto pai (neoflw-token)
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent  # sobe 2 níveis: scripts -> BOX-TOKEN -> neoflw-token
    env_path = project_root / ".env"
    if env_path.exists():
        load_dotenv(dotenv_path=env_path)
except ImportError:
    pass  # dotenv não instalado, continua sem ele

# Configurações
CONTRACT_ADDRESS = "0xBc972E10Df612C7d65054BC67aBCA96B3C22a017"
CHAIN_ID = "56"  # BSC Mainnet
API_BASE_URL = "https://api.etherscan.io/v2/api"  # API V2 (V1 está depreciada)

def get_api_key():
    """Obtém a API key de variável de ambiente ou input do usuário"""
    # Tenta obter da variável de ambiente (já carregada do .env se dotenv disponível)
    api_key = os.getenv("ETHERSCAN_API_KEY") or os.getenv("BSCSCAN_API_KEY")
    
    if not api_key:
        print("⚠️  API Key não encontrada nas variáveis de ambiente.")
        print("   Variáveis verificadas: ETHERSCAN_API_KEY, BSCSCAN_API_KEY")
        print()
        api_key = input("Digite sua API Key do Etherscan/BSCScan: ").strip()
    
    if not api_key:
        print("❌ API Key não fornecida!")
        sys.exit(1)
    
    return api_key

def check_contract_verification(api_key):
    """Verifica se o contrato está verificado"""
    print("🔍 Verificando se o contrato está verificado...")
    
    # API V2: chainid deve estar na URL base, não nos params
    url = f"{API_BASE_URL}?chainid={CHAIN_ID}"
    
    params = {
        "module": "contract",
        "action": "getsourcecode",
        "address": CONTRACT_ADDRESS,
        "apikey": api_key
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data.get("status") == "1" and data.get("result"):
            result = data["result"][0] if isinstance(data["result"], list) else data["result"]
            source_code = result.get("SourceCode", "")
            
            if source_code and source_code != "":
                print("   ✅ Contrato verificado!")
                return True
            else:
                print("   ⚠️  Contrato ainda não está verificado!")
                print("   📋 Verifique o contrato primeiro em:")
                print(f"      https://bscscan.com/address/{CONTRACT_ADDRESS}#code")
                return False
        else:
            print(f"   ⚠️  Erro ao verificar: {data.get('message', 'Unknown error')}")
            return False
            
    except Exception as e:
        print(f"   ❌ Erro ao verificar contrato: {e}")
        return False

def get_contract_abi(api_key):
    """Obtém o ABI do contrato verificado"""
    print("📥 Obtendo ABI do contrato...")
    
    # API V2: chainid deve estar na URL base, não nos params
    url = f"{API_BASE_URL}?chainid={CHAIN_ID}"
    
    params = {
        "module": "contract",
        "action": "getabi",
        "address": CONTRACT_ADDRESS,
        "apikey": api_key
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data.get("status") == "1":
            # O result vem como string JSON, precisa fazer parse
            abi_str = data.get("result", "[]")
            try:
                abi = json.loads(abi_str)
                print("   ✅ ABI obtido com sucesso!")
                return abi
            except json.JSONDecodeError as e:
                print(f"   ❌ Erro ao fazer parse do ABI: {e}")
                print(f"   Result: {abi_str[:200]}...")
                return None
        else:
            message = data.get("message", "Unknown error")
            result = data.get("result", "")
            print(f"   ❌ Erro: {message}")
            if result:
                print(f"   Detalhes: {result}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"   ❌ Erro na requisição: {e}")
        return None
    except Exception as e:
        print(f"   ❌ Erro inesperado: {e}")
        return None

def save_abi(abi, output_path):
    """Salva o ABI em um arquivo JSON formatado"""
    try:
        # Cria o diretório se não existir
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Salva o ABI formatado
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(abi, f, indent=2, ensure_ascii=False)
        
        print(f"   ✅ ABI salvo em: {output_path}")
        return True
    except Exception as e:
        print(f"   ❌ Erro ao salvar ABI: {e}")
        return False

def main():
    """Função principal"""
    print("=" * 70)
    print("  📋 Obter ABI do Contrato InterboxCoin (BOX Token)")
    print("=" * 70)
    print()
    print(f"📍 Endereço do Contrato: {CONTRACT_ADDRESS}")
    print(f"🌐 Rede: BSC Mainnet (Chain ID: {CHAIN_ID})")
    print()
    
    # Obtém API key
    api_key = get_api_key()
    print()
    
    # Verifica se o contrato está verificado
    if not check_contract_verification(api_key):
        print()
        print("⚠️  Não é possível obter o ABI sem o contrato verificado.")
        print("   Siga o guia: VERIFICAR_AGORA_BSCSCAN.md")
        sys.exit(1)
    
    print()
    
    # Obtém o ABI
    abi = get_contract_abi(api_key)
    
    if not abi:
        print()
        print("❌ Não foi possível obter o ABI.")
        sys.exit(1)
    
    print()
    print("=" * 70)
    print("  📊 ABI Obtido")
    print("=" * 70)
    print()
    print(f"Total de itens no ABI: {len(abi)}")
    print()
    
    # Mostra algumas informações sobre o ABI
    functions = [item for item in abi if item.get("type") == "function"]
    events = [item for item in abi if item.get("type") == "event"]
    constructor = [item for item in abi if item.get("type") == "constructor"]
    
    print("📋 Resumo:")
    print(f"   - Funções: {len(functions)}")
    print(f"   - Eventos: {len(events)}")
    print(f"   - Constructor: {len(constructor)}")
    print()
    
    # Salva o ABI
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    output_path = project_root / "abi" / "InterboxCoin_abi.json"
    
    print("💾 Salvando ABI...")
    if save_abi(abi, output_path):
        print()
        print("=" * 70)
        print("  ✅ Sucesso!")
        print("=" * 70)
        print()
        print(f"📁 ABI salvo em: {output_path}")
        print()
        print("💡 Você pode usar este ABI para:")
        print("   - Interagir com o contrato via Web3.js/Ethers.js")
        print("   - Criar interfaces de usuário")
        print("   - Testes automatizados")
    else:
        print()
        print("⚠️  ABI obtido, mas houve erro ao salvar.")
        print("   O ABI ainda está disponível acima para copiar manualmente.")
    
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Operação cancelada pelo usuário.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

