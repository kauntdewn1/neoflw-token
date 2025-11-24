# 📁 Organização do Projeto NEOFLW Token

## 🎯 Estrutura de Diretórios

```
neoflw-token/
├── contracts/              # ✅ Smart Contracts (todos aqui)
│   ├── NeoFlowToken.sol
│   ├── StakingVault.sol
│   ├── NeoFlowClaim.sol
│   ├── DaoGovernor.sol
│   ├── NeoFlowTokenVotes.sol
│   └── GamificationController.sol
│
├── scripts/                # Scripts Python para deploy e operações
│   ├── deploy_token.py
│   ├── deploy_vault.py
│   ├── deploy_claim.py
│   └── ...
│
├── tests/                  # Testes automatizados
│   ├── test_token.py
│   ├── test_vault.py
│   ├── test_claim.py
│   └── test_security_fixes.py
│
├── frontend/               # DApp Frontend (Next.js)
│   ├── src/
│   │   ├── app/
│   │   ├── components/
│   │   ├── hooks/
│   │   └── config/
│   └── package.json
│
├── docs/                   # Documentação completa
│   ├── contracts/          # Documentação de contratos
│   ├── deploy/             # Guias de deploy
│   ├── frontend/           # Documentação do frontend
│   ├── project/            # Documentação do projeto
│   ├── setup/              # Guias de setup
│   └── temp/               # Arquivos temporários/documentação antiga
│
├── artifacts/              # ✅ Arquivos gerados e temporários
│   ├── flattened/          # Contratos flattened (para verificação)
│   ├── verification/       # JSONs de verificação (Etherscan/Sourcify)
│   └── addresses/          # Arquivos de endereços deployados
│
├── metadata/               # Metadados do token
│   └── token-metadata.json
│
├── public/                 # Arquivos públicos (imagens, etc)
│   └── images/
│
└── [arquivos de config]    # Configuração raiz
    ├── ape-config.yaml
    ├── package.json
    ├── Makefile
    └── .env.example
```

---

## ✅ Organização Realizada

### **Contratos:**
- ✅ **Todos os contratos** estão em `contracts/`
- ✅ **Nenhum contrato** solto na raiz
- ✅ `NeoFlowToken_flattened.sol` movido para `artifacts/flattened/`

### **Arquivos de Verificação:**
- ✅ `etherscan_verification.json` → `artifacts/verification/`
- ✅ `etherscan_verification_fixed.json` → `artifacts/verification/`
- ✅ `sourcify_verification.json` → `artifacts/verification/`
- ✅ `sourcify_standard_json.json` → `artifacts/verification/`

### **Arquivos de Endereços:**
- ✅ `.token_address.txt` → `artifacts/addresses/`
- ✅ `.vault_address.txt` → `artifacts/addresses/`
- ✅ `.claim_address.txt` → `artifacts/addresses/`

### **Arquivos Temporários:**
- ✅ `AVATAR_IPFS_INFO.txt` → `docs/temp/`
- ✅ `CONSTRUCTOR_ARGS_CORRETO.txt` → `docs/temp/`
- ✅ `INSTRUCOES_CLAIM_SIMPLES.txt` → `docs/temp/`
- ✅ `claim.html` → `docs/temp/`

---

## 📋 Regras de Organização

### **Onde Colocar Arquivos:**

1. **Smart Contracts:**
   - ✅ Sempre em `contracts/`
   - ❌ Nunca na raiz

2. **Arquivos Gerados:**
   - ✅ `artifacts/flattened/` - Contratos flattened
   - ✅ `artifacts/verification/` - JSONs de verificação
   - ✅ `artifacts/addresses/` - Endereços deployados

3. **Documentação:**
   - ✅ `docs/` - Organizada por categoria
   - ✅ `docs/temp/` - Arquivos temporários/antigos

4. **Scripts:**
   - ✅ `scripts/` - Todos os scripts Python

5. **Testes:**
   - ✅ `tests/` - Todos os testes

6. **Frontend:**
   - ✅ `frontend/` - Todo código frontend

---

## 🚫 Arquivos que NÃO Devem Estar na Raiz

- ❌ Contratos `.sol` (exceto se for necessário para build)
- ❌ Arquivos de verificação `.json`
- ❌ Arquivos temporários `.txt`
- ❌ Arquivos de endereços `.txt`
- ❌ HTMLs de teste

---

## ✅ Arquivos que PODEM Estar na Raiz

- ✅ `ape-config.yaml` - Configuração do Ape Framework
- ✅ `package.json` - Configuração npm
- ✅ `Makefile` - Comandos make
- ✅ `README.md` - Documentação principal
- ✅ `.env.example` - Exemplo de variáveis de ambiente
- ✅ `thirdweb-api.json` - OpenAPI spec (se necessário)

---

## 📝 Checklist de Organização

- [x] Contratos organizados em `contracts/`
- [x] Arquivos flattened movidos para `artifacts/flattened/`
- [x] Arquivos de verificação em `artifacts/verification/`
- [x] Arquivos de endereços em `artifacts/addresses/`
- [x] Arquivos temporários em `docs/temp/`
- [x] `.gitignore` atualizado
- [x] Estrutura documentada

---

**✅ Projeto organizado e limpo!**

