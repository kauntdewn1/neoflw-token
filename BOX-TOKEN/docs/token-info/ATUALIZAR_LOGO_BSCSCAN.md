# 🖼️ Como Atualizar Logo do Token no BSCScan

## 🌐 Rede: Binance Smart Chain (BSC) Mainnet

**⚠️ IMPORTANTE:** Este token está deployado na **BSC Mainnet**.

- **Rede:** Binance Smart Chain (BSC) Mainnet
- **Chain ID:** 56
- **Explorer:** https://bscscan.com
- **Token Address:** `0xBc972E10Df612C7d65054BC67aBCA96B3C22a017`

---

## ⚠️ BSCScan NÃO Possui API Pública para Atualizar Logo

### **Limitação do BSCScan (Similar ao Etherscan):**

Mesmo usando **APIs** ou **scripts**, você **ainda precisa fazer manualmente** porque:

- ❌ **BSCScan NÃO possui API pública** para atualizar logo/avatar de tokens
- ❌ **Processo manual** é a única forma disponível
- ✅ **A única forma** é através da interface web do BSCScan

**Isso é uma limitação do próprio BSCScan**, não das ferramentas!

---

## 🎯 Método: Atualização Manual no BSCScan

### **Passo a Passo Detalhado:**

#### **PASSO 1: Acessar a Página Correta**

⚠️ **IMPORTANTE:** Acesse a página do **TOKEN**, não do contrato!

**URL Correta:**
```
https://bscscan.com/token/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017
```

❌ **NÃO use:**
```
https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017
```

**Diferença:**
- `/token/` → Página do token (tem opção de atualizar)
- `/address/` → Página do contrato (não tem opção de atualizar)

---

#### **PASSO 2: Conectar Wallet**

1. **No BSCScan**, procure por:
   - Botão **"Connect to Web3"** (canto superior direito)
   - Ou ícone de perfil/login
   - Ou menu **"My Account"**

2. **Clique em conectar:**
   - Escolha sua wallet (MetaMask, WalletConnect, etc)
   - **Certifique-se de estar na rede BSC Mainnet**
   - Confirme a conexão na sua wallet
   - Autorize o BSCScan

3. **Verifique se conectou:**
   - Deve aparecer seu endereço no canto superior direito
   - Ou deve aparecer **"Connected"** ou similar

---

#### **PASSO 3: Verificar Rede**

1. **No MetaMask**, deve aparecer **"BSC Mainnet"** no topo
2. **Se não estiver na BSC Mainnet**, mude:
   - Clique no nome da rede (topo do MetaMask)
   - Selecione **"BSC Mainnet"**
   - Se não aparecer, adicione:
     ```
     Network Name: BSC Mainnet
     RPC URL: https://bsc-dataseed.binance.org/
     Chain ID: 56
     Currency Symbol: BNB
     Block Explorer: https://bscscan.com
     ```

---

#### **PASSO 4: Encontrar o Botão de Atualização**

O botão pode estar em **diferentes lugares**. Procure por:

**Localização 1: Topo da Página (Próximo ao Nome)**
- Procure ao lado do nome do token
- Pode ser um botão **"Update"** ou **"Edit"**
- Ou um ícone de lápis ✏️

**Localização 2: Menu "More" ou "⋮"**
- Botão com três pontos **"⋮"** ou **"More"**
- Menu dropdown com **"Update Token Info"**

**Localização 3: Seção "Other Info"**
- Role a página até o final
- Procure na seção **"Other Info"** ou **"Token Info"**
- Botão **"Update Token Info"** ou **"Edit Token"**

**Localização 4: Via "My Account"**
1. Clique em seu endereço/perfil (canto superior direito)
2. Procure por **"Token Management"** ou **"My Tokens"**
3. Selecione seu token na lista
4. Clique em **"Update"** ou **"Edit"**

---

#### **PASSO 5: Se NÃO Encontrar o Botão**

**Possíveis motivos:**
- ⚠️ Você precisa fazer login primeiro
- ⚠️ O serviço de login está temporariamente indisponível
- ⚠️ A interface mudou

**Soluções:**
- ✅ Tente fazer login primeiro
- ✅ Aguarde algumas horas se o login estiver indisponível
- ✅ Limpe o cache do navegador
- ✅ Tente outro navegador ou modo anônimo
- ✅ Verifique se está na rede correta (BSC Mainnet)

---

#### **PASSO 6: Preparar o Logo**

Antes de atualizar, você precisa:

1. **Ter o logo em formato adequado:**
   - Formato: PNG, SVG, ou JPG
   - Tamanho recomendado: 256x256 ou 512x512 pixels
   - Tamanho do arquivo: máximo 1MB (geralmente)

2. **Fazer upload para IPFS ou servidor público:**
   - Use um serviço como **Pinata**, **NFT.Storage**, **Lighthouse**, etc
   - Obtenha a URL pública do logo
   - Exemplo: `https://gateway.pinata.cloud/ipfs/Qm...`

3. **Teste a URL:**
   - Abra a URL no navegador
   - Certifique-se de que a imagem aparece corretamente

---

#### **PASSO 7: Preencher o Formulário**

Quando encontrar o formulário, preencha:

**Campo: Token Logo (URL)**
```
https://gateway.lighthouse.storage/ipfs/bafybeia34i4ey5a7hd7odmazmyts4m6dasnceqtqky5gozrqbqylevjg6e
```

**CID do Logo:**
```
bafybeia34i4ey5a7hd7odmazmyts4m6dasnceqtqky5gozrqbqylevjg6e
```

