# 🔧 Corrigir Erro: "Standard JSON input must contain a language field"

## ❌ Erro Encontrado

```
invalid_parameter: Standard JSON input must contain a language field
```

## 🎯 O Que Este Erro Significa

O BSCScan está reclamando que o arquivo JSON que você está tentando anexar **não possui o campo `"language"`** no nível raiz do JSON.

O campo `"language"` é **OBRIGATÓRIO** e deve ser `"Solidity"`.

---

## ✅ Solução: Adicionar o Campo "language"

### **Passo 1: Abra o Seu Arquivo JSON**

Abra o arquivo JSON que você está tentando anexar no BSCScan.

### **Passo 2: Verifique a Estrutura**

O JSON deve começar assim:

```json
{
  "language": "Solidity",  // <-- ESTE CAMPO ESTÁ FALTANDO!
  "sources": {
    // ...
  },
  "settings": {
    // ...
  }
}
```

### **Passo 3: Adicione o Campo "language"**

Se o seu JSON **NÃO** começa com `"language": "Solidity"`, adicione na **primeira linha**:

**ANTES (Errado):**
```json
{
  "sources": {
    // ...
  },
  "settings": {
    // ...
  }
}
```

**DEPOIS (Correto):**
```json
{
  "language": "Solidity",
  "sources": {
    // ...
  },
  "settings": {
    // ...
  }
}
```

⚠️ **IMPORTANTE:** O campo `"language"` deve ser o **PRIMEIRO campo** no objeto JSON (ou pelo menos estar presente no nível raiz).

---

## 📋 Estrutura Completa do Standard JSON Input

O JSON completo deve ter esta estrutura:

```json
{
  "language": "Solidity",
  "sources": {
    "caminho/para/SeuContrato.sol": {
      "content": "pragma solidity ^0.8.X;\n\ncontract SeuContrato {\n    // código aqui\n}"
    }
  },
  "settings": {
    "optimizer": {
      "enabled": true,
      "runs": 200
    },
    "outputSelection": {
      "*": {
        "*": [
          "abi",
          "evm.bytecode",
          "evm.deployedBytecode",
          "evm.methodIdentifiers",
          "metadata"
        ]
      }
    },
    "evmVersion": "london"
  }
}
```

---

## 🛠️ Solução Rápida: Script para Corrigir

Se você tem um JSON que está faltando o campo `language`, podemos criar um script para corrigir automaticamente.

**⚠️ ATENÇÃO:** Este script será criado **APENAS na pasta BOX-TOKEN**, não mexe nos arquivos do NEOFLW.

---

## 📝 Passo a Passo no BSCScan

Depois de corrigir o JSON:

1. **Acesse:** https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017#code
2. **Clique em:** "Verify and Publish"
3. **Selecione:**
   - **Compiler Type:** `Solidity (Standard-JSON-Input)`
   - **Compiler Version:** (selecione a versão correta)
   - **License:** (selecione a licença)
4. **Cole o JSON corrigido** no campo "Enter the Solidity Contract Code below"
5. **Clique em:** "Verify and Publish"

---

## 🔍 Como Descobrir o JSON Correto

### **Opção 1: Se Você Tem o Projeto Original**

**Hardhat:**
- Procure em: `artifacts/build-info/*.json`
- Ou execute: `npx hardhat compile` e procure o JSON gerado

**Foundry:**
- Procure em: `out/*.json`

**Truffle:**
- Procure em: `build/contracts/*.json`

**Ape Framework:**
- Procure em: `.build/__local__.json`

### **Opção 2: Se Você NÃO Tem o Projeto Original**

Você terá que:
1. Obter o código fonte do contrato BOX Token
2. Criar manualmente o Standard JSON Input
3. Ou usar o método "Single File" ao invés de Standard JSON

---

## ✅ Checklist

- [ ] Abri o arquivo JSON
- [ ] Adicionei `"language": "Solidity"` no nível raiz
- [ ] Verifiquei que o JSON está bem formatado (sem erros de sintaxe)
- [ ] Colei o JSON corrigido no BSCScan
- [ ] Preenchi todos os campos necessários (Compiler Version, License, etc)
- [ ] Cliquei em "Verify and Publish"

---

## 🆘 Se Ainda Não Funcionar

Se mesmo após adicionar o campo `language` ainda der erro:

1. **Verifique se o JSON está válido:**
   - Use um validador JSON online (jsonlint.com)
   - Certifique-se de que todas as chaves estão fechadas corretamente

2. **Verifique se tem todos os campos necessários:**
   - `language`: "Solidity" ✅
   - `sources`: objeto com os arquivos .sol ✅
   - `settings`: objeto com configurações de compilação ✅

3. **Tente o Sourcify como alternativa:**
   - O Sourcify é mais tolerante com JSONs
   - Siga o guia: `docs/verification/SOURCIFY_PASSO_A_PASSO_BSC.md`

---

## 🔗 Links Úteis

- **Token BOX:** https://bscscan.com/token/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017
- **Contrato BOX:** https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017#code
- **Validador JSON:** https://jsonlint.com/

---

**Boa sorte!** Após adicionar o campo `language`, o erro deve ser resolvido. 🚀

