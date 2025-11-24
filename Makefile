# Makefile para NEOFLOW Protocol
# Orquestração de comandos para deploy e testes

.PHONY: help install compile test clean deploy-token deploy-vault deploy-claim verify-token verify-vault verify-claim setup-claim test-claim test-token test-vault

# Variáveis
NETWORK ?= ethereum:sepolia
ACCOUNT ?= neoflow-admin

help: ## Mostra esta mensagem de ajuda
	@echo "🚀 NEOFLOW Protocol - Comandos Disponíveis"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Instala plugins e dependências
	@echo "📦 Instalando plugins..."
	@npm run plugins || true
	@echo "✅ Plugins verificados (ignorando avisos se já instalados)"

compile: ## Compila contratos Solidity
	@echo "🔨 Compilando contratos..."
	npm run compile

test: ## Executa todos os testes
	@echo "🧪 Executando testes..."
	npm run test

test-token: ## Executa testes do token
	@echo "🧪 Executando testes do token..."
	ape test tests/test_token.py

test-vault: ## Executa testes do vault
	@echo "🧪 Executando testes do vault..."
	ape test tests/test_vault.py

test-claim: ## Executa testes do claim
	@echo "🧪 Executando testes do claim..."
	ape test tests/test_claim.py

clean: ## Limpa build e cache
	@echo "🧹 Limpando build e cache..."
	npm run clean

# Deploy de Contratos
deploy-token: ## Deploy do token NeoFlowToken
	@echo "🚀 Deploying NeoFlowToken..."
	ape run scripts/deploy/deploy_token --network $(NETWORK)

deploy-vault: ## Deploy do vault StakingVault
	@echo "🚀 Deploying StakingVault..."
	ape run scripts/deploy/deploy_vault --network $(NETWORK)

deploy-claim: ## Deploy do contrato NeoFlowClaim
	@echo "🚀 Deploying NeoFlowClaim..."
	ape run scripts/deploy/deploy_claim --network $(NETWORK)

# Verificação no Etherscan
verify-token: ## Verifica token no Etherscan
	@echo "✅ Verificando token no Etherscan..."
	ape etherscan verify NeoFlowToken --network $(NETWORK)

verify-vault: ## Verifica vault no Etherscan
	@echo "✅ Verificando vault no Etherscan..."
	ape etherscan verify StakingVault --network $(NETWORK)

verify-claim: ## Verifica claim no Etherscan
	@echo "✅ Verificando claim no Etherscan..."
	ape etherscan verify NeoFlowClaim --network $(NETWORK)

# Verificação no Blockscout (Manual via interface web)
verify-blockscout: ## Instruções para verificar no Blockscout
	@echo "📋 Para verificar no Blockscout:"
	@echo "   1. Acesse: https://eth-sepolia.blockscout.com/address/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87"
	@echo "   2. Vá para aba 'Contract'"
	@echo "   3. Clique em 'Verify & publish'"
	@echo "   4. Use Standard JSON Input de: sourcify_standard_json.json"
	@echo "      ⚠️ IMPORTANTE: Use sourcify_standard_json.json (tem campo 'language')"
	@echo "      ❌ NÃO use etherscan_verification_fixed.json (formato Ape, sem 'language')"
	@echo ""
	@echo "📖 Guia completo: docs/verification/VERIFICAR_BLOCKSCOUT.md"

# Corrigir JSON para Blockscout (se necessário)
fix-blockscout-json: ## Corrige JSON para formato Blockscout
	@echo "🔧 Corrigindo JSON para Blockscout..."
	python scripts/fix_json_for_blockscout.py
	@echo "✅ JSON corrigido salvo em: blockscout_standard_json.json"

# Setup e Configuração
setup-claim: ## Script auxiliar para configurar claim
	@echo "⚙️  Configurando claim..."
	ape run setup_claim --network $(NETWORK)

transfer-to-claim: ## Transferir 50M tokens para o contrato de Claim
	@echo "💰 Transferindo tokens para o contrato de Claim..."
	ape run transfer_to_claim --network $(NETWORK)

add-whitelist: ## Adicionar endereços na whitelist do Claim
	@echo "📝 Adicionando endereços na whitelist..."
	ape run add_whitelist --network $(NETWORK)

console: ## Abre console Ape interativo
	@echo "💻 Abrindo console Ape..."
	ape console --network $(NETWORK)

# Pipeline Completo
deploy-all: compile test deploy-token deploy-vault deploy-claim ## Pipeline completo: compile + test + deploy todos os contratos
	@echo "✅ Deploy completo finalizado!"

verify-all: verify-token verify-vault verify-claim ## Verifica todos os contratos no Etherscan
	@echo "✅ Verificação completa finalizada!"

# Desenvolvimento
dev: install compile test ## Setup completo de desenvolvimento (contratos)
	@echo "✅ Ambiente de desenvolvimento configurado!"

dev-frontend: ## Roda frontend localmente (porta 3002)
	@echo "🚀 Iniciando frontend..."
	@cd frontend && npm run dev

frontend: dev-frontend ## Alias para dev-frontend

# Utilitários
check-addresses: ## Verifica endereços salvos nos arquivos
	@echo "📋 Endereços salvos:"
	@if [ -f .token_address.txt ]; then \
		echo "  Token: $$(cat .token_address.txt)"; \
	else \
		echo "  Token: Não encontrado"; \
	fi
	@if [ -f .vault_address.txt ]; then \
		echo "  Vault: $$(cat .vault_address.txt)"; \
	else \
		echo "  Vault: Não encontrado"; \
	fi
	@if [ -f .claim_address.txt ]; then \
		echo "  Claim: $$(cat .claim_address.txt)"; \
	else \
		echo "  Claim: Não encontrado"; \
	fi

# Documentação
docs: ## Abre documentação relevante
	@echo "📚 Arquivos de documentação disponíveis:"
	@echo "  - README.md"
	@echo "  - DEPLOY_INSTRUCTIONS.md"
	@echo "  - CLAIM_SETUP.md"
	@echo "  - TESTES_COMPLETOS.md"

