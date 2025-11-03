#!/usr/bin/env python3
"""
Script para atualizar metadados do token BOX no BSCScan
Atualiza logo e informações do token seguindo padrões BEP-20
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
env_path = project_root.parent / ".env"  # .env na raiz do projeto principal
load_dotenv(dotenv_path=env_path)

# Se não encontrar, tenta na pasta BOX-TOKEN
if not env_path.exists():
    env_path = project_root / ".env"
    load_dotenv(dotenv_path=env_path)

def get_token_address():
    """Obtém o endereço do token do .env ou usa o padrão"""
    token_address = os.getenv('BOX_TOKEN_ADDRESS')
    
    if not token_address:
        # Endereço padrão do token BOX
        token_address = "0xBc972E10Df612C7d65054BC67aBCA96B3C22a017"
        print(f"⚠️  Usando endereço padrão do token BOX: {token_address}")
        print("   Para usar outro endereço, adicione BOX_TOKEN_ADDRESS=0x... no .env")
    
    return token_address

def upload_metadata_to_ipfs(metadata_file: str) -> str:
    """
    Faz upload do JSON de metadados para IPFS via Lighthouse ou Pinata
    
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
    print(f"   1. Acesse: https://pinata.cloud/ ou https://lighthouse.storage/")
    print(f"   2. Faça upload do arquivo: {metadata_file}")
    print(f"   3. Copie o CID retornado")
    
    return None

def update_bscscan_token_info(token_address: str, logo_url: str, website: str = None):
    """
    Mostra instruções para atualizar informações do token no BSCScan via interface web
    
    Args:
        token_address: Endereço do contrato do token
        logo_url: URL do logo do token
        website: URL do website (opcional)
    """
    bscscan_api_key = os.getenv('BSCSCAN_API_KEY')
    
    print(f"\n📋 Instruções para atualizar informações do token no BSCScan...")
    print(f"   Token: {token_address}")
    print(f"   Logo: {logo_url}")
    
    # Nota: O BSCScan não tem API pública para atualizar logo
    # O logo precisa ser atualizado manualmente na interface web
    print("\n⚠️  ATENÇÃO: BSCScan não possui API pública para atualizar logo do token.")
    print("   Você precisa atualizar manualmente:")
    print(f"\n   1. Acesse: https://bscscan.com/token/{token_address}")
    print(f"   2. Faça login no BSCScan (conecte sua wallet)")
    print(f"   3. Clique em 'Update Token Info' ou 'Edit Token'")
    print(f"   4. Adicione a URL do logo: {logo_url}")
    print(f"   5. Preencha outras informações se necessário")
    print(f"\n   📖 Guia completo: docs/token-info/ATUALIZAR_LOGO_BSCSCAN.md")
    
    return True

