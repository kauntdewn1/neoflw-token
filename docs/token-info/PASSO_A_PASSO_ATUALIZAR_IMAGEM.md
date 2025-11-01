# 🖼️ Passo a Passo: Atualizar Imagem do Token no Etherscan

## 🎯 Objetivo

Atualizar a imagem/logo do token **NEOFLW** no Etherscan Sepolia usando a interface web.

---

## ✅ Checklist Pré-requisitos

Antes de começar, verifique:

- [ ] **Wallet conectada** (MetaMask, WalletConnect, etc)
- [ ] **Wallet na rede Sepolia** (não mainnet)
- [ ] **Mesma wallet que fez o deploy** do contrato
- [ ] **ETH de teste** na wallet (para transações, se necessário)
- [ ] **URL do logo acessível** (IPFS funcionando)

---

## 📋 Informações do Token

```
Endereço: 0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
Rede: Ethereum Sepolia (Testnet)
Chain ID: 11155111
Logo URL: https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i
Nome: NeoFlowOFF
Símbolo: NEOFLW
Decimals: 18
```

---

## 🚀 Passo a Passo Detalhado

### **PASSO 1: Acessar a Página Correta**

⚠️ **IMPORTANTE:** Acesse a página do **TOKEN**, não do contrato!

**URL Correta:**
```
https://sepolia.etherscan.io/token/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
```

❌ **NÃO use:**
```
https://sepolia.etherscan.io/address/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
```

**Diferença:**
- `/token/` → Página do token (tem opção de atualizar)
- `/address/` → Página do contrato (não tem opção de atualizar)

---

### **PASSO 2: Verificar Conexão da Wallet**

1. **Verifique se está na rede Sepolia:**
   - No MetaMask, deve aparecer "Sepolia" no topo
   - Se aparecer "Ethereum Mainnet", **mude para Sepolia**

2. **Como mudar para Sepolia no MetaMask:**
   - Clique no nome da rede (topo do MetaMask)
   - Selecione "Sepolia test network"
   - Se não aparecer, adicione:
     ```
     Network Name: Sepolia
     RPC URL: https://rpc.sepolia.org
     Chain ID: 11155111
     Currency Symbol: ETH
     Block Explorer: https://sepolia.etherscan.io
     ```

---

### **PASSO 3: Conectar Wallet no Etherscan**

1. **No Etherscan Sepolia**, procure por:
   - Botão "Connect to Web3" (canto superior direito)
   - Ou ícone de perfil/login
   - Ou menu "My Account"

2. **Clique em conectar:**
   - Escolha sua wallet (MetaMask, WalletConnect, etc)
   - Confirme a conexão na sua wallet
   - Autorize o Etherscan

3. **Verifique se conectou:**
   - Deve aparecer seu endereço no canto superior direito
   - Ou deve aparecer "Connected" ou similar

---

### **PASSO 4: Encontrar o Botão de Atualização**

O botão pode estar em **diferentes lugares**. Procure por:

#### **Localização 1: Topo da Página (Próximo ao Nome)**
- Procure ao lado do nome "NeoFlowOFF" ou símbolo "NEOFLW"
- Pode ser um botão "Update" ou "Edit"
- Ou um ícone de lápis ✏️

#### **Localização 2: Menu "More" ou "⋮"**
- Botão com três pontos "⋮" ou "More"
- Menu dropdown com "Update Token Info"

#### **Localização 3: Seção "Other Info"**
- Role a página até o final
- Procure na seção "Other Info" ou "Token Info"
- Botão "Update Token Info" ou "Edit Token"

#### **Localização 4: Via "My Account"**
1. Clique em seu endereço/perfil (canto superior direito)
2. Procure por "Token Management" ou "My Tokens"
3. Selecione seu token na lista
4. Clique em "Update" ou "Edit"

#### **Localização 5: Se o Token Já Existe**
Se o token já tem informações básicas:
- Procure por um badge/link "Token Information"
- Ou "View Token Information"
- Dentro, deve ter opção de editar

