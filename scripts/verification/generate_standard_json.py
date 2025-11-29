#!/usr/bin/env python3
"""
Gera Standard JSON Input para verificação no OKLink
"""

import json
from pathlib import Path

# Configurações
PROJECT_ROOT = Path(__file__).parent.parent.parent
FLATTENED_FILE = PROJECT_ROOT / "artifacts" / "flattened" / "NeoFlowToken_flattened.sol"
OUTPUT_FILE = PROJECT_ROOT / "artifacts" / "verification" / "oklink_standard_json.json"

def read_flattened_source():
    """Lê o arquivo flattened (limpo e corrigido se existir)"""
    # Prioridade: clean > fixed > original
    clean_file = PROJECT_ROOT / "artifacts" / "flattened" / "NeoFlowToken_flattened_clean.sol"
    fixed_file = PROJECT_ROOT / "artifacts" / "flattened" / "NeoFlowToken_flattened_fixed.sol"
    
    if clean_file.exists():
        with open(clean_file, "r", encoding="utf-8") as f:
            return f.read()
    
    if fixed_file.exists():
        with open(fixed_file, "r", encoding="utf-8") as f:
            return f.read()
    
    if not FLATTENED_FILE.exists():
        raise FileNotFoundError(f"Arquivo flattened não encontrado: {FLATTENED_FILE}")
    
    with open(FLATTENED_FILE, "r", encoding="utf-8") as f:
        return f.read()

def generate_standard_json():
    """Gera Standard JSON Input para OKLink"""
    
    source_code = read_flattened_source()
    
    # Standard JSON Input conforme documentação OKLink
    standard_json = {
        "language": "Solidity",
        "sources": {
            "contracts/NeoFlowToken.sol": {
                "content": source_code
            }
        },
        "settings": {
            "optimizer": {
                "enabled": True,
                "runs": 200
            },
            "evmVersion": "paris",  # Conforme cache: "evmVersion": "paris"
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
    
    # Criar diretório se não existir
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    # Salvar JSON
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(standard_json, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Standard JSON Input gerado com sucesso!")
    print(f"📁 Localização: {OUTPUT_FILE}")
    print(f"📊 Tamanho: {OUTPUT_FILE.stat().st_size / 1024:.1f} KB")
    print("")
    print("💡 Use este arquivo para verificação no OKLink:")
    print(f"   - Método: solidity-standard-json-input")
    print(f"   - Arquivo: {OUTPUT_FILE.name}")
    
    return OUTPUT_FILE

if __name__ == "__main__":
    generate_standard_json()

