#!/bin/bash
# 🔑 Script Interativo para Recuperar/Redefinir Senha da Conta APE

set -e

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

echo "🔑 =========================================="
echo "   RECUPERAR/REDEFINIR SENHA DA CONTA"
echo "🔑 =========================================="
echo ""

echo "📋 O que é passphrase?"
echo "   É a SENHA que você criou ao importar/gerar a conta 'neoflow-admin'"
echo ""

echo "Você lembra da senha?"
echo "1) Sim, lembro da senha"
echo "2) Não lembro, mas tenho a private key"
echo "3) Não lembro e não tenho a private key"
echo ""
read -p "Escolha uma opção (1, 2 ou 3): " OPCAO

case $OPCAO in
    1)
        echo ""
        echo -e "${GREEN}✅ Perfeito!${NC}"
        echo ""
        echo "Quando executar o deploy, você verá:"
        echo "  Sign: [y/N]: y"
        echo "  Enter passphrase: [digite sua senha]"
        echo ""
        echo "Execute:"
        echo "  source scripts/shell/setup_env.sh"
        echo "  make deploy-token"
        echo ""
        ;;
    2)
        echo ""
        echo -e "${YELLOW}🔄 Vamos reimportar a conta com nova senha${NC}"
        echo ""
        echo "⚠️  Você precisará da PRIVATE KEY da conta atual"
        echo "   (66 caracteres, começa com 0x)"
        echo ""
        read -p "Tem certeza que tem a private key? (s/n): " TEM_KEY
        
        if [ "$TEM_KEY" != "s" ] && [ "$TEM_KEY" != "S" ]; then
            echo -e "${RED}❌ Você precisa da private key para reimportar${NC}"
            echo ""
            echo "Opções:"
            echo "  1. Buscar a private key na sua wallet (MetaMask, etc)"
            echo "  2. Criar uma nova conta (vai precisar transferir ETH)"
            exit 1
        fi
        
        echo ""
        echo "📝 Passos para reimportar:"
        echo ""
        echo "1. Remover conta antiga:"
        echo "   rm ~/.ape/accounts/neoflow-admin.json"
        echo ""
        echo "2. Reimportar com nova senha:"
        echo "   ape accounts import neoflow-admin"
        echo ""
        echo "   Quando pedir:"
        echo "   - Cole sua private key"
        echo "   - Defina uma NOVA senha (anote em local seguro!)"
        echo "   - Confirme a senha"
        echo ""
        read -p "Quer que eu remova a conta antiga agora? (s/n): " REMOVER
        
        if [ "$REMOVER" = "s" ] || [ "$REMOVER" = "S" ]; then
            if [ -f ~/.ape/accounts/neoflow-admin.json ]; then
                rm ~/.ape/accounts/neoflow-admin.json
                echo -e "${GREEN}✅ Conta antiga removida${NC}"
                echo ""
                echo "Agora execute:"
                echo "  ape accounts import neoflow-admin"
            else
                echo -e "${YELLOW}⚠️  Conta não encontrada${NC}"
            fi
        fi
        ;;
    3)
        echo ""
        echo -e "${YELLOW}🆕 Vamos criar uma nova conta${NC}"
        echo ""
        echo "⚠️  ATENÇÃO:"
        echo "  - A conta atual será removida"
        echo "  - Você precisará transferir POL (Polygon) para a nova conta"
        echo "  - OU solicitar novo ETH no faucet"
        echo ""
        read -p "Continuar? (s/n): " CONTINUAR
        
        if [ "$CONTINUAR" != "s" ] && [ "$CONTINUAR" != "S" ]; then
            echo "Operação cancelada"
            exit 0
        fi
        
        echo ""
        echo "📝 Removendo conta antiga..."
        if [ -f ~/.ape/accounts/neoflow-admin.json ]; then
            rm ~/.ape/accounts/neoflow-admin.json
            echo -e "${GREEN}✅ Conta antiga removida${NC}"
        else
            echo -e "${YELLOW}⚠️  Conta não encontrada${NC}"
        fi
        
        echo ""
        echo "🆕 Criando nova conta..."
        echo ""
        echo "⚠️  IMPORTANTE:"
        echo "  - Anote a PRIVATE KEY que será exibida"
        echo "  - Anote a SENHA que você criar"
        echo "  - Guarde ambos em local seguro!"
        echo ""
        read -p "Pronto para criar? (s/n): " PRONTO
        
        if [ "$PRONTO" = "s" ] || [ "$PRONTO" = "S" ]; then
            ape accounts generate neoflow-admin
            echo ""
            echo -e "${GREEN}✅ Nova conta criada!${NC}"
            echo ""
            echo "📋 Próximos passos:"
            echo "  1. Verifique o novo endereço: ape accounts list"
            echo "  2. Obtenha POL para Polygon: https://polygon.technology/polygon-faucet"
            echo "  3. Depois execute: source scripts/shell/setup_env.sh && make deploy-token"
        else
            echo "Operação cancelada"
        fi
        ;;
    *)
        echo -e "${RED}❌ Opção inválida${NC}"
        exit 1
        ;;
esac

echo ""
echo "📚 Guia completo: RECUPERAR_PASSPHRASE.md"
echo ""

