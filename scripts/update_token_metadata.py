#!/usr/bin/env python3
"""
Script para atualizar metadados do token no Etherscan
Atualiza logo e informações do token seguindo padrões ERC-20
"""
import os
import sys
import json
import requests
from pathlib import Path
from dotenv import load_dotenv

# Carrega variáveis de ambiente
script_dir = Path(__file__).parent
project_root = script_dir.parent
env_path = project_root / ".env"
load_dotenv(dotenv_path=env_path)

def get_token_address():
    """Obtém o endereço do token do .env ou arquivo de status"""
    # Tenta ler do .env primeiro
    token_address = os.getenv('TOKEN_ADDRESS')
    
    if not token_address:
        # Tenta ler do arquivo STATUS_FINAL.md
        status_file = project_root / "STATUS_FINAL.md"
        if status_file.exists():
            with open(status_file, 'r') as f:
                content = f.read()
                # Procura pelo padrão de endereço do token
                import re
                match = re.search(r'NeoFlowToken.*?`([0-9a-fA-Fx]{42})`', content)
                if match:
                    token_address = match.group(1)
    
    return token_address

def upload_metadata_to_ipfs(metadata_file: str) -> str:
    """
    Faz upload do JSON de metadados para IPFS via Lighthouse
    
    Args:
        metadata_file: Caminho para o arquivo JSON de metadados
        
    Returns:
        str: CID do arquivo no IPFS
    """
    print(f"📤 Fazendo upload de metadados para IPFS...")
    
    # Lê o arquivo JSON
    with open(metadata_file, 'r') as f:
        metadata_content = f.read()
    
    # Para usar Lighthouse, você precisaria de uma API key
    # Por enquanto, vamos retornar instruções manuais
    print("⚠️  Upload manual necessário:")
    print(f"   1. Acesse: https://lighthouse.storage/")
    print(f"   2. Faça upload do arquivo: {metadata_file}")
    print(f"   3. Copie o CID retornado")
    
    return None

def update_etherscan_token_info(token_address: str, logo_url: str, website: str = None):
    """
    Atualiza informações do token no Etherscan via API
    
    Args:
        token_address: Endereço do contrato do token
        logo_url: URL do logo do token
        website: URL do website (opcional)
    """
    etherscan_api_key = os.getenv('ETHERSCAN_API_KEY')
    network = os.getenv('APE_NETWORK', 'ethereum:sepolia')
    
    if not etherscan_api_key:
        print("❌ ETHERSCAN_API_KEY não encontrada no .env")
        return False
    
    # Determina a URL base do Etherscan baseado na rede
    if 'sepolia' in network.lower():
        api_url = "https://api-sepolia.etherscan.io/api"
        explorer_url = "https://sepolia.etherscan.io"
    else:
        api_url = "https://api.etherscan.io/api"
        explorer_url = "https://etherscan.io"
    
    print(f"\n📋 Atualizando informações do token no Etherscan...")
    print(f"   Token: {token_address}")
    print(f"   Logo: {logo_url}")
    print(f"   Network: {network}")
    
    # Nota: A API do Etherscan não tem endpoint direto para atualizar logo
    # O logo precisa ser atualizado manualmente na interface web
    print("\n⚠️  ATENÇÃO: Etherscan não possui API pública para atualizar logo do token.")
    print("   Você precisa atualizar manualmente:")
    print(f"\n   1. Acesse: {explorer_url}/token/{token_address}")
    print(f"   2. Faça login no Etherscan")
    print(f"   3. Clique em 'Update Token Info' ou 'Edit Token'")
    print(f"   4. Adicione a URL do logo: {logo_url}")
    print(f"   5. Preencha outras informações se necessário")
    
    return True

def main():
    """Função principal"""
    print("🚀 Atualização de Metadados do Token NEOFLW\n")
    
    # Carrega configurações
    avatar_url = os.getenv('AVATAR_IPFS_URL')
    avatar_cid = os.getenv('AVATAR_IPFS_CID')
    
    if not avatar_url:
        print("❌ AVATAR_IPFS_URL não encontrada no .env")
        sys.exit(1)
    
    # Caminho do arquivo de metadados
    metadata_file = project_root / "metadata" / "token-metadata.json"
    
    if not metadata_file.exists():
        print(f"❌ Arquivo de metadados não encontrado: {metadata_file}")
        sys.exit(1)
    
    # Lê e valida o JSON de metadados
    try:
        with open(metadata_file, 'r') as f:
            metadata = json.load(f)
        print("✅ Metadados JSON válido")
        print(f"   Nome: {metadata.get('name')}")
        print(f"   Símbolo: {metadata.get('symbol')}")
        print(f"   Logo: {metadata.get('image')}")
    except json.JSONDecodeError as e:
        print(f"❌ Erro ao ler JSON de metadados: {e}")
        sys.exit(1)
    
    # Obtém endereço do token
    token_address = get_token_address()
    if not token_address:
        # Endereço padrão do token em Sepolia (do STATUS_FINAL.md)
        token_address = "0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87"
        print(f"⚠️  Usando endereço padrão do token (Sepolia): {token_address}")
        print("   Para usar outro endereço, adicione TOKEN_ADDRESS=0x... no .env")
    
    print(f"\n📍 Endereço do Token: {token_address}")
    
    # Mostra informações e instruções
    print("\n" + "="*60)
    print("📋 INFORMAÇÕES PARA ATUALIZAÇÃO")
    print("="*60)
    print(f"\n✅ Metadados JSON prontos: {metadata_file}")
    print(f"✅ Logo IPFS disponível: {avatar_url}")
    print(f"✅ Endereço do Token: {token_address}")
    
    # Instruções para Etherscan
    print("\n" + "="*60)
    print("🚀 PRÓXIMOS PASSOS")
    print("="*60)
    update_etherscan_token_info(token_address, avatar_url)
    
    # Resumo final
    print("\n" + "="*60)
    print("✅ PROCESSO CONCLUÍDO")
    print("="*60)
    print(f"\n📋 Informações do Token:")
    print(f"   Nome: {metadata.get('name')}")
    print(f"   Símbolo: {metadata.get('symbol')}")
    print(f"   Logo IPFS: {avatar_url}")
    print(f"   CID: {avatar_cid}")
    print(f"\n🔗 Links Úteis:")
    network = os.getenv('APE_NETWORK', 'ethereum:sepolia')
    if 'sepolia' in network.lower():
        explorer_base = "https://sepolia.etherscan.io"
    else:
        explorer_base = "https://etherscan.io"
    print(f"   Etherscan: {explorer_base}/token/{token_address}")
    print(f"   Metadados: {metadata_file}")
    
    print(f"\n💡 Próximos Passos:")
    print(f"   1. Faça upload dos metadados JSON para IPFS (se ainda não fez)")
    print(f"   2. Atualize o logo no Etherscan manualmente")
    print(f"   3. Configure o logo em wallets (Trust Wallet Assets, etc)")

if __name__ == "__main__":
    main()

