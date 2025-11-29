# 🚀 Deploy dos Contratos com ContractMetadata - Guia Completo

**Data:** 2025-01-XX  
**Objetivo:** Fazer novo deploy dos contratos com suporte a `ContractMetadata` para usar embed do thirdweb  
**Status:** ⚠️ **AÇÃO NECESSÁRIA**

---

## 📋 RESUMO RÁPIDO

### Wallet para Deploy
- **Label:** `neoflow-admin`
- **Endereço:** `0x460F9D0cf3e6E84faC1A7Abc524ddfa66fb64f60`
- **Network:** Polygon Mainnet (Chain ID: 137)

### Custos Estimados
- **Token:** ~$0.50-1.00 POL
- **Vault:** ~$0.50-1.00 POL  
- **Claim:** ~$0.50-1.00 POL
- **Total:** ~$1.50-3.00 POL (~$1-2 USD)

### ⚠️ IMPORTANTE
- **Novos endereços serão gerados** (diferentes dos atuais)
- **Atualizar frontend** com novos endereços
- **Transferir tokens** do contrato antigo para o novo (se necessário)

---

## ✅ PRÉ-REQUISITOS

### 1. Verificar Saldo de POL na Wallet

```bash
# Verificar saldo no Polygonscan
# https://polygonscan.com/address/0x460F9D0cf3e6E84faC1A7Abc524ddfa66fb64f60

# OU via Ape
ape accounts list
```

**Necessário:** Mínimo **5 POL** (recomendado **10 POL** para segurança)

**Se não tiver POL suficiente:**
1. Comprar em exchange (Binance, Coinbase, etc)
2. Fazer bridge: https://portal.polygon.technology/polygon/bridge
3. Transferir para: `0x460F9D0cf3e6E84faC1A7Abc524ddfa66fb64f60`

### 2. Compilar Contratos Atualizados

```bash
cd /Users/nettomello/CODIGOS/TOKENS/neoflw-token
npm run compile
```

**Verificar:**
- ✅ Sem erros de compilação
- ✅ Contratos `NeoFlowToken`, `StakingVault`, `NeoFlowClaim` compilados
- ✅ Arquivos `.json` gerados em `build/`

---

## 🚀 PROCESSO DE DEPLOY (Ordem de Execução)

### **PASSO 1: Deploy do Token (Primeiro)**

```bash
ape run scripts/deploy/deploy_token --network polygon:mainnet
```

**O que acontece:**
- Deploy do `NeoFlowToken` com `ContractMetadata`
- Mint de 1 bilhão de tokens para a wallet `neoflow-admin`
- Salva endereço em `.token_address.txt`

**Após deploy:**
1. **Anotar o novo endereço do Token** (será exibido no terminal)
2. **Verificar no Polygonscan:**
   ```
   https://polygonscan.com/address/[NOVO_ENDERECO_TOKEN]
   ```

**Exemplo de saída:**
```
✅ NEOFLW Token deployed at: 0x[NOVO_ENDERECO]
🔗 Ver no Explorer:
   https://polygonscan.com/address/0x[NOVO_ENDERECO]
```

---

### **PASSO 2: Deploy do StakingVault**

```bash
ape run scripts/deploy/deploy_vault --network polygon:mainnet
```

**O que acontece:**
- Deploy do `StakingVault` usando o novo endereço do token
- Salva endereço em `.vault_address.txt`

**Após deploy:**
1. **Anotar o novo endereço do Vault**
2. **Verificar no Polygonscan**

---

### **PASSO 3: Deploy do NeoFlowClaim**

```bash
ape run scripts/deploy/deploy_claim --network polygon:mainnet
```

**O que acontece:**
- Deploy do `NeoFlowClaim` usando o novo endereço do token
- Salva endereço em `.claim_address.txt`

**Após deploy:**
1. **Anotar o novo endereço do Claim**
2. **Verificar no Polygonscan**

---

## 📝 ATUALIZAR CONFIGURAÇÕES

### 1. Atualizar `.env` (Raiz do Projeto)

