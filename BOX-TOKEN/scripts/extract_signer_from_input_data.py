#!/usr/bin/env python3
"""
Script para extrair o signer do Input Data da transação de criação
Específico para BOX Token - NÃO mexe em arquivos do NEOFLW
"""
import sys
import re

def extract_signer_from_input_data(input_data: str):
    """
    Extrai o endereço do signer do Input Data da transação
    
    Args:
        input_data: Input Data completo da transação (hexadecimal)
        
    Returns:
        str: Endereço do signer ou None
    """
    # Remove 0x se tiver
    if input_data.startswith('0x'):
        input_data = input_data[2:]
    
    # O contrato InterboxCoin tem constructor(address _signer)
    # Um endereço tem 20 bytes = 40 caracteres hex
    # O signer está nos últimos bytes do Input Data
    
    # Um endereço ABI-encoded tem padding de zeros à esquerda até 64 chars
    # Então procuramos pelos últimos 64 caracteres
    
    if len(input_data) < 64:
        print("❌ Input Data muito curto")
        return None
    
    # Pega os últimos 64 caracteres (32 bytes = tamanho de um address ABI-encoded)
    last_64_chars = input_data[-64:]
    
    # Verifica se parece um endereço (padding de zeros + endereço)
    # Formato: 000000000000000000000000 + [40 chars do endereço]
    # Total: 24 zeros + 40 chars = 64 chars
    
    # Extrai os últimos 40 caracteres (o endereço em si)
    address_hex = last_64_chars[24:]  # Pula os 24 primeiros chars (zeros)
    
    if len(address_hex) != 40:
        print("❌ Não conseguiu extrair endereço (não tem 40 chars)")
        return None
    
    # Forma o endereço completo
    signer_address = '0x' + address_hex
    
    # Valida se parece um endereço válido (hex apenas)
    if not re.match(r'^0x[0-9a-fA-F]{40}$', signer_address):
        print("❌ Endereço extraído não parece válido")
        return None
    
    return signer_address

def main():
    """Função principal"""
    print("🔍 Extrair Signer do Input Data - InterboxCoin (BOX Token)\n")
    print("⚠️  Este script é APENAS para o token BOX\n")
    
    if len(sys.argv) < 2:
        print("Uso: python extract_signer_from_input_data.py <input_data_hex>")
        print("\nExemplo:")
        print("  python extract_signer_from_input_data.py 0x60806040523480...ABC123DEF456")
        print("\nOu cole o Input Data agora:")
        print("(Cole o Input Data completo e pressione Enter)")
        input_data = input().strip()
    else:
        input_data = sys.argv[1]
    
    if not input_data:
        print("❌ Input Data não fornecido")
        sys.exit(1)
    
    print(f"\n📋 Analisando Input Data...")
    print(f"   Tamanho: {len(input_data)} caracteres")
    
    # Verifica se parece ser apenas o hash da transação (muito curto)
    if len(input_data) < 200:
        print("\n⚠️  ATENÇÃO: Input Data muito curto!")
        print("   Parece que você passou o HASH da transação ao invés do INPUT DATA completo.")
        print("   O Input Data deve ter MILHARES de caracteres, não apenas 66!")
        print("\n   Para copiar o Input Data completo:")
        print("   1. Acesse a transação no BSCScan")
        print("   2. Procure pela seção 'Input Data'")
        print("   3. Copie TODO o código hexadecimal (é muito longo!)")
        print("   Veja o guia: COMO_COPIAR_INPUT_DATA.md")
    
    signer = extract_signer_from_input_data(input_data)
    
    if signer:
        print("\n" + "="*60)
        print("✅ SIGNER ENCONTRADO!")
        print("="*60)
        print(f"\n📍 Endereço do Signer: {signer}")
        
        # Calcula o constructor argument
        try:
            from web3 import Web3
            from eth_abi import encode as abi_encode
            
            # Valida e normaliza o endereço
            signer_checksum = Web3.to_checksum_address(signer)
            
            # Codifica o endereço como ABI
            encoded = abi_encode(['address'], [signer_checksum])
            hex_encoded = Web3.to_hex(encoded)[2:]
            
            print("\n" + "="*60)
            print("✅ CONSTRUCTOR ARGUMENT CALCULADO")
            print("="*60)
            print(f"\nCole este valor no BSCScan (campo 'Constructor Arguments'):")
            print(f"\n{hex_encoded}")
            print("\n" + "="*60)
            print("\n💡 Use este valor no BSCScan para verificar o contrato!")
            
        except ImportError:
            print("\n⚠️  web3 não instalado. Use o script calculate_constructor_args_box.py:")
            print(f"   python scripts/calculate_constructor_args_box.py {signer}")
        except Exception as e:
            print(f"\n⚠️  Erro ao calcular constructor argument: {e}")
            print(f"   Use: python scripts/calculate_constructor_args_box.py {signer}")
        
    else:
        print("\n❌ Não conseguiu extrair o signer do Input Data")
        print("\n💡 Verificações:")
        print("   1. O Input Data está completo?")
        print("   2. É a transação de criação do contrato?")
        print("   3. O contrato tem constructor(address _signer)?")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Operação cancelada pelo usuário")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        sys.exit(1)

