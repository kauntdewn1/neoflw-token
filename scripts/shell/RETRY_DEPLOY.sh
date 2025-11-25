#!/bin/bash
# Script para retentar deploy com delay

set -e

# Obter diretório do script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$( cd "$SCRIPT_DIR/../.." && pwd )"

cd "$PROJECT_ROOT"

# Carregar variáveis de ambiente
if [ -f .env ]; then
    source .env
    export ALCHEMY_API_KEY=${ALCHEMY_API_KEY}
else
    echo "❌ Arquivo .env não encontrado!"
    exit 1
fi

echo "⏳ Aguardando 30 segundos para evitar rate limiting..."
sleep 30

echo ""
echo "🚀 Tentando deploy novamente..."
echo ""

# Usar network do .env ou padrão
NETWORK=${APE_NETWORK:-polygon:mainnet}

echo "📦 Fazendo deploy do token NEOFLW em $NETWORK..."
echo ""

ape run scripts/deploy/deploy_token --network $NETWORK

echo ""
echo "✅ Deploy concluído!"
echo ""
echo "📋 Verifique no explorer apropriado"

