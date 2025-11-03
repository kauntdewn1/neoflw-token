# 📋 Como Preencher o Sourcify - BOX Token (Tela Atual)

## 🎯 Você está na Tela de "Single File" (Arquivo Único)

Esta tela é para fazer upload de um **arquivo `.sol` único**. Mas **recomendamos usar o método "Standard JSON Input"** que é mais robusto.

---

## ⚠️ IMPORTANTE: Dois Métodos Disponíveis

### **Método 1: Single File (Tela Atual) ⚠️**

- Mais simples, mas limitado
- Requer o arquivo `.sol` do contrato BOX
- Funciona melhor para contratos simples sem muitas dependências

### **Método 2: Standard JSON Input (Recomendado) ✅**

- Mais robusto e completo
- Inclui todas as dependências automaticamente
- Melhor para contratos com OpenZeppelin ou outras libs

---

## 🎯 Se Você Quer Continuar na Tela Atual (Single File)

### **1. Compiler Version (Versão do Compilador)**

**O que preencher:**

- Selecione a versão **exata** do compilador Solidity que foi usada para compilar o contrato BOX Token
- A versão mostrada na tela (`0.8.30+commit.73712a01`) é apenas um exemplo
- **Você precisa descobrir qual versão foi usada no deploy do BOX Token**

**Como descobrir:**

- Olhe o código do contrato BOX Token (se tiver)
- Verifique na linha `pragma solidity ^0.8.30;` ou similar
- Ou verifique nos artifacts de compilação do projeto onde foi feito o deploy

**Exemplo:**
```
0.8.30+commit.73712a01
```
(Use a versão que foi realmente usada no deploy do BOX Token)

---

### **2. Contract Identifier (Identificador do Contrato)**

**O que preencher:**

Este campo precisa seguir o formato: `caminho/do/arquivo.sol:NomeDoContrato`

**Exemplo para BOX Token:**

Se o contrato está em `contracts/BoxToken.sol` e o nome da classe é `BoxToken`:
```
contracts/BoxToken.sol:BoxToken
```

**Se o arquivo está na raiz:**
```
BoxToken.sol:BoxToken
```

**Como descobrir:**

- Você precisa saber o **nome exato do arquivo** `.sol` do contrato BOX
- Você precisa saber o **nome exato da classe/contrato** dentro desse arquivo
- Geralmente são iguais (ex: arquivo `BoxToken.sol` tem classe `BoxToken`)

**⚠️ O valor atual `contracts/Storage.sol:Storage` está ERRADO - é apenas exemplo!**

---

### **3. Upload do Arquivo**

**O que fazer:**
- Faça upload do arquivo `.sol` do contrato BOX Token
- Procure por um botão "Upload File" ou área de "drag and drop"
- O arquivo deve ser o código fonte completo do contrato

**⚠️ IMPORTANTE:**
- Se o contrato usa dependências (como OpenZeppelin), você pode precisar do código "flattened" (achatado)
- Ou usar o método Standard JSON Input que inclui dependências automaticamente

---

## ✅ RECOMENDAÇÃO: Use Standard JSON Input

### **Por que usar Standard JSON Input?**

1. ✅ Inclui **todas as dependências** automaticamente
2. ✅ Inclui **configurações de compilação** (otimização, etc)
3. ✅ Mais robusto e menos propenso a erros
4. ✅ É o método recomendado pelo Sourcify

---

### **Como Trocar para Standard JSON Input:**

1. **Procure por uma opção/abas** na interface do Sourcify que diga:
   - **"Standard JSON Input"**
   - **"JSON Input"**
   - **"Verify with JSON"**
   - Ou um botão para **alternar métodos**

2. **Se não encontrar na tela atual:**
   - Volte para a página inicial do Sourcify
   - Procure por opções de método de verificação
   - Selecione **"Standard JSON Input"**

---

## 📄 Qual JSON Anexar (Standard JSON Input)

Se você trocar para Standard JSON Input, você precisará de um arquivo JSON específico.

### **Onde Encontrar o JSON:**

#### **Opção 1: Se Você Tem o Projeto Original (Onde Foi Feito o Deploy)**

**Para Hardhat:**
- Procure em: `artifacts/build-info/*.json`
- O arquivo terá um nome com hash longo (ex: `1234567890abcdef.json`)

**Para Foundry:**
- Procure em: `out/*.json`

**Para Truffle:**
- Procure em: `build/contracts/*.json`

**Para Ape Framework:**
- Procure em: `.build/__local__.json` ou similar
- Ou em artifacts de compilação

#### **Opção 2: Se Você NÃO Tem o Projeto Original**

**Opções:**

1. **Extrair do BSCScan (se o contrato já foi verificado):**
   - Acesse: https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017#code
   - Se o contrato estiver verificado, você pode ver o código fonte
   - Mas ainda precisará criar o Standard JSON manualmente

2. **Usar o Método Single File:**
   - Volte para a tela atual
   - Use o código fonte do contrato (se tiver acesso)
   - Faça upload do arquivo `.sol`

3. **Pedir ao Desenvolvedor Original:**
   - Se você não fez o deploy, peça o Standard JSON para quem fez

---

## 📋 Checklist do Que Você Precisa

### **Para Método Single File (Tela Atual):**
- [ ] Versão do compilador usada no deploy
- [ ] Caminho do arquivo `.sol` do contrato BOX
- [ ] Nome da classe do contrato BOX
- [ ] Arquivo `.sol` do contrato (ou flattened)
- [ ] Preencher: `contracts/BoxToken.sol:BoxToken` (exemplo - ajuste para seu caso)

### **Para Método Standard JSON Input (Recomendado):**
- [ ] Arquivo JSON de compilação do projeto original
- [ ] Ou criar manualmente com todas as dependências

---

## 🔍 Informações Específicas do BOX Token

Para preencher corretamente, você precisa saber:

1. **Qual arquivo `.sol` contém o contrato BOX Token?**
   - Nome do arquivo: `?` (você precisa descobrir)

2. **Qual o nome da classe/contrato dentro desse arquivo?**
   - Nome: `?` (geralmente é o mesmo do arquivo, mas pode variar)

3. **Qual versão do compilador foi usada?**
   - Versão: `?` (veja no código ou artifacts)

4. **O contrato tem constructor com argumentos?**
   - Se sim, quais? (precisa ser informado como ABI-encoded)

---

## 💡 Próximos Passos

1. **Se você tem acesso ao código fonte:**
   - Identifique o arquivo `.sol` do BOX Token
   - Identifique o nome da classe
   - Preencha os campos na tela atual

2. **Se você prefere usar Standard JSON:**
   - Troque para o método "Standard JSON Input"
   - Procure ou crie o arquivo JSON de compilação

3. **Se você não tem essas informações:**
   - Entre em contato com quem fez o deploy do contrato
   - Ou verifique se há documentação do projeto original

---

## 🔗 Links Úteis

- **Sourcify:** https://sourcify.dev/
- **Token BOX no BSCScan:** https://bscscan.com/token/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017
- **Contrato BOX no BSCScan:** https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017

---

**⚠️ Lembre-se:** Os arquivos do NEOFLW estão preservados e não serão modificados. Este guia é apenas para o BOX Token.

