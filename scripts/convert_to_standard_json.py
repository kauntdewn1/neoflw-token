#!/usr/bin/env python3
"""
Converte JSON do Ape Framework para Standard JSON Input do Solidity
"""
import json
from pathlib import Path

def convert_to_standard_json():
    """Converte formato Ape para Standard JSON Input"""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    json_file = project_root / "etherscan_verification_fixed.json"
    
    if not json_file.exists():
        json_file = project_root / ".build" / "__local__.json"
    
    if not json_file.exists():
        print("❌ Arquivo JSON não encontrado")
        return False
    
    print(f"📂 Lendo: {json_file}")
    
    with open(json_file, 'r', encoding='utf-8') as f:
        ape_data = json.load(f)
    
    # Extrai informações do formato Ape
    compiler_info = ape_data.get('compilers', [{}])[0] if ape_data.get('compilers') else {}
    settings = compiler_info.get('settings', {})
    sources = ape_data.get('sources', {})
    
    # Cria Standard JSON Input
    standard_json = {
        "language": "Solidity",
        "sources": {},
        "settings": {
            "optimizer": settings.get('optimizer', {
                "enabled": True,
                "runs": 200
            }),
            "outputSelection": settings.get('outputSelection', {}),
            "remappings": settings.get('remappings', [])
        }
    }
    
    # Copia sources (removendo URLs se existirem)
    for source_path, source_data in sources.items():
        standard_json["sources"][source_path] = {
            "content": source_data.get("content", "")
        }
        # Remove URLs se existirem
        if "urls" in standard_json["sources"][source_path]:
            del standard_json["sources"][source_path]["urls"]
    
    # NÃO adiciona compilerVersion - não é válido no Standard JSON Input
    # A versão do compilador é especificada no Sourcify separadamente
    
    # Salva o JSON no formato correto
    output_file = project_root / "sourcify_standard_json.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(standard_json, f, indent=2)
    
    print(f"\n✅ JSON convertido para Standard JSON Input")
    print(f"   Arquivo: {output_file}")
    print(f"   Language: {standard_json['language']}")
    print(f"   Sources: {len(standard_json['sources'])} arquivos")
    
    return True

if __name__ == "__main__":
    convert_to_standard_json()

