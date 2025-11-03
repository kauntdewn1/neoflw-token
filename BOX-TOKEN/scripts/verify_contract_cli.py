#!/usr/bin/env python3
"""
Script CLI para verificar o contrato InterboxCoin (BOX Token) no BSCScan
Usa a API V2 do Etherscan para verificação automática via CLI
"""
import os
import sys
import json
import requests
from pathlib import Path
import time

# Tenta importar dotenv para carregar .env automaticamente
try:
    from dotenv import load_dotenv
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    env_path = project_root / ".env"
    if env_path.exists():
        load_dotenv(dotenv_path=env_path)
except ImportError:
    pass

# Configurações
CONTRACT_ADDRESS = "0xBc972E10Df612C7d65054BC67aBCA96B3C22a017"
CHAIN_ID = "56"  # BSC Mainnet
API_BASE_URL = "https://api.etherscan.io/v2/api"  # API V2
SOLIDITY_FILE = Path(__file__).parent.parent / "InterboxCoin_Flattened_Final.sol"
CONSTRUCTOR_ARGS = "00000000000000000000000000000000000000000000d3c21bcecceda100000000000000000000000000000045f9c5af31678bc1dacddf348936a6a6e4d42a53"
# Versões do compilador para tentar (em ordem de preferência)
COMPILER_VERSIONS = [
    "v0.8.24+commit.e11b9ed9",
    "v0.8.23+commit.fca61c90",
    "v0.8.22+commit.4fc1097e",
    "v0.8.20+commit.a1b79de6",
    "v0.8.19+commit.7dd6d404",
]

COMPILER_VERSION = COMPILER_VERSIONS[0]  # Tenta a primeira
# EVM Versions para tentar (em ordem)
EVM_VERSIONS = ["london", "shanghai", "istanbul", "berlin"]  # "default" não funciona via API
EVERSION = EVM_VERSIONS[0]  # Começa com "london"
OPTIMIZATION = "1"  # "1" para Yes, "0" para No
OPTIMIZATION_RUNS = "200"
LICENSE = "3"  # MIT License

def get_api_key():
    """Obtém a API key"""
    api_key = os.getenv("ETHERSCAN_API_KEY") or os.getenv("BSCSCAN_API_KEY")
    
    if not api_key:
        print("⚠️  API Key não encontrada.")
        print("   Configure: export ETHERSCAN_API_KEY=sua_api_key")
        print("   Ou adicione ao .env: ETHERSCAN_API_KEY=sua_api_key")
        sys.exit(1)
    
    return api_key

def read_source_code():
    """Lê o código fonte do contrato"""
    if not SOLIDITY_FILE.exists():
        print(f"❌ Arquivo não encontrado: {SOLIDITY_FILE}")
        sys.exit(1)
    
    with open(SOLIDITY_FILE, 'r', encoding='utf-8') as f:
        return f.read()

