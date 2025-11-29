#!/usr/bin/env python3
"""
Script de Auditoria de Endereços de Contratos
Verifica todos os endereços salvos e identifica qual rede cada um pertence
"""

from ape import project, networks
import os
import sys
from pathlib import Path

def check_contract_on_chain(address: str, network_name: str):
    """
    Verifica se um contrato existe on-chain em uma rede específica
    Retorna informações sobre o contrato
    """
    try:
        # Conectar à rede
        with networks.parse_network_choice(network_name) as provider:
            code = provider.get_code(address)
            
            if code and code != "0x" and len(code) > 2:
                # Contrato existe
                return {
                    "exists": True,
                    "has_code": True,
                    "code_length": len(code) if code else 0
                }
            else:
                return {
                    "exists": False,
                    "has_code": False,
                    "code_length": 0
                }
    except Exception as e:
        return {
            "exists": False,
            "error": str(e)
        }

def read_address_file(file_path: str):
    """Lê endereço de um arquivo"""
    try:
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                content = f.read().strip()
                if content and content.startswith("0x"):
                    return content
        return None
    except Exception as e:
        return None

def audit_all_addresses():
    """Audita todos os endereços encontrados no projeto"""
    
    print("=" * 80)
    print("🔍 AUDITORIA DE ENDEREÇOS DE CONTRATOS")
    print("=" * 80)
    print()
    
    # Lista de arquivos para verificar
    address_files = {
        "Token (raiz)": ".token_address.txt",
        "Token (artifacts)": "artifacts/addresses/.token_address.txt",
        "Vault (raiz)": ".vault_address.txt",
        "Vault (artifacts)": "artifacts/addresses/.vault_address.txt",
        "Claim (raiz)": ".claim_address.txt",
        "Claim (artifacts)": "artifacts/addresses/.claim_address.txt",
    }
    
    # Endereços do .env
    env_addresses = {}
    try:
        with open(".env", "r") as f:
            for line in f:
                line = line.strip()
                if line.startswith("NEXT_PUBLIC_TOKEN_ADDRESS="):
                    addr = line.split("=", 1)[1].strip()
                    if addr:
                        env_addresses["Token (.env)"] = addr
                elif line.startswith("NEXT_PUBLIC_VAULT_ADDRESS="):
                    addr = line.split("=", 1)[1].strip()
                    if addr:
                        env_addresses["Vault (.env)"] = addr
                elif line.startswith("NEXT_PUBLIC_CLAIM_ADDRESS="):
                    addr = line.split("=", 1)[1].strip()
                    if addr:
                        env_addresses["Claim (.env)"] = addr
    except Exception as e:
        print(f"⚠️  Erro ao ler .env: {e}")
    
    # Coletar todos os endereços únicos
    all_addresses = {}
    
    print("📋 Lendo arquivos de endereços...")
    print()
    
    for label, file_path in address_files.items():
        addr = read_address_file(file_path)
        if addr:
            if addr not in all_addresses:
                all_addresses[addr] = []
            all_addresses[addr].append(f"{label} ({file_path})")
            print(f"✅ {label}: {addr}")
        else:
            print(f"❌ {label}: Arquivo não encontrado ou vazio")
    
    print()
    print("📋 Lendo endereços do .env...")
    print()
    
    for label, addr in env_addresses.items():
        if addr:
            if addr not in all_addresses:
                all_addresses[addr] = []
            all_addresses[addr].append(f"{label} (.env)")
            print(f"✅ {label}: {addr}")
    
    print()
    print("=" * 80)
    print("🌐 VERIFICANDO CONTRATOS ON-CHAIN")
    print("=" * 80)
    print()
    
    # Redes para verificar
    networks_to_check = [
        "polygon:mainnet",
        "ethereum:sepolia",
        "ethereum:mainnet",
    ]
    
    results = {}
    
    for address in all_addresses.keys():
        print(f"🔍 Verificando: {address}")
        print(f"   Encontrado em: {', '.join(all_addresses[address])}")
        print()
        
        address_results = {}
        
        for network_name in networks_to_check:
            print(f"   🌐 Testando {network_name}...", end=" ")
            try:
                result = check_contract_on_chain(address, network_name)
                if result.get("exists") and result.get("has_code"):
                    print("✅ ENCONTRADO!")
                    address_results[network_name] = {
                        "found": True,
                        "code_length": result.get("code_length", 0)
                    }
                else:
                    print("❌ Não encontrado")
                    address_results[network_name] = {"found": False}
            except Exception as e:
                print(f"⚠️  Erro: {e}")
                address_results[network_name] = {"found": False, "error": str(e)}
        
        results[address] = {
            "sources": all_addresses[address],
            "networks": address_results
        }
        print()
    
    # Gerar relatório
    print("=" * 80)
    print("📊 RELATÓRIO FINAL")
    print("=" * 80)
    print()
    
    polygon_contracts = {}
    sepolia_contracts = {}
    mainnet_contracts = {}
    not_found = []
    
    for address, data in results.items():
        found_any = False
        
        for network, result in data["networks"].items():
            if result.get("found"):
                found_any = True
                if "polygon:mainnet" in network:
                    polygon_contracts[address] = data["sources"]
                elif "sepolia" in network:
                    sepolia_contracts[address] = data["sources"]
                elif "ethereum:mainnet" in network:
                    mainnet_contracts[address] = data["sources"]
        
        if not found_any:
            not_found.append((address, data["sources"]))
    
    # Relatório por rede
    if polygon_contracts:
        print("✅ CONTRATOS ENCONTRADOS NO POLYGON MAINNET:")
        print()
        for addr, sources in polygon_contracts.items():
            print(f"   📍 {addr}")
            for source in sources:
                print(f"      └─ {source}")
            print()
    
    if sepolia_contracts:
        print("⚠️  CONTRATOS ENCONTRADOS NO SEPOLIA (TESTNET):")
        print()
        for addr, sources in sepolia_contracts.items():
            print(f"   📍 {addr}")
            for source in sources:
                print(f"      └─ {source}")
            print()
    
    if mainnet_contracts:
        print("⚠️  CONTRATOS ENCONTRADOS NO ETHEREUM MAINNET:")
        print()
        for addr, sources in mainnet_contracts.items():
            print(f"   📍 {addr}")
            for source in sources:
                print(f"      └─ {source}")
            print()
    
    if not_found:
        print("❌ CONTRATOS NÃO ENCONTRADOS EM NENHUMA REDE:")
        print()
        for addr, sources in not_found:
            print(f"   📍 {addr}")
            for source in sources:
                print(f"      └─ {source}")
            print()
    
    # Recomendações
    print("=" * 80)
    print("💡 RECOMENDAÇÕES")
    print("=" * 80)
    print()
    
    if polygon_contracts:
        print("✅ Use estes endereços para Polygon Mainnet:")
        for addr, sources in polygon_contracts.items():
            # Tentar identificar tipo de contrato
            contract_type = "Desconhecido"
            for source in sources:
                if "Token" in source:
                    contract_type = "Token"
                    break
                elif "Vault" in source:
                    contract_type = "Vault"
                    break
                elif "Claim" in source:
                    contract_type = "Claim"
                    break
            
            print(f"   {contract_type}: {addr}")
        print()
    
    if sepolia_contracts:
        print("⚠️  ATENÇÃO: Estes endereços são de Sepolia (testnet):")
        for addr, sources in sepolia_contracts.items():
            print(f"   {addr}")
        print("   Considere removê-los ou marcá-los claramente como testnet.")
        print()
    
    # Salvar relatório
    report_file = "artifacts/addresses/AUDIT_REPORT.txt"
    os.makedirs(os.path.dirname(report_file), exist_ok=True)
    
    with open(report_file, "w") as f:
        f.write("AUDITORIA DE ENDEREÇOS DE CONTRATOS\n")
        f.write("=" * 80 + "\n\n")
        
        if polygon_contracts:
            f.write("POLYGON MAINNET:\n")
            for addr, sources in polygon_contracts.items():
                f.write(f"  {addr}\n")
                for source in sources:
                    f.write(f"    - {source}\n")
            f.write("\n")
        
        if sepolia_contracts:
            f.write("SEPOLIA (TESTNET):\n")
            for addr, sources in sepolia_contracts.items():
                f.write(f"  {addr}\n")
                for source in sources:
                    f.write(f"    - {source}\n")
            f.write("\n")
    
    print(f"📄 Relatório salvo em: {report_file}")
    print()

def main():
    """Função principal"""
    try:
        audit_all_addresses()
    except Exception as e:
        print(f"❌ Erro durante auditoria: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()

