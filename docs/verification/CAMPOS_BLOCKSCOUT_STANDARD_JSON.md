# 📋 Campos Obrigatórios no Blockscout (Standard JSON Input)

## ⚠️ IMPORTANTE

Mesmo usando **"Standard JSON Input"**, o Blockscout **AINDA EXIGE** que você preencha vários campos no formulário!

**O Standard JSON Input NÃO substitui os campos do formulário - eles trabalham juntos!**

---

## ✅ Checklist Completo de Campos

### **Campos Visíveis no Topo (Você Já Preencheu):**

1. ✅ **Contract License:** `MIT License (MIT)`

2. ✅ **Verification Method:** `Solidity (Standard JSON input)`

3. ✅ **Compiler:** `v0.8.30+commit.73712a01`

4. ✅ **Standard JSON Input File:** `sourcify_standard_json.json` (carregado)

---

### **Campos Que Estão Mais Abaixo na Página (FALTAM!):**

**⚠️ ESSES CAMPOS SÃO OBRIGATÓRIOS! Role a página para baixo e preencha todos:**

#### **1. Contract Name**
```
NeoFlowToken
```

#### **2. Contract File Path / Contract File**
```
contracts/NeoFlowToken.sol
```

#### **3. Constructor Arguments**
**ABI-encoded (recomendado):**
```
0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000
```

**Ou valor decimal:**
```
1000000000000000000000000000
```

#### **4. Optimization Enabled**
- ✅ Selecione: `Yes` ou `true` ou marque o checkbox
- ❌ NÃO deixe como `No` ou desmarcado!

#### **5. Optimization Runs**
```
200
```

#### **6. EVM Version**
- Deixe como `default` (geralmente é o padrão)
- Ou selecione conforme foi usado no deploy

---

## 🔍 Como Encontrar Esses Campos

1. **Role a página para baixo** (use a barra de rolagem à direita)

2. **Procure por seções como:**
   - "Contract Information"
   - "Optimization Settings"
   - "Constructor Arguments"
   - "Additional Settings"

3. **Alguns campos podem estar em:**
   - Dropdowns
   - Text inputs
   - Checkboxes
   - Caixas de texto

---

## 💡 Por Que Isso é Importante?

O Blockscout **combina** os valores do formulário com o Standard JSON Input. Se algum campo do formulário estiver:

- ❌ Vazio
- ❌ Diferente do que está no JSON
- ❌ Diferente do que foi usado no deploy original

**Resultado:** "Partial Match" ou erro "Cannot update partially verified..."

---

## ✅ Solução Completa

1. ✅ **Preencha TODOS os campos visíveis** (você já fez isso)

2. ✅ **Role para baixo e encontre os campos adicionais**

3. ✅ **Preencha:**
   - Contract Name: `NeoFlowToken`
   - Contract File Path: `contracts/NeoFlowToken.sol`
   - Constructor Arguments: `0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000`
   - Optimization: Enabled, 200 runs
   - EVM Version: default

4. ✅ **Verifique novamente**

5. ✅ **Agora deve conseguir "Full Match"!**

---

## 🎯 Valores Exatos para Preencher

### **Configurações Completas:**

```
Contract License: MIT License (MIT)
Verification Method: Solidity (Standard JSON input)
Compiler: v0.8.30+commit.73712a01
Standard JSON Input: sourcify_standard_json.json (carregado)

Contract Name: NeoFlowToken
Contract File Path: contracts/NeoFlowToken.sol
Constructor Arguments: 0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000
Optimization Enabled: Yes / true
Optimization Runs: 200
EVM Version: default
```

**Use estes valores exatos para conseguir "Full Match"!**

---

**Não se esqueça de rolar a página para baixo e preencher TODOS os campos!** 📋✅

