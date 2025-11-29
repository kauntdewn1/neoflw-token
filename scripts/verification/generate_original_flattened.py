#!/usr/bin/env python3
"""
Gera código flattened do NeoFlowToken ORIGINAL (sem ContractMetadata)
para verificar o contrato deployado em 0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2
"""

from pathlib import Path
import subprocess

PROJECT_ROOT = Path(__file__).parent.parent.parent
OUTPUT_FILE = PROJECT_ROOT / "artifacts" / "flattened" / "NeoFlowToken_original_flattened.sol"

# Código original do NeoFlowToken (sem ContractMetadata)
ORIGINAL_CODE = """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NeoFlowToken is ERC20, Ownable {
    event Burned(address indexed account, uint256 amount);

    constructor(uint256 initialSupply) ERC20("NEOFlowOFF", "NEOFLW") {
        _mint(msg.sender, initialSupply);
    }

    function burn(uint256 amount) public {
        require(amount > 0, "Amount must be greater than 0");
        _burn(msg.sender, amount);
        emit Burned(msg.sender, amount);
    }
}
"""

def generate_flattened():
    """Gera código flattened do contrato original"""
    
    # Criar arquivo temporário com código original
    temp_file = PROJECT_ROOT / "contracts" / "NeoFlowToken_original.sol"
    temp_file.write_text(ORIGINAL_CODE)
    
    try:
        # Usar Ape para fazer flatten
        print("🔨 Gerando código flattened do contrato original...")
        print("   (sem ContractMetadata)")
        print()
        
        # Compilar e fazer flatten
        result = subprocess.run(
            ["ape", "compile", "--format", "flattened"],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            # Procurar arquivo flattened gerado
            flattened_dir = PROJECT_ROOT / "artifacts" / "flattened"
            flattened_file = flattened_dir / "NeoFlowToken_original_flattened.sol"
            
            if flattened_file.exists():
                # Mover para o local correto
                OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
                OUTPUT_FILE.write_text(flattened_file.read_text())
                print(f"✅ Arquivo flattened gerado!")
                print(f"📁 Localização: {OUTPUT_FILE}")
                return OUTPUT_FILE
            else:
                print("⚠️  Arquivo flattened não encontrado automaticamente")
                print("   Tentando método alternativo...")
        
        # Método alternativo: usar solc diretamente ou fazer flatten manual
        print("💡 Use o código flattened manualmente:")
        print("   1. Remova a linha: import './ContractMetadata.sol';")
        print("   2. Remova: , ContractMetadata da herança")
        print("   3. Remova a função: _canSetContractURI()")
        print("   4. Use o arquivo: artifacts/flattened/NeoFlowToken_flattened_clean.sol")
        print("      e remova manualmente as partes do ContractMetadata")
        
    finally:
        # Limpar arquivo temporário
        if temp_file.exists():
            temp_file.unlink()

if __name__ == "__main__":
    generate_flattened()

