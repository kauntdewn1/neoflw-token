# ⚡ Resumo: Contrato Não Verificado - Encontrar Signer

## ❌ Situação

Você está na aba "Contract" mas está vazia porque o contrato **não está verificado ainda**.

Não conseguimos ver a função `signer()` porque o código não está público.

---

## ✅ Solução Rápida: Use o Sourcify (Recomendado!)

O Sourcify pode verificar mesmo sem você ter o constructor argument!

### **5 Passos:**

1. **Acesse:** https://sourcify.dev/

2. **Selecione:**
   - Network: `Binance Smart Chain` (Chain ID: 56)
   - Address: `0xBc972E10Df612C7d65054BC67aBCA96B3C22a017`

3. **Escolha:** "Solidity Files"

4. **Upload:** `InterboxCoin_Flattened_Final.sol`

5. **Clique em:** "Verify"

**O Sourcify pode calcular o constructor argument automaticamente!** ✅

---

## 🔍 Alternativa: Encontrar na Transação de Criação

Se o Sourcify não funcionar, encontre o signer na transação:

### **Passo a Passo:**

1. **Na página atual**, veja **"CONTRACT CREATOR"**: `0x45f9C5Af...6E4D42A53`

2. **Clique neste endereço**

3. **Na nova página**, procure por **"Contract Creation"** ou lista de transações

4. **Clique na transação** que criou `0xBc972E10Df612C7d65054BC67aBCA96B3C22a017`

5. **Na página da transação**, procure **"Input Data"**

6. **O signer está nos últimos bytes** do Input Data

7. **Use o script para extrair:**
   ```bash
   python scripts/extract_signer_from_input_data.py [COLE_O_INPUT_DATA_AQUI]
   ```

---

## 🎯 Recomendação

**Tente o Sourcify PRIMEIRO** - é muito mais fácil e pode funcionar sem o constructor argument!

Se não funcionar, aí sim procure na transação de criação.

---

## 🔗 Links

- **Sourcify:** https://sourcify.dev/
- **Contrato:** https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017

---

**Comece pelo Sourcify! É mais fácil!** 🚀

