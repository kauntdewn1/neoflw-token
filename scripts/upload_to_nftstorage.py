#!/usr/bin/env python3
"""
Script para fazer upload de imagem para NFT.Storage
"""
import os
import sys
import requests
from pathlib import Path
from dotenv import load_dotenv

# Carrega variáveis de ambiente
script_dir = Path(__file__).parent
project_root = script_dir.parent
env_path = project_root / ".env"
load_dotenv(dotenv_path=env_path)

def upload_to_nftstorage(file_path: str, api_key: str) -> dict:
    """
    Faz upload de um arquivo para NFT.Storage usando a API HTTP
    
    Args:
        file_path: Caminho para o arquivo a ser enviado
        api_key: Chave de API do NFT.Storage
        
    Returns:
        dict: Resposta da API com CID e outras informações
    """
    url = "https://api.nft.storage/upload"
    
    # Verifica se o arquivo existe
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")
    
    # Lê o arquivo
    with open(file_path, 'rb') as f:
        file_data = f.read()
    
    print(f"📤 Fazendo upload de {file_path} para NFT.Storage...")
    print(f"   Tamanho do arquivo: {len(file_data)} bytes")
    
    # A API do NFT.Storage espera o arquivo como binary data no body
    # com Authorization Bearer token
    headers = {
        'Authorization': f'Bearer {api_key}'
    }
    
    # Faz o upload
    response = requests.post(url, headers=headers, data=file_data)
    
    # Verifica a resposta
    if response.status_code == 200:
        result = response.json()
        print("✅ Upload realizado com sucesso!")
        print(f"\n📋 Informações do upload:")
        
        # A resposta tem formato: {"ok": true, "value": {"cid": "...", "size": ...}}
        if result.get('ok') and result.get('value'):
            cid = result['value'].get('cid', 'N/A')
            ipfs_url = f"https://{cid}.ipfs.nftstorage.link"
            print(f"   CID: {cid}")
            print(f"   IPFS Gateway: {ipfs_url}")
            return {
                'value': {
                    'cid': cid
                },
                'ipfs_url': ipfs_url
            }
        else:
            print(f"   Resposta: {result}")
            return result
    else:
        error_msg = response.text
        print(f"❌ Erro no upload: {response.status_code}")
        print(f"   Resposta: {error_msg}")
        
        # Tenta mostrar mais detalhes do erro
        try:
            error_json = response.json()
            print(f"   Detalhes: {error_json}")
        except:
            pass
        
        response.raise_for_status()
        return {}

def main():
    """Função principal"""
    # Configurações - tenta carregar do .env
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    env_path = project_root / ".env"
    
    # Carrega novamente o .env explicitamente
    load_dotenv(dotenv_path=env_path, override=True)
    
    # Tenta ler diretamente do arquivo se dotenv não funcionar
    api_key = os.getenv('NFT_API_KEY')
    if not api_key:
        # Lê diretamente do arquivo
        try:
            with open(env_path, 'r') as f:
                for line in f:
                    if line.startswith('NFT_API_KEY='):
                        api_key = line.split('=', 1)[1].strip()
                        break
        except Exception as e:
            print(f"⚠️  Erro ao ler .env: {e}")
    
    if not api_key:
        print("❌ Erro: NFT_API_KEY não encontrada no arquivo .env")
        print("   Por favor, adicione NFT_API_KEY=sua_chave no arquivo .env")
        sys.exit(1)
    
    # Remove espaços e quebras de linha da API key
    api_key = api_key.strip()
    
    # Valida formato básico da API key (deve ter pelo menos 30 caracteres)
    if len(api_key) < 30:
        print("⚠️  Aviso: A API key parece muito curta. Verifique se está correta.")
        print(f"   Tamanho atual: {len(api_key)} caracteres")
    
    print(f"🔑 Usando API Key: {api_key[:10]}...{api_key[-5:]}")
    
    # Caminho da imagem
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    image_path = project_root / "public" / "images" / "avatar_neoflow.png"
    
    if not image_path.exists():
        print(f"❌ Erro: Imagem não encontrada em {image_path}")
        sys.exit(1)
    
    try:
        # Faz o upload
        result = upload_to_nftstorage(str(image_path), api_key)
        
        # Salva o CID em um arquivo para referência futura
        if result.get('value', {}).get('cid'):
            cid_file = project_root / "NFT_STORAGE_CID.txt"
            cid = result['value']['cid']
            ipfs_url = f"https://{cid}.ipfs.nftstorage.link"
            
            with open(cid_file, 'w') as f:
                f.write(f"CID: {cid}\n")
                f.write(f"IPFS URL: {ipfs_url}\n")
                f.write(f"Arquivo: avatar_neoflow.png\n")
            
            print(f"\n💾 CID salvo em: {cid_file}")
            print(f"\n🔗 URL IPFS da imagem:")
            print(f"   {ipfs_url}")
            
    except Exception as e:
        print(f"❌ Erro ao fazer upload: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

