#!/usr/bin/env python3
"""
Script para criar código Solidity "flattened" (achatado) para verificação no Etherscan
Inclui todas as dependências do OpenZeppelin inline
"""
import os
import re
from pathlib import Path

def read_file_content(file_path):
    """Lê o conteúdo de um arquivo"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"⚠️  Erro ao ler {file_path}: {e}")
        return None

def resolve_imports(content, base_path, already_included=None):
    """Resolve imports recursivamente"""
    if already_included is None:
        already_included = set()
    
    result = []
    lines = content.split('\n')
    
    for line in lines:
        # Procura por imports
        import_match = re.match(r'^\s*import\s+["\'](.+)["\'];?\s*$', line)
        
        if import_match:
            import_path = import_match.group(1)
            
            # Resolve caminho do import
            if import_path.startswith('@openzeppelin/'):
                # Converte @openzeppelin/ para o caminho real
                relative_path = import_path.replace('@openzeppelin/', 'contracts/.cache/openzeppelin/4.9.6/contracts/')
                full_path = base_path / relative_path
            elif import_path.startswith('./') or import_path.startswith('../'):
                full_path = (base_path / import_path).resolve()
            else:
                full_path = base_path / import_path
            
            # Lê o arquivo importado se ainda não foi incluído
            if str(full_path) not in already_included and full_path.exists():
                imported_content = read_file_content(full_path)
                if imported_content:
                    already_included.add(str(full_path))
                    # Remove imports do arquivo importado e resolve recursivamente
                    imported_content = resolve_imports(imported_content, full_path.parent, already_included)
                    result.append(f"\n// === Imported from {import_path} ===\n")
                    result.append(imported_content)
                    result.append(f"\n// === End of {import_path} ===\n\n")
            # Não adiciona a linha de import original
        else:
            result.append(line)
    
    return '\n'.join(result)

def create_flattened_code():
    """Cria código Solidity flattened para o NeoFlowToken"""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    # Caminho do contrato
    contract_file = project_root / "contracts" / "NeoFlowToken.sol"
    
    if not contract_file.exists():
        print(f"❌ Arquivo não encontrado: {contract_file}")
        return False
    
    print("📝 Criando código flattened para NeoFlowToken...")
    
    # Lê o contrato
    contract_content = read_file_content(contract_file)
    if not contract_content:
        return False
    
    # Resolve imports
    print("🔍 Resolvendo imports...")
    flattened = resolve_imports(contract_content, contract_file.parent)
    
    # Salva o arquivo flattened
    output_file = project_root / "NeoFlowToken_flattened.sol"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(flattened)
    
    print(f"✅ Código flattened criado: {output_file}")
    print(f"   Tamanho: {len(flattened)} caracteres")
    
    return True

if __name__ == "__main__":
    create_flattened_code()

