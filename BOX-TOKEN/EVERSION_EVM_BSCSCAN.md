# 🎯 EVM Version para BSCScan - Qual Escolher?

## ✅ Resposta Rápida

Para o contrato **InterboxCoin** (`pragma solidity ^0.8.24`) na **BSC (Binance Smart Chain)**:

### **Recomendação: Use "default" ou deixe em branco**

Se a opção "default" não existir, tente nesta ordem:
1. **"default"** (se disponível)
2. **"london"** 
3. **"shanghai"**
4. **"cancun"** (pode não funcionar ainda no BSC)

---

## 📊 Detalhes Técnicos

### **Por que não usar "Cancun"?**

Embora o Solidity 0.8.24 suporte "Cancun", a BSC pode ainda não ter implementado todas as atualizações Cancun:
- Cancun introduz novos opcodes (EIP-1153, EIP-4844)
- BSC pode ainda usar uma versão anterior da EVM
- O bytecode pode não corresponder se usar Cancun

### **Compatibilidade com BSC:**

A Binance Smart Chain geralmente usa:
- **EVM Version:** London ou Shanghai (mais comum)
- **Não Cancun** (ainda não totalmente suportado)

---

## 🔧 Configuração no BSCScan

### **Opções de Campo "EVM Version":**

Quando o BSCScan pedir "EVM Version to target", você verá opções como:

- ✅ **"default"** ← **USE ESTA (se disponível)**
- `london`
- `shanghai`
- `istanbul`
- `berlin`
- `cancun` ← **EVITE (pode não funcionar)**

### **Como Escolher:**

1. **Se houver opção "default":** Selecione ela ✅
2. **Se não houver "default":** Selecione **"london"** ou **"shanghai"**
3. **Evite "cancun"** até que a BSC tenha atualização confirmada

---

## ⚠️ Se Der Erro de Bytecode

Se mesmo com "default" ou "london" der erro de bytecode mismatch:

### **Tente estas variações:**

1. **EVM Version:** `london` + **Optimization:** `Yes`, Runs: `200`
2. **EVM Version:** `shanghai` + **Optimization:** `Yes`, Runs: `200`
3. **EVM Version:** `london` + **Optimization:** `No`

---

## 📋 Configuração Completa Recomendada

**No formulário do BSCScan, preencha:**

| Campo | Valor |
|-------|-------|
| **Compiler Type** | `Solidity (Single file)` |
| **Compiler Version** | `0.8.24+commit.e11b9ed9` |
| **EVM Version** | **"default"** ou **"london"** |
| **License** | `MIT License (MIT)` |
| **Optimization** | `Yes` ✅ |
| **Runs** | `200` |
| **Constructor Arguments** | `00000000000000000000000000000000000000000000d3c21bcecceda100000000000000000000000000000045f9c5af31678bc1dacddf348936a6a6e4d42a53` |

---

## 💡 Nota Importante

**EVM Version** geralmente afeta apenas:
- Otimizações específicas do compilador
- Opcodes disponíveis
- Estrutura do bytecode

Para a maioria dos casos na BSC, **"default"** ou **"london"** funciona perfeitamente com Solidity 0.8.24, mesmo que o contrato possa ter sido compilado originalmente com outra configuração.

---

## ✅ Resumo

**Para BSCScan com Solidity 0.8.24 na BSC:**
- ✅ Use **"default"** (se disponível)
- ✅ Ou **"london"** (alternativa segura)
- ❌ Evite **"cancun"** (ainda não totalmente suportado na BSC)

---

**Essa configuração deve funcionar!** 🚀

