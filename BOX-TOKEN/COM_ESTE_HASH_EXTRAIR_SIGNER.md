# ⚡ Extrair Signer - Hash da Transação Fornecido

## ✅ Hash da Transação de Criação

```
0xfc9fff5ef2bcee846a2eac7b5b05d83378beefdf486e2b050dce7fc2a3197e69
```

---

## 🚀 Ação Imediata (3 Passos)

### **Passo 1: Acessar a Transação**

**Clique aqui:**
```
https://bscscan.com/tx/0xfc9fff5ef2bcee846a2eac7b5b05d83378beefdf486e2b050dce7fc2a3197e69
```

### **Passo 2: Copiar Input Data**

Na página da transação:
1. **Role para baixo** até encontrar **"Input Data"**
2. **Clique no Input Data** ou use botão "Copy" se houver
3. **Copie TODO o código hexadecimal** (é muito longo!)

**Formato:** Começa com `0x6080604052...` e tem milhares de caracteres

### **Passo 3: Extrair com Script**

**Cole o Input Data no script:**

```bash
cd BOX-TOKEN
python scripts/extract_signer_from_input_data.py [COLE_O_INPUT_DATA_COMPLETO_AQUI]
```

**O script vai retornar:**
- ✅ Endereço do signer
- ✅ Constructor argument formatado
- ✅ Valor pronto para colar no BSCScan

---

## 📋 Exemplo de Uso do Script

**Depois de copiar o Input Data da transação:**

```bash
cd BOX-TOKEN
python scripts/extract_signer_from_input_data.py 0x608060405234801561001057600080fd5b5060405162000e2438038062000e24833981016040819052620000349162000XYZ...
```

**Substitua `...XYZ...` pelo Input Data completo!**

---

## ✅ Depois de Ter o Constructor Argument

**Use no BSCScan:**

1. **URL:** https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017#code
2. **"Verify and Publish"**
3. **Preencha:**
   - Compiler: `0.8.24` (ou tente `0.8.23`)
   - Single file
   - Code: Cole `InterboxCoin_Flattened_Final.sol`
   - **Constructor Arguments:** Cole o valor do script
   - Optimization: `Yes`, Runs: `200`

---

## 🔗 Link Direto da Transação

```
https://bscscan.com/tx/0xfc9fff5ef2bcee846a2eac7b5b05d83378beefdf486e2b050dce7fc2a3197e69
```

**Clique, copie o Input Data e use o script!** 🚀

