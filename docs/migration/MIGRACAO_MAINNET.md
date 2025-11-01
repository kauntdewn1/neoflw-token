# 🚀 Guia de Migração: Sepolia Testnet → Ethereum Mainnet

## 📋 Resumo

Este guia completa o processo de migração do token NEOFLW de Sepolia Testnet para Ethereum Mainnet.

---

## ✅ Pré-requisitos

### 1. **ETH na Mainnet**

Você precisa de ETH real na wallet para pagar gas fees:

- **Estimativa de custo:** ~0.05 - 0.1 ETH ($100-200 USD, dependendo do preço do ETH)
- **Inclui:**
  - Deploy do contrato (~$20-50)
  - Verificação no Etherscan (grátis)
  - Atualização de metadados (grátis)
  - Buffer para segurança

**Como obter ETH:**
- Comprar em exchange (Coinbase, Binance, etc)
- Transferir para sua wallet `neoflow-admin`

### 2. **API Keys Configuradas**

✅ **Alchemy API Key:** Já configurada (mesma funciona para mainnet)
✅ **Etherscan API Key:** Já configurada (mesma funciona para mainnet)

### 3. **Wallet Preparada**

- ✅ Wallet `neoflow-admin` importada no Ape
- ✅ Wallet conectada na rede Ethereum Mainnet
- ✅ ETH disponível na wallet

### 4. **Contratos Validados**

- ✅ Contratos testados em Sepolia
- ✅ Contratos verificados no Etherscan (Sepolia)
- ✅ Tudo funcionando corretamente

---

## 🔧 Configuração Inicial

### **1. Verificar Configurações**

O arquivo `ape-config.yaml` já está configurado com mainnet:

```yaml
networks:
  ethereum:
    mainnet:
      default_provider: alchemy
      providers:
        alchemy:
          api_key: ${ALCHEMY_API_KEY}
```

### **2. Verificar Wallet**

```bash
# Verificar se wallet está importada
ape accounts list

# Deve mostrar: neoflow-admin
```

### **3. Verificar Saldo**

```bash
# Verificar saldo ETH na mainnet
ape accounts show neoflow-admin --network ethereum:mainnet
```

---

## 🚀 Passo a Passo: Deploy na Mainnet

### **Passo 1: Compilar Contratos**

```bash
npm run compile
```

Ou:

```bash
ape compile
```

**Verificar:** Deve compilar sem erros.

---

### **Passo 2: Verificar Saldo de ETH**

```bash
# Ver saldo na wallet
ape accounts show neoflow-admin --network ethereum:mainnet
```

**Requisito mínimo:** 0.05 ETH (~$100-200 USD)

---

### **Passo 3: Deploy do Token**

```bash
ape run scripts/deploy_token.py --network ethereum:mainnet
```

**O que acontece:**
1. ✅ Carrega wallet `neoflow-admin`
2. ✅ Faz deploy do contrato `NeoFlowToken`
3. ✅ Mint de 1 bilhão de tokens
4. ✅ Salva endereço em `.token_address.txt`

**Output esperado:**
```
🚀 Deploying NeoFlowToken...
📊 From: 0x...
💰 Initial Supply: 1,000,000,000 NEOFLW

✅ NEOFLW Token deployed at: 0x[ENDERECO]
🔗 Ver no Etherscan:
   https://etherscan.io/address/0x[ENDERECO]
```

---

### **Passo 4: Anotar Endereço**

**IMPORTANTE:** Copie o endereço do contrato deployado!

```
Token Address: 0x[ENDERECO]
```

Este endereço será usado para:
- Verificação no Etherscan
- Verificação no Sourcify
- Atualização de metadados
- Integração com outras plataformas

---

### **Passo 5: Verificar no Etherscan**

1. **Acesse:** https://etherscan.io/address/[ENDERECO]
2. **Verifique:** Contrato aparece como "Contract"
3. **Aguarde:** Pode levar alguns minutos para aparecer

---

## 🔐 Verificação do Contrato

### **Método 1: Sourcify (Recomendado - Mais Fácil)**

1. **Acesse:** https://sourcify.dev/
2. **Selecione:** Ethereum Mainnet
3. **Cole o endereço** do contrato
4. **Faça upload do JSON:**
   - Use o arquivo: `sourcify_standard_json.json`
   - Ou gere novo: `ape compile --standard-json`
5. **Confirme** e aguarde verificação

**Vantagens:**
- ✅ Mais fácil que Etherscan
- ✅ Aceita Standard JSON Input
- ✅ Etherscan reconhece automaticamente

---

### **Método 2: Etherscan Direto**

1. **Acesse:** https://etherscan.io/address/[ENDERECO]
2. **Clique em:** "Contract" → "Verify and Publish"
3. **Selecione:**
   - Compiler: `0.8.30` (mesma versão do deploy)
   - Optimization: `Yes` (200 runs)
   - License: `MIT`
4. **Faça upload:** `sourcify_standard_json.json`
5. **Constructor Arguments:** 
   ```
   0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000
   ```
   (mesmo valor do testnet)

---

## 📝 Atualizar Informações do Token

### **1. Atualizar no Etherscan**

1. **Acesse:** https://etherscan.io/token/[ENDERECO]
2. **Faça login** no Etherscan (conecte wallet)
3. **Clique em:** "Update Token Info" ou "Edit Token"
4. **Preencha:**

   ```
   Token Logo: https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i
   Token Name: NeoFlowOFF
   Token Symbol: NEOFLW
   Decimals: 18
   Website: neoflowoff.eth
   Description: Token oficial do protocolo NEOFLW - um protocolo modular DAO focado em governança descentralizada e crescimento sustentável.
   ```

