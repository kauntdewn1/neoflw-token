#!/bin/bash
# Script para exportar variáveis de ambiente do .env

# Carregar variáveis do .env se existir
if [ -f .env ]; then
    export $(grep -v '^#' .env | grep -v '^$' | xargs)
    echo "✅ Variáveis carregadas do .env"
else
    echo "⚠️  Arquivo .env não encontrado!"
    echo "   Crie um arquivo .env baseado em .env.example"
    exit 1
fi

# Verificar se API keys estão configuradas
if [ -z "$ALCHEMY_API_KEY" ]; then
    echo "❌ ALCHEMY_API_KEY não configurada no .env!"
    exit 1
fi

# Ape Framework também precisa dessas variáveis WEB3
export WEB3_ALCHEMY_API_KEY=${ALCHEMY_API_KEY}
export WEB3_ETHEREUM_SEPOLIA_ALCHEMY_API_KEY=${ALCHEMY_API_KEY}

echo "✅ Variáveis de ambiente exportadas!"
echo "   ALCHEMY_API_KEY: ${ALCHEMY_API_KEY:0:10}..."
if [ -n "$ETHERSCAN_API_KEY" ]; then
    echo "   ETHERSCAN_API_KEY: ${ETHERSCAN_API_KEY:0:10}..."
fi
echo "   WEB3_ALCHEMY_API_KEY: ${WEB3_ALCHEMY_API_KEY:0:10}..."
