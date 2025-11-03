# ✅ Como Verificar Sem Ter o JSON - BOX Token

## 🎯 Situação

Você não tem o arquivo Standard JSON Input do contrato BOX Token. Não tem problema! Existem alternativas mais simples.

---

## ✅ Opção 1: Método "Single File" no BSCScan (Mais Simples)

Este método é mais fácil porque você só precisa do código fonte do contrato em um arquivo `.sol`.

### **Passo a Passo:**

#### **1. Obtenha o Código Fonte**

Você precisa do código `.sol` do contrato BOX Token. Onde encontrar:

**Opção A: Se o contrato já foi verificado antes**
- Acesse: https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017#code
- Se já estiver verificado, você pode copiar o código fonte

**Opção B: Se você tem o projeto original**
- Procure pelo arquivo `.sol` do contrato BOX
- Pode estar em: `contracts/`, `src/`, ou pasta raiz

**Opção C: Se você tem código "flattened" (achatado)**
- Arquivo `.sol` com todas as dependências inline
- Muito útil para este método!

**Opção D: Pedir para quem fez o deploy**
- Se você não fez o deploy, peça o código fonte

---

#### **2. Acesse o BSCScan**

1. **Acesse:** https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017#code
2. **Clique em:** "Verify and Publish" (ou "Contract" → "Verify and Publish")

---

#### **3. Preencha o Formulário**

**Compiler Type:**
```
Solidity (Single file)
```
⚠️ **IMPORTANTE:** Selecione **"Single file"**, não "Standard JSON Input"!

**Compiler Version:**
- Selecione a versão que foi usada no deploy
- Exemplos comuns: `0.8.30`, `0.8.20`, `0.8.19`
- Se não souber, tente versões comuns

**Open Source License Type:**
```
MIT License (MIT)
```
(ou a licença que foi usada)

**Enter the Solidity Contract Code below:**
- Cole o código fonte completo do contrato aqui
- Deve incluir todas as dependências (se usar código "flattened")
- Certifique-se de incluir o `pragma solidity` no topo

**Constructor Arguments (se necessário):**
- Se o contrato tem constructor com argumentos, forneça aqui
- Formato: hexadecimal ABI-encoded
- Se não tiver argumentos, deixe em branco

---

#### **4. Configurações de Otimização**

**Optimization:**
- Se o contrato foi compilado com otimização: `Yes`
- Se não: `No`
- Se não souber, tente ambas (comece com `No`)

**Runs (se otimização = Yes):**
- Geralmente: `200`
- Ou o valor usado na compilação original

---

#### **5. Clique em "Verify and Publish"**

---

### **⚠️ Se o Contrato Tem Dependências (OpenZeppelin, etc):**

Se o contrato usa bibliotecas externas, você tem duas opções:

**Opção A: Usar Código "Flattened"**
- Um arquivo `.sol` único com todas as dependências inline
- Ferramentas como Hardhat/Foundry podem gerar isso
- Comando exemplo: `npx hardhat flatten contracts/BoxToken.sol > flattened.sol`

**Opção B: Usar Método "Multi-file"**
- Alguns explorers suportam múltiplos arquivos
- Ou usar Sourcify (melhor para múltiplos arquivos)

---

## ✅ Opção 2: Sourcify com Arquivos .sol

O Sourcify é mais tolerante e aceita arquivos `.sol` diretamente.

### **Passo a Passo:**

#### **1. Acesse o Sourcify**

**URL:** https://sourcify.dev/

#### **2. Selecione a Rede**

- **Network:** `Binance Smart Chain`
- **Chain ID:** `56`

#### **3. Informe o Endereço**

```
0xBc972E10Df612C7d65054BC67aBCA96B3C22a017
```

#### **4. Escolha "Solidity Files"**

- Selecione o método: **"Solidity Files"** (não Standard JSON)
- Faça upload dos arquivos `.sol` do contrato
- Inclua arquivos de dependências se necessário

#### **5. Preencha as Informações**

- **Compiler Version:** Selecione a versão usada
- **Contract Name:** Nome da classe do contrato (ex: `BoxToken`)
- **Optimization:** Se usou otimização ou não

#### **6. Clique em "Verify"**

O Sourcify é mais permissivo e geralmente funciona melhor sem JSON.

---

## ✅ Opção 3: Obter o Código do BSCScan (Se Já Estiver Verificado)

Se o contrato já foi verificado anteriormente:

1. **Acesse:** https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017#code
2. **Copie todo o código fonte** mostrado
3. **Use no método "Single File"** acima

---

## 📋 Checklist - Método Single File

Para usar o método "Single File", você precisa:

- [ ] Código fonte do contrato em arquivo `.sol`
- [ ] Versão do compilador (ou tentar versões comuns)
- [ ] Informações de otimização (Yes/No, runs)
- [ ] Constructor arguments (se houver)

---

## 🔍 Como Descobrir Informações do Contrato

### **Versão do Compilador:**

**Se você tem o código:**
- Procure por: `pragma solidity ^0.8.XX;` no topo do arquivo

**Se não tem o código:**
- Tente versões comuns: `0.8.30`, `0.8.20`, `0.8.19`, `0.8.18`

### **Nome do Contrato:**

**Se você tem o código:**
- Procure por: `contract NomeDoContrato {`
- O nome está entre `contract` e `{`

**Exemplos:**
- `contract BoxToken {`
- `contract Token {`
- `contract InterboxToken {`

### **Constructor Arguments:**

**Se o contrato tem constructor:**
- Verifique na transação de deploy original
- Ou pergunte para quem fez o deploy
- Ou deixe vazio e veja se funciona

---

## 💡 Dica: Código Flattened

Se você tem acesso ao projeto original, pode gerar código "flattened":

**Hardhat:**
```bash
npx hardhat flatten contracts/BoxToken.sol > box_token_flattened.sol
```

**Foundry:**
```bash
forge flatten contracts/BoxToken.sol > box_token_flattened.sol
```

O código flattened tem todas as dependências inline, perfeito para o método "Single File"!

---

## 🔗 Links Úteis

- **BSCScan:** https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017#code
- **Sourcify:** https://sourcify.dev/
- **Token BOX:** https://bscscan.com/token/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017

---

## ✅ Resumo

**Sem JSON? Use:**
1. ✅ **Método "Single File" no BSCScan** - Mais simples
2. ✅ **Sourcify com arquivos .sol** - Mais tolerante
3. ✅ **Código Flattened** - Melhor para contratos com dependências

**Não precisa de JSON para nenhum desses métodos!** 🚀

