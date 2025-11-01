#!/usr/bin/env python3
"""
Script para corrigir o JSON de compilação removendo URLs e incluindo conteúdo literal
"""
import json
import os
from pathlib import Path

def read_file_content(file_path):
    """Lê o conteúdo de um arquivo"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"⚠️  Erro ao ler {file_path}: {e}")
        return None

def fix_json_sources(json_data, project_root):
    """Remove URLs e adiciona conteúdo literal às fontes"""
    if 'sources' not in json_data:
        return json_data
    
    sources = json_data['sources']
    fixed_count = 0
    
    print("🔧 Corrigindo fontes no JSON...")
    
    for source_path, source_data in sources.items():
        # Se tem URLs mas não tem content, tenta ler o arquivo
        if source_data.get('urls') and not source_data.get('content'):
            # Tenta encontrar o arquivo no projeto
            file_path = project_root / source_path
            
            if file_path.exists():
                content = read_file_content(file_path)
                if content:
                    source_data['content'] = content
                    source_data.pop('urls', None)  # Remove URLs
                    fixed_count += 1
                    print(f"   ✅ Corrigido: {source_path}")
            else:
                print(f"   ⚠️  Arquivo não encontrado: {source_path}")
                # Remove a fonte se não conseguir encontrar
                # Não removemos, apenas avisamos
    
    print(f"\n✅ {fixed_count} fontes corrigidas")
    return json_data

def main():
    """Função principal"""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    # Encontra o arquivo JSON
    json_files = [
        project_root / ".build" / "__local__.json",
        project_root / "__local__.json",
        project_root / ".ape" / "__local__.json"
    ]
    
    json_file = None
    for f in json_files:
        if f.exists():
            json_file = f
            break
    
    if not json_file:
        print("❌ Arquivo JSON de compilação não encontrado")
        print("   Execute 'ape compile' primeiro")
        return False
    
    print(f"📂 Lendo JSON: {json_file}")
    
    # Lê o JSON
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
    except Exception as e:
        print(f"❌ Erro ao ler JSON: {e}")
        return False
    
    # Corrige as fontes
    json_data = fix_json_sources(json_data, project_root)
    
    # Salva o JSON corrigido
    output_file = project_root / "etherscan_verification.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=2)
    
    print(f"\n✅ JSON corrigido salvo em: {output_file}")
    print(f"   Use este arquivo no Etherscan!")
    
    return True

if __name__ == "__main__":
    main()

