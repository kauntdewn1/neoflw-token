# ✅ Passo a Passo Sourcify - BOX Token (BSC)

## 🎯 Objetivo

Verificar o contrato BOX Token na Binance Smart Chain usando o Sourcify, seguindo o mesmo processo usado para o NEOFLW na Ethereum.

---

## 📋 Informações do Token

- **Rede:** Binance Smart Chain (BSC) Mainnet
- **Chain ID:** 56
- **Token Address:** `0xBc972E10Df612C7d65054BC67aBCA96B3C22a017`
- **Sourcify URL:** https://sourcify.dev/

---

## 🚀 Passo a Passo Completo

### **PASSO 1: Acessar o Sourcify**

1. **Acesse:** https://sourcify.dev/
2. **Clique em:** "Verify Contract" ou "Verificar Contrato"

---

### **PASSO 2: Selecionar Rede**

1. **Procure por:** "Select Network" ou "Selecionar Rede"
2. **Digite ou selecione:** `Binance Smart Chain` ou `BSC` ou `BNB Smart Chain`
3. **Chain ID:** 56 (deve aparecer automaticamente)

⚠️ **IMPORTANTE:** Certifique-se de selecionar **BSC Mainnet** (não testnet)

---

### **PASSO 3: Informar Endereço do Contrato**

1. **No campo "Contract Address":**
   ```
   0xBc972E10Df612C7d65054BC67aBCA96B3C22a017
   ```
2. **Clique em "Continue"** ou **"Continuar"**

---

### **PASSO 4: Escolher Método de Verificação**

O Sourcify oferece diferentes métodos. Recomendamos:

#### **Opção A: Standard JSON Input (Recomendado) ✅**

**Melhor para:** Contratos com imports e dependências

1. **Selecione:** "Standard JSON Input"
2. **Faça upload** do arquivo JSON do compilador
   - Geralmente é um arquivo `.json` gerado durante a compilação
   - Pode ser encontrado em `artifacts/` ou pasta de build
   - Formato: Standard JSON do Solidity Compiler

**Se você não tem o JSON completo:**

- Veja a opção B ou C abaixo
- Ou compile novamente o contrato gerando o Standard JSON

#### **Opção B: Solidity Files**

**Melhor para:** Contratos simples ou quando você tem todos os arquivos

1. **Selecione:** "Solidity Files"
2. **Faça upload** dos arquivos `.sol` do contrato
   - Inclua o arquivo principal do contrato
   - Inclua arquivos de dependências (OpenZeppelin, etc)
   - Mantenha a estrutura de pastas se possível

#### **Opção C: Flattened Code**

**Melhor para:** Quando você tem o código "achatado" (flattened)

1. **Selecione:** "Flattened Code" ou similar
2. **Cole todo o código** em um único campo
   - Deve incluir todas as dependências inline
   - Geralmente é um arquivo `.sol` muito grande

---

### **PASSO 5: Selecionar Contrato Principal**

Se você usou arquivos múltiplos ou Standard JSON:

1. **Procure por:** "Contract Name" ou "Select Contract"
2. **Selecione o contrato principal:**
   - Exemplo: `BoxToken.sol:BoxToken`
   - Ou: `contracts/BoxToken.sol:BoxToken`

⚠️ **IMPORTANTE:** Selecione o contrato correto, não uma dependência ou library!

---

### **PASSO 6: Informar Versão do Compilador**

1. **Selecione a versão do compilador** usada no deploy
   - Exemplo: `0.8.30+commit.87f61d96`
   - Deve ser **exatamente** a mesma versão usada no deploy

**Como descobrir a versão:**

- Olhe o código do contrato (pragma solidity ^0.8.30;)
- Verifique nos artifacts de compilação
- Use a mesma versão que foi usada no deploy

---

### **PASSO 7: Configurações Adicionais (Se Necessário)**

Se o contrato foi compilado com otimização:

1. **Marque:** "Optimization enabled"
2. **Informe:** "Runs" (geralmente 200 ou similar)

Se o contrato tem constructor com argumentos:

1. **Procure por:** "Constructor Arguments"
2. **Informe os argumentos** codificados (ABI-encoded)
3. **Ou deixe em branco** se o Sourcify pedir apenas quando necessário

---

### **PASSO 8: Verificar e Enviar**

