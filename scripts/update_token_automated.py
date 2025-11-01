#!/usr/bin/env python3
"""
Script automatizado para atualizar informações do token no Etherscan
Usa automação de navegador para preencher o formulário automaticamente
"""
import os
import sys
import json
import time
from pathlib import Path
from dotenv import load_dotenv

# Carrega variáveis de ambiente
script_dir = Path(__file__).parent
project_root = script_dir.parent
env_path = project_root / ".env"
load_dotenv(dotenv_path=env_path)

# Tenta importar playwright, se não estiver instalado, usa método manual
try:
    from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    PLAYWRIGHT_AVAILABLE = False
    print("⚠️  Playwright não instalado. Instalando...")
    print("   Execute: pip install playwright && playwright install chromium")

def get_token_info():
    """Carrega informações do token do metadata.json e .env"""
    # Carrega metadados
    metadata_file = project_root / "metadata" / "token-metadata.json"
    if not metadata_file.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {metadata_file}")
    
    with open(metadata_file, 'r') as f:
        metadata = json.load(f)
    
    # Endereço do token
    token_address = os.getenv('TOKEN_ADDRESS') or "0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87"
    
    return {
        'address': token_address,
        'name': metadata.get('name', 'NeoFlowOFF'),
        'symbol': metadata.get('symbol', 'NEOFLW'),
        'decimals': metadata.get('decimals', 18),
        'logo_url': metadata.get('image') or metadata.get('logo') or os.getenv('AVATAR_IPFS_URL'),
        'website': metadata.get('website') or metadata.get('external_url', 'neoflowoff.eth'),
        'description': metadata.get('description', 'Token oficial do protocolo NEOFLW')
    }

def update_token_via_browser(token_info):
    """
    Atualiza informações do token no Etherscan usando automação de navegador
    """
    if not PLAYWRIGHT_AVAILABLE:
        print("❌ Playwright não está disponível")
        print("   Instale com: pip install playwright && playwright install chromium")
        return False
    
    network = os.getenv('APE_NETWORK', 'ethereum:sepolia')
    is_sepolia = 'sepolia' in network.lower()
    
    token_url = f"https://{'sepolia.' if is_sepolia else ''}etherscan.io/token/{token_info['address']}"
    
    print(f"\n🌐 Abrindo navegador para atualizar token...")
    print(f"   URL: {token_url}")
    print(f"\n⚠️  ATENÇÃO: Você precisará:")
    print(f"   1. Fazer login no Etherscan (conectar wallet)")
    print(f"   2. Confirmar a transação quando solicitado")
    print(f"   3. O script preencherá os campos automaticamente")
    
    input("\n👉 Pressione ENTER para continuar...")
    
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)  # Mostra o navegador
            page = browser.new_page()
            
            print(f"\n📱 Navegando para: {token_url}")
            page.goto(token_url)
            
            # Aguarda a página carregar
            print("⏳ Aguardando página carregar...")
            time.sleep(3)
            
            # Tenta encontrar o botão de atualização
            print("\n🔍 Procurando botão 'Update Token Info'...")
            
            # Múltiplas tentativas de seletores
            selectors = [
                'text="Update Token Info"',
                'text="Edit Token Info"',
                'text="Update"',
                '[href*="update"]',
                'button:has-text("Update")',
                'a:has-text("Update")',
            ]
            
            button_found = False
            for selector in selectors:
                try:
                    button = page.locator(selector).first
                    if button.is_visible(timeout=2000):
                        print(f"✅ Botão encontrado: {selector}")
                        button.click()
                        button_found = True
                        break
                except:
                    continue
            
            if not button_found:
                print("\n⚠️  Botão não encontrado automaticamente")
                print("   Possíveis motivos:")
                print("   - Você precisa fazer login primeiro")
                print("   - O botão pode estar em outro lugar")
                print("   - A interface pode ter mudado")
                print("\n💡 Instruções manuais:")
                print(f"   1. Procure por 'Update Token Info' ou 'Edit Token' na página")
                print(f"   2. Clique manualmente")
                print(f"   3. Preencha os campos com estas informações:")
                print(f"\n   Token Logo: {token_info['logo_url']}")
                print(f"   Token Name: {token_info['name']}")
                print(f"   Token Symbol: {token_info['symbol']}")
                print(f"   Decimals: {token_info['decimals']}")
                print(f"   Website: {token_info['website']}")
                print(f"   Description: {token_info['description']}")
                
                input("\n👉 Pressione ENTER depois de encontrar o botão...")
            
            # Aguarda o formulário aparecer
            print("\n⏳ Aguardando formulário aparecer...")
            time.sleep(3)
            
            # Preenche os campos do formulário
            print("\n📝 Preenchendo formulário...")
            
            fields_mapping = {
                'logo_url': ['tokenLogo', 'logo', 'image', 'token-logo'],
                'name': ['tokenName', 'name', 'token-name'],
                'symbol': ['tokenSymbol', 'symbol', 'token-symbol'],
                'decimals': ['decimals', 'tokenDecimals'],
                'website': ['website', 'tokenWebsite', 'external-url'],
                'description': ['description', 'tokenDescription']
            }
            
            filled_fields = []
            
            for field_name, possible_ids in fields_mapping.items():
                value = token_info.get(field_name)
                if not value:
                    continue
                
                for field_id in possible_ids:
                    try:
                        # Tenta por id
                        field = page.locator(f'#{field_id}')
                        if field.is_visible(timeout=1000):
                            field.fill(str(value))
                            filled_fields.append(field_name)
                            print(f"   ✅ {field_name}: {value}")
                            break
                    except:
                        try:
                            # Tenta por name
                            field = page.locator(f'[name="{field_id}"]')
                            if field.is_visible(timeout=1000):
                                field.fill(str(value))
                                filled_fields.append(field_name)
                                print(f"   ✅ {field_name}: {value}")
                                break
                        except:
                            continue
            
            if filled_fields:
                print(f"\n✅ {len(filled_fields)} campos preenchidos automaticamente")
            else:
                print("\n⚠️  Campos não encontrados automaticamente")
                print("   Preencha manualmente com estas informações:")
                print(f"\n   Token Logo: {token_info['logo_url']}")
                print(f"   Token Name: {token_info['name']}")
                print(f"   Token Symbol: {token_info['symbol']}")
                print(f"   Decimals: {token_info['decimals']}")
                print(f"   Website: {token_info['website']}")
                print(f"   Description: {token_info['description']}")
            
            print("\n💡 Próximos passos:")
            print("   1. Verifique se todos os campos estão preenchidos")
            print("   2. Clique em 'Submit' ou 'Enviar'")
            print("   3. Confirme a transação na sua wallet")
            print("   4. Aguarde alguns minutos para a atualização aparecer")
            
            input("\n👉 Pressione ENTER para fechar o navegador após concluir...")
            
            browser.close()
            
            return True
            
    except Exception as e:
        print(f"\n❌ Erro durante automação: {e}")
        print("\n💡 Use o método manual:")
        print(f"   1. Acesse: {token_url}")
        print(f"   2. Faça login")
        print(f"   3. Clique em 'Update Token Info'")
        print(f"   4. Preencha os campos manualmente")
        return False

