#!/usr/bin/env python3
"""
Script para verificar se o bytecode compilado localmente corresponde ao deployado on-chain
"""

import json
from pathlib import Path
from ape import project, networks

# Configurações
CONTRACT_ADDRESS = "0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2"
CONTRACT_NAME = "NeoFlowToken"
PROJECT_ROOT = Path(__file__).parent.parent.parent

def get_deployed_bytecode():
    """Obtém o bytecode deployado on-chain"""
    print("🔍 Conectando à blockchain...")
    
    with networks.parse_network_choice("polygon:mainnet"):
        provider = networks.active_provider
        print(f"🌐 Network: {provider.network.name}")
        print(f"🔗 Chain ID: {provider.chain_id}")
        print()
        
        # Obter bytecode do contrato deployado
        bytecode_bytes = provider.get_code(CONTRACT_ADDRESS)
        
        # Converter bytes para hex string
        if isinstance(bytecode_bytes, bytes):
            bytecode_hex = bytecode_bytes.hex()
        else:
            bytecode_hex = str(bytecode_bytes)
        
        # Remover prefixo 0x se existir
        bytecode_hex = bytecode_hex.replace("0x", "")
        
        print(f"📦 Bytecode deployado (primeiros 100 chars): {bytecode_hex[:100]}...")
        print(f"📏 Tamanho: {len(bytecode_hex)} caracteres ({len(bytecode_hex)//2} bytes)")
        print()
        
        return bytecode_hex

def get_compiled_bytecode():
    """Obtém o bytecode compilado localmente"""
    print("🔨 Carregando contrato compilado...")
    
    try:
        # Obter bytecode do artifact diretamente
        artifact_path = PROJECT_ROOT / "artifacts" / "contracts" / "NeoFlowToken.sol" / "NeoFlowToken.json"
        
        if artifact_path.exists():
            with open(artifact_path, "r") as f:
                artifact = json.load(f)
            
            print(f"✅ Artifact encontrado: {artifact_path}")
            
            # Tentar diferentes caminhos no JSON (dependendo da estrutura do Ape)
            deployed_bytecode = None
            
            # Formato Ape Framework
            if "deployedBytecode" in artifact:
                if isinstance(artifact["deployedBytecode"], dict):
                    deployed_bytecode = artifact["deployedBytecode"].get("bytecode", {}).get("object", "")
                elif isinstance(artifact["deployedBytecode"], str):
                    deployed_bytecode = artifact["deployedBytecode"]
            
            # Formato Hardhat (fallback)
            if not deployed_bytecode and "deployedBytecode" in artifact:
                deployed_bytecode = artifact.get("deployedBytecode", "")
            
            if deployed_bytecode:
                # Remover prefixo 0x se existir
                deployed_bytecode = deployed_bytecode.replace("0x", "")
                print(f"📦 Bytecode compilado (primeiros 100 chars): {deployed_bytecode[:100]}...")
                print(f"📏 Tamanho: {len(deployed_bytecode)} caracteres ({len(deployed_bytecode)//2} bytes)")
                print()
                return deployed_bytecode
            else:
                print("❌ Bytecode não encontrado no artifact")
                print(f"   Chaves disponíveis: {list(artifact.keys())[:10]}")
                return None
        else:
            print(f"❌ Artifact não encontrado: {artifact_path}")
            print("💡 Execute 'ape compile' primeiro para gerar os artifacts")
            return None
            
    except Exception as e:
        print(f"❌ Erro ao carregar contrato: {e}")
        import traceback
        traceback.print_exc()
        return None

def compare_bytecodes(deployed, compiled):
    """Compara os dois bytecodes"""
    print("=" * 60)
    print("🔍 COMPARAÇÃO DE BYTECODES")
    print("=" * 60)
    print()
    
    if not deployed or not compiled:
        print("❌ Não foi possível obter ambos os bytecodes")
        return False
    
    # Remover prefixo 0x se existir
    deployed = deployed.replace("0x", "").lower()
    compiled = compiled.replace("0x", "").lower()
    
    # Comparar tamanhos
    print(f"📏 Tamanho deployado: {len(deployed)} chars ({len(deployed)//2} bytes)")
    print(f"📏 Tamanho compilado: {len(compiled)} chars ({len(compiled)//2} bytes)")
    print()
    
    if len(deployed) != len(compiled):
        print("⚠️  TAMANHOS DIFERENTES!")
        print(f"   Diferença: {abs(len(deployed) - len(compiled))} caracteres")
        print()
    
    # Comparar bytecode (ignorar metadata no final)
    # Metadata geralmente está nos últimos ~50 bytes
    # Vamos comparar até o menor tamanho menos 100 bytes (para ignorar metadata)
    min_len = min(len(deployed), len(compiled))
    compare_len = min_len - 100  # Ignorar últimos 100 chars (metadata)
    
    deployed_compare = deployed[:compare_len]
    compiled_compare = compiled[:compare_len]
    
    if deployed_compare == compiled_compare:
        print("✅ BYTECODES CORRESPONDEM (ignorando metadata)!")
        print("   Os bytecodes são idênticos até a seção de metadata.")
        return True
    else:
        print("❌ BYTECODES NÃO CORRESPONDEM!")
        print()
        
        # Encontrar primeira diferença
        for i in range(min(compare_len, 200)):  # Verificar primeiros 200 chars
            if deployed_compare[i] != compiled_compare[i]:
                print(f"   Primeira diferença na posição {i}:")
                print(f"   Deployado:  ...{deployed_compare[max(0,i-10):i+10]}...")
                print(f"   Compilado: ...{compiled_compare[max(0,i-10):i+10]}...")
                break
        
        print()
        print("💡 Possíveis causas:")
        print("   1. Versão do compilador diferente")
        print("   2. Configurações de optimizer diferentes")
        print("   3. EVM version diferente")
        print("   4. Código fonte diferente")
        return False

def main():
    print("=" * 60)
    print("🔍 VERIFICAÇÃO DE BYTECODE")
    print("=" * 60)
    print()
    
    # Obter bytecodes
    deployed = get_deployed_bytecode()
    compiled = get_compiled_bytecode()
    
    # Comparar
    match = compare_bytecodes(deployed, compiled)
    
    print()
    print("=" * 60)
    if match:
        print("✅ RESULTADO: Bytecodes correspondem!")
        print("   O contrato pode ser verificado.")
    else:
        print("❌ RESULTADO: Bytecodes NÃO correspondem!")
        print("   Verifique as configurações de compilação.")
    print("=" * 60)

if __name__ == "__main__":
    main()

