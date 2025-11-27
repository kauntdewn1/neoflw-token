#!/usr/bin/env python3
"""
Gera código Solidity flattened completo para NeoFlowToken
Inclui todos os contratos do OpenZeppelin inline
"""
import re
from pathlib import Path

# Caminhos dos contratos OpenZeppelin (versão 4.9.6)
OPENZEPPELIN_BASE = "https://raw.githubusercontent.com/OpenZeppelin/openzeppelin-contracts/v4.9.6/contracts"

# Mapeamento de imports para URLs do GitHub
IMPORT_MAP = {
    "@openzeppelin/contracts/token/ERC20/ERC20.sol": "token/ERC20/ERC20.sol",
    "@openzeppelin/contracts/token/ERC20/IERC20.sol": "token/ERC20/IERC20.sol",
    "@openzeppelin/contracts/token/ERC20/extensions/IERC20Metadata.sol": "token/ERC20/extensions/IERC20Metadata.sol",
    "@openzeppelin/contracts/access/Ownable.sol": "access/Ownable.sol",
    "@openzeppelin/contracts/utils/Context.sol": "utils/Context.sol",
}

def download_from_github(relative_path):
    """Baixa arquivo do GitHub OpenZeppelin"""
    import urllib.request
    url = f"{OPENZEPPELIN_BASE}/{relative_path}"
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        print(f"⚠️  Erro ao baixar {url}: {e}")
        return None

def resolve_import_path(import_path, current_file_path=None):
    """Resolve um caminho de import para URL do GitHub"""
    if import_path.startswith('@openzeppelin/'):
        # Mapeamento direto
        if import_path in IMPORT_MAP:
            return IMPORT_MAP[import_path]
        # Extrai caminho relativo
        return import_path.replace('@openzeppelin/contracts/', '')
    elif import_path.startswith('./') or import_path.startswith('../'):
        # Import relativo - precisa do contexto do arquivo atual
        if current_file_path:
            # Calcula caminho relativo baseado no arquivo atual
            if current_file_path.startswith('token/ERC20/'):
                if import_path == './IERC20.sol':
                    return 'token/ERC20/IERC20.sol'
                elif import_path == './extensions/IERC20Metadata.sol':
                    return 'token/ERC20/extensions/IERC20Metadata.sol'
            elif current_file_path.startswith('access/'):
                if import_path == '../utils/Context.sol':
                    return 'utils/Context.sol'
            elif current_file_path.startswith('token/ERC20/extensions/'):
                if import_path == '../IERC20.sol':
                    return 'token/ERC20/IERC20.sol'
            elif current_file_path.startswith('utils/'):
                # Context não tem imports
                pass
        # Tenta resolver baseado no padrão
        if import_path.endswith('IERC20.sol'):
            return 'token/ERC20/IERC20.sol'
        elif import_path.endswith('IERC20Metadata.sol'):
            return 'token/ERC20/extensions/IERC20Metadata.sol'
        elif import_path.endswith('Context.sol'):
            return 'utils/Context.sol'
    return None

def resolve_imports_recursive(content, current_file_path=None, already_included=None):
    """Resolve imports recursivamente, baixando do GitHub se necessário"""
    if already_included is None:
        already_included = set()
    
    result = []
    lines = content.split('\n')
    
    for line in lines:
        # Procura por imports
        import_match = re.match(r'^\s*import\s+["\'](.+)["\'];?\s*$', line)
        
        if import_match:
            import_path = import_path_raw = import_match.group(1)
            
            # Cria chave única para o import
            import_key = f"{current_file_path or 'root'}:{import_path}"
            
            # Verifica se já foi incluído
            if import_key in already_included:
                continue  # Pula o import
            
            already_included.add(import_key)
            
            # Resolve caminho do import
            relative_path = resolve_import_path(import_path, current_file_path)
            
            imported_content = None
            if relative_path:
                print(f"📥 Baixando {import_path}...")
                imported_content = download_from_github(relative_path)
            
            # Processa o conteúdo importado
            if imported_content:
                # Remove imports do arquivo importado e resolve recursivamente
                imported_content = resolve_imports_recursive(imported_content, relative_path, already_included)
                result.append(f"\n// === Imported from {import_path} ===\n")
                result.append(imported_content)
                result.append(f"\n// === End of {import_path} ===\n\n")
            else:
                print(f"⚠️  Não foi possível resolver: {import_path}")
        else:
            # Linha normal, adiciona ao resultado
            result.append(line)
    
    return '\n'.join(result)

def generate_flattened_token():
    """Gera código flattened completo para NeoFlowToken"""
    project_root = Path(__file__).parent.parent.parent
    contract_file = project_root / "contracts" / "NeoFlowToken.sol"
    output_file = project_root / "artifacts" / "flattened" / "NeoFlowToken_flattened.sol"
    
    if not contract_file.exists():
        print(f"❌ Arquivo não encontrado: {contract_file}")
        return False
    
    print("📝 Gerando código flattened para NeoFlowToken...")
    
    # Lê o contrato
    with open(contract_file, 'r', encoding='utf-8') as f:
        contract_content = f.read()
    
    # Resolve imports
    print("🔍 Resolvendo imports do OpenZeppelin...")
    flattened = resolve_imports_recursive(contract_content, contract_file.parent)
    
    # Garante que o diretório existe
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Salva o arquivo flattened
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(flattened)
    
    print(f"✅ Código flattened criado: {output_file}")
    print(f"   Tamanho: {len(flattened):,} caracteres")
    print(f"   Linhas: {len(flattened.splitlines()):,}")
    
    return True

if __name__ == "__main__":
    generate_flattened_token()

