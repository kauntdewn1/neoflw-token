#!/usr/bin/env python3
"""
Remove URLs do JSON de compilação, mantendo apenas content
"""
import json
from pathlib import Path

def remove_urls_from_json():
    """Remove URLs do JSON, mantendo apenas content"""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    json_file = project_root / "etherscan_verification.json"
    
    if not json_file.exists():
        json_file = project_root / ".build" / "__local__.json"
    
    if not json_file.exists():
        print("❌ Arquivo JSON não encontrado")
        return False
    
    print(f"📂 Lendo: {json_file}")
    
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Remove URLs de todas as fontes
    if 'sources' in data:
        removed_count = 0
        for source_path, source_data in data['sources'].items():
            if 'urls' in source_data:
                if 'content' in source_data:
                    # Tem content, pode remover URLs
                    del source_data['urls']
                    removed_count += 1
                    print(f"   ✅ Removido URLs de: {source_path}")
                else:
                    print(f"   ⚠️  {source_path} tem URLs mas não tem content")
        
        print(f"\n✅ {removed_count} URLs removidas")
    
    # Salva o JSON corrigido
    output_file = project_root / "etherscan_verification_fixed.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    
    print(f"\n✅ JSON corrigido salvo em: {output_file}")
    print(f"   Use este arquivo no Etherscan!")
    
    return True

if __name__ == "__main__":
    remove_urls_from_json()

