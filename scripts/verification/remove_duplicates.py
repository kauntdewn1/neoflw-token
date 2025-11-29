#!/usr/bin/env python3
"""
Remove declarações duplicadas do arquivo flattened
Mantém apenas a primeira ocorrência de cada interface/contrato
"""

import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent
FLATTENED_FILE = PROJECT_ROOT / "artifacts" / "flattened" / "NeoFlowToken_flattened_fixed.sol"
CLEAN_FILE = PROJECT_ROOT / "artifacts" / "flattened" / "NeoFlowToken_flattened_clean.sol"

def remove_duplicates():
    """Remove declarações duplicadas mantendo apenas a primeira ocorrência"""
    
    with open(FLATTENED_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    
    lines = content.split('\n')
    seen_declarations = set()
    clean_lines = []
    skip_until_end = False
    current_declaration = None
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Detectar início de declaração (interface, contract, abstract contract, library)
        match = re.match(r'^\s*(interface|contract|abstract\s+contract|library)\s+(\w+)', line)
        
        if match:
            decl_type = match.group(1)
            decl_name = match.group(2)
            decl_key = f"{decl_type} {decl_name}"
            
            # Se já vimos esta declaração, pular até o final
            if decl_key in seen_declarations:
                skip_until_end = True
                current_declaration = decl_name
                # Pular a linha de declaração
                i += 1
                continue
            else:
                # Primeira vez vendo esta declaração
                seen_declarations.add(decl_key)
                skip_until_end = False
                current_declaration = None
        
        # Se estamos pulando uma declaração duplicada
        if skip_until_end:
            # Verificar se chegamos ao final do bloco (próxima declaração ou fim do arquivo)
            # Procurar por chaves fechadas ou próxima declaração
            if re.match(r'^\s*(interface|contract|abstract\s+contract|library|// ===)', line):
                # Próxima declaração encontrada, parar de pular
                skip_until_end = False
                current_declaration = None
                # Não pular esta linha, processar normalmente
            else:
                # Ainda dentro da declaração duplicada, pular
                i += 1
                continue
        
        # Adicionar linha ao resultado
        clean_lines.append(line)
        i += 1
    
    clean_content = '\n'.join(clean_lines)
    
    # Salvar arquivo limpo
    with open(CLEAN_FILE, "w", encoding="utf-8") as f:
        f.write(clean_content)
    
    print(f"✅ Arquivo limpo gerado!")
    print(f"📁 Original: {FLATTENED_FILE}")
    print(f"📁 Limpo: {CLEAN_FILE}")
    print(f"📊 Linhas: {len(lines)} → {len(clean_lines)}")
    print(f"📋 Declarações únicas: {len(seen_declarations)}")
    
    return CLEAN_FILE

if __name__ == "__main__":
    remove_duplicates()

