#!/usr/bin/env python3
"""
Converte JSON do Ape para Standard JSON Input correto para Blockscout
Garante que tem o campo 'language' obrigatório
"""
import json
from pathlib import Path

def fix_json_for_blockscout():
    """Converte etherscan_verification_fixed.json para formato Blockscout"""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    # Lê o arquivo do Ape
    ape_file = project_root / "etherscan_verification_fixed.json"
    output_file = project_root / "blockscout_standard_json.json"
    
    if not ape_file.exists():
        print("❌ Arquivo etherscan_verification_fixed.json não encontrado")
        return False
    
    print(f"📂 Lendo: {ape_file}")
    
    with open(ape_file, 'r', encoding='utf-8') as f:
        ape_data = json.load(f)
    
    # Extrai informações do formato Ape
    compilers = ape_data.get('compilers', [])
    if not compilers:
        print("❌ Formato inválido: não encontrou 'compilers'")
        return False
    
    compiler_info = compilers[0]
    settings = compiler_info.get('settings', {})
    sources = ape_data.get('sources', {})
    
    # Cria Standard JSON Input no formato correto
    standard_json = {
        "language": "Solidity",  # OBRIGATÓRIO para Blockscout!
        "sources": {},
        "settings": {
            "optimizer": settings.get('optimizer', {
                "enabled": True,
                "runs": 200
            }),
            "outputSelection": settings.get('outputSelection', {}),
            "evmVersion": settings.get('evmVersion', "default"),
            "remappings": settings.get('remappings', [])
        }
    }
    
    # Copia sources removendo URLs se existirem
    for source_path, source_data in sources.items():
        standard_json["sources"][source_path] = {
            "content": source_data.get("content", "")
        }
    
    # Salva o JSON no formato correto
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(standard_json, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ JSON corrigido e salvo em: {output_file}")
    print(f"   Language: {standard_json['language']}")
    print(f"   Sources: {len(standard_json['sources'])} arquivos")
    print(f"   Optimization: {standard_json['settings']['optimizer']['enabled']}")
    print(f"   Runs: {standard_json['settings']['optimizer']['runs']}")
    
    return True

if __name__ == "__main__":
    fix_json_for_blockscout()