def print_manual_instructions(token_info):
    """Imprime instruções para atualização manual"""
    network = os.getenv('APE_NETWORK', 'ethereum:sepolia')
    is_sepolia = 'sepolia' in network.lower()
    token_url = f"https://{'sepolia.' if is_sepolia else ''}etherscan.io/token/{token_info['address']}"
    
    print("\n" + "="*70)
    print("📋 INSTRUÇÕES PARA ATUALIZAÇÃO MANUAL")
    print("="*70)
    print(f"\n1️⃣  Acesse a página do token:")
    print(f"   {token_url}")
    print(f"\n2️⃣  Faça login no Etherscan:")
    print(f"   - Clique em 'Connect to Web3' ou 'Login'")
    print(f"   - Conecte sua wallet (mesma que fez o deploy)")
    print(f"\n3️⃣  Procure o botão 'Update Token Info' ou 'Edit Token'")
    print(f"\n4️⃣  Preencha os campos:")
    print(f"\n   📎 Token Logo (URL):")
    print(f"   {token_info['logo_url']}")
    print(f"\n   📝 Token Name:")
    print(f"   {token_info['name']}")
    print(f"\n   🏷️  Token Symbol:")
    print(f"   {token_info['symbol']}")
    print(f"\n   🔢 Decimals:")
    print(f"   {token_info['decimals']}")
    print(f"\n   🌐 Website (opcional):")
    print(f"   {token_info['website']}")
    print(f"\n   📄 Description (opcional):")
    print(f"   {token_info['description']}")
    print(f"\n5️⃣  Clique em 'Submit' ou 'Enviar'")
    print(f"\n6️⃣  Confirme a transação na sua wallet")
    print(f"\n7️⃣  Aguarde alguns minutos para aparecer")
    print("\n" + "="*70)

def main():
    """Função principal"""
    print("🚀 Script de Atualização Automatizada de Token no Etherscan\n")
    
    try:
        token_info = get_token_info()
        
        print("✅ Informações do token carregadas:")
        print(f"   Endereço: {token_info['address']}")
        print(f"   Nome: {token_info['name']}")
        print(f"   Símbolo: {token_info['symbol']}")
        print(f"   Logo: {token_info['logo_url']}")
        
        print("\n" + "="*70)
        print("Escolha o método de atualização:")
        print("="*70)
        print("1️⃣  Automatizado (usa navegador)")
        print("2️⃣  Manual (mostra instruções)")
        print("3️⃣  Abrir página do token (copiar informações)")
        
        choice = input("\n👉 Escolha (1/2/3): ").strip()
        
        if choice == "1":
            if update_token_via_browser(token_info):
                print("\n✅ Processo automatizado concluído!")
            else:
                print_manual_instructions(token_info)
        elif choice == "2":
            print_manual_instructions(token_info)
        elif choice == "3":
            network = os.getenv('APE_NETWORK', 'ethereum:sepolia')
            is_sepolia = 'sepolia' in network.lower()
            token_url = f"https://{'sepolia.' if is_sepolia else ''}etherscan.io/token/{token_info['address']}"
            print(f"\n🔗 Abra esta URL no navegador:")
            print(f"   {token_url}")
            print_manual_instructions(token_info)
        else:
            print("❌ Opção inválida")
            sys.exit(1)
            
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

