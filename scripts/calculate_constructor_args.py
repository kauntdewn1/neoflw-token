#!/usr/bin/env python3
"""
Script para calcular os argumentos do construtor no formato ABI-encoded
"""
from web3 import Web3

def calculate_constructor_args():
    """
    Calcula os argumentos do construtor do NeoFlowToken em formato ABI-encoded
    """
    # Valor do initialSupply: 1 bilhão de tokens com 18 decimais
    # 1,000,000,000 * 10^18 = 1000000000000000000000000000 wei
    initial_supply = 1_000_000_000 * 10**18
    
    print("🔢 Calculando argumentos do construtor...")
    print(f"\nValor decimal: {initial_supply:,}")
    print(f"Valor em wei: {initial_supply}")
    
    # Usa Web3 para fazer ABI encoding
    w3 = Web3()
    
    # Abi do construtor: constructor(uint256 initialSupply)
    abi = [{"type": "uint256", "name": "initialSupply"}]
    
    # Encode os valores
    encoded = w3.codec.encode(abi, [initial_supply])
    
    # Remove o '0x' prefix se existir
    hex_encoded = encoded.hex() if isinstance(encoded, bytes) else encoded
    
    print(f"\n✅ Formato ABI-encoded (hexadecimal):")
    print(f"   {hex_encoded}")
    
    print(f"\n📋 Para usar no Etherscan:")
    print(f"   Cole este valor no campo 'Constructor Arguments':")
    print(f"   {hex_encoded}")
    
    # Também mostra o formato sem 0x
    if hex_encoded.startswith('0x'):
        hex_encoded_no_prefix = hex_encoded[2:]
    else:
        hex_encoded_no_prefix = hex_encoded
    
    print(f"\n   Ou sem o prefixo '0x':")
    print(f"   {hex_encoded_no_prefix}")
    
    # Verifica o tamanho (deve ser 64 caracteres para uint256)
    expected_length = 64
    actual_length = len(hex_encoded_no_prefix)
    
    if actual_length < expected_length:
        # Adiciona zeros à esquerda
        hex_encoded_padded = hex_encoded_no_prefix.zfill(expected_length)
        print(f"\n⚠️  Adicionando padding (zeros à esquerda):")
        print(f"   {hex_encoded_padded}")
        return hex_encoded_padded
    elif actual_length > expected_length:
        print(f"\n⚠️  Valor muito longo ({actual_length} chars), truncando para {expected_length}:")
        hex_encoded_truncated = hex_encoded_no_prefix[-expected_length:]
        print(f"   {hex_encoded_truncated}")
        return hex_encoded_truncated
    else:
        return hex_encoded_no_prefix

if __name__ == "__main__":
    try:
        result = calculate_constructor_args()
        print(f"\n✅ Valor final para usar: {result}")
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        print("\nTentando método alternativo...")
        
        # Método alternativo: conversão manual
        initial_supply = 1_000_000_000 * 10**18
        hex_value = hex(initial_supply)[2:]  # Remove '0x'
        hex_padded = hex_value.zfill(64)  # Preenche com zeros à esquerda até 64 chars
        
        print(f"\n✅ Valor calculado manualmente:")
        print(f"   {hex_padded}")
        print(f"\n📋 Use este valor no Etherscan:")
        print(f"   {hex_padded}")