**URLs Alternativas (se necessário):**
```
https://ipfs.io/ipfs/bafybeia34i4ey5a7hd7odmazmyts4m6dasnceqtqky5gozrqbqylevjg6e
https://cloudflare-ipfs.com/ipfs/bafybeia34i4ey5a7hd7odmazmyts4m6dasnceqtqky5gozrqbqylevjg6e
```

⚠️ **IMPORTANTE:**
- URL deve começar com `https://`
- URL deve estar acessível (teste abrindo no navegador)
- Formato de imagem deve ser suportado (PNG, SVG, JPG)

**Campo: Token Name**
```
[COLE_AQUI_O_NOME_DO_TOKEN]
```

**Campo: Token Symbol**
```
[COLE_AQUI_O_SIMBOLO_DO_TOKEN]
```

**Campo: Decimals**
```
18
```
(ou o número correto de decimais do seu token)

**Campo: Website (Opcional)**
```
[COLE_AQUI_O_WEBSITE]
```

**Campo: Description (Opcional)**
```
[COLE_AQUI_A_DESCRICAO_DO_TOKEN]
```

---

#### **PASSO 8: Verificar Antes de Enviar**

Antes de clicar em **"Submit"** ou **"Enviar"**, verifique:

- [ ] URL do logo está correta e acessível
- [ ] Nome está correto
- [ ] Símbolo está correto
- [ ] Decimals está correto
- [ ] Wallet está conectada
- [ ] Está na rede BSC Mainnet (não testnet)

---

#### **PASSO 9: Enviar e Confirmar**

1. **Clique em "Submit" ou "Enviar"**

2. **Confirme na sua wallet:**
   - Uma transação pode aparecer no MetaMask
   - ⚠️ **NÃO deve ter custo de gas** para atualizar informações
   - Se pedir gas, **CANCELE** e verifique se está no lugar certo

3. **Aguarde confirmação:**
   - Pode levar alguns segundos
   - Pode aparecer mensagem de sucesso

---

#### **PASSO 10: Verificar Se Funcionou**

1. **Aguarde alguns minutos** (pode demorar para aparecer)

2. **Atualize a página** (Ctrl+Shift+R ou Cmd+Shift+R)

3. **Verifique se o logo apareceu:**
   - No topo da página do token
   - Ao lado do nome/símbolo
   - Na seção de informações

4. **Se não apareceu:**
   - Aguarde mais alguns minutos
   - Limpe cache do navegador
   - Verifique se a URL do logo está acessível

---

## 🔧 Troubleshooting

### **Problema 1: "Account Login service is temporarily unavailable"**

**Solução:**
- ✅ Aguarde algumas horas
- ✅ Tente limpar cache do navegador
- ✅ Use outro navegador
- ✅ Tente modo anônimo
- ✅ Verifique se está na rede correta (BSC Mainnet)

### **Problema 2: Botão "Update Token Info" não aparece**

**Solução:**
- ✅ Certifique-se de estar **logado**
- ✅ Use a **mesma wallet** que fez o deploy
- ✅ Verifique se está na **página do token** (`/token/`) e não do contrato (`/address/`)
- ✅ Role a página até o final
- ✅ Procure no menu **"More"** ou **"⋮"**

### **Problema 3: Logo não aparece após atualizar**

**Solução:**
- ✅ Aguarde alguns minutos (pode demorar)
- ✅ Limpe o cache do navegador (Ctrl+Shift+R ou Cmd+Shift+R)
- ✅ Verifique se a URL do logo está acessível (abra no navegador)
- ✅ Certifique-se de que a URL começa com `https://`

### **Problema 4: Transação pede gas fee**

**Isso NÃO deveria acontecer!**

**Solução:**
1. **CANCELE a transação**
2. Verifique se está na página correta (`/token/`)
3. Verifique se está atualizando **"Token Info"** e não algo do contrato
4. Se persistir, pode ser bug do BSCScan - tente mais tarde

**Nota:** Atualizar informações do token **não deve custar gas.

---

## 📝 Informações para Copiar e Colar

### **URL Completa do Logo:**
```
[SUBSTITUA_PELA_URL_DO_SEU_LOGO]
```

### **Informações Completas:**
```
Token Address: 0xBc972E10Df612C7d65054BC67aBCA96B3C22a017
Token Name: [NOME_DO_TOKEN]
Token Symbol: [SIMBOLO_DO_TOKEN]
Decimals: [NUMERO_DE_DECIMAIS]
Token Logo: [URL_DO_LOGO]
Website: [WEBSITE_OPCIONAL]
Description: [DESCRICAO_OPCIONAL]
```

---

## 🎯 Resumo Rápido

1. ✅ Acesse: https://bscscan.com/token/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017
2. ✅ Conecte sua wallet (BSC Mainnet)
3. ✅ Procure **"Update Token Info"** (vários lugares possíveis)
4. ✅ Cole a URL do logo IPFS
5. ✅ Preencha outros campos
6. ✅ Envie e confirme
7. ✅ Aguarde alguns minutos
8. ✅ Verifique se apareceu

---

## 🔗 Links Úteis

- **Token no BSCScan:** https://bscscan.com/token/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017
- **BSCScan My Account:** https://bscscan.com/myaccount
- **Serviços IPFS:**
  - Pinata: https://pinata.cloud/
  - NFT.Storage: https://nft.storage/
  - Lighthouse: https://lighthouse.storage/

---

## 💡 Dicas Finais

1. **Seja paciente** - Pode levar tempo para aparecer
2. **Tente diferentes horários** - Servidor pode estar menos carregado
3. **Teste a URL do logo** - Antes de enviar, abra no navegador
4. **Guarde screenshot** - Caso precise mostrar o problema
5. **Use BNB para gas** - Se necessário (mas não deveria pedir)

---

**Boa sorte atualizando a imagem!** 🚀