1. **Revise todas as informações:**
   - ✅ Rede: Binance Smart Chain (56)
   - ✅ Endereço: 0xBc972E10Df612C7d65054BC67aBCA96B3C22a017
   - ✅ Método: Standard JSON / Files / Flattened
   - ✅ Contrato principal selecionado
   - ✅ Versão do compilador correta

2. **Clique em:** "Verify" ou **"Verificar"**

3. **Aguarde o processamento:**
   - Pode levar alguns minutos
   - O Sourcify comparará o bytecode

---

### **PASSO 9: Verificar Resultado**

#### **Se Sucesso: ✅**

Você verá uma mensagem de sucesso e um link para:
```
https://repo.sourcify.dev/chains/56/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017
```

**O que isso significa:**
- ✅ Contrato verificado com sucesso!
- ✅ Código fonte está público e verificável
- ✅ O BSCScan reconhecerá automaticamente (pode levar algumas horas)

#### **Se Erro: ❌**

**Erros comuns:**

1. **"Bytecode mismatch"**
   - ✅ Verifique a versão do compilador (deve ser exata)
   - ✅ Verifique configurações de otimização
   - ✅ Verifique os arquivos enviados

2. **"Contract not found"**
   - ✅ Certifique-se de selecionar o contrato principal
   - ✅ Verifique se os arquivos estão completos

3. **"Network mismatch"**
   - ✅ Certifique-se de selecionar Binance Smart Chain (Chain ID 56)
   - ✅ Verifique se o endereço está correto

---

## ✅ Após Verificação no Sourcify

### **1. Verificar no BSCScan (Pode Demorar)**

Após verificação no Sourcify, o BSCScan reconhece automaticamente:

1. **Acesse:** https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017#code
2. **Aguarde algumas horas** (pode demorar até 24h)
3. **Verifique se aparece:** "Contract Source Code Verified"

**Se não aparecer imediatamente:**
- ✅ É normal, pode demorar
- ✅ O contrato está verificado no Sourcify
- ✅ Usuários podem verificar no Sourcify diretamente

### **2. Link Permanente no Sourcify**

```
https://repo.sourcify.dev/chains/56/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017
```

Este link mostra:
- ✅ Código fonte completo
- ✅ Metadados do contrato
- ✅ Informações de compilação

---

## 📋 Checklist de Verificação

- [ ] Acessei o Sourcify (https://sourcify.dev/)
- [ ] Selecionei Binance Smart Chain (Chain ID 56)
- [ ] Informei o endereço: 0xBc972E10Df612C7d65054BC67aBCA96B3C22a017
- [ ] Escolhi o método de verificação (Standard JSON recomendado)
- [ ] Fiz upload dos arquivos/código necessário
- [ ] Selecionei o contrato principal correto
- [ ] Informei a versão correta do compilador
- [ ] Configurei otimização (se necessário)
- [ ] Cliquei em "Verify"
- [ ] Recebi confirmação de sucesso
- [ ] Anotei o link do Sourcify

---

## 🔗 Links Úteis

- **Sourcify:** https://sourcify.dev/
- **Sourcify Repo (BSC):** https://repo.sourcify.dev/chains/56
- **Contrato no BSCScan:** https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017
- **Token no BSCScan:** https://bscscan.com/token/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017

---

## ⚠️ Nota sobre APIs do BSCScan

**Importante:** As APIs do BSCScan foram depreciadas e substituídas pela **Etherscan API V2**.

**O que isso significa:**
- ⚠️ Se você tinha scripts usando APIs antigas do BSCScan, precisará migrar
- ✅ **O Sourcify NÃO é afetado** - funciona independentemente
- ✅ **Verificação manual no BSCScan ainda funciona** (interface web)
- ✅ **Sourcify é uma alternativa recomendada** por não depender de APIs

**Para mais informações sobre migração de API:**
- Etherscan API V2: https://docs.etherscan.io/v2-migration
- BSCScan continua funcionando normalmente na interface web

---

## 💡 Dicas Finais

1. **Se você já tem o Standard JSON** do NEOFLW, pode adaptar para o BOX
2. **O processo é idêntico** ao usado na Ethereum, apenas muda a rede
3. **Sourcify é gratuito** e não requer cadastro
4. **A verificação é permanente** uma vez concluída

---

**Boa sorte com a verificação!** 🚀