def verify_contract_via_api(api_key, source_code):
    """Verifica o contrato via API do BSCScan/Etherscan"""
    print("=" * 70)
    print("  🚀 Verificando Contrato via CLI - BSCScan API V2")
    print("=" * 70)
    print()
    print(f"📍 Contrato: {CONTRACT_ADDRESS}")
    print(f"🌐 Rede: BSC Mainnet (Chain ID: {CHAIN_ID})")
    print(f"⚙️  Optimization: {'Yes' if OPTIMIZATION == '1' else 'No'}, Runs: {OPTIMIZATION_RUNS}")
    print()
    
    # Tenta cada combinação de compilador e EVM version
    for compiler_version in COMPILER_VERSIONS:
        for evm_version in EVM_VERSIONS:
            print(f"📝 Tentando: Compiler={compiler_version}, EVM={evm_version}")
            
            # URL para verificação (API V2)
            url = f"{API_BASE_URL}?chainid={CHAIN_ID}"
            
            # Parâmetros para verificação
            data = {
                "module": "contract",
                "action": "verifysourcecode",
                "apikey": api_key,
                "contractaddress": CONTRACT_ADDRESS,
                "sourceCode": source_code,
                "codeformat": "solidity-single-file",  # Single file
                "contractname": "InterboxCoin",
                "compilerversion": compiler_version,
                "optimizationUsed": OPTIMIZATION,
                "runs": OPTIMIZATION_RUNS,
                "constructorArguements": CONSTRUCTOR_ARGS,  # Nota: API usa "Arguements" (com typo, mas é assim que funciona)
                "evmversion": evm_version,
                "licenseType": LICENSE
            }
            
            print("📤 Enviando requisição de verificação...")
            
            try:
                response = requests.post(url, data=data, timeout=30)
                response.raise_for_status()
                result = response.json()
                
                if result.get("status") == "1":
                    guid = result.get("result")
                    print(f"   ✅ Requisição enviada com sucesso!")
                    print(f"   📋 GUID: {guid}")
                    print(f"   ✅ Versão do compilador aceita: {compiler_version}")
                    print(f"   ✅ EVM version aceita: {evm_version}")
                    print()
                    print("   ⏳ Aguardando processamento...")
                    print("   (Isso pode levar alguns minutos)")
                    print()
                    
                    # Aguarda a verificação
                    success = check_verification_status(api_key, guid)
                    
                    # Se deu erro de bytecode mismatch, tenta próxima combinação
                    if not success:
                        # Verifica se foi erro de bytecode - se sim, continua tentando
                        print(f"   ⚠️  Bytecode não correspondeu com esta combinação")
                        print(f"   🔄 Tentando próxima combinação...")
                        print()
                        continue
                    
                    return success
                else:
                    message = result.get("message", "Unknown error")
                    result_text = result.get("result", "")
                    
                    # Se for erro de versão do compilador ou EVM, tenta próxima
                    if "Invalid compiler version" in message or "compiler version" in message.lower():
                        print(f"   ⚠️  Versão não suportada: {compiler_version}")
                        print(f"   🔄 Tentando próxima versão...")
                        print()
                        break  # Quebra loop do compilador, tenta próxima versão
                    elif "Invalid EVM version" in message or "EVM version" in message.lower():
                        print(f"   ⚠️  EVM version não suportada: {evm_version}")
                        print(f"   🔄 Tentando próxima EVM version...")
                        print()
                        continue  # Continua no mesmo compilador, tenta próxima EVM
                    else:
                        # Outro tipo de erro - mostra e para
                        print(f"   ❌ Erro: {message}")
                        if result_text:
                            print(f"   Detalhes: {result_text}")
                        return False
                        
            except requests.exceptions.RequestException as e:
                print(f"   ⚠️  Erro na requisição: {e}")
                print(f"   🔄 Tentando próxima combinação...")
                print()
                continue
            except Exception as e:
                print(f"   ❌ Erro inesperado: {e}")
                print(f"   🔄 Tentando próxima combinação...")
                print()
                continue
    
    # Se chegou aqui, nenhuma combinação funcionou
    print("   ❌ Nenhuma combinação de compilador/EVM funcionou!")
    print("   💡 Tente verificar manualmente no BSCScan:")
    print(f"      https://bscscan.com/address/{CONTRACT_ADDRESS}#code")
    print("   Ou verifique quais versões estão disponíveis em:")
    print("      https://etherscan.io/solcversions")
    return False

def check_verification_status(api_key, guid, max_attempts=10, delay=10):
    """Verifica o status da verificação"""
    url = f"{API_BASE_URL}?chainid={CHAIN_ID}"
    
    params = {
        "module": "contract",
        "action": "checkverifystatus",
        "apikey": api_key,
        "guid": guid
    }
    
    for attempt in range(1, max_attempts + 1):
        try:
            time.sleep(delay)
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            result = response.json()
            
            status = result.get("status")
            message = result.get("message", "")
            
            print(f"   Tentativa {attempt}/{max_attempts}: {message}")
            
            if status == "1":
                print()
                print("=" * 70)
                print("  ✅ CONTRATO VERIFICADO COM SUCESSO!")
                print("=" * 70)
                print()
                print(f"   🌐 Veja em: https://bscscan.com/address/{CONTRACT_ADDRESS}#code")
                return True
            elif "Pending" in message or "in queue" in message.lower():
                continue  # Continua aguardando
            else:
                print(f"   ⚠️  Status: {message}")
                if result.get("result"):
                    print(f"   Detalhes: {result.get('result')}")
                return False
                
        except Exception as e:
            print(f"   ⚠️  Erro ao verificar status: {e}")
            if attempt < max_attempts:
                continue
            else:
                return False
    
    print()
    print("   ⏳ Tempo máximo de espera atingido.")
    print("   Verifique manualmente em:")
    print(f"   https://bscscan.com/address/{CONTRACT_ADDRESS}#code")
    return False

def main():
    """Função principal"""
    # Verifica API key
    api_key = get_api_key()
    
    # Lê código fonte
    print("📄 Lendo código fonte...")
    source_code = read_source_code()
    print(f"   ✅ Código fonte lido ({len(source_code)} caracteres)")
    print()
    
    # Verifica contrato
    success = verify_contract_via_api(api_key, source_code)
    
    if success:
        print()
        print("🎉 Verificação concluída!")
    else:
        print()
        print("⚠️  Verificação não concluída automaticamente.")
        print("   Tente verificar manualmente:")
        print(f"   https://bscscan.com/address/{CONTRACT_ADDRESS}#code")
        print()
        print("   Ou verifique os parâmetros e tente novamente.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Operação cancelada pelo usuário.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

