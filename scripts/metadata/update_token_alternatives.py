#!/usr/bin/env python3
"""
Script para atualizar informações do token em plataformas alternativas
quando o login do Etherscan está indisponível
"""
import os
import sys
import json
import webbrowser
from pathlib import Path
from dotenv import load_dotenv

# Carrega variáveis de ambiente
script_dir = Path(__file__).parent
project_root = script_dir.parent
env_path = project_root / ".env"
load_dotenv(dotenv_path=env_path)

def get_token_info():
    """Carrega informações do token do metadata.json e .env"""
    metadata_file = project_root / "metadata" / "token-metadata.json"
    if not metadata_file.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {metadata_file}")
    
    with open(metadata_file, 'r') as f:
        metadata = json.load(f)
    
    token_address = os.getenv('TOKEN_ADDRESS') or "0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87"
    
    return {
        'address': token_address,
        'name': metadata.get('name', 'NeoFlowOFF'),
        'symbol': metadata.get('symbol', 'NEOFLW'),
        'decimals': metadata.get('decimals', 18),
        'logo_url': metadata.get('image') or metadata.get('logo') or os.getenv('AVATAR_IPFS_URL'),
        'website': metadata.get('website') or metadata.get('external_url', 'neoflowoff.eth'),
        'description': metadata.get('description', 'Token oficial do protocolo NEOFLW'),
        'sourcify_link': 'https://repo.sourcify.dev/11155111/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87'
    }

def print_token_info(token_info):
    """Imprime informações formatadas do token"""
    print("\n" + "="*70)
    print("📋 INFORMAÇÕES DO TOKEN")
    print("="*70)
    print(f"\n📍 Endereço: {token_info['address']}")
    print(f"📝 Nome: {token_info['name']}")
    print(f"🏷️  Símbolo: {token_info['symbol']}")
    print(f"🔢 Decimals: {token_info['decimals']}")
    print(f"🖼️  Logo: {token_info['logo_url']}")
    print(f"🌐 Website: {token_info['website']}")
    print(f"📄 Descrição: {token_info['description']}")
    print(f"✅ Contrato Verificado: {token_info['sourcify_link']}")
    print("\n" + "="*70)

def open_geckoterminal(token_info):
    """Abre GeckoTerminal e mostra informações"""
    print("\n🚀 Abrindo GeckoTerminal...")
    print("   URL: https://www.geckoterminal.com/pt/update-token-info")
    
    webbrowser.open('https://www.geckoterminal.com/pt/update-token-info')
    
    print("\n📋 Informações para copiar e colar no formulário:")
    print_token_info(token_info)
    print("\n💡 Dica: Preencha o formulário com as informações acima")
    print("   Aguarde até 24 horas para revisão")

def open_coingecko(token_info):
    """Abre CoinGecko e mostra informações"""
    print("\n🚀 Abrindo CoinGecko...")
    print("   URL: https://www.coingecko.com/en/contact")
    
    webbrowser.open('https://www.coingecko.com/en/contact')
    
    print("\n📋 Informações para incluir na mensagem:")
    print_token_info(token_info)
    print("\n💡 Dica: Use o template de mensagem do guia ALTERNATIVAS_SEM_LOGIN_ETHERSCAN.md")

def open_debank(token_info):
    """Abre DeBank e mostra informações"""
    print("\n🚀 Abrindo DeBank...")
    print("   URL: https://debank.com/")
    
    webbrowser.open('https://debank.com/')
    
    print("\n📋 Informações para usar:")
    print_token_info(token_info)
    print("\n💡 Dica: Procure pelo token ou entre em contato via formulário")

def open_coinmarketcap(token_info):
    """Abre CoinMarketCap e mostra informações"""
    print("\n🚀 Abrindo CoinMarketCap...")
    print("   URL: https://coinmarketcap.com/")
    
    webbrowser.open('https://coinmarketcap.com/')
    
    print("\n📋 Informações para usar:")
    print_token_info(token_info)
    print("\n💡 Dica: Procure pelo token ou use o formulário de contato")

def show_email_template(token_info):
    """Mostra template de email para Etherscan"""
    print("\n" + "="*70)
    print("📧 TEMPLATE DE EMAIL PARA ETHERSCAN")
    print("="*70)
    print("\nPara: support@etherscan.io")
    print("Assunto: Atualização de Informações de Token - Login Indisponível")
    print("\n---")
    print(f"""
Olá,

Preciso atualizar as informações do meu token ERC-20 no Etherscan, mas o serviço de login está temporariamente indisponível.

Informações do Token:
- Endereço: {token_info['address']}
- Rede: Sepolia Testnet
- Nome: {token_info['name']}
- Símbolo: {token_info['symbol']}
- Logo: {token_info['logo_url']}
- Website: {token_info['website']}
- Descrição: {token_info['description']}

Contrato verificado em: {token_info['sourcify_link']}

Posso fornecer prova de propriedade se necessário.

Obrigado!
""")
    print("---")
    print("\n💡 Copie e cole este email para enviar ao suporte do Etherscan")

def main():
    """Função principal"""
    print("🚀 Script de Atualização de Token em Plataformas Alternativas")
    print("   (Quando login do Etherscan está indisponível)\n")
    
    try:
        token_info = get_token_info()
        
        print("✅ Informações do token carregadas!")
        print_token_info(token_info)
        
        print("\n" + "="*70)
        print("Escolha uma plataforma para atualizar:")
        print("="*70)
        print("1️⃣  GeckoTerminal (Recomendado - Mais rápido)")
        print("2️⃣  CoinGecko (Maior visibilidade)")
        print("3️⃣  DeBank (Bom para wallets)")
        print("4️⃣  CoinMarketCap (Grande visibilidade)")
        print("5️⃣  Mostrar template de email para Etherscan")
        print("6️⃣  Abrir todas as opções")
        print("0️⃣  Sair")
        
        choice = input("\n👉 Escolha (1/2/3/4/5/6/0): ").strip()
        
        if choice == "1":
            open_geckoterminal(token_info)
        elif choice == "2":
            open_coingecko(token_info)
        elif choice == "3":
            open_debank(token_info)
        elif choice == "4":
            open_coinmarketcap(token_info)
        elif choice == "5":
            show_email_template(token_info)
        elif choice == "6":
            print("\n🚀 Abrindo todas as plataformas...")
            open_geckoterminal(token_info)
            import time
            time.sleep(2)
            open_coingecko(token_info)
            time.sleep(2)
            open_debank(token_info)
            time.sleep(2)
            open_coinmarketcap(token_info)
            print("\n✅ Todas as plataformas abertas!")
        elif choice == "0":
            print("\n👋 Até logo!")
            sys.exit(0)
        else:
            print("❌ Opção inválida")
            sys.exit(1)
        
        print("\n" + "="*70)
        print("✅ PROCESSO CONCLUÍDO")
        print("="*70)
        print("\n💡 Próximos passos:")
        print("   1. Preencha os formulários das plataformas")
        print("   2. Aguarde revisão (24-48 horas)")
        print("   3. Quando Etherscan voltar, atualize lá também")
        print("\n📖 Veja o guia completo: ALTERNATIVAS_SEM_LOGIN_ETHERSCAN.md")
        
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

