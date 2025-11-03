#!/usr/bin/env python3
"""
Script para verificar contrato do token BOX no BSCScan
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

def check_contract_verification(token_address: str):
    """
    Verifica se o contrato já está verificado no BSCScan
    
    Args:
        token_address: Endereço do contrato
        
    Returns:
        bool: True se verificado, False caso contrário
    """
    bscscan_api_key = os.getenv('BSCSCAN_API_KEY')
    
    if not bscscan_api_key:
        print("⚠️  BSCSCAN_API_KEY não encontrada no .env")
        print("   Configure a API key seguindo: docs/setup/BSCSCAN_API_SETUP.md")
        return False
    
    url = "https://api.bscscan.com/api"
    params = {
        'module': 'contract',
        'action': 'getsourcecode',
        'address': token_address,
        'apikey': bscscan_api_key
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        if data['status'] == '1' and data['result']:
            source_code = data['result'][0].get('SourceCode', '')
            contract_name = data['result'][0].get('ContractName', '')
            
            if source_code and source_code != '':
                print(f"✅ Contrato já está verificado no BSCScan!")
                print(f"   Nome do contrato: {contract_name}")
                return True
            else:
                print(f"⚠️  Contrato ainda não está verificado no BSCScan")
                return False
        else:
            print(f"⚠️  Não foi possível verificar o status do contrato")
            return False
            
    except Exception as e:
        print(f"❌ Erro ao verificar contrato: {e}")
        return False

def main():
    """Função principal"""
    print("🔍 Verificação de Contrato do Token BOX (BSC)\n")
    
    # Obtém endereço do token
    token_address = get_token_address()
    print(f"📍 Endereço do Token: {token_address}")
    
    # Verifica se já está verificado
    print("\n" + "="*60)
    print("🔍 VERIFICANDO STATUS DO CONTRATO")
    print("="*60)
    
    is_verified = check_contract_verification(token_address)
    
    print("\n" + "="*60)
    print("📋 PRÓXIMOS PASSOS")
    print("="*60)
    
    if is_verified:
        print("\n✅ O contrato já está verificado!")
        print("   Você pode ver o código fonte em:")
        print(f"   https://bscscan.com/address/{token_address}#code")
    else:
        print("\n⚠️  O contrato ainda não está verificado.")
        print("\n   📋 Para verificar o contrato:")
        print("\n   Opção 1: BSCScan (Método Manual)")
        print(f"   1. Acesse: https://bscscan.com/address/{token_address}#code")
        print("   2. Clique em 'Verify and Publish'")
        print("   3. Se der erro 'language field', veja: SOLUCAO_RAPIDA_ERRO_LANGUAGE.md")
        print("   4. Guia completo: docs/verification/VERIFICAR_BSCSCAN.md")
        print("\n   Opção 2: Sourcify (Recomendado - Mais Fácil)")
        print("   1. Acesse: https://sourcify.dev/")
        print("   2. Selecione a rede: Binance Smart Chain (Chain ID: 56)")
        print(f"   3. Endereço: {token_address}")
        print("   4. Guia completo: docs/verification/SOURCIFY_PASSO_A_PASSO_BSC.md")
        print("\n   ⚡ NÃO TEM JSON? Use métodos que não precisam de JSON:")
        print("   - Guia rápido: VERIFICAR_SEM_JSON.md")
        print("   - Guia completo: docs/verification/SEM_JSON_VERIFICAR.md")
    
    print("\n🔗 Links Úteis:")
    print(f"   Contrato: https://bscscan.com/address/{token_address}")
    print(f"   Token: https://bscscan.com/token/{token_address}")
    print(f"   BSCScan API Docs: https://docs.bscscan.com/api-endpoints/contracts")

if __name__ == "__main__":
    main()

