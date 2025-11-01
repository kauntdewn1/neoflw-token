#!/bin/bash
# Script de deploy simplificado para $NEOFLW

set -e

echo "🚀 Deploy do Token $NEOFLW"
echo "============================"
echo ""

# Carregar variáveis do .env.local
if [ -f .env.local ]; then
    export $(grep -v '^#' .env.local | xargs)
    echo "✅ Variáveis carregadas do .env.local"
else
    echo "❌ Arquivo .env.local não encontrado!"
    exit 1
fi

# Verificar se API key está configurada
if [ -z "$ALCHEMY_API_KEY" ]; then
    echo "❌ ALCHEMY_API_KEY não configurada!"
    echo "Configure no .env.local"
    exit 1
fi

echo "✅ API Key configurada"
echo ""

# Verificar se conta existe
if ! ape accounts list 2>&1 | grep -q "neoflow-admin"; then
    echo "⚠️  Conta 'neoflow-admin' não encontrada!"
    echo ""
    echo "Para importar uma conta:"
    echo "  ape accounts import neoflow-admin"
    echo ""
    exit 1
fi

echo "✅ Conta 'neoflow-admin' encontrada"
echo ""

# Compilar contratos
echo "📦 Compilando contratos..."
ape compile
echo "✅ Contratos compilados"
echo ""

# Deploy do token
echo "🚀 Fazendo deploy do token em Sepolia..."
echo ""
ape run deploy_token --network ethereum:sepolia

echo ""
echo "✅ Deploy concluído!"
echo ""
echo "📋 PRÓXIMO PASSO:"
echo "1. Copie o endereço do token acima"
echo "2. Edite scripts/deploy_vault.py e cole o endereço"
echo "3. Execute: npm run deploy:vault"

