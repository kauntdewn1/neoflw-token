#!/usr/bin/env python3
"""
Corrige múltiplas licenças SPDX no arquivo flattened
Mantém apenas uma licença no topo do arquivo
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent
FLATTENED_FILE = PROJECT_ROOT / "artifacts" / "flattened" / "NeoFlowToken_flattened.sol"
FIXED_FILE = PROJECT_ROOT / "artifacts" / "flattened" / "NeoFlowToken_flattened_fixed.sol"

def fix_license():
    """Remove múltiplas licenças SPDX, mantendo apenas uma no topo"""
    
    with open(FLATTENED_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    
    lines = content.split('\n')
    fixed_lines = []
    seen_first_license = False
    
    for i, line in enumerate(lines):
        # Primeira licença SPDX - manter
        if "SPDX-License-Identifier" in line and not seen_first_license:
            fixed_lines.append("// SPDX-License-Identifier: MIT")
            seen_first_license = True
            # Pular a linha original e a próxima se for vazia
            continue
        
        # Ignorar outras licenças SPDX
        if "SPDX-License-Identifier" in line and seen_first_license:
            continue
        
        # Manter todas as outras linhas
        fixed_lines.append(line)
    
    fixed_content = '\n'.join(fixed_lines)
    
    # Salvar arquivo corrigido
    with open(FIXED_FILE, "w", encoding="utf-8") as f:
        f.write(fixed_content)
    
    print(f"✅ Arquivo corrigido gerado!")
    print(f"📁 Original: {FLATTENED_FILE}")
    print(f"📁 Corrigido: {FIXED_FILE}")
    print(f"📊 Linhas: {len(lines)} → {len(fixed_lines)}")
    
    # Contar licenças
    original_licenses = content.count("SPDX-License-Identifier")
    fixed_licenses = fixed_content.count("SPDX-License-Identifier")
    print(f"📋 Licenças SPDX: {original_licenses} → {fixed_licenses}")
    
    return FIXED_FILE

if __name__ == "__main__":
    fix_license()

