#!/usr/bin/env python3
"""
Script para calcular Constructor Arguments do contrato InterboxCoin
Especifico para BOX Token - NÃO mexe em arquivos do NEOFLW
"""
import sys
from web3 import Web3

def calculate_constructor_args(signer_address: str):
    """
    Calcula o ABI-encoded constructor argument para o contrato InterboxCoin
    
    Args:
        signer_address: Endereço do signer (ex: "0x1234...5678")
        
    Returns:
        str: Hexadecimal ABI-encoded sem 0x
    """
    try:
        # Valida o endereço
        if not signer_address.startswith('0x'):
            signer_address = '0x' + signer_address
        
        # Valida se é um endereço válido
        if not Web3.is_address(signer_address):
            print(f"❌ Endereço inválido: {signer_address}")
            return None
        
        # Normaliza o endereço (checksum)
        signer_address = Web3.to_checksum_address(signer_address)
        
        # Codifica o endereço como ABI usando eth_abi
        try:
            from eth_abi import encode as abi_encode
            encoded = abi_encode(['address'], [signer_address])
        except ImportError:
            # Fallback: manual encoding para address
            # Address tem 20 bytes, ABI-encoded tem 32 bytes com padding
            address_bytes = bytes.fromhex(signer_address[2:])
            # Padding à esquerda até 32 bytes
            encoded = b'\x00' * 12 + address_bytes
        
        # Converte para hex e remove 0x
        hex_encoded = Web3.to_hex(encoded)[2:]
        
        return hex_encoded
        
    except Exception as e:
        print(f"❌ Erro ao calcular: {e}")
        return None

def main():
    """Função principal"""
    print("🔧 Calcular Constructor Arguments - InterboxCoin (BOX Token)\n")
    print("⚠️  Este script é APENAS para o token BOX\n")
    
    if len(sys.argv) < 2:
        print("Uso: python calculate_constructor_args_box.py <endereco_signer>")
        print("\nExemplo:")
        print("  python calculate_constructor_args_box.py 0x1234567890123456789012345678901234567890")
        print("\nOu digite o endereço agora:")
        signer = input("Digite o endereço do signer (0x...): ").strip()
    else:
        signer = sys.argv[1]
    
    if not signer:
        print("❌ Endereço do signer não fornecido")
        sys.exit(1)
    
    print(f"\n📍 Endereço do Signer: {signer}")
    print("📋 Calculando constructor argument...")
    
    encoded = calculate_constructor_args(signer)
    
    if encoded:
        print("\n" + "="*60)
        print("✅ CONSTRUCTOR ARGUMENT CALCULADO")
        print("="*60)
        print(f"\nCopie este valor e cole no campo 'Constructor Arguments' do BSCScan:")
        print(f"\n{encoded}")
        print("\n" + "="*60)
        print("\n📋 Informações:")
        print(f"   Endereço original: {signer}")
        print(f"   ABI-encoded (64 chars): {encoded}")
        print(f"   Tamanho: {len(encoded)} caracteres")
        print("\n💡 Dica: Cole este valor no BSCScan SEM o '0x' no início")
        print("   O valor já está no formato correto!")
    else:
        print("\n❌ Falha ao calcular constructor argument")
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

