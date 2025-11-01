# 📚 Documentação NEOFLW Token

## 📋 Sumário

Este repositório contém toda a documentação do projeto NEOFLW Token, organizada por categoria.

---

## 🚀 **PRÓXIMOS PASSOS: MIGRAÇÃO PARA MAINNET**

### ⭐ **DESTAQUE: Pronto para Migração!**

O token está **verificado e funcionando** em Sepolia Testnet. Agora é hora de migrar para Ethereum Mainnet.

**📖 Guia Completo:** [`docs/migration/MIGRACAO_MAINNET.md`](./docs/migration/MIGRACAO_MAINNET.md)

### **Checklist Rápido:**

1. ✅ **Preparação:**
   - [ ] ETH na wallet (~0.1 ETH recomendado)
   - [ ] Wallet `neoflow-admin` configurada
   - [ ] APIs configuradas (Alchemy, Etherscan)

2. ✅ **Deploy:**
   ```bash
   npm run compile
   ape run scripts/deploy_token.py --network ethereum:mainnet
   ```

3. ✅ **Verificação:**
   - Verificar no Sourcify
   - Verificar no Etherscan

4. ✅ **Atualização:**
   - Atualizar metadados no Etherscan
   - Adicionar em GeckoTerminal, CoinGecko, etc.

**👉 Veja o guia completo:** [`docs/migration/MIGRACAO_MAINNET.md`](./docs/migration/MIGRACAO_MAINNET.md)

---

## 📁 Estrutura da Documentação

### **Setup e Configuração** (`docs/setup/`)

Documentação inicial do projeto:

- **`ALCHEMY_SETUP.md`** - Como configurar Alchemy API
- **`SEPOLIA_SETUP.md`** - Como obter Sepolia ETH (faucets)
- **`METAMASK_SEPOLIA.md`** - Configurar MetaMask para Sepolia
- **`WALLET_SETUP.md`** - Configurar wallet no Ape Framework

**Quando usar:** Primeira vez configurando o projeto ou nova máquina.

---

### **Deploy e Operação** (`docs/deploy/`)

Guias para fazer deploy dos contratos:

- **`DEPLOY_INSTRUCTIONS.md`** - Instruções completas de deploy
- **`CLAIM_SETUP.md`** - Como configurar sistema de claim
- **`COMO_FAZER_CLAIM.md`** - Guia para usuários fazerem claim

**Quando usar:** Para fazer deploy de contratos ou configurar funcionalidades.

---

### **Verificação de Contratos** (`docs/verification/`)

Como verificar contratos no Etherscan/Sourcify:

- **`CONTRATO_VERIFICADO_SUCESSO.md`** - Status da verificação (Sepolia)
- **`SOURCIFY_PASSO_A_PASSO.md`** - Guia passo a passo do Sourcify

**Quando usar:** Após fazer deploy, para verificar contratos publicamente.

---

### **Informações do Token** (`docs/token-info/`)

Como atualizar informações do token em diferentes plataformas:

- **`ALTERNATIVAS_SEM_LOGIN_ETHERSCAN.md`** - Alternativas quando login Etherscan está indisponível
- **`COMO_ADICIONAR_GECKOTERMINAL.md`** - Como adicionar token no GeckoTerminal
- **`COMO_ATUALIZAR_DEBANK.md`** - Como atualizar no DeBank
- **`COMO_ATUALIZAR_UNISWAP.md`** - Como funciona na Uniswap
- **`O_QUE_E_OPENZEPPELIN_BUILDER.md`** - Explicação sobre OpenZeppelin Builder

**Quando usar:** Para atualizar logo, nome, descrição do token em diferentes plataformas.

---

### **Migração para Mainnet** (`docs/migration/`)

**⭐ IMPORTANTE:** Próximo passo principal!

- **`MIGRACAO_MAINNET.md`** - Guia completo de migração Sepolia → Mainnet

**Quando usar:** Quando estiver pronto para fazer deploy na rede principal.

---

## 📊 Status Atual

### ✅ **Concluído (Sepolia Testnet):**

