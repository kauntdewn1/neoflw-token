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
	npm run plugins

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
	ape run deploy_token --network $(NETWORK)

deploy-vault: ## Deploy do vault StakingVault
	@echo "🚀 Deploying StakingVault..."
	ape run deploy_vault --network $(NETWORK)

deploy-claim: ## Deploy do contrato NeoFlowClaim
	@echo "🚀 Deploying NeoFlowClaim..."
	ape run deploy_claim --network $(NETWORK)

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
dev: install compile test ## Setup completo de desenvolvimento
	@echo "✅ Ambiente de desenvolvimento configurado!"

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

