#!/usr/bin/env python3
"""
Baixa arquivos do OpenZeppelin do GitHub e adiciona ao JSON
"""
import json
import requests
from pathlib import Path

OPENZEPPELIN_VERSION = "4.9.6"
BASE_URL = f"https://raw.githubusercontent.com/OpenZeppelin/openzeppelin-contracts/v{OPENZEPPELIN_VERSION}/contracts"

FILES_TO_DOWNLOAD = {
    "contracts/.cache/openzeppelin/4.9.6/contracts/access/Ownable.sol": "access/Ownable.sol",
    "contracts/.cache/openzeppelin/4.9.6/contracts/token/ERC20/ERC20.sol": "token/ERC20/ERC20.sol",
    "contracts/.cache/openzeppelin/4.9.6/contracts/token/ERC20/IERC20.sol": "token/ERC20/IERC20.sol",
    "contracts/.cache/openzeppelin/4.9.6/contracts/token/ERC20/extensions/IERC20Metadata.sol": "token/ERC20/extensions/IERC20Metadata.sol",
    "contracts/.cache/openzeppelin/4.9.6/contracts/utils/Context.sol": "utils/Context.sol",
    "contracts/.cache/openzeppelin/4.9.6/contracts/security/ReentrancyGuard.sol": "security/ReentrancyGuard.sol"
}

def download_file(url):
    """Baixa arquivo do GitHub"""
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.text
        else:
            print(f"   ⚠️  Erro HTTP {response.status_code}: {url}")
            return None
    except Exception as e:
        print(f"   ⚠️  Erro ao baixar {url}: {e}")
        return None

def add_openzeppelin_to_json():
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
    
    print("📦 Baixando fontes do OpenZeppelin do GitHub...")
    added_count = 0
    
    for json_path, github_path in FILES_TO_DOWNLOAD.items():
        url = f"{BASE_URL}/{github_path}"
        print(f"   📥 Baixando: {github_path}")
        
        content = download_file(url)
        if content:
            data["sources"][json_path] = {"content": content}
            added_count += 1
            print(f"   ✅ Adicionado: {json_path}")
        else:
            print(f"   ❌ Falha ao baixar: {github_path}")
    
    # Salva o JSON atualizado
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    
    print(f"\n✅ JSON atualizado: {json_file}")
    print(f"   Total de fontes: {len(data['sources'])}")
    print(f"   Fontes OpenZeppelin adicionadas: {added_count}")
    
    return True

if __name__ == "__main__":
    add_openzeppelin_to_json()

