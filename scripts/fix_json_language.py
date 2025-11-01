#!/usr/bin/env python3
"""
Adiciona o campo 'language' ao JSON de compilação para Sourcify/Etherscan
"""
import json
from pathlib import Path

def fix_json():
    """Adiciona campo language ao JSON"""
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
        data = json.load(f)
    
    # Adiciona campo language no topo
    if 'language' not in data:
        data['language'] = 'Solidity'
        print("   ✅ Campo 'language' adicionado")
    
    # Verifica se tem sources no formato correto
    if 'sources' not in data:
        print("   ⚠️  Campo 'sources' não encontrado")
    
    # Salva o JSON corrigido
    output_file = project_root / "sourcify_verification.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    
    print(f"\n✅ JSON corrigido salvo em: {output_file}")
    print(f"   Use este arquivo no Sourcify!")
    
    return True

if __name__ == "__main__":
    fix_json()

