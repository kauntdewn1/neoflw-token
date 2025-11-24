# 📜 Scripts do Projeto NEOFLW

## 📁 Organização

Os scripts estão organizados em categorias:

```
scripts/
├── deploy/          # Scripts de deploy de contratos
├── setup/           # Scripts de configuração e setup
├── verification/    # Scripts para verificação de contratos
├── utils/           # Scripts utilitários
└── metadata/        # Scripts de atualização de metadata
```

---

## 🚀 Scripts de Deploy (`deploy/`)

### **Deploy de Contratos:**

- `deploy_token.py` - Deploy do NeoFlowToken
- `deploy_vault.py` - Deploy do StakingVault
- `deploy_claim.py` - Deploy do NeoFlowClaim
- `deploy_governor.py` - Deploy do DaoGovernor
- `deploy_gamification.py` - Deploy do GamificationController
- `deploy_token_direct.py` - Deploy direto (alternativo)

### **Uso:**
```bash
# Deploy Token
ape run scripts/deploy/deploy_token --network polygon:mainnet

# Deploy Vault
ape run scripts/deploy/deploy_vault --network polygon:mainnet

# Deploy Claim
ape run scripts/deploy/deploy_claim --network polygon:mainnet
```

---

## ⚙️ Scripts de Setup (`setup/`)

### **Configuração e Setup:**

- `setup_claim.py` - Configurar contrato de claim
- `setup_whitelist.py` - Configurar whitelist
- `add_whitelist.py` - Adicionar endereços à whitelist
- `transfer_to_claim.py` - Transferir tokens para o contrato de claim

### **Uso:**
```bash
# Configurar claim
ape run scripts/setup/setup_claim --network polygon:mainnet

# Adicionar whitelist
ape run scripts/setup/add_whitelist --network polygon:mainnet
```

---

## ✅ Scripts de Verificação (`verification/`)

### **Verificação de Contratos:**

- `create_flattened_code.py` - Criar código flattened
- `convert_to_standard_json.py` - Converter para Standard JSON
- `create_complete_json.py` - Criar JSON completo
- `fix_json_for_etherscan.py` - Corrigir JSON para Etherscan
- `fix_json_for_blockscout.py` - Corrigir JSON para Blockscout
- `fix_json_language.py` - Corrigir campo language no JSON
- `remove_compiler_version.py` - Remover versão do compilador
- `remove_urls_from_json.py` - Remover URLs do JSON

### **Uso:**
```bash
# Criar código flattened
python scripts/verification/create_flattened_code.py

# Converter para Standard JSON
python scripts/verification/convert_to_standard_json.py
```

---

## 🛠️ Scripts Utilitários (`utils/`)

### **Utilitários:**

- `analyze_bytecode.py` - Analisar bytecode
- `calculate_constructor_args.py` - Calcular argumentos do construtor
- `download_openzeppelin.py` - Baixar contratos OpenZeppelin
- `add_openzeppelin_sources.py` - Adicionar fontes OpenZeppelin

### **Uso:**
```bash
# Analisar bytecode
python scripts/utils/analyze_bytecode.py

# Calcular constructor args
python scripts/utils/calculate_constructor_args.py
```

---

## 📝 Scripts de Metadata (`metadata/`)

### **Atualização de Metadata:**

- `update_token_metadata.py` - Atualizar metadata do token
- `update_token_automated.py` - Atualização automática
- `update_token_alternatives.py` - Atualização alternativa
- `upload_to_nftstorage.py` - Upload para NFT.Storage

### **Uso:**
```bash
# Atualizar metadata
python scripts/metadata/update_token_metadata.py

# Upload para IPFS
python scripts/metadata/upload_to_nftstorage.py
```

---

## 📋 Comandos Rápidos

### **Via Makefile:**
```bash
make deploy-token    # Deploy token
make deploy-vault    # Deploy vault
make deploy-claim    # Deploy claim
```

### **Via Ape diretamente:**
```bash
ape run scripts/deploy/deploy_token --network polygon:mainnet
```

---

## 🔄 Migração de Comandos Antigos

Se você estava usando comandos antigos, atualize para:

| Antigo | Novo |
|--------|------|
| `ape run deploy_token` | `ape run scripts/deploy/deploy_token` |
| `ape run deploy_vault` | `ape run scripts/deploy/deploy_vault` |
| `ape run deploy_claim` | `ape run scripts/deploy/deploy_claim` |
| `ape run setup_claim` | `ape run scripts/setup/setup_claim` |

---

**✅ Scripts organizados e documentados!**