---

### **PASSO 5: Se NÃO Encontrar o Botão**

#### **Solução A: Verificar Se é Owner**
1. Certifique-se que sua wallet conectada é a mesma do deploy
2. Verifique no contrato se você é owner:
   - Acesse: https://sepolia.etherscan.io/address/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87#readContract
   - Procure função `owner()` ou `getOwner()`
   - Veja se retorna seu endereço

#### **Solução B: Tentar Diferentes Navegadores**
- Tente Chrome/Edge
- Tente Firefox
- Tente modo anônimo
- Limpe cache e cookies

#### **Solução C: Aguardar Login Ficar Disponível**
Se aparecer "Account Login service is temporarily unavailable":
- Aguarde algumas horas
- Tente novamente mais tarde
- O serviço pode estar em manutenção

#### **Solução D: Verificar Se Token Foi Reconhecido**
1. O Etherscan pode não ter reconhecido ainda como ERC-20
2. Aguarde algumas horas após deploy
3. Verifique se o contrato tem funções `name()` e `symbol()`

---

### **PASSO 6: Preencher o Formulário**

Quando encontrar o formulário, preencha:

#### **Campo: Token Logo (URL)**
```
https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i
```

⚠️ **IMPORTANTE:**
- URL deve começar com `https://`
- URL deve estar acessível (teste abrindo no navegador)
- Formato de imagem deve ser suportado (PNG, SVG, JPG)

#### **Campo: Token Name**
```
NeoFlowOFF
```

#### **Campo: Token Symbol**
```
NEOFLW
```

#### **Campo: Decimals**
```
18
```

#### **Campo: Website (Opcional)**
```
neoflowoff.eth
```
ou
```
https://neoflowoff.eth
```

#### **Campo: Description (Opcional)**
```
Token oficial do protocolo NEOFLW - um protocolo modular DAO focado em governança descentralizada e crescimento sustentável.
```

---

### **PASSO 7: Verificar Antes de Enviar**

Antes de clicar em "Submit" ou "Enviar", verifique:

- [ ] URL do logo está correta e acessível
- [ ] Nome está correto (NeoFlowOFF)
- [ ] Símbolo está correto (NEOFLW)
- [ ] Decimals está correto (18)
- [ ] Wallet está conectada
- [ ] Está na rede Sepolia (não mainnet)

---

### **PASSO 8: Enviar e Confirmar**

1. **Clique em "Submit" ou "Enviar"**

2. **Confirme na sua wallet:**
   - Uma transação pode aparecer no MetaMask
   - ⚠️ **NÃO deve ter custo de gas** para atualizar informações
   - Se pedir gas, **CANCELE** e verifique se está no lugar certo

3. **Aguarde confirmação:**
   - Pode levar alguns segundos
   - Pode aparecer mensagem de sucesso

---

### **PASSO 9: Verificar Se Funcionou**

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

## 🔧 Troubleshooting Específico

### **Problema 1: "Account Login service is temporarily unavailable"**

⚠️ **Este é o erro mais comum atualmente!**

**Você verá esta mensagem:**
```
"Sorry, the Account Login service is temporarily unavailable. 
Please try again later."
```

**Soluções Imediatas:**

1. **Use Blockscout (Funciona Agora!):**
   - Acesse: https://eth-sepolia.blockscout.com/address/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
   - Blockscout não depende do login do Etherscan
   - Pode atualizar logo mesmo quando Etherscan está offline
   - Interface similar, funciona da mesma forma

2. **Aguarde e Tente Novamente:**
   - Aguarde 2-4 horas (geralmente volta rápido)
   - Tente em horários diferentes (madrugada menos carregado)
   - Este erro é temporário e comum no Etherscan

3. **Outras Alternativas:**
   - Limpe cache do navegador (Ctrl+Shift+Del)
   - Tente outro navegador (Chrome, Firefox, Edge)
   - Tente modo anônimo
   - Verifique: https://status.sepolia.org (se disponível)

