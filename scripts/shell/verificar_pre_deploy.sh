#!/bin/bash
# Script de verificação rápida antes do deploy em Polygon Mainnet

set -e

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo "🔍 Verificando pré-requisitos para deploy..."
echo ""

# 1. Verificar .env
echo "1️⃣ Verificando arquivo .env..."
if [ ! -f .env ]; then
    echo -e "${RED}❌ Arquivo .env não encontrado!${NC}"
    echo "   Crie um arquivo .env baseado em .env.example"
    exit 1
fi
echo -e "${GREEN}✅ Arquivo .env encontrado${NC}"

# 2. Verificar ALCHEMY_API_KEY
echo ""
echo "2️⃣ Verificando ALCHEMY_API_KEY..."
source .env
if [ -z "$ALCHEMY_API_KEY" ]; then
    echo -e "${RED}❌ ALCHEMY_API_KEY não configurada no .env!${NC}"
    exit 1
fi
echo -e "${GREEN}✅ ALCHEMY_API_KEY configurada${NC}"

# 3. Verificar APE_NETWORK
echo ""
echo "3️⃣ Verificando APE_NETWORK..."
if [ -z "$APE_NETWORK" ]; then
    echo -e "${YELLOW}⚠️  APE_NETWORK não configurado, usando padrão polygon:mainnet${NC}"
    export APE_NETWORK=polygon:mainnet
elif [ "$APE_NETWORK" != "polygon:mainnet" ]; then
    echo -e "${YELLOW}⚠️  APE_NETWORK está configurado como: $APE_NETWORK${NC}"
    echo "   Recomendado: polygon:mainnet"
    read -p "   Continuar mesmo assim? (s/N): " CONTINUAR
    if [[ ! $CONTINUAR =~ ^[Ss]$ ]]; then
        exit 1
    fi
else
    echo -e "${GREEN}✅ APE_NETWORK configurado como polygon:mainnet${NC}"
fi

# 4. Verificar wallet
echo ""
echo "4️⃣ Verificando wallet 'neoflow-admin'..."
if ! ape accounts list 2>/dev/null | grep -q "neoflow-admin"; then
    echo -e "${RED}❌ Wallet 'neoflow-admin' não encontrada!${NC}"
    echo "   Execute: ape accounts import neoflow-admin"
    exit 1
fi
echo -e "${GREEN}✅ Wallet 'neoflow-admin' encontrada${NC}"

# 5. Verificar saldo de POL
echo ""
echo "5️⃣ Verificando saldo de POL na wallet..."
WALLET_ADDRESS=$(ape accounts show neoflow-admin 2>/dev/null | grep -i "address" | head -1 | awk '{print $2}' || echo "")
if [ -z "$WALLET_ADDRESS" ]; then
    echo -e "${YELLOW}⚠️  Não foi possível obter endereço da wallet${NC}"
    echo "   Verifique manualmente no Polygonscan"
else
    echo "   Endereço: $WALLET_ADDRESS"
    echo "   Verificar saldo: https://polygonscan.com/address/$WALLET_ADDRESS"
    echo ""
    echo -e "${YELLOW}⚠️  Verifique se há pelo menos 50 POL na wallet${NC}"
    echo "   Mínimo recomendado: 50 POL (~$30-60 USD)"
    echo ""
    read -p "   Confirma que tem POL suficiente? (s/N): " TEM_POL
    if [[ ! $TEM_POL =~ ^[Ss]$ ]]; then
        echo ""
        echo "   Obtenha POL em:"
        echo "   - Exchange (Binance, Coinbase)"
        echo "   - Bridge: https://portal.polygon.technology/polygon/bridge"
        echo "   - Migrar MATIC → POL: https://portal.polygon.technology/pol-upgrade"
        exit 1
    fi
fi

# 6. Verificar compilação
echo ""
echo "6️⃣ Verificando se contratos estão compilados..."
if [ ! -d "contracts/.cache" ] && [ ! -f "contracts/NeoFlowToken.json" ]; then
    echo -e "${YELLOW}⚠️  Contratos não compilados${NC}"
    echo "   Execute: npm run compile"
    read -p "   Compilar agora? (S/n): " COMPILAR
    if [[ ! $COMPILAR =~ ^[Nn]$ ]]; then
        echo ""
        echo "   Compilando contratos..."
        npm run compile
        if [ $? -ne 0 ]; then
            echo -e "${RED}❌ Erro na compilação!${NC}"
            exit 1
        fi
        echo -e "${GREEN}✅ Contratos compilados${NC}"
    else
        echo -e "${RED}❌ Compilação necessária antes do deploy${NC}"
        exit 1
    fi
else
    echo -e "${GREEN}✅ Contratos compilados${NC}"
fi

# Resumo final
echo ""
echo "=========================================="
echo -e "${GREEN}✅ TODOS OS PRÉ-REQUISITOS VERIFICADOS!${NC}"
echo "=========================================="
echo ""
echo "🚀 Pronto para deploy!"
echo ""
echo "Próximos passos:"
echo "  1. Deploy Token:"
echo "     ape run scripts/deploy/deploy_token --network polygon:mainnet"
echo ""
echo "  2. Anotar endereço do Token e atualizar frontend/.env"
echo ""
echo "  3. Deploy Vault:"
echo "     ape run scripts/deploy/deploy_vault --network polygon:mainnet"
echo ""
echo "  4. Deploy Claim:"
echo "     ape run scripts/deploy/deploy_claim --network polygon:mainnet"
echo ""

