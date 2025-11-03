# 📋 Como Copiar o Input Data da Transação

## 🎯 Problema

Você executou o script com o **hash da transação** (`0xfc9fff5e...`), mas o script precisa do **Input Data completo** (muito mais longo).

---

## ✅ Solução: Copiar o Input Data Correto

### **Passo 1: Acesse a Transação**

**Clique aqui:**
```
https://bscscan.com/tx/0xfc9fff5ef2bcee846a2eac7b5b05d83378beefdf486e2b050dce7fc2a3197e69
```

### **Passo 2: Encontre "Input Data"**

Na página da transação:

1. **Role a página para baixo**
2. **Procure pela seção "Input Data"**
3. **Você verá algo assim:**

```
Input Data
0x608060405234801561001057600080fd5b5060405162000e2438038062000e24833981016040819052620000349162000...
[muito código hexadecimal aqui - pode ter milhares de caracteres]
```

### **Passo 3: Copie TODO o Input Data**

**O Input Data é MUITO MAIOR que o hash da transação!**

- **Hash da transação:** `0xfc9fff5ef2bcee846a2eac7b5b05d83378beefdf486e2b050dce7fc2a3197e69` (66 caracteres)
- **Input Data:** Começa com `0x6080604052...` e tem **MILHARES de caracteres**

**Como copiar:**
1. **Clique no campo do Input Data**
2. **Se houver botão "Copy"**, use-o
3. **Ou selecione tudo:** `Ctrl+A` / `Cmd+A`
4. **Copie:** `Ctrl+C` / `Cmd+C`

⚠️ **IMPORTANTE:** Copie TUDO, do início (`0x`) até o fim!

---

## 🔧 Usar o Script Corretamente

### **Depois de Copiar o Input Data Completo:**

```bash
cd BOX-TOKEN
python scripts/extract_signer_from_input_data.py [COLE_O_INPUT_DATA_COMPLETO]
```

**O Input Data completo é algo como:**
```
0x608060405234801561001057600080fd5b5060405162000e2438038062000e24833981016040819052620000349162000XYZ... [continua por muito tempo]
```

**Não é apenas o hash!** É o código hexadecimal completo da transação.

---

## 📊 Diferença

| Tipo | Tamanho | Exemplo |
|------|---------|---------|
| **Hash da Transação** | ~66 caracteres | `0xfc9fff5ef2bcee846a2eac7b5b05d83378beefdf486e2b050dce7fc2a3197e69` |
| **Input Data** | **MILHARES de caracteres** | `0x608060405234801561001057600080fd5b5060405162000e2438038062000e24833981016040819052620000349162000...` (muito longo!) |

---

## ✅ Checklist

- [ ] Acessei a transação no BSCScan
- [ ] Encontrei a seção "Input Data"
- [ ] Copiei TODO o código hexadecimal (muito longo, não apenas o hash)
- [ ] O Input Data começa com `0x6080604052...`
- [ ] Colei o Input Data completo no script
- [ ] Executei o script com sucesso

---

## 🎯 Quick Action

1. **Abra:** https://bscscan.com/tx/0xfc9fff5ef2bcee846a2eac7b5b05d83378beefdf486e2b050dce7fc2a3197e69
2. **Role até:** "Input Data"
3. **Copie TUDO** (é muito longo!)
4. **Execute:**
   ```bash
   python scripts/extract_signer_from_input_data.py [COLE_O_INPUT_DATA_AQUI]
   ```

---

**O Input Data é muito maior que o hash! Copie tudo!** 🚀