4. **Enquanto Aguarda:**
   - Use Blockscout para visualizar/atualizar logo
   - Use Otterscan como alternativa
   - O logo funcionará em qualquer explorer que suporte

---

### **Problema 2: Botão "Update Token Info" não aparece**

**Verificações:**
1. ✅ Está na página `/token/` e não `/address/`?
2. ✅ Wallet está conectada?
3. ✅ Está na rede Sepolia?
4. ✅ É a mesma wallet que fez o deploy?
5. ✅ Já fez login no Etherscan?

**Soluções:**
- Role a página completamente (pode estar no final)
- Procure no menu "More" ou "⋮"
- Tente via "My Account" → "Token Management"
- Aguarde algumas horas (pode ser problema temporário)
- Verifique se o contrato está verificado

---

### **Problema 3: Logo não carrega após atualizar**

**Verificações:**
1. **Teste a URL do logo diretamente:**
   ```
   https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i
   ```
   - Deve abrir a imagem no navegador
   - Se não abrir, o gateway pode estar offline

2. **Tente gateway alternativo:**
   - Use: `https://ipfs.io/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i`
   - Ou: `https://cloudflare-ipfs.com/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i`

3. **Aguarde mais tempo:**
   - Pode levar até 24 horas para aparecer
   - Etherscan faz cache de imagens

4. **Limpe cache:**
   - Limpe cache do navegador (Ctrl+Shift+Del)
   - Ou abra em modo anônimo

---

### **Problema 4: Transação pede gas fee**

**Isso NÃO deveria acontecer!**

**Solução:**
1. **CANCELE a transação**
2. Verifique se está na página correta (`/token/`)
3. Verifique se está atualizando "Token Info" e não algo do contrato
4. Se persistir, pode ser bug do Etherscan - tente mais tarde

**Nota:** Atualizar informações do token **não deve custar gas**.

---

### **Problema 5: Erro "You are not authorized"**

**Possíveis causas:**
1. Wallet conectada não é a mesma do deploy
2. Contrato não tem função `owner()` implementada
3. Você não é o owner do contrato

**Soluções:**
1. Verifique se está usando a wallet correta
2. Verifique o owner do contrato:
   - Acesse: https://sepolia.etherscan.io/address/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87#readContract
   - Procure função `owner()`
   - Veja se retorna seu endereço

---

## 📝 Informações para Copiar e Colar

### **URL Completa do Logo:**
```
https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i
```

### **Informações Completas:**
```
Token Address: 0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
Token Name: NeoFlowOFF
Token Symbol: NEOFLW
Decimals: 18
Token Logo: https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i
Website: neoflowoff.eth
Description: Token oficial do protocolo NEOFLW - um protocolo modular DAO focado em governança descentralizada e crescimento sustentável.
```

---

## 🎯 Resumo Rápido

1. ✅ Acesse: https://sepolia.etherscan.io/token/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
2. ✅ Conecte sua wallet (Sepolia)
3. ✅ Procure "Update Token Info" (vários lugares possíveis)
4. ✅ Cole a URL do logo IPFS
5. ✅ Preencha outros campos
6. ✅ Envie e confirme
7. ✅ Aguarde alguns minutos
8. ✅ Verifique se apareceu

---

## 🔗 Links Úteis

- **Página do Token:** https://sepolia.etherscan.io/token/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
- **Logo IPFS:** https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i
- **My Account:** https://sepolia.etherscan.io/myaccount
- **Contrato Verificado:** https://repo.sourcify.dev/11155111/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87

---

## 💡 Dicas Finais

1. **Seja paciente** - Pode levar tempo para aparecer
2. **Tente diferentes horários** - Servidor pode estar menos carregado
3. **Use Blockscout como alternativa** - Se Etherscan não funcionar
4. **Teste a URL do logo** - Antes de enviar, abra no navegador
5. **Guarde screenshot** - Caso precise mostrar o problema

---

**Boa sorte atualizando a imagem!** Se encontrar algum problema específico, consulte a seção de Troubleshooting acima. 🚀