5. **Confirme** e aguarde

---

### **2. Adicionar em Outras Plataformas**

**GeckoTerminal:**
- Agora funcionará! Use o link correto:
  ```
  https://www.geckoterminal.com/ethereum/pools/[ENDERECO]
  ```

**CoinGecko:**
- https://www.coingecko.com/en/contact
- Formulário de adição de token

**Uniswap:**
- Aparecerá automaticamente quando você adicionar liquidez
- Acesse: https://app.uniswap.org/
- Adicione liquidez criando um par

**DeBank:**
- Detectará automaticamente quando você adicionar na MetaMask

---

## 📋 Informações para Atualizar

```
Endereço do Contrato: [ENDERECO_DEPLOYADO]
Rede: Ethereum Mainnet (Chain ID: 1)
Nome: NeoFlowOFF
Símbolo: NEOFLW
Decimals: 18
Total Supply: 1,000,000,000 NEOFLW
Logo: https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i
Website: neoflowoff.eth
Descrição: Token oficial do protocolo NEOFLW - um protocolo modular DAO focado em governança descentralizada e crescimento sustentável.
```

---

## ⚠️ Importante: Diferenças Mainnet vs Testnet

| Aspecto | Sepolia (Testnet) | Mainnet |
|---------|-------------------|---------|
| **ETH** | Grátis (faucets) | Custa dinheiro real |
| **Gas Fee** | Sem custo real | $10-100+ por transação |
| **Irreversível** | Pode redeployar | Permanente e imutável |
| **Risco** | Nenhum | Risco financeiro real |
| **Etherscan** | sepolia.etherscan.io | etherscan.io |
| **Suporte** | Limitado | Completo |

---

## 💰 Custos Estimados

### **Deploy:**
- **Token:** ~$20-50 USD
- **Vault (se deployar):** ~$30-60 USD
- **Claim (se deployar):** ~$30-60 USD

### **Total Estimado:**
- **Apenas Token:** ~$20-50 USD
- **Completo (Token + Vault + Claim):** ~$80-170 USD

**Nota:** Custos variam conforme preço do ETH e congestionamento da rede.

---

## ✅ Checklist Final

### **Antes do Deploy:**
- [ ] ETH suficiente na wallet (~0.1 ETH recomendado)
- [ ] Wallet `neoflow-admin` importada e funcionando
- [ ] Contratos compilados sem erros
- [ ] Testes passando (se houver)
- [ ] Backup da wallet feito

### **Durante o Deploy:**
- [ ] Executar deploy na mainnet
- [ ] Anotar endereço do contrato
- [ ] Verificar no Etherscan

### **Após o Deploy:**
- [ ] Verificar contrato no Sourcify/Etherscan
- [ ] Atualizar informações no Etherscan
- [ ] Adicionar em GeckoTerminal
- [ ] Adicionar em CoinGecko
- [ ] Preparar para adicionar liquidez no Uniswap
- [ ] Atualizar documentação com endereço mainnet

---

## 🔗 Links Úteis

- **Etherscan Mainnet:** https://etherscan.io/
- **Sourcify:** https://sourcify.dev/
- **GeckoTerminal:** https://www.geckoterminal.com/ethereum/pools/
- **Uniswap:** https://app.uniswap.org/
- **CoinGecko:** https://www.coingecko.com/
- **DeBank:** https://debank.com/

---

## 🚨 Troubleshooting

### **Erro: "Insufficient funds"**
- **Solução:** Adicione mais ETH na wallet
- **Requerido:** ~0.05-0.1 ETH mínimo

### **Erro: "Network not found"**
- **Solução:** Verifique `ape-config.yaml` tem configuração `mainnet`
- **Verificar:** `ape networks list` deve mostrar `ethereum:mainnet`

### **Erro: "Wallet not found"**
- **Solução:** Importe wallet novamente: `ape accounts import neoflow-admin`

### **Contrato não aparece no Etherscan**
- **Solução:** Aguarde alguns minutos (pode levar até 5-10 minutos)
- **Verificar:** Use o hash da transação para encontrar

---

## 📝 Próximos Passos Após Deploy

1. **Adicionar Liquidez (Uniswap):**
   - Criar par ETH/NEOFLW
   - Fornecer liquidez inicial

2. **Marketing:**
   - Anunciar lançamento
   - Compartilhar em redes sociais
   - Listar em agregadores

3. **Monitoramento:**
   - Monitorar transações
   - Acompanhar métricas
   - Responder comunidade

---

## 🎯 Resumo Rápido

```bash
# 1. Compilar
npm run compile

# 2. Verificar saldo ETH
ape accounts show neoflow-admin --network ethereum:mainnet

# 3. Deploy
ape run scripts/deploy_token.py --network ethereum:mainnet

# 4. Anotar endereço
# [ENDERECO_DEPLOYADO]

# 5. Verificar no Etherscan
# https://etherscan.io/address/[ENDERECO]

# 6. Verificar no Sourcify
# https://sourcify.dev/

# 7. Atualizar informações
# https://etherscan.io/token/[ENDERECO]
```

---

**Pronto para migrar!** 🚀

Lembre-se: Mainnet é permanente. Certifique-se de que tudo está correto antes de fazer deploy!

