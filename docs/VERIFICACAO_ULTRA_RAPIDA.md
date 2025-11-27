# ⚡ Verificação Ultra Rápida - Sourcify (2 minutos)

## 🎯 Método Mais Rápido: Sourcify

**Por quê?**
- ✅ Não precisa preencher formulários complexos
- ✅ Funciona automaticamente com Polygonscan
- ✅ Apenas upload de arquivo JSON
- ✅ 2-3 minutos por contrato

---

## 📋 PASSO A PASSO (Super Rápido)

### 1. Acesse Sourcify
```
https://sourcify.dev/verifier
```

### 2. Preencha:

**Network:** Polygon Mainnet (137)

**Contract Address:**
- Token: `0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2`
- Claim: `0x407C037906d6441ECD4a3F9064eab2E6CF03b36b`
- Vault: `0x07E39107d4B35b64f9f2310B9A2B8e5262A4ee41`

**Upload File:**
```
artifacts/verification/sourcify_standard_json.json
```

### 3. Clique em "Verify"

**Pronto!** ✅ Polygonscan reconhecerá automaticamente.

---

## 📄 ARQUIVO NECESSÁRIO

**Caminho completo:**
```
/Users/nettomello/CODIGOS/TOKENS/neoflw-token/artifacts/verification/sourcify_standard_json.json
```

**O que contém:**
- ✅ Código-fonte completo
- ✅ ABI
- ✅ Configurações do compilador
- ✅ Tudo em um arquivo só!

**❌ NÃO precisa colar ABI separadamente!**

---

## 🔧 SE SOURCIFY NÃO FUNCIONAR: Polygonscan Manual

### 1. Acesse o contrato:
```
https://polygonscan.com/address/[ENDERECO]#code
```

### 2. Clique: "Contract" → "Verify and Publish"

### 3. Método: "Via Standard JSON Input"

### 4. Preencha:

**Compiler Version:**
```
v0.8.30+commit.73712a01
```

**License:**
```
MIT License (MIT)
```

**Standard JSON Input:**
- Upload: `artifacts/verification/sourcify_standard_json.json`

**Contract Name:**
- Token: `NeoFlowToken`
- Claim: `NeoFlowClaim`
- Vault: `StakingVault`

**Constructor Arguments (ABI-encoded):**

**Token:**
```
0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000
```

**Claim:**
```
00000000000000000000000059aa4eae743d608fbdd4205eba59b38dca755dd2
```

**Vault:**
```
00000000000000000000000059aa4eae743d608fbdd4205eba59b38dca755dd2
```

**Optimization:**
- ✅ Yes
- Runs: `200`

### 5. Clique em "Verify and Publish"

---

## 📊 RESUMO DOS ARGUMENTOS DO CONSTRUTOR

| Contrato | Argumento | Hex (ABI-encoded) |
|----------|-----------|-------------------|
| **Token** | `1_000_000_000 * 10**18` | `0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000` |
| **Claim** | `0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2` | `00000000000000000000000059aa4eae743d608fbdd4205eba59b38dca755dd2` |
| **Vault** | `0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2` | `00000000000000000000000059aa4eae743d608fbdd4205eba59b38dca755dd2` |

---

## 🔗 LINKS DIRETOS

### Sourcify:
- **Verificador:** https://sourcify.dev/verifier

### Contratos no Polygonscan:
- **Token:** https://polygonscan.com/address/0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2
- **Claim:** https://polygonscan.com/address/0x407C037906d6441ECD4a3F9064eab2E6CF03b36b
- **Vault:** https://polygonscan.com/address/0x07E39107d4B35b64f9f2310B9A2B8e5262A4ee41

---

## ✅ CHECKLIST RÁPIDO

- [ ] Arquivo `sourcify_standard_json.json` existe
- [ ] Acessou https://sourcify.dev/verifier
- [ ] Selecionou Polygon Mainnet (137)
- [ ] Colou endereço do contrato
- [ ] Fez upload do arquivo JSON
- [ ] Clicou em "Verify"
- [ ] Aguardou confirmação (2-3 minutos)
- [ ] Verificou no Polygonscan que apareceu "Verified"

---

**⏱️ Tempo total: 2-3 minutos por contrato!**

