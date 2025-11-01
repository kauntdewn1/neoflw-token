#!/usr/bin/env python3
"""
Remove campo compilerVersion inválido do JSON
"""
import json
from pathlib import Path

def remove_compiler_version():
    """Remove compilerVersion do JSON"""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    json_file = project_root / "sourcify_standard_json.json"
    
    if not json_file.exists():
        print("❌ Arquivo não encontrado")
        return False
    
    print(f"📂 Lendo: {json_file}")
    
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Remove compilerVersion se existir em settings
    if 'settings' in data and 'compilerVersion' in data['settings']:
        del data['settings']['compilerVersion']
        print("   ✅ Campo 'compilerVersion' removido")
    
    # Salva o JSON corrigido
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    
    print(f"\n✅ JSON corrigido: {json_file}")
    
    return True

if __name__ == "__main__":
    remove_compiler_version()