- ✅ Token deployado: `0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87`
- ✅ Contrato verificado no Sourcify
- ✅ Logo hospedado no IPFS
- ✅ Metadados prontos
- ⏳ Informações do token aguardando atualização no Etherscan (login indisponível)

### 🎯 **Próximo Passo:**

**MIGRAÇÃO PARA MAINNET** - Veja: [`docs/migration/MIGRACAO_MAINNET.md`](./docs/migration/MIGRACAO_MAINNET.md)

---

## 🔗 Links Úteis

### **Sepolia Testnet (Atual):**
- **Token:** https://sepolia.etherscan.io/token/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
- **Contrato:** https://sepolia.etherscan.io/address/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
- **Sourcify:** https://repo.sourcify.dev/11155111/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87

### **Mainnet (Após Migração):**
- **Token:** https://etherscan.io/token/[ENDERECO]
- **Contrato:** https://etherscan.io/address/[ENDERECO]
- **Uniswap:** https://app.uniswap.org/
- **GeckoTerminal:** https://www.geckoterminal.com/ethereum/pools/

---

## 📝 Informações do Token

```
Nome: NeoFlowOFF
Símbolo: NEOFLW
Decimals: 18
Total Supply: 1,000,000,000 NEOFLW
Logo: https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i
Website: neoflowoff.eth
Descrição: Token oficial do protocolo NEOFLW - um protocolo modular DAO focado em governança descentralizada e crescimento sustentável.
```

---

## 🗂️ Arquivos Importantes

### **Configuração:**
- `ape-config.yaml` - Configuração do Ape Framework
- `.env` - Variáveis de ambiente (API keys, etc)
- `package.json` - Scripts npm disponíveis

### **Contratos:**
- `contracts/NeoFlowToken.sol` - Contrato principal do token
- `contracts/StakingVault.sol` - Contrato de staking
- `contracts/NeoFlowClaim.sol` - Contrato de claim

### **Scripts:**
- `scripts/deploy_token.py` - Deploy do token
- `scripts/update_token_automated.py` - Atualização automática de metadados

### **Metadados:**
- `metadata/token-metadata.json` - Metadados do token (ERC-20)
- `sourcify_standard_json.json` - JSON para verificação no Sourcify

---

## 🚀 Comandos Rápidos

### **Setup:**
```bash
npm run plugins      # Instalar plugins
npm run compile      # Compilar contratos
npm run test         # Executar testes
```

### **Deploy (Sepolia):**
```bash
ape run scripts/deploy_token.py --network ethereum:sepolia
```

### **Deploy (Mainnet):**
```bash
ape run scripts/deploy_token.py --network ethereum:mainnet
```

### **Verificação:**
```bash
# Via Sourcify (recomendado)
# Acesse: https://sourcify.dev/
```

---

## 📖 Como Usar Esta Documentação

1. **Primeira vez?** Comece por [`docs/setup/`](./docs/setup/)
2. **Fazer deploy?** Veja [`docs/deploy/DEPLOY_INSTRUCTIONS.md`](./docs/deploy/DEPLOY_INSTRUCTIONS.md)
3. **Verificar contrato?** Veja [`docs/verification/`](./docs/verification/)
4. **Migrar para mainnet?** Veja [`docs/migration/MIGRACAO_MAINNET.md`](./docs/migration/MIGRACAO_MAINNET.md) ⭐

---

## ✅ Checklist de Migração

- [ ] **Preparação:**
  - [ ] ETH suficiente na wallet (~0.1 ETH)
  - [ ] Wallet configurada e testada
  - [ ] APIs configuradas

- [ ] **Deploy:**
  - [ ] Compilar contratos
  - [ ] Fazer deploy na mainnet
  - [ ] Anotar endereço do contrato

- [ ] **Verificação:**
  - [ ] Verificar no Sourcify
  - [ ] Verificar no Etherscan

- [ ] **Atualização:**
  - [ ] Atualizar metadados no Etherscan
  - [ ] Adicionar em GeckoTerminal
  - [ ] Adicionar em CoinGecko
  - [ ] Preparar para Uniswap (liquidez)

---

**📖 Documentação completa organizada! Pronto para migração!** 🚀

