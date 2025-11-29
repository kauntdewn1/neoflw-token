# 🔧 Corrigir Endereços de Contratos - Polygon Mainnet

**Data:** 2025-01-XX  
**Status:** ⚠️ **AÇÃO NECESSÁRIA** - Endereços do Sepolia encontrados

---

## 📊 Situação Atual

### ✅ **Endereços Corretos (Polygon Mainnet)**

| Contrato | Endereço | Status |
|----------|----------|--------|
| **Token** | `0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2` | ✅ Correto |
| **Vault** | `0x07E39107d4B35b64f9f2310B9A2B8e5262A4ee41` | ✅ Correto |
| **Claim** | `0x407C037906d6441ECD4a3F9064eab2E6CF03b36b` | ✅ Correto |

### ⚠️ **Endereços Incorretos (Sepolia - Testnet)**

| Contrato | Endereço Sepolia | Onde está |
|----------|------------------|-----------|
| **Token** | `0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87` | `.token_address.txt` |
| **Vault** | `0x7A3109a7A978473142c655C3DBbfad4e5Bc37aeD` | `.env` |
| **Claim** | `0xEE96C0813e84bb7Ea162b1594b8Bff61dB79A7Ca` | `.env` |

---

## 🚀 Solução: Script Automático

### **Executar Correção Automática**

```bash
# Executar script de correção
python scripts/fix_contract_addresses.py
```

**OU via Ape:**

```bash
ape run fix_contract_addresses
```

### **O que o script faz:**

1. ✅ Atualiza `.token_address.txt` com endereço do Polygon
2. ✅ Atualiza `artifacts/addresses/.token_address.txt`
3. ✅ Atualiza `.vault_address.txt` (já está correto)
4. ✅ Atualiza `artifacts/addresses/.vault_address.txt` (já está correto)
5. ✅ Atualiza `.claim_address.txt` (já está correto)
6. ✅ Atualiza `artifacts/addresses/.claim_address.txt` (já está correto)
7. ✅ Atualiza `.env` com endereços corretos:
   - `NEXT_PUBLIC_TOKEN_ADDRESS`
   - `NEXT_PUBLIC_VAULT_ADDRESS`
   - `NEXT_PUBLIC_CLAIM_ADDRESS`

---

## 📝 Correção Manual (Alternativa)

Se preferir corrigir manualmente:

### **1. Atualizar `.token_address.txt`**

```bash
echo "0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2" > .token_address.txt
```

### **2. Atualizar `artifacts/addresses/.token_address.txt`**

```bash
echo "0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2" > artifacts/addresses/.token_address.txt
```

### **3. Atualizar `.env`**

Edite o arquivo `.env` e altere:

```env
# ANTES (Sepolia - ERRADO):
NEXT_PUBLIC_TOKEN_ADDRESS=
NEXT_PUBLIC_VAULT_ADDRESS=0x7A3109a7A978473142c655C3DBbfad4e5Bc37aeD
NEXT_PUBLIC_CLAIM_ADDRESS=0xEE96C0813e84bb7Ea162b1594b8Bff61dB79A7Ca

# DEPOIS (Polygon - CORRETO):
NEXT_PUBLIC_TOKEN_ADDRESS=0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2
NEXT_PUBLIC_VAULT_ADDRESS=0x07E39107d4B35b64f9f2310B9A2B8e5262A4ee41
NEXT_PUBLIC_CLAIM_ADDRESS=0x407C037906d6441ECD4a3F9064eab2E6CF03b36b
```

---

## ✅ Verificar Correção

Após executar o script, verifique:

```bash
# Executar auditoria novamente
ape run audit_contract_addresses
```

**Resultado esperado:**
- ✅ Todos os endereços devem aparecer como Polygon Mainnet
- ❌ Nenhum endereço do Sepolia deve aparecer

---

## 📋 Checklist Pós-Correção

- [ ] Script executado com sucesso
- [ ] `.token_address.txt` atualizado
- [ ] `artifacts/addresses/.token_address.txt` atualizado
- [ ] `.env` atualizado com todos os endereços
- [ ] Auditoria executada e confirmada
- [ ] Frontend atualizado (se necessário)

---

## 🔗 Links dos Contratos (Polygon)

- **Token:** https://polygonscan.com/address/0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2
- **Vault:** https://polygonscan.com/address/0x07E39107d4B35b64f9f2310B9A2B8e5262A4ee41
- **Claim:** https://polygonscan.com/address/0x407C037906d6441ECD4a3F9064eab2E6CF03b36b

---

## 💡 Próximos Passos

1. ✅ Executar script de correção
2. ✅ Verificar com auditoria
3. ✅ Atualizar frontend (se necessário)
4. ✅ Testar integração com novos endereços

---

**Última atualização:** 2025-01-XX

