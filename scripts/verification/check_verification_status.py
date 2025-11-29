#!/usr/bin/env python3
"""
Script para verificar o status da verificação do contrato no OKLink
"""

import os
import requests
from pathlib import Path

# Configurações
CHECK_STATUS_URL = "https://www.oklink.com/api/v5/explorer/contract/check-verify-result"
CHAIN_SHORT_NAME = "POLYGON"
CONTRACT_ADDRESS = "0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2"

def check_status(guid=None):
    """Verifica o status da verificação"""
    
    if not guid:
        print("⚠️  GUID não fornecido")
        print("💡 Se você tem o GUID da verificação, execute:")
        print("   python3 scripts/verification/check_verification_status.py <GUID>")
        print()
        print("🔗 Ou verifique manualmente no OKLink:")
        print(f"   https://www.oklink.com/polygon/address/{CONTRACT_ADDRESS}")
        return
    
    payload = {
        "chainShortName": CHAIN_SHORT_NAME,
        "guid": guid
    }
    
    headers = {"Content-Type": "application/json"}
    oklink_api_key = os.getenv("OKLINK_API_KEY")
    if oklink_api_key:
        headers["Ok-Access-Key"] = oklink_api_key
    
    print(f"🔍 Verificando status da verificação...")
    print(f"📋 GUID: {guid}")
    print(f"🌐 Chain: {CHAIN_SHORT_NAME}")
    print()
    
    try:
        response = requests.post(CHECK_STATUS_URL, json=payload, headers=headers)
        response.raise_for_status()
        
        result = response.json()
        
        if result.get("code") == "0" and result.get("data"):
            status = result["data"][0]
            
            print("=" * 60)
            print(f"📊 STATUS: {status}")
            print("=" * 60)
            print()
            
            if status == "Success":
                print("✅ VERIFICAÇÃO BEM-SUCEDIDA!")
                print()
                print(f"🔗 Ver contrato verificado:")
                print(f"   https://www.oklink.com/polygon/address/{CONTRACT_ADDRESS}")
            elif status == "Pending":
                print("⏳ Verificação ainda em processamento...")
                print("   Aguarde alguns minutos e verifique novamente.")
            elif status == "Fail":
                print("❌ Verificação falhou")
                print("   Verifique os parâmetros e tente novamente.")
            else:
                print(f"📋 Status: {status}")
        else:
            print(f"❌ Erro ao verificar status:")
            print(f"   Code: {result.get('code')}")
            print(f"   Message: {result.get('msg')}")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao verificar status: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"   Response: {e.response.text}")

def check_on_explorer():
    """Verifica se o contrato está verificado no explorer"""
    print("=" * 60)
    print("🔍 VERIFICAÇÃO MANUAL NO OKLINK")
    print("=" * 60)
    print()
    print(f"🔗 Acesse o contrato no OKLink:")
    print(f"   https://www.oklink.com/polygon/address/{CONTRACT_ADDRESS}")
    print()
    print("📋 O que verificar:")
    print("   ✅ Se o código fonte está visível")
    print("   ✅ Se aparece 'Verified' ou 'Contract Verified'")
    print("   ✅ Se as funções estão listadas corretamente")
    print()
    print("⏱️  Tempo médio de verificação: 30-60 segundos")
    print("   Se passou mais de 2 minutos, pode ter falhado.")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        guid = sys.argv[1]
        check_status(guid)
    else:
        check_on_explorer()
        print()
        print("💡 Para verificar com GUID:")
        print("   python3 scripts/verification/check_verification_status.py <GUID>")

