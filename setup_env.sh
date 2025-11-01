#!/bin/bash
# Script para exportar variáveis de ambiente

export ALCHEMY_API_KEY=h47p2nw-NDUbS0nQfSUuV
export ETHERSCAN_API_KEY=WYII9Y7JICTMERA89H6P3X9C3JKTIW8V75

# Ape Framework também precisa dessas variáveis WEB3
export WEB3_ALCHEMY_API_KEY=${ALCHEMY_API_KEY}
export WEB3_ETHEREUM_SEPOLIA_ALCHEMY_API_KEY=${ALCHEMY_API_KEY}

echo "✅ Variáveis de ambiente exportadas!"
echo "   ALCHEMY_API_KEY: ${ALCHEMY_API_KEY:0:10}..."
echo "   ETHERSCAN_API_KEY: ${ETHERSCAN_API_KEY:0:10}..."
echo "   WEB3_ALCHEMY_API_KEY: ${WEB3_ALCHEMY_API_KEY:0:10}..."
