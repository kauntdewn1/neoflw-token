#!/usr/bin/env python3
"""
Script para verificar contrato no OKLink usando API direta
Útil quando o plugin Hardhat não consegue fazer match do bytecode
"""

import os
import json
import requests
from pathlib import Path

# Configurações
OKLINK_API_URL = "https://www.oklink.com/api/v5/explorer/contract/verify-source-code"
CHAIN_SHORT_NAME = "POLYGON"
CONTRACT_ADDRESS = "0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2"
CONTRACT_NAME = "NeoFlowToken"

# Caminhos
PROJECT_ROOT = Path(__file__).parent.parent.parent
FLATTENED_FILE = PROJECT_ROOT / "artifacts" / "flattened" / "NeoFlowToken_flattened.sol"

def read_flattened_source():
    """Lê o arquivo flattened do contrato"""
    if not FLATTENED_FILE.exists():
        raise FileNotFoundError(f"Arquivo flattened não encontrado: {FLATTENED_FILE}")
    
    with open(FLATTENED_FILE, "r", encoding="utf-8") as f:
        return f.read()

def verify_contract():
    """Envia verificação para OKLink via API"""
    
    source_code = read_flattened_source()
    
    # Preparar payload conforme documentação OKLink
    # Constructor args: 1_000_000_000 * 10**18 = 0x33b2e3c9fd0803ce8000000 (em hex, 24 bytes)
    constructor_args = "0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000"
    
    # Versão do compilador usada no deploy (conforme cache)
    # Cache mostra: "version": "0.8.30" com optimizer enabled, runs: 200
    compiler_version = "v0.8.30+commit.8c9944cf"  # Versão exata do deploy
    
    payload = {
        "chainShortName": CHAIN_SHORT_NAME,
        "contractAddress": CONTRACT_ADDRESS,
        "contractName": CONTRACT_NAME,
        "sourceCode": source_code,
        "codeFormat": "solidity-single-file",
        "compilerVersion": compiler_version,
        "optimization": "1",  # Habilitado
        "optimizationRuns": "200",
        "licenseType": "MIT License (MIT)",
        "contractAbi": "",  # Opcional, mas pode ajudar
    }
    
    # Headers
    headers = {
        "Content-Type": "application/json",
    }
    
    # Adicionar API key se disponível
    oklink_api_key = os.getenv("OKLINK_API_KEY")
    if oklink_api_key:
        headers["Ok-Access-Key"] = oklink_api_key
    
    print(f"🚀 Enviando verificação para OKLink...")
    print(f"📍 Contrato: {CONTRACT_ADDRESS}")
    print(f"🌐 Chain: {CHAIN_SHORT_NAME}")
    print(f"🔧 Compiler: {payload['compilerVersion']}")
    print(f"⚙️  Optimization: {payload['optimization']} (runs: {payload['optimizationRuns']})")
    print("")
    
    try:
        response = requests.post(OKLINK_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        
        result = response.json()
        
        if result.get("code") == "0":
            guid = result.get("data", [""])[0]
            print(f"✅ Verificação enviada com sucesso!")
            print(f"📋 GUID: {guid}")
            print("")
            print(f"⏳ Tempo estimado: 30-60 segundos")
            print(f"🔗 Verificar status: https://www.oklink.com/polygon/address/{CONTRACT_ADDRESS}")
            print("")
            print(f"💡 Para verificar status via API:")
            print(f"   curl -X POST https://www.oklink.com/api/v5/explorer/contract/check-verify-result \\")
            print(f"     -H 'Content-Type: application/json' \\")
            print(f"     -d '{{\"chainShortName\":\"{CHAIN_SHORT_NAME}\",\"guid\":\"{guid}\"}}'")
            return guid
        else:
            print(f"❌ Erro na verificação:")
            print(f"   Code: {result.get('code')}")
            print(f"   Message: {result.get('msg')}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao enviar requisição: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"   Response: {e.response.text}")
        return None

if __name__ == "__main__":
    verify_contract()

