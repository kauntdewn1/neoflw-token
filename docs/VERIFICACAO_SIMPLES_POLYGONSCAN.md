# ⚡ Verificação Simples no Polygonscan - Método Mais Rápido

**Método: Flattened Source Code** (copiar e colar)

---

## 🎯 PARA O TOKEN (Comece Aqui)

### 1. Acesse:
```
https://polygonscan.com/address/0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2#code
```

### 2. Clique: **"Contract"** → **"Verify and Publish"**

### 3. Escolha: **"Flattened Source Code"**

### 4. Preencha:

**Compiler Version:**
```
v0.8.18+commit.87f61d96
```

**License:**
```
MIT License (MIT)
```

**Contract Name:**
```
NeoFlowToken
```

**Flattened Source Code:**
- Abra: `artifacts/flattened/NeoFlowToken_flattened.sol`
- **Copie TODO** (Ctrl+A, Ctrl+C)
- **Cole aqui**

**Constructor Arguments (ABI-encoded):**
```
0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000
```

**Optimization:**
- ✅ **Yes**
- **Runs:** `200`

### 5. Clique: **"Verify and Publish"**

**Pronto!** ✅

---

## 📋 PARA CLAIM E VAULT

**Mesmo processo, mas:**

### Claim:
- **Endereço:** `0x407C037906d6441ECD4a3F9064eab2E6CF03b36b`
- **Contract Name:** `NeoFlowClaim`
- **Constructor Args:** `00000000000000000000000059aa4eae743d608fbdd4205eba59b38dca755dd2`
- **Flattened:** Precisa gerar (veja abaixo)

### Vault:
- **Endereço:** `0x07E39107d4B35b64f9f2310B9A2B8e5262A4ee41`
- **Contract Name:** `StakingVault`
- **Constructor Args:** `00000000000000000000000059aa4eae743d608fbdd4205eba59b38dca755dd2`
- **Flattened:** Precisa gerar (veja abaixo)

---

## 🔧 GERAR FLATTENED PARA CLAIM E VAULT

Se os arquivos flattened não existirem, você pode:

### Opção 1: Usar o código-fonte direto (mais rápido)

1. Abra `contracts/NeoFlowClaim.sol`
2. Copie TODO o conteúdo
3. No Polygonscan, cole no campo "Flattened Source Code"
4. O Polygonscan vai tentar resolver os imports automaticamente

**Se der erro de imports**, use a **Opção 2**.

### Opção 2: Criar flattened manualmente

1. Abra `contracts/NeoFlowClaim.sol`
2. Copie o código
3. Substitua os imports por:
   ```solidity
   // Substituir:
   import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
   import "@openzeppelin/contracts/access/Ownable.sol";
   
   // Por: copiar o conteúdo desses arquivos do OpenZeppelin
   // Ou usar um flatten tool online
   ```

### Opção 3: Usar ferramenta online

1. Acesse: https://flattener.online/
2. Cole o código do contrato
3. Ele vai gerar o flattened automaticamente
4. Copie e cole no Polygonscan

---

## 📊 RESUMO - O QUE COLAR

### ❌ NÃO precisa colar ABI separadamente!

O **Flattened Source Code** já contém tudo:
- ✅ Código-fonte completo
- ✅ Imports resolvidos
- ✅ Tudo em um arquivo só

**O Polygonscan extrai o ABI automaticamente do código!**

---

## 🔗 LINKS DIRETOS

### Verificar Contratos:
- **Token:** https://polygonscan.com/address/0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2#code
- **Claim:** https://polygonscan.com/address/0x407C037906d6441ECD4a3F9064eab2E6CF03b36b#code
- **Vault:** https://polygonscan.com/address/0x07E39107d4B35b64f9f2310B9A2B8e5262A4ee41#code

### Ferramentas Úteis:
- **Flattener Online:** https://flattener.online/
- **ABI Encoder:** https://abi.hashex.org/

---

## ✅ CHECKLIST RÁPIDO

- [ ] Acessei o contrato no Polygonscan
- [ ] Cliquei em "Contract" → "Verify and Publish"
- [ ] Escolhi "Flattened Source Code"
- [ ] Preenchi: Compiler v0.8.18, License MIT
- [ ] Colei código flattened completo
- [ ] Preenchi constructor args (hex)
- [ ] Optimization: Yes, Runs: 200
- [ ] Cliquei em "Verify and Publish"

---

**⏱️ Tempo: 3-5 minutos por contrato**

**✅ Método mais simples e direto!**

