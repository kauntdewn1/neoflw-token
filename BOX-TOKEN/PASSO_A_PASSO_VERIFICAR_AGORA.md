# ✅ Passo a Passo: Verificar BOX Token Agora!

## 🎯 Arquivo Pronto!

Você já tem o arquivo flattened pronto:
```
BOX-TOKEN/InterboxCoin_Flattened_Final.sol
```

---

## 🚀 Método 1: BSCScan - Single File (Recomendado para Começar)

### **Passo 1: Abra o Arquivo**

Abra o arquivo:
```
/Users/nettomello/CODIGOS/neoflw-token/BOX-TOKEN/InterboxCoin_Flattened_Final.sol
```

### **Passo 2: Copie Todo o Código**

- Selecione tudo: `Ctrl+A` (Windows/Linux) ou `Cmd+A` (Mac)
- Copie: `Ctrl+C` (Windows/Linux) ou `Cmd+C` (Mac)

### **Passo 3: Acesse o BSCScan**

Abra no navegador:
```
https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017#code
```

### **Passo 4: Clique em "Verify and Publish"**

Na página do contrato, procure e clique no botão:
- **"Verify and Publish"**
- Ou **"Contract"** → **"Verify and Publish"**

### **Passo 5: Preencha o Formulário**

#### **5.1. Compiler Type:**
```
Solidity (Single file)
```
⚠️ **IMPORTANTE:** Selecione **"Single file"**, NÃO "Standard JSON Input"!

#### **5.2. Compiler Version:**
Olhe na primeira linha do arquivo `.sol`:
```solidity
pragma solidity ^0.8.XX;
```

Selecione a versão correspondente:
- Se for `^0.8.30` → Selecione `0.8.30+commit.xxxxx`
- Se for `^0.8.20` → Selecione `0.8.20+commit.xxxxx`
- Se for `^0.8.19` → Selecione `0.8.19+commit.xxxxx`
- E assim por diante...

#### **5.3. Open Source License Type:**
```
MIT License (MIT)
```
(ou a licença que foi usada no contrato)

#### **5.4. Enter the Solidity Contract Code below:**
Cole todo o código que você copiou do arquivo `InterboxCoin_Flattened_Final.sol`

⚠️ **Certifique-se de:**
- Colar TUDO (todo o conteúdo do arquivo)
- Incluir a linha `pragma solidity` no início
- Não faltar nenhuma parte

#### **5.5. Constructor Arguments (Se Necessário):**

**Como descobrir se precisa:**
- Se o contrato tem um constructor com argumentos, você precisa informar
- Verifique no código do contrato se há um constructor
- Se não tiver argumentos, deixe em branco

**Formato:**
- Hexadecimal ABI-encoded
- Se não souber, tente deixar vazio primeiro

#### **5.6. Optimization:**

Tente primeiro com:
- **Optimization:** `No`

Se não funcionar, tente:
- **Optimization:** `Yes`
- **Runs:** `200` (ou o valor que foi usado)

### **Passo 6: Clique em "Verify and Publish"**

Revise se preencheu tudo corretamente:
- ✅ Compiler Type: Single file
- ✅ Compiler Version: Correta
- ✅ License: Selecionada
- ✅ Código: Colado completamente
- ✅ Optimization: Configurada

Clique em **"Verify and Publish"**

### **Passo 7: Aguarde**

- Pode levar alguns minutos
- Você verá uma mensagem de sucesso ou erro
- Se der erro, veja a seção de troubleshooting abaixo

---

## 🌐 Método 2: Sourcify (Alternativa - Mais Tolerante)

Se o BSCScan não funcionar, tente o Sourcify:

### **Passo 1: Acesse o Sourcify**

```
https://sourcify.dev/
```

### **Passo 2: Selecione a Rede**

- **Network:** `Binance Smart Chain`
- **Chain ID:** `56`

### **Passo 3: Informe o Endereço**

```
0xBc972E10Df612C7d65054BC67aBCA96B3C22a017
```

### **Passo 4: Escolha "Solidity Files"**

- Selecione: **"Solidity Files"** (não Standard JSON Input)
- Faça upload do arquivo: `InterboxCoin_Flattened_Final.sol`

### **Passo 5: Preencha Informações**

- **Compiler Version:** A versão do `pragma solidity`
- **Contract Name:** O nome do contrato (ex: `InterboxCoin`)

### **Passo 6: Clique em "Verify"**

---

## 🔍 Informações do Arquivo

Para preencher corretamente, você precisa saber:

### **Versão do Compilador:**
Olhe na primeira linha do arquivo:
```solidity
pragma solidity ^0.8.XX;
```

### **Nome do Contrato:**
Procure por:
```solidity
contract NomeDoContrato {
```

### **Constructor:**
Procure por:
```solidity
constructor(...) {
```

Se encontrar, veja se tem argumentos ou se está vazio.

---

## ❌ Troubleshooting

### **Erro: "Bytecode mismatch"**

**Solução:**
- ✅ Verifique se a versão do compilador está EXATA
- ✅ Verifique se a otimização está correta (tente ambas: Yes e No)
- ✅ Verifique se colou TODO o código (não faltou nada)

### **Erro: "Contract name does not match"**

**Solução:**
- ✅ Verifique o nome do contrato no código
- ✅ Use o nome exato (case-sensitive)

### **Erro: "Constructor arguments"**

**Solução:**
- ✅ Verifique se o contrato tem constructor
- ✅ Se tiver argumentos, calcule o ABI-encoded
- ✅ Se não tiver, deixe em branco

### **Ainda Não Funciona?**

Tente:
1. ✅ Usar o Sourcify (mais tolerante)
2. ✅ Verificar se o arquivo está completo
3. ✅ Tentar diferentes versões do compilador próximas
4. ✅ Tentar com e sem otimização

---

## ✅ Checklist Antes de Enviar

- [ ] Arquivo `InterboxCoin_Flattened_Final.sol` aberto
- [ ] Todo o código copiado (Ctrl+A, Ctrl+C)
- [ ] BSCScan aberto na página correta
- [ ] "Verify and Publish" clicado
- [ ] Compiler Type: "Single file" selecionado
- [ ] Compiler Version correta (da linha pragma)
- [ ] License selecionada
- [ ] Código colado completamente
- [ ] Optimization configurada
- [ ] Constructor arguments (se necessário)
- [ ] Tudo revisado
- [ ] "Verify and Publish" clicado

---

## 🎯 Quick Start (Versão Super Rápida)

```bash
# 1. Abra o arquivo
open BOX-TOKEN/InterboxCoin_Flattened_Final.sol

# 2. Selecione tudo e copie (Ctrl+A, Ctrl+C ou Cmd+A, Cmd+C)

# 3. Abra no navegador:
# https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017#code

# 4. Clique em "Verify and Publish"

# 5. Selecione:
#    - Compiler Type: Solidity (Single file)
#    - Compiler Version: (da linha pragma do arquivo)
#    - License: MIT
#    - Cole o código

# 6. Clique em "Verify and Publish"
```

---

## 🔗 Links Úteis

- **BSCScan:** https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017#code
- **Sourcify:** https://sourcify.dev/
- **Token BOX:** https://bscscan.com/token/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017

---

**Tudo pronto! Siga os passos acima e você verá o contrato verificado!** 🚀

