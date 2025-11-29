#!/usr/bin/env python3
"""
Script para corrigir endereços de contratos após auditoria
Atualiza todos os arquivos com os endereços corretos do Polygon Mainnet
"""

import os
import sys
from pathlib import Path

# Endereços corretos do Polygon Mainnet (da auditoria)
POLYGON_ADDRESSES = {
    "token": "0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2",
    "vault": "0x07E39107d4B35b64f9f2310B9A2B8e5262A4ee41",
    "claim": "0x407C037906d6441ECD4a3F9064eab2E6CF03b36b",
}

# Endereços do Sepolia (para remover/marcar)
SEPOLIA_ADDRESSES = {
    "token": "0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87",
    "vault": "0x7A3109a7A978473142c655C3DBbfad4e5Bc37aeD",
    "claim": "0xEE96C0813e84bb7Ea162b1594b8Bff61dB79A7Ca",
}

def update_address_file(file_path: str, address: str, contract_type: str):
    """Atualiza um arquivo de endereço"""
    try:
        os.makedirs(os.path.dirname(file_path) if os.path.dirname(file_path) else ".", exist_ok=True)
        
        with open(file_path, "w") as f:
            f.write(address + "\n")
        
        print(f"✅ {contract_type}: {file_path} → {address}")
        return True
    except Exception as e:
        print(f"❌ Erro ao atualizar {file_path}: {e}")
        return False

def update_env_file(env_path: str = ".env"):
    """Atualiza o arquivo .env com os endereços corretos"""
    try:
        if not os.path.exists(env_path):
            print(f"⚠️  Arquivo {env_path} não encontrado")
            return False
        
        # Ler arquivo atual
        with open(env_path, "r") as f:
            lines = f.readlines()
        
        # Atualizar linhas
        updated = False
        new_lines = []
        
        for line in lines:
            original_line = line
            
            # Atualizar Token
            if line.startswith("NEXT_PUBLIC_TOKEN_ADDRESS="):
                line = f"NEXT_PUBLIC_TOKEN_ADDRESS={POLYGON_ADDRESSES['token']}\n"
                if original_line.strip() != line.strip():
                    updated = True
                    print(f"✅ Atualizado .env: NEXT_PUBLIC_TOKEN_ADDRESS → {POLYGON_ADDRESSES['token']}")
            
            # Atualizar Vault
            elif line.startswith("NEXT_PUBLIC_VAULT_ADDRESS="):
                line = f"NEXT_PUBLIC_VAULT_ADDRESS={POLYGON_ADDRESSES['vault']}\n"
                if original_line.strip() != line.strip():
                    updated = True
                    print(f"✅ Atualizado .env: NEXT_PUBLIC_VAULT_ADDRESS → {POLYGON_ADDRESSES['vault']}")
            
            # Atualizar Claim
            elif line.startswith("NEXT_PUBLIC_CLAIM_ADDRESS="):
                line = f"NEXT_PUBLIC_CLAIM_ADDRESS={POLYGON_ADDRESSES['claim']}\n"
                if original_line.strip() != line.strip():
                    updated = True
                    print(f"✅ Atualizado .env: NEXT_PUBLIC_CLAIM_ADDRESS → {POLYGON_ADDRESSES['claim']}")
            
            new_lines.append(line)
        
        # Escrever arquivo atualizado
        if updated:
            with open(env_path, "w") as f:
                f.writelines(new_lines)
            print(f"✅ Arquivo .env atualizado com sucesso!")
        else:
            print(f"ℹ️  Arquivo .env já está atualizado")
        
        return True
    except Exception as e:
        print(f"❌ Erro ao atualizar .env: {e}")
        return False

def main():
    """Função principal"""
    print("=" * 80)
    print("🔧 CORREÇÃO DE ENDEREÇOS DE CONTRATOS")
    print("=" * 80)
    print()
    print("📋 Endereços do Polygon Mainnet:")
    print(f"   Token: {POLYGON_ADDRESSES['token']}")
    print(f"   Vault: {POLYGON_ADDRESSES['vault']}")
    print(f"   Claim: {POLYGON_ADDRESSES['claim']}")
    print()
    print("=" * 80)
    print("📝 ATUALIZANDO ARQUIVOS...")
    print("=" * 80)
    print()
    
    # Lista de arquivos para atualizar
    files_to_update = [
        # Token
        (".token_address.txt", POLYGON_ADDRESSES['token'], "Token"),
        ("artifacts/addresses/.token_address.txt", POLYGON_ADDRESSES['token'], "Token"),
        
        # Vault
        (".vault_address.txt", POLYGON_ADDRESSES['vault'], "Vault"),
        ("artifacts/addresses/.vault_address.txt", POLYGON_ADDRESSES['vault'], "Vault"),
        
        # Claim
        (".claim_address.txt", POLYGON_ADDRESSES['claim'], "Claim"),
        ("artifacts/addresses/.claim_address.txt", POLYGON_ADDRESSES['claim'], "Claim"),
    ]
    
    success_count = 0
    for file_path, address, contract_type in files_to_update:
        if update_address_file(file_path, address, contract_type):
            success_count += 1
    
    print()
    print("=" * 80)
    print("📝 ATUALIZANDO .env...")
    print("=" * 80)
    print()
    
    update_env_file()
    
    print()
    print("=" * 80)
    print("✅ RESUMO")
    print("=" * 80)
    print()
    print(f"✅ {success_count}/{len(files_to_update)} arquivos atualizados")
    print()
    print("📋 Endereços atualizados:")
    print(f"   Token:  {POLYGON_ADDRESSES['token']}")
    print(f"   Vault: {POLYGON_ADDRESSES['vault']}")
    print(f"   Claim: {POLYGON_ADDRESSES['claim']}")
    print()
    print("⚠️  Endereços do Sepolia removidos/substituídos:")
    print(f"   Token:  {SEPOLIA_ADDRESSES['token']} → {POLYGON_ADDRESSES['token']}")
    print(f"   Vault: {SEPOLIA_ADDRESSES['vault']} → {POLYGON_ADDRESSES['vault']}")
    print(f"   Claim: {SEPOLIA_ADDRESSES['claim']} → {POLYGON_ADDRESSES['claim']}")
    print()
    print("💡 Próximos passos:")
    print("   1. Verificar se todos os arquivos foram atualizados corretamente")
    print("   2. Executar auditoria novamente para confirmar:")
    print("      ape run audit_contract_addresses")
    print("   3. Atualizar frontend/.env se necessário")
    print()

if __name__ == "__main__":
    main()

