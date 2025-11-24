#!/usr/bin/env python3
"""
Adiciona todas as fontes do OpenZeppelin ao JSON
"""
import json
from pathlib import Path

def read_file_content(file_path):
    """Lê conteúdo de arquivo"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"   ⚠️  Erro ao ler {file_path}: {e}")
        return None

def add_openzeppelin_sources():
    """Adiciona fontes do OpenZeppelin ao JSON"""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    json_file = project_root / "sourcify_standard_json.json"
    
    if not json_file.exists():
        print("❌ Arquivo JSON não encontrado")
        return False
    
    print(f"📂 Lendo: {json_file}")
    
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Lista de arquivos OpenZeppelin necessários
    openzeppelin_files = [
        "contracts/.cache/openzeppelin/4.9.6/contracts/access/Ownable.sol",
        "contracts/.cache/openzeppelin/4.9.6/contracts/token/ERC20/ERC20.sol",
        "contracts/.cache/openzeppelin/4.9.6/contracts/token/ERC20/IERC20.sol",
        "contracts/.cache/openzeppelin/4.9.6/contracts/token/ERC20/extensions/IERC20Metadata.sol",
        "contracts/.cache/openzeppelin/4.9.6/contracts/utils/Context.sol",
        "contracts/.cache/openzeppelin/4.9.6/contracts/security/ReentrancyGuard.sol"
    ]
    
    print("📦 Adicionando fontes do OpenZeppelin...")
    added_count = 0
    
    for oz_path in openzeppelin_files:
        full_path = project_root / oz_path
        
        if full_path.exists():
            content = read_file_content(full_path)
            if content:
                data["sources"][oz_path] = {"content": content}
                added_count += 1
                print(f"   ✅ {oz_path}")
            else:
                print(f"   ⚠️  Arquivo vazio: {oz_path}")
        else:
            print(f"   ❌ Não encontrado: {oz_path}")
    
    # Salva o JSON atualizado
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    
    print(f"\n✅ JSON atualizado: {json_file}")
    print(f"   Total de fontes: {len(data['sources'])}")
    print(f"   Fontes OpenZeppelin adicionadas: {added_count}")
    
    return True

if __name__ == "__main__":
    add_openzeppelin_sources()

