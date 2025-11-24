#!/usr/bin/env python3
"""
Cria JSON completo com todas as fontes incluídas (incluindo OpenZeppelin)
"""
import json
from pathlib import Path

def read_file_content(file_path):
    """Lê conteúdo de arquivo"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return None

def create_complete_json():
    """Cria JSON completo com todas as fontes"""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    # Lê o JSON original do Ape que tem todas as fontes
    ape_json = project_root / "etherscan_verification_fixed.json"
    
    if not ape_json.exists():
        print("❌ Arquivo não encontrado")
        return False
    
    print(f"📂 Lendo: {ape_json}")
    
    with open(ape_json, 'r', encoding='utf-8') as f:
        ape_data = json.load(f)
    
    # Extrai settings
    compiler_info = ape_data.get('compilers', [{}])[0] if ape_data.get('compilers') else {}
    settings = compiler_info.get('settings', {})
    
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
    
    # Copia TODAS as fontes do JSON original (incluindo OpenZeppelin)
    sources = ape_data.get('sources', {})
    
    for source_path, source_data in sources.items():
        # Só inclui se tiver content
        if source_data.get('content'):
            standard_json["sources"][source_path] = {
                "content": source_data["content"]
            }
    
    # Se não encontrou fontes do OpenZeppelin no JSON, tenta ler dos arquivos
    if len(standard_json["sources"]) <= 3:  # Só tem os 3 contratos principais
        print("   ⚠️  Fontes do OpenZeppelin não encontradas, tentando ler dos arquivos...")
        
        # Tenta adicionar fontes do OpenZeppelin manualmente
        openzeppelin_paths = [
            "contracts/.cache/openzeppelin/4.9.6/contracts/access/Ownable.sol",
            "contracts/.cache/openzeppelin/4.9.6/contracts/token/ERC20/ERC20.sol",
            "contracts/.cache/openzeppelin/4.9.6/contracts/token/ERC20/IERC20.sol",
            "contracts/.cache/openzeppelin/4.9.6/contracts/token/ERC20/extensions/IERC20Metadata.sol",
            "contracts/.cache/openzeppelin/4.9.6/contracts/utils/Context.sol",
            "contracts/.cache/openzeppelin/4.9.6/contracts/security/ReentrancyGuard.sol"
        ]
        
        for oz_path in openzeppelin_paths:
            full_path = project_root / oz_path
            if full_path.exists():
                content = read_file_content(full_path)
                if content:
                    standard_json["sources"][oz_path] = {"content": content}
                    print(f"   ✅ Adicionado: {oz_path}")
    
    # Salva o JSON completo
    output_file = project_root / "sourcify_standard_json.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(standard_json, f, indent=2)
    
    print(f"\n✅ JSON completo criado: {output_file}")
    print(f"   Total de fontes: {len(standard_json['sources'])}")
    print(f"   Fontes incluídas:")
    for source in sorted(standard_json['sources'].keys()):
        print(f"     - {source}")
    
    return True

if __name__ == "__main__":
    create_complete_json()

