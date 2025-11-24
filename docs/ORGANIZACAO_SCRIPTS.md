# 📁 Organização dos Scripts do Projeto

## 🎯 Estrutura de Scripts

O projeto possui scripts organizados em diferentes diretórios conforme sua função:

```
scripts/
├── deploy/          # Scripts Python para deploy de contratos
├── setup/           # Scripts Python para configuração
├── metadata/        # Scripts Python para metadados e IPFS
└── shell/           # Scripts Bash para automação e setup
```

---

## 🐚 Scripts Shell (`scripts/shell/`)

Scripts bash para automação, setup e deploy. Todos foram organizados e **não contêm mais API keys hardcoded**.

### Scripts Disponíveis:

1. **`setup_env.sh`** - Exporta variáveis do `.env`
2. **`setup_wallet.sh`** - Configuração interativa de wallet
3. **`deploy.sh`** - Deploy simplificado do token
4. **`RETRY_DEPLOY.sh`** - Retenta deploy com delay
5. **`recuperar_senha.sh`** - Recupera/redefine senha da conta APE

📖 **Documentação completa:** [`scripts/shell/README.md`](../scripts/shell/README.md)

---

## 🐍 Scripts Python

### **`scripts/deploy/`** - Deploy de Contratos

Scripts para fazer deploy dos contratos inteligentes:

- `deploy_token.py` - Deploy do token NEOFLW
- `deploy_vault.py` - Deploy do StakingVault
- `deploy_claim.py` - Deploy do NeoFlowClaim
- `deploy_governor.py` - Deploy do DAO Governor
- `deploy_gamification.py` - Deploy do GamificationController

**Uso:**
```bash
ape run scripts/deploy/deploy_token --network polygon:mainnet
```

---

### **`scripts/setup/`** - Configuração

Scripts para configurar contratos após deploy:

- `setup_claim.py` - Configura o contrato de Claim
- `add_whitelist.py` - Adiciona endereços na whitelist
- `setup_whitelist.py` - Setup completo da whitelist
- `transfer_to_claim.py` - Transfere tokens para o contrato de Claim

**Uso:**
```bash
ape run scripts/setup/setup_claim --network polygon:mainnet
```

---

### **`scripts/metadata/`** - Metadados e IPFS

Scripts para gerenciar metadados e upload para IPFS:

- `upload_to_nftstorage.py` - Upload de arquivos para NFT.Storage
- `update_token_metadata.py` - Atualiza metadados do token
- `update_token_automated.py` - Atualização automatizada
- `update_token_alternatives.py` - Atualiza alternativas de metadados

**Uso:**
```bash
ape run scripts/metadata/upload_to_nftstorage
```

---

## 🔧 Makefile

O `Makefile` na raiz do projeto fornece comandos simplificados:

```bash
# Deploy
make deploy-token    # Deploy do token
make deploy-vault     # Deploy do vault
make deploy-claim     # Deploy do claim
make deploy-all       # Deploy de todos os contratos

# Testes
make test            # Todos os testes
make test-token      # Testes do token
make test-vault      # Testes do vault
make test-claim      # Testes do claim

# Desenvolvimento
make dev             # Setup completo (contratos)
make dev-frontend    # Roda frontend localmente

# Verificação
make verify-token    # Verifica token no explorer
make verify-vault    # Verifica vault no explorer
make verify-claim    # Verifica claim no explorer
```

---

## ⚠️ Segurança

### ✅ Boas Práticas Implementadas:

1. **Nenhuma API key hardcoded** - Todos os scripts carregam do `.env`
2. **`.env` no `.gitignore`** - Credenciais não são commitadas
3. **Scripts organizados** - Fácil manutenção e auditoria
4. **Documentação completa** - Cada script tem seu propósito documentado

### 🔒 Antes de Executar Scripts:

1. Certifique-se de ter um `.env` configurado
2. Use `source scripts/shell/setup_env.sh` para exportar variáveis
3. Nunca commite o arquivo `.env`

---

## 📋 Exemplos de Uso

### **Setup Completo:**
```bash
# 1. Configurar wallet
bash scripts/shell/setup_wallet.sh

# 2. Exportar variáveis
source scripts/shell/setup_env.sh

# 3. Deploy
make deploy-token
```

### **Deploy Rápido:**
```bash
source scripts/shell/setup_env.sh && make deploy-token
```

### **Configurar Claim Após Deploy:**
```bash
# 1. Deploy do claim
make deploy-claim

# 2. Configurar claim
ape run scripts/setup/setup_claim --network polygon:mainnet

# 3. Transferir tokens
ape run scripts/setup/transfer_to_claim --network polygon:mainnet
```

---

## 🔄 Migração de Comandos Antigos

Se você estava usando comandos antigos na raiz:

| Antigo | Novo |
|--------|------|
| `source setup_env.sh` | `source scripts/shell/setup_env.sh` |
| `bash deploy.sh` | `bash scripts/shell/deploy.sh` |
| `bash setup_wallet.sh` | `bash scripts/shell/setup_wallet.sh` |
| `ape run deploy_token` | `ape run scripts/deploy/deploy_token` |

---

**✅ Scripts organizados, seguros e documentados!**

