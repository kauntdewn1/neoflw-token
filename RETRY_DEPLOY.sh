#!/bin/bash
# Script para retentar deploy com delay

set -e

echo "⏳ Aguardando 30 segundos para evitar rate limiting..."
sleep 30

echo ""
echo "🚀 Tentando deploy novamente..."
echo ""

cd /Users/nettomello/CODIGOS/flwff-protocol
source .venv/bin/activate
export ALCHEMY_API_KEY=h47p2nw-NDUbS0nQfSUuV

echo "📦 Fazendo deploy do token NEOFLW em Sepolia..."
echo ""

ape run deploy_token --network ethereum:sepolia

echo ""
echo "✅ Deploy concluído!"
echo ""
echo "📋 Verifique no Etherscan:"
echo "   https://sepolia.etherscan.io/address/0xf96c428e3b6d9CB01489f848F3A4579f7444132e"

