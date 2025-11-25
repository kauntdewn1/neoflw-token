#!/bin/bash
# 🔧 Script Interativo de Configuração de Wallet

set -e

echo "🔧 =========================================="
echo "   SETUP COMPLETO - CONTA E WALLET"
echo "🔧 =========================================="
echo ""

# Cores
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Passo 1: Verificar/Criar .env
echo "📝 Passo 1: Configurando arquivo .env..."
if [ ! -f .env ]; then
    if [ -f .env.local ]; then
        cp .env.local .env
        echo -e "${GREEN}✅ Arquivo .env criado a partir do .env.local${NC}"
    else
        echo -e "${YELLOW}⚠️  Arquivo .env.local não encontrado${NC}"
        echo "Criando .env básico..."
        cat > .env << EOF
ALCHEMY_API_KEY=h47p2nw-NDUbS0nQfSUuV
ETHERSCAN_API_KEY=WYII9Y7JICTMERA89H6P3X9C3JKTIW8V75
EOF
        echo -e "${GREEN}✅ Arquivo .env criado${NC}"
    fi
else
    echo -e "${GREEN}✅ Arquivo .env já existe${NC}"
fi

# Passo 2: Exportar variáveis
echo ""
echo "🔑 Passo 2: Exportando variáveis de ambiente..."
source .env
export ALCHEMY_API_KEY=${ALCHEMY_API_KEY}
export ETHERSCAN_API_KEY=${ETHERSCAN_API_KEY}

if [ -n "$ALCHEMY_API_KEY" ]; then
    echo -e "${GREEN}✅ ALCHEMY_API_KEY exportada${NC}"
else
    echo -e "${RED}❌ ALCHEMY_API_KEY não encontrada${NC}"
    exit 1
fi

# Passo 3: Verificar contas existentes
echo ""
echo "👤 Passo 3: Verificando contas..."
ACCOUNTS=$(ape accounts list 2>&1 | grep -E "Found|alias" || echo "")

if echo "$ACCOUNTS" | grep -q "neoflow-admin"; then
    echo -e "${GREEN}✅ Conta 'neoflow-admin' encontrada${NC}"
    ACCOUNT_ADDRESS=$(ape accounts list | grep -o "0x[a-fA-F0-9]\{40\}" | head -1)
    echo "   Endereço: $ACCOUNT_ADDRESS"
    
    echo ""
    echo "💰 Verificando saldo na Sepolia..."
    python3 << PYEOF
from ape import accounts, networks
import sys

try:
    with networks.ethereum.sepolia.use_provider("alchemy"):
        acct = accounts.load("neoflow-admin")
        balance = acct.balance
        eth_balance = balance / 10**18
        
        print(f"   Saldo: {eth_balance:.6f} ETH")
        
        if eth_balance >= 0.001:
            print(f"\n✅ Saldo suficiente para deploy!")
            sys.exit(0)
        else:
            print(f"\n⚠️  Saldo insuficiente")
            print(f"   Precisa de ~0.001 ETH para deploy completo")
            print(f"\n💡 Obtenha Sepolia ETH em:")
            print(f"   https://www.alchemy.com/faucets/ethereum-sepolia")
            print(f"   Endereço: {acct.address}")
            sys.exit(1)
except Exception as e:
    print(f"❌ Erro ao verificar saldo: {e}")
    sys.exit(1)
PYEOF
    
    SALDO_OK=$?
    
else
    echo -e "${YELLOW}⚠️  Conta 'neoflow-admin' não encontrada${NC}"
    echo ""
    echo "Escolha uma opção:"
    echo "1) Importar conta existente (com private key)"
    echo "2) Criar nova conta"
    echo ""
    read -p "Opção (1 ou 2): " OPCAO
    
    case $OPCAO in
        1)
            echo ""
            echo "📥 Importando conta..."
            echo "⚠️  Você precisará da sua private key (66 caracteres, começa com 0x)"
            ape accounts import neoflow-admin
            echo -e "${GREEN}✅ Conta importada!${NC}"
            ;;
        2)
            echo ""
            echo "🆕 Criando nova conta..."
            echo "⚠️  ANOTE a private key que será gerada!"
            ape accounts generate neoflow-admin
            echo -e "${GREEN}✅ Conta criada!${NC}"
            ;;
        *)
            echo -e "${RED}❌ Opção inválida${NC}"
            exit 1
            ;;
    esac
    
    SALDO_OK=1
fi

# Passo 4: Resumo final
echo ""
echo "=========================================="
echo "📋 RESUMO DA CONFIGURAÇÃO"
echo "=========================================="
echo ""
echo "✅ Arquivo .env: $(test -f .env && echo 'OK' || echo 'FALTANDO')"
echo "✅ Variáveis exportadas: $(test -n "$ALCHEMY_API_KEY" && echo 'OK' || echo 'FALTANDO')"
echo "✅ Conta neoflow-admin: $(ape accounts list | grep -q neoflow-admin && echo 'OK' || echo 'FALTANDO')"

if [ $SALDO_OK -eq 0 ]; then
    echo ""
    echo -e "${GREEN}🎉 TUDO PRONTO PARA DEPLOY!${NC}"
    echo ""
    echo "Execute:"
    echo "  make deploy-all"
    echo ""
    echo "Ou passo a passo:"
    echo "  make deploy-token"
    echo "  make deploy-vault"
    echo "  make deploy-claim"
else
    echo ""
    echo -e "${YELLOW}⚠️  PRECISA OBTER SEPOLIA ETH${NC}"
    echo ""
    echo "1. Acesse: https://www.alchemy.com/faucets/ethereum-sepolia"
    echo "2. Cole seu endereço: $ACCOUNT_ADDRESS"
    echo "3. Solicite Sepolia ETH"
    echo "4. Aguarde alguns minutos"
    echo "5. Execute este script novamente para verificar"
fi

echo ""
echo "📚 Documentação completa: SETUP_COMPLETO.md"
echo ""

