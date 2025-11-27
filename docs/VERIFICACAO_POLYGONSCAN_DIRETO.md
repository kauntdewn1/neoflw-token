# ✅ Verificação no Polygonscan - Método Direto e Rápido

**Método mais confiável para Polygon Mainnet**

---

## 🎯 MÉTODO: Flattened Source Code (Mais Simples)

### ✅ Vantagens:
- ✅ **Mais rápido** - apenas copiar e colar código
- ✅ **Funciona sempre** - não depende de arquivos JSON
- ✅ **Menos erros** - método mais direto
- ✅ **Não precisa de ABI separado**

---

## 📋 PASSO A PASSO - TOKEN

### 1. Acesse o Contrato no Polygonscan

```
https://polygonscan.com/address/0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2#code
```

### 2. Clique em "Contract" → "Verify and Publish"

### 3. Escolha o Método: **"Flattened Source Code"**

### 4. Preencha os Campos:

**Compiler Version:**
```
v0.8.18+commit.87f61d96
```
*(ou a versão que você usou no deploy - verifique no terminal do deploy)*

**License:**
```
MIT License (MIT)
```

**Contract Name:**
```
NeoFlowToken
```

**Flattened Source Code:**
- Abra o arquivo: `artifacts/flattened/NeoFlowToken_flattened.sol`
- **Copie TODO o conteúdo** (Ctrl+A, Ctrl+C)
- **Cole no campo** do Polygonscan

**Constructor Arguments (ABI-encoded):**
```
0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000
```

**Optimization:**
- ✅ **Yes** (habilitado)
- **Runs:** `200`

**EVM Version:**
- Deixe como `default` ou `london`

### 5. Clique em "Verify and Publish"

---

## 📋 PASSO A PASSO - CLAIM

### 1. Acesse:
```
https://polygonscan.com/address/0x407C037906d6441ECD4a3F9064eab2E6CF03b36b#code
```

### 2. Clique: "Contract" → "Verify and Publish"

### 3. Método: **"Flattened Source Code"**

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
NeoFlowClaim
```

**Flattened Source Code:**
- **Precisa gerar o arquivo flattened para Claim:**
```bash
cd /Users/nettomello/CODIGOS/TOKENS/neoflw-token
ape compile --format flattened
```
- Procure por: `artifacts/flattened/NeoFlowClaim_flattened.sol`
- Se não existir, copie o código de `contracts/NeoFlowClaim.sol` e adicione os imports do OpenZeppelin manualmente

**Constructor Arguments:**
```
00000000000000000000000059aa4eae743d608fbdd4205eba59b38dca755dd2
```

**Optimization:**
- ✅ Yes
- Runs: `200`

### 5. Clique em "Verify and Publish"

---

## 📋 PASSO A PASSO - VAULT

### 1. Acesse:
```
https://polygonscan.com/address/0x07E39107d4B35b64f9f2310B9A2B8e5262A4ee41#code
```

### 2. Clique: "Contract" → "Verify and Publish"

### 3. Método: **"Flattened Source Code"**

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
StakingVault
```

**Flattened Source Code:**
- Gere o arquivo flattened:
```bash
ape compile --format flattened
```
- Procure por: `artifacts/flattened/StakingVault_flattened.sol`

**Constructor Arguments:**
```
00000000000000000000000059aa4eae743d608fbdd4205eba59b38dca755dd2
```

**Optimization:**
- ✅ Yes
- Runs: `200`

### 5. Clique em "Verify and Publish"

---

## 🔧 GERAR ARQUIVOS FLATTENED

Se os arquivos flattened não existirem:

```bash
cd /Users/nettomello/CODIGOS/TOKENS/neoflw-token

# Compilar e gerar flattened
ape compile --format flattened

# Os arquivos estarão em:
# artifacts/flattened/NeoFlowToken_flattened.sol
# artifacts/flattened/NeoFlowClaim_flattened.sol
# artifacts/flattened/StakingVault_flattened.sol
```

---

## 📊 RESUMO DOS ARGUMENTOS DO CONSTRUTOR

| Contrato | Argumento | Hex (ABI-encoded) |
|----------|-----------|-------------------|
| **Token** | `1_000_000_000 * 10**18` | `0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000` |
| **Claim** | `0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2` | `00000000000000000000000059aa4eae743d608fbdd4205eba59b38dca755dd2` |
| **Vault** | `0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2` | `00000000000000000000000059aa4eae743d608fbdd4205eba59b38dca755dd2` |

---

## ⚠️ IMPORTANTE: Versão do Compilador

**Verifique qual versão foi usada no deploy:**

Olhe no terminal onde você fez o deploy. Deve aparecer algo como:
```
INFO:     Compiling using Solidity compiler '0.8.30+commit.73712a01'.
```

**Use EXATAMENTE essa versão no Polygonscan!**

Se não souber, tente:
- `v0.8.18+commit.87f61d96` (mais comum)
- `v0.8.30+commit.73712a01` (se foi usado no deploy)

---

## 🔗 LINKS DIRETOS

### Contratos:
- **Token:** https://polygonscan.com/address/0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2#code
- **Claim:** https://polygonscan.com/address/0x407C037906d6441ECD4a3F9064eab2E6CF03b36b#code
- **Vault:** https://polygonscan.com/address/0x07E39107d4B35b64f9f2310B9A2B8e5262A4ee41#code

---

## ✅ CHECKLIST RÁPIDO

- [ ] Acessei o contrato no Polygonscan
- [ ] Cliquei em "Contract" → "Verify and Publish"
- [ ] Escolhi método "Flattened Source Code"
- [ ] Preenchi versão do compilador (correta!)
- [ ] Colei código flattened completo
- [ ] Preenchi constructor arguments (hex)
- [ ] Marquei Optimization: Yes, Runs: 200
- [ ] Cliquei em "Verify and Publish"
- [ ] Aguardei confirmação

---

**⏱️ Tempo: 5-10 minutos por contrato**

**✅ Método mais confiável e direto!**