```env
# Adicionar/atualizar com novos endereços
TOKEN_ADDRESS=0x[NOVO_ENDERECO_TOKEN]
VAULT_ADDRESS=0x[NOVO_ENDERECO_VAULT]
CLAIM_ADDRESS=0x[NOVO_ENDERECO_CLAIM]
```

### 2. Atualizar `frontend/.env`

```env
NEXT_PUBLIC_TOKEN_ADDRESS=0x[NOVO_ENDERECO_TOKEN]
NEXT_PUBLIC_VAULT_ADDRESS=0x[NOVO_ENDERECO_VAULT]
NEXT_PUBLIC_CLAIM_ADDRESS=0x[NOVO_ENDERECO_CLAIM]
```

### 3. Configurar ContractURI (Opcional - Para Embed Thirdweb)

Após deploy, você pode configurar a URI de metadata:

```python
# Via console Python ou script
from ape import accounts, project

acct = accounts.load("neoflow-admin")
token = project.NeoFlowToken.at("0x[NOVO_ENDERECO_TOKEN]")

# Definir contractURI (exemplo com IPFS)
contract_uri = "https://gateway.ipfs.io/ipfs/QmSeuHashAqui/metadata.json"
token.setContractURI(contract_uri, sender=acct)
```

**Formato do metadata.json:**
```json
{
  "name": "NEOFlowOFF",
  "description": "Token NEOFLW - Protocolo de Gamificação",
  "image": "https://gateway.ipfs.io/ipfs/QmSeuHashAqui/logo.png",
  "external_link": "https://neoflow.com",
  "seller_fee_basis_points": 0,
  "fee_recipient": "0x0000000000000000000000000000000000000000"
}
```

---

## 🔄 MIGRAÇÃO DE DADOS (Se Necessário)

### Se você tinha tokens no contrato antigo:

1. **Verificar saldo no contrato antigo:**
   ```python
   old_token = project.NeoFlowToken.at("0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2")
   balance = old_token.balanceOf("0x460F9D0cf3e6E84faC1A7Abc524ddfa66fb64f60")
   ```

2. **Transferir para novo contrato (se aplicável):**
   - Os tokens já estão na wallet `neoflow-admin` (foram mintados no novo deploy)
   - Se havia tokens em outros contratos (Vault, Claim), você precisará transferir manualmente

---

## ✅ CHECKLIST PÓS-DEPLOY

- [ ] Token deployado com sucesso
- [ ] Vault deployado com sucesso
- [ ] Claim deployado com sucesso
- [ ] Endereços anotados e salvos
- [ ] `.env` atualizado (raiz e frontend)
- [ ] Contratos verificados no Polygonscan
- [ ] ContractURI configurado (opcional)
- [ ] Frontend testado com novos endereços
- [ ] Embed thirdweb funcionando

---

## 🐛 TROUBLESHOOTING

### Erro: "Insufficient funds"
- **Solução:** Adicionar mais POL na wallet `neoflow-admin`

### Erro: "Contract compilation failed"
- **Solução:** 
  ```bash
  npm run compile
  # Verificar erros e corrigir
  ```

### Erro: "Token address required" (no deploy do Vault/Claim)
- **Solução:** Verificar se `.token_address.txt` existe e tem o endereço correto

### Embed thirdweb não funciona
- **Solução:** 
  1. Verificar se `contractURI()` retorna uma URI válida
  2. Verificar se o JSON de metadata está acessível
  3. Verificar se o contrato está importado no dashboard thirdweb

---

## 📚 RECURSOS ÚTEIS

- **Polygonscan:** https://polygonscan.com
- **Thirdweb Dashboard:** https://thirdweb.com/dashboard
- **Polygon Bridge:** https://portal.polygon.technology/polygon/bridge
- **IPFS Gateway:** https://gateway.ipfs.io

---

## 🎯 PRÓXIMOS PASSOS

1. ✅ Fazer deploy dos contratos atualizados
2. ✅ Configurar ContractURI
3. ✅ Testar embed thirdweb
4. ✅ Atualizar documentação com novos endereços
5. ✅ Notificar usuários sobre novos endereços (se aplicável)

---

**Última atualização:** 2025-01-XX

