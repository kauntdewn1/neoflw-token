#!/usr/bin/env python3
"""
Gera Standard JSON Input para verificação do contrato ORIGINAL (sem ContractMetadata)
"""

import json
from pathlib import Path

# Configurações
CONTRACT_NAME = "NeoFlowToken"
COMPILER_VERSION = "v0.8.30+commit.73712a01"  # Versão usada no deploy
OPTIMIZER_ENABLED = True
OPTIMIZER_RUNS = 200
EVM_VERSION = "paris"

# Caminhos
PROJECT_ROOT = Path(__file__).parent.parent.parent
ORIGINAL_FLATTENED_FILE = PROJECT_ROOT / "artifacts" / "flattened" / "NeoFlowToken_original_flattened.sol"
OUTPUT_JSON_FILE = PROJECT_ROOT / "artifacts" / "verification" / "oklink_standard_json_original.json"

def read_source_code(file_path):
    """Lê o conteúdo de um arquivo."""
    if not file_path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def generate_standard_json():
    """Gera o Standard JSON Input para verificação."""
    try:
        source_code_content = read_source_code(ORIGINAL_FLATTENED_FILE)
    except FileNotFoundError as e:
        print(f"❌ Erro: {e}")
        print("💡 Certifique-se de que o arquivo original foi gerado:")
        print("   artifacts/flattened/NeoFlowToken_original_flattened.sol")
        return

    # O Standard JSON Input espera um dicionário de fontes onde a chave é o caminho do arquivo
    # e o valor é um dicionário com a chave "content".
    sources = {
        f"contracts/{CONTRACT_NAME}.sol": {
            "content": source_code_content
        }
    }

    standard_json_input = {
        "language": "Solidity",
        "sources": sources,
        "settings": {
            "optimizer": {
                "enabled": OPTIMIZER_ENABLED,
                "runs": OPTIMIZER_RUNS
            },
            "evmVersion": EVM_VERSION,
            "outputSelection": {
                "*": {
                    "*": [
                        "abi",
                        "evm.bytecode",
                        "evm.deployedBytecode",
                        "evm.methodIdentifiers",
                        "metadata"
                    ],
                    "": [
                        "ast"
                    ]
                }
            }
        }
    }

    # Garantir que o diretório de saída existe
    OUTPUT_JSON_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(standard_json_input, f, indent=2, ensure_ascii=False)

    print(f"✅ Standard JSON Input gerado com sucesso!")
    print(f"📁 Localização: {OUTPUT_JSON_FILE}")
    print(f"📊 Tamanho: {OUTPUT_JSON_FILE.stat().st_size / 1024:.1f} KB")
    print()
    print("📋 Configurações:")
    print(f"   - Compiler: {COMPILER_VERSION}")
    print(f"   - Optimization: {OPTIMIZER_ENABLED} (runs: {OPTIMIZER_RUNS})")
    print(f"   - EVM Version: {EVM_VERSION}")
    print()
    print("💡 Use este arquivo para verificação no OKLink/Tenderly:")
    print(f"   - Método: solidity-standard-json-input")
    print(f"   - Arquivo: {OUTPUT_JSON_FILE.name}")
    print()
    print("📝 Constructor Arguments (ABI-encoded):")
    print("   0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000")

if __name__ == "__main__":
    generate_standard_json()

