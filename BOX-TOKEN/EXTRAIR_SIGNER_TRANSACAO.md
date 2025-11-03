# 🔍 Extrair Signer da Transação de Criação

## 📋 Transação de Criação

**Hash:** `0xfc9fff5ef2bcee846a2eac7b5b05d83378beefdf486e2b050dce7fc2a3197e69`

**Link Direto:**
```
https://bscscan.com/tx/0xfc9fff5ef2bcee846a2eac7b5b05d83378beefdf486e2b050dce7fc2a3197e69
```

---

## ✅ Passo a Passo para Extrair o Signer

### **Passo 1: Acessar a Transação**

**Clique neste link ou copie no navegador:**
```
https://bscscan.com/tx/0xfc9fff5ef2bcee846a2eac7b5b05d83378beefdf486e2b050dce7fc2a3197e69
```

### **Passo 2: Encontrar Input Data**

Na página da transação:
1. **Role a página para baixo**
2. **Procure pela seção "Input Data"**
3. **Você verá um código hexadecimal muito longo**
4. **Começa com:** `0x6080604052...`
5. **Pode ter milhares de caracteres**

### **Passo 3: Copiar o Input Data**

1. **Clique no campo do Input Data** (se houver um botão "Copy", use-o)
2. **Selecione tudo:** `Ctrl+A` (Windows/Linux) ou `Cmd+A` (Mac)
3. **Copie:** `Ctrl+C` (Windows/Linux) ou `Cmd+C` (Mac)

⚠️ **IMPORTANTE:** Copie TUDO, do início ao fim!

### **Passo 4: Usar o Script para Extrair**

Depois de copiar o Input Data:

```bash
cd BOX-TOKEN
python scripts/extract_signer_from_input_data.py [COLE_O_INPUT_DATA_AQUI]
```

**Exemplo:**
```bash
python scripts/extract_signer_from_input_data.py 0x608060405234801561001057600080fd5b5060405162000e24...
```

O script vai:
- ✅ Analisar o Input Data
- ✅ Extrair o endereço do signer automaticamente
- ✅ Calcular o constructor argument no formato correto
- ✅ Mostrar o valor pronto para usar no BSCScan

---

## 📋 O Que o Script Vai Mostrar

O script vai retornar algo como:

```
✅ SIGNER ENCONTRADO!
📍 Endereço do Signer: 0xABC123DEF456...

✅ CONSTRUCTOR ARGUMENT CALCULADO
Cole este valor no BSCScan:
000000000000000000000000ABC123DEF456...
```

**Copie o valor do "CONSTRUCTOR ARGUMENT"** e use no BSCScan!

---

## 🚀 Depois de Ter o Constructor Argument

### **Usar no BSCScan:**

1. **Acesse:**
   ```
   https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017#code
   ```

2. **Clique em:** "Verify and Publish"

3. **Preencha:**
   - Compiler Type: `Solidity (Single file)`
   - Compiler Version: `0.8.24` (ou tente `0.8.23`)
   - License: `MIT License (MIT)`
   - Contract Code: Cole o código de `InterboxCoin_Flattened_Final.sol`
   - **Constructor Arguments:** Cole o valor que o script retornou (sem `0x`)
   - Optimization: Tente `Yes` com `Runs: 200`

4. **Clique em:** "Verify and Publish"

---

## 🔍 Se o Script Não Funcionar

### **Método Manual:**

1. **Copie o Input Data** completo da transação

2. **Identifique os últimos bytes:**
   - O Input Data tem: `[Bytecode][Constructor Args]`
   - O constructor precisa de 1 endereço = 20 bytes = 40 caracteres hex
   - Em formato ABI-encoded: 64 caracteres hex (com padding)

3. **Pegue os últimos 64 caracteres** do Input Data (sem o `0x`)

4. **Os últimos 40 caracteres** (depois de 24 zeros) são o signer

**Exemplo:**
- Se Input Data termina com: `...000000000000000000000000ABC123DEF456789012345678901234567890ABCD`
- O signer é: `0xABC123DEF456789012345678901234567890ABCD`
- O constructor argument (para BSCScan) é: `000000000000000000000000ABC123DEF456789012345678901234567890ABCD`

---

## ✅ Checklist

- [ ] Acessei a transação: https://bscscan.com/tx/0xfc9fff5ef2bcee846a2eac7b5b05d83378beefdf486e2b050dce7fc2a3197e69
- [ ] Encontrei a seção "Input Data"
- [ ] Copiei TODO o Input Data (é muito longo!)
- [ ] Executei o script com o Input Data
- [ ] Copiei o constructor argument retornado
- [ ] Tentei no BSCScan com o constructor argument

---

## 🔗 Links Diretos

- **Transação:** https://bscscan.com/tx/0xfc9fff5ef2bcee846a2eac7b5b05d83378beefdf486e2b050dce7fc2a3197e69
- **Contrato:** https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017#code

---

**Acesse a transação, copie o Input Data e use o script!** 🚀

