#!/usr/bin/env python3
"""
Script para calcular os Constructor Arguments COMPLETOS do InterboxCoin
Baseado na análise do Input Data - descobriu que há DOIS argumentos!
"""
import sys

def main():
    """Função principal"""
    print("=" * 70)
    print("  ✅ CONSTRUCTOR ARGUMENTS COMPLETOS - InterboxCoin")
    print("=" * 70)
    print()
    print("🔍 Análise do Input Data revelou que o contrato foi deployado")
    print("   com DOIS argumentos no constructor!")
    print()
    print("=" * 70)
    print("  📋 VALOR PRONTO PARA COLAR NO BSCSCAN")
    print("=" * 70)
    print()
    
    # Constructor arguments completos (baseado na análise do Input Data)
    full_constructor_args = (
        "00000000000000000000000000000000000000000000d3c21bcecceda1000000"  # uint256: 1M tokens
        "00000000000000000000000045f9c5af31678bc1dacddf348936a6a6e4d42a53"  # address: signer
    )
    
    print(full_constructor_args)
    print()
    print("=" * 70)
    print("  📊 O QUE É CADA ARGUMENTO?")
    print("=" * 70)
    print()
    print("Argumento 1 (uint256 - 64 chars):")
    print("  00000000000000000000000000000000000000000000d3c21bcecceda1000000")
    print("  → Valor: 1,000,000 tokens (com 18 decimais)")
    print("  → Em wei: 1000000000000000000000000")
    print()
    print("Argumento 2 (address - 64 chars):")
    print("  00000000000000000000000045f9c5af31678bc1dacddf348936a6a6e4d42a53")
    print("  → Endereço: 0x45f9c5af31678bc1dacddf348936a6a6e4d42a53")
    print("  → Este é o signer")
    print()
    print("=" * 70)
    print("  ⚠️  IMPORTANTE")
    print("=" * 70)
    print()
    print("O código fonte atual mostra apenas 1 parâmetro (address _signer).")
    print("Mas o contrato deployado recebeu DOIS parâmetros!")
    print()
    print("Isso pode significar que:")
    print("  - O código fonte foi modificado após o deploy")
    print("  - Foi usada uma versão diferente do contrato no deploy")
    print()
    print("=" * 70)
    print("  🚀 COMO USAR")
    print("=" * 70)
    print()
    print("1. Copie o valor completo acima (128 caracteres)")
    print("2. No BSCScan, cole no campo 'Constructor Arguments'")
    print("3. Configure:")
    print("   - Compiler Version: 0.8.24+commit.e11b9ed9")
    print("   - Optimization: Yes, Runs: 200")
    print("4. Clique em 'Verify and Publish'")
    print()
    print("=" * 70)
    print("  🔗 Links Úteis")
    print("=" * 70)
    print()
    print("Contrato:")
    print("  https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017#code")
    print()
    print("Transação:")
    print("  https://bscscan.com/tx/0xfc9fff5ef2bcee846a2eac7b5b05d83378beefdf486e2b050dce7fc2a3197e69")
    print()
    print("=" * 70)

if __name__ == "__main__":
    main()

