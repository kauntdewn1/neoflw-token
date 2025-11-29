# ✅ Verificação do Contrato no PolygonScan

**Data:** 2025-01-XX  
**Status:** Contrato deployado mas **NÃO verificado**

---

## 📋 Informações do Contrato

### **Endereços**

| Tipo | Endereço | Link |
|------|----------|------|
| **Token/Contrato** | `0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2` | [Ver no PolygonScan](https://polygonscan.com/address/0x59aa4eae743d608fbdd4205eba59b38dca755dd2) |
| **Owner/Deployer** | `0x460F9D0cf3e6E84faC1A7Abc524ddfa66fb64f60` | [Ver no PolygonScan](https://polygonscan.com/address/0x460f9d0cf3e6e84fac1a7abc524ddfa66fb64f60) |

### **Links Diretos**

1. **Token (ERC-20):**
   ```
   https://polygonscan.com/token/0x59aa4eae743d608fbdd4205eba59b38dca755dd2
   ```

2. **Contrato:**
   ```
   https://polygonscan.com/address/0x59aa4eae743d608fbdd4205eba59b38dca755dd2
   ```

3. **Carteira Owner (com tokens):**
   ```
   https://polygonscan.com/token/0x59aa4eae743d608fbdd4205eba59b38dca755dd2?a=0x460f9d0cf3e6e84fac1a7abc524ddfa66fb64f60
   ```

---

## 📊 Dados do Contrato (PolygonScan)

### **Informações Básicas**

- **Nome do Token:** `NeoFlowOFF` (NEOFLW)
- **Tipo:** ERC-20 Token
- **Network:** Polygon Mainnet (Chain ID: 137)
- **Criador:** `0x460F9D0c...66fb64f60` (3 dias atrás)
- **Status:** ❌ **NÃO VERIFICADO** (mostra "Decompile Bytecode")

### **Transações**

- **Total:** 2 transações
- **Tipo:** Ambas são `Transfer`
- **Última:** 43 horas atrás

### **Saldo**

- **POL Balance:** 0 POL
- **Token Balance (Owner):** Verificar no link da carteira

---

## ⚠️ Observações Importantes

### **1. Contrato NÃO Verificado**

O contrato está deployado mas **não está verificado** no PolygonScan. Isso significa:

- ❌ Código-fonte não está público
- ❌ Não é possível ver as funções disponíveis
- ❌ Não é possível confirmar se tem `ContractMetadata`

### **2. Endereço Diferente do Arquivo**

**Arquivo `.token_address.txt`:**
```
0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
```

**Contrato Real (PolygonScan):**
```
0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2
```

⚠️ **Os endereços são diferentes!** Isso indica que:
- Pode haver múltiplos deploys
- O arquivo pode estar desatualizado
- Pode ser um contrato diferente

---

## 🔍 Próximos Passos

### **1. Verificar Qual Contrato Está Sendo Usado**

```bash
# Verificar endereço no arquivo
cat .token_address.txt

# Comparar com o contrato no PolygonScan
# 0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87 (arquivo)
# 0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2 (PolygonScan)
```

### **2. Verificar se o Contrato Tem ContractMetadata**

```bash
# Verificar o contrato no PolygonScan
source scripts/shell/setup_env.sh
ape run check_contract_metadata --network polygon:mainnet
```

**Nota:** O script vai ler de `.token_address.txt`. Se quiser verificar o contrato do PolygonScan, atualize o arquivo:

```bash
echo "0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2" > .token_address.txt
```

### **3. Verificar o Contrato no PolygonScan**

Para verificar o código-fonte:

1. Acesse: https://polygonscan.com/address/0x59aa4eae743d608fbdd4205eba59b38dca755dd2
2. Clique em **"Contract"** → **"Verify and Publish"**
3. Use os argumentos do construtor:
   ```
   0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000
   ```

---

## 📝 Checklist de Verificação

- [ ] Confirmar qual endereço está sendo usado (arquivo vs PolygonScan)
- [ ] Verificar se o contrato tem `ContractMetadata` (via script)
- [ ] Verificar código-fonte no PolygonScan
- [ ] Atualizar `.token_address.txt` com o endereço correto
- [ ] Atualizar `.env` com o endereço correto (se necessário)

---

## 🔗 Links Úteis

- **Token:** https://polygonscan.com/token/0x59aa4eae743d608fbdd4205eba59b38dca755dd2
- **Contrato:** https://polygonscan.com/address/0x59aa4eae743d608fbdd4205eba59b38dca755dd2
- **Owner:** https://polygonscan.com/address/0x460f9d0cf3e6e84fac1a7abc524ddfa66fb64f60
- **Owner com Tokens:** https://polygonscan.com/token/0x59aa4eae743d608fbdd4205eba59b38dca755dd2?a=0x460f9d0cf3e6e84fac1a7abc524ddfa66fb64f60

---

**Última atualização:** 2025-01-XX