def main():
    """Função principal"""
    print("🚀 Atualização de Metadados do Token BOX (BSC)\n")
    
    # Carrega configurações
    avatar_url = os.getenv('BOX_AVATAR_IPFS_URL')
    avatar_cid = os.getenv('BOX_AVATAR_IPFS_CID')
    
    if not avatar_url:
        print("⚠️  BOX_AVATAR_IPFS_URL não encontrada no .env")
        print("   Você pode continuar, mas precisará fornecer a URL do logo manualmente")
        avatar_url = input("\n   Digite a URL do logo IPFS (ou pressione Enter para pular): ").strip()
        
        if not avatar_url:
            print("   Continuando sem URL do logo...")
            avatar_url = "[URL_DO_LOGO_AQUI]"
    
    # Caminho do arquivo de metadados
    metadata_file = project_root / "metadata" / "token-metadata.json"
    
    if not metadata_file.exists():
        print(f"⚠️  Arquivo de metadados não encontrado: {metadata_file}")
        print(f"   Criando arquivo de exemplo...")
        
        # Cria arquivo de exemplo
        metadata_dir = metadata_file.parent
        metadata_dir.mkdir(parents=True, exist_ok=True)
        
        example_metadata = {
            "name": "BOX Token",
            "symbol": "BOX",
            "image": avatar_url if avatar_url != "[URL_DO_LOGO_AQUI]" else "[URL_DO_LOGO_AQUI]",
            "logo": avatar_url if avatar_url != "[URL_DO_LOGO_AQUI]" else "[URL_DO_LOGO_AQUI]",
            "description": "BOX Token on Binance Smart Chain",
            "website": "[WEBSITE_AQUI]"
        }
        
        with open(metadata_file, 'w') as f:
            json.dump(example_metadata, f, indent=2)
        
        print(f"   ✅ Arquivo de exemplo criado: {metadata_file}")
        print(f"   ⚠️  Edite o arquivo e adicione as informações corretas do token")
    
    # Lê e valida o JSON de metadados
    try:
        with open(metadata_file, 'r') as f:
            metadata = json.load(f)
        print("✅ Metadados JSON válido")
        print(f"   Nome: {metadata.get('name', 'N/A')}")
        print(f"   Símbolo: {metadata.get('symbol', 'N/A')}")
        print(f"   Logo: {metadata.get('image', 'N/A')}")
    except json.JSONDecodeError as e:
        print(f"❌ Erro ao ler JSON de metadados: {e}")
        sys.exit(1)
    
    # Obtém endereço do token
    token_address = get_token_address()
    
    print(f"\n📍 Endereço do Token: {token_address}")
    
    # Mostra informações e instruções
    print("\n" + "="*60)
    print("📋 INFORMAÇÕES PARA ATUALIZAÇÃO")
    print("="*60)
    print(f"\n✅ Metadados JSON prontos: {metadata_file}")
    
    logo_from_metadata = metadata.get('image') or metadata.get('logo')
    if logo_from_metadata and logo_from_metadata != "[URL_DO_LOGO_AQUI]":
        print(f"✅ Logo IPFS disponível: {logo_from_metadata}")
        logo_url = logo_from_metadata
    elif avatar_url and avatar_url != "[URL_DO_LOGO_AQUI]":
        print(f"✅ Logo IPFS disponível: {avatar_url}")
        logo_url = avatar_url
    else:
        print(f"⚠️  Logo IPFS não configurado")
        logo_url = "[URL_DO_LOGO_AQUI]"
    
    print(f"✅ Endereço do Token: {token_address}")
    
    # Instruções para BSCScan
    print("\n" + "="*60)
    print("🚀 PRÓXIMOS PASSOS")
    print("="*60)
    
    if logo_url != "[URL_DO_LOGO_AQUI]":
        update_bscscan_token_info(token_address, logo_url, metadata.get('website'))
    else:
        print("\n⚠️  URL do logo não configurada.")
        print("   Configure BOX_AVATAR_IPFS_URL no .env ou edite metadata/token-metadata.json")
        print(f"\n   Depois, acesse: https://bscscan.com/token/{token_address}")
    
    # Resumo final
    print("\n" + "="*60)
    print("✅ PROCESSO CONCLUÍDO")
    print("="*60)
    print(f"\n📋 Informações do Token:")
    print(f"   Nome: {metadata.get('name', 'N/A')}")
    print(f"   Símbolo: {metadata.get('symbol', 'N/A')}")
    if logo_url != "[URL_DO_LOGO_AQUI]":
        print(f"   Logo IPFS: {logo_url}")
        if avatar_cid:
            print(f"   CID: {avatar_cid}")
    
    print(f"\n🔗 Links Úteis:")
    print(f"   BSCScan: https://bscscan.com/token/{token_address}")
    print(f"   Metadados: {metadata_file}")
    
    print(f"\n💡 Próximos Passos:")
    print(f"   1. Faça upload dos metadados JSON para IPFS (se ainda não fez)")
    print(f"   2. Atualize o logo no BSCScan manualmente")
    print(f"   3. Configure o logo em wallets (Trust Wallet Assets, etc)")
    print(f"   4. Consulte a documentação em docs/token-info/ para mais detalhes")

if __name__ == "__main__":
    main()

