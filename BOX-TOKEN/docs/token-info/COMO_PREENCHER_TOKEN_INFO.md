# 📝 Como Preencher Informações do Token no BSCScan

## 🌐 Rede: Binance Smart Chain (BSC) Mainnet

**⚠️ IMPORTANTE:** Este guia mostra como preencher todas as informações do token BOX no BSCScan.

- **Rede:** Binance Smart Chain (BSC) Mainnet
- **Token Address:** `0xBc972E10Df612C7d65054BC67aBCA96B3C22a017`

---

## 📋 Informações que Podem ser Atualizadas

No BSCScan, você pode atualizar:

- ✅ **Token Logo** (URL da imagem)
- ✅ **Token Name** (Nome do token)
- ✅ **Token Symbol** (Símbolo do token)
- ✅ **Decimals** (Número de decimais)
- ✅ **Website** (URL do website - opcional)
- ✅ **Description** (Descrição do token - opcional)

---

## 🎯 Passo a Passo

### **1. Acesse a Página do Token**

```
https://bscscan.com/token/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017
```

⚠️ **IMPORTANTE:** Use `/token/` e não `/address/`

---

### **2. Conecte sua Wallet**

1. **Faça login no BSCScan**
   - Clique em **"Connect to Web3"**
   - Conecte sua wallet (MetaMask, WalletConnect, etc)
   - Certifique-se de estar na **BSC Mainnet**

2. **Verifique a conexão:**
   - Deve aparecer seu endereço no canto superior direito

---

### **3. Encontre o Botão de Edição**

Procure por um dos seguintes:

- **"Update Token Info"**
- **"Edit Token"**
- **"Update"** (ao lado do nome)
- Ícone de lápis ✏️
- Menu **"⋮"** → **"Update Token Info"**

**Onde procurar:**
- Topo da página (próximo ao nome)
- Final da página (seção "Other Info")
- Menu lateral (se disponível)
- **"My Account"** → **"Token Management"**

---

### **4. Preencha o Formulário**

#### **Token Logo (URL):**

```
https://gateway.lighthouse.storage/ipfs/bafybeia34i4ey5a7hd7odmazmyts4m6dasnceqtqky5gozrqbqylevjg6e
```

**CID:** `bafybeia34i4ey5a7hd7odmazmyts4m6dasnceqtqky5gozrqbqylevjg6e`

**Requisitos:**
- ✅ URL deve começar com `https://`
- ✅ URL deve estar acessível (teste abrindo no navegador)
- ✅ Formato suportado: PNG, SVG, JPG
- ✅ Tamanho recomendado: 256x256 ou 512x512 pixels

**Exemplos de URLs válidas:**
```
https://gateway.pinata.cloud/ipfs/QmYourHashHere
https://ipfs.io/ipfs/QmYourHashHere
https://cloudflare-ipfs.com/ipfs/QmYourHashHere
```

#### **Token Name:**

```
BOX Token
```
(ou o nome real do seu token)

#### **Token Symbol:**

```
BOX
```
(ou o símbolo real do seu token)

#### **Decimals:**

```
18
```
(ou o número correto de decimais - geralmente 18 para tokens BEP-20)

#### **Website (Opcional):**

```
https://seuwebsite.com
```
ou deixe em branco se não tiver website

#### **Description (Opcional):**

```
Descrição do seu token aqui. Pode incluir informações sobre o projeto, uso do token, etc.
```

---

### **5. Verifique Antes de Enviar**

Antes de clicar em **"Submit"**, verifique:

- [ ] URL do logo está correta e acessível
- [ ] Nome está correto
- [ ] Símbolo está correto
- [ ] Decimals está correto (geralmente 18)
- [ ] Wallet está conectada
- [ ] Está na rede BSC Mainnet

---

### **6. Envie e Confirme**

1. **Clique em "Submit" ou "Enviar"**

2. **Confirme na sua wallet:**
   - Uma transação pode aparecer
   - ⚠️ **NÃO deve ter custo de gas** para atualizar informações
   - Se pedir gas, **CANCELE** e verifique

3. **Aguarde confirmação:**
   - Pode levar alguns segundos
   - Pode aparecer mensagem de sucesso

---

### **7. Verifique se Funcionou**

1. **Aguarde alguns minutos** (pode demorar)

2. **Atualize a página** (Ctrl+Shift+R ou Cmd+Shift+R)

3. **Verifique se as informações apareceram:**
   - Logo no topo da página
   - Nome e símbolo corretos
   - Descrição (se adicionou)

---

## 📝 Exemplo Completo de Preenchimento

```
Token Logo (URL):
https://gateway.lighthouse.storage/ipfs/bafybeia34i4ey5a7hd7odmazmyts4m6dasnceqtqky5gozrqbqylevjg6e

Token Name:
BOX Token

Token Symbol:
BOX

Decimals:
18

Website:
[SEU_WEBSITE_AQUI]

Description:
[SUA_DESCRICAO_AQUI]
```

**Logo CID:** `bafybeia34i4ey5a7hd7odmazmyts4m6dasnceqtqky5gozrqbqylevjg6e`

---

## 🔧 Troubleshooting

### **Problema 1: Botão não aparece**

**Soluções:**
- ✅ Certifique-se de estar **logado**
- ✅ Use a **mesma wallet** que fez o deploy
- ✅ Verifique se está na página `/token/` e não `/address/`
- ✅ Role a página até o final
- ✅ Procure no menu **"More"** ou **"⋮"**

### **Problema 2: Logo não aparece**

**Soluções:**
- ✅ Aguarde alguns minutos (pode demorar)
- ✅ Limpe cache do navegador
- ✅ Verifique se a URL está acessível (abra no navegador)
- ✅ Certifique-se de que a URL começa com `https://`

### **Problema 3: Transação pede gas**

**Isso NÃO deveria acontecer!**

**Solução:**
1. **CANCELE a transação**
2. Verifique se está na página correta (`/token/`)
3. Verifique se está atualizando **"Token Info"** e não algo do contrato

---

## 🔗 Links Úteis

- **Token no BSCScan:** https://bscscan.com/token/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017
- **BSCScan My Account:** https://bscscan.com/myaccount
- **Serviços IPFS:**
  - Pinata: https://pinata.cloud/
  - NFT.Storage: https://nft.storage/
  - Lighthouse: https://lighthouse.storage/

---

## ✅ Checklist Final

- [ ] Página do token acessada (`/token/`)
- [ ] Wallet conectada
- [ ] Botão "Update Token Info" encontrado
- [ ] Logo URL preparada e testada
- [ ] Todos os campos preenchidos
- [ ] Informações verificadas antes de enviar
- [ ] Formulário enviado
- [ ] Informações apareceram na página

---

**Boa sorte preenchendo as informações do token!** 🚀

