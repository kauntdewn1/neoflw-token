# ⚡ Verificação Rápida de Contratos - Polygon Mainnet

**Método mais rápido e fácil: Sourcify** (recomendado)

---

## 🚀 OPÇÃO 1: SOURCIFY (Mais Rápido e Fácil) ⭐

### ✅ Vantagens:
- ✅ **Mais rápido** - apenas upload de arquivos
- ✅ **Funciona automaticamente** com Polygonscan
- ✅ **Não precisa preencher formulários** complexos
- ✅ **Suporta múltiplos contratos** de uma vez

### 📋 Passo a Passo:

#### 1. Acesse Sourcify
```
https://sourcify.dev/
```

#### 2. Clique em "Verify Contract"
- Ou acesse diretamente: https://sourcify.dev/verifier

#### 3. Selecione a Rede
- **Network:** Polygon Mainnet
- **Chain ID:** 137

#### 4. Preencha o Endereço do Contrato

**Token:**
```
0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2
```

**Claim:**
```
0x407C037906d6441ECD4a3F9064eab2E6CF03b36b
```

**Vault:**
```
0x07E39107d4B35b64f9f2310B9A2B8e5262A4ee41
```

#### 5. Upload dos Arquivos

**Arquivo principal necessário:**
```
artifacts/verification/sourcify_standard_json.json
```

**Localização completa:**
```
/Users/nettomello/CODIGOS/TOKENS/neoflw-token/artifacts/verification/sourcify_standard_json.json
```

#### 6. Clique em "Verify"
- Pronto! ✅

---

## 🔧 OPÇÃO 2: POLYGONSCAN (Manual)

### 📋 Passo a Passo:

#### 1. Acesse o Contrato no Polygonscan

**Token:**
```
https://polygonscan.com/address/0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2#code
```

**Claim:**
```
https://polygonscan.com/address/0x407C037906d6441ECD4a3F9064eab2E6CF03b36b#code
```

**Vault:**
```
https://polygonscan.com/address/0x07E39107d4B35b64f9f2310B9A2B8e5262A4ee41#code
```

#### 2. Clique em "Contract" → "Verify and Publish"

#### 3. Escolha o Método: **"Via Standard JSON Input"**

#### 4. Preencha os Campos:

**Compiler Version:**
```
v0.8.30+commit.73712a01
```

**License:**
```
MIT License (MIT)
```

**Standard JSON Input:**
- Clique em "Choose File"
- Selecione: `artifacts/verification/sourcify_standard_json.json`

**Contract Name:**
- **Token:** `NeoFlowToken`
- **Claim:** `NeoFlowClaim`
- **Vault:** `StakingVault`

**Constructor Arguments (ABI-encoded):**

**Para Token:**
```
0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000
```
*(1,000,000,000 * 10^18 = 1 bilhão de tokens)*

**Para Claim:**
```
00000000000000000000000059aa4eae743d608fbdd4205eba59b38dca755dd2
```
*(Endereço do token: 0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2)*

**Para Vault:**
```
00000000000000000000000059aa4eae743d608fbdd4205eba59b38dca755dd2
```
*(Endereço do token: 0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2)*

#### 5. Optimization Settings:
- ✅ **Yes** (habilitado)
- **Runs:** `200`

#### 6. Clique em "Verify and Publish"

---

## 📄 O QUE COLAR DE ABI?

### ❌ NÃO precisa colar ABI separadamente!

O **Standard JSON Input** já contém tudo:
- ✅ Código-fonte
- ✅ ABI
- ✅ Metadados
- ✅ Configurações do compilador

**Arquivo a usar:**
```
artifacts/verification/sourcify_standard_json.json
```

---

## 🎯 RESUMO RÁPIDO (Sourcify - Recomendado)

1. **Acesse:** https://sourcify.dev/verifier
2. **Rede:** Polygon Mainnet (137)
3. **Endereço:** Cole o endereço do contrato
4. **Upload:** `artifacts/verification/sourcify_standard_json.json`
5. **Verify:** Clique e pronto! ✅

**Tempo estimado:** 2-3 minutos por contrato

---

## 📋 CHECKLIST RÁPIDO

### Antes de Verificar:
- [ ] Arquivo `sourcify_standard_json.json` existe em `artifacts/verification/`
- [ ] Endereço do contrato está correto
- [ ] Você está na rede correta (Polygon Mainnet)

### Durante Verificação (Sourcify):
- [ ] Rede selecionada: Polygon Mainnet (137)
- [ ] Endereço do contrato preenchido
- [ ] Arquivo JSON carregado
- [ ] Clicou em "Verify"

### Após Verificação:
- [ ] Status mostra "Verified" ou "Fully Verified"
- [ ] Código aparece no Polygonscan automaticamente
- [ ] Contrato mostra badge "Verified"

---

## 🔗 LINKS ÚTEIS

### Sourcify:
- **Verificador:** https://sourcify.dev/verifier
- **Documentação:** https://docs.sourcify.dev/

### Polygonscan:
- **Token:** https://polygonscan.com/address/0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2
- **Claim:** https://polygonscan.com/address/0x407C037906d6441ECD4a3F9064eab2E6CF03b36b
- **Vault:** https://polygonscan.com/address/0x07E39107d4B35b64f9f2310B9A2B8e5262A4ee41

### Arquivos:
- **Standard JSON:** `artifacts/verification/sourcify_standard_json.json`

---

## 💡 DICA PRO

**Use Sourcify primeiro!** É mais rápido e:
- ✅ Funciona automaticamente com Polygonscan
- ✅ Não precisa preencher formulários complexos
- ✅ Suporta múltiplos contratos
- ✅ Mais confiável

**Se Sourcify não funcionar**, aí sim use Polygonscan manual.

---

## ⚠️ PROBLEMAS COMUNS

### "Contract not found"
- Verifique se o endereço está correto
- Certifique-se que está na rede correta (Polygon Mainnet)

### "Compilation failed"
- Verifique se o arquivo JSON está correto
- Certifique-se que a versão do compilador está correta

### "Constructor arguments mismatch"
- Para Token: use o hex do initial supply (1B tokens)
- Para Claim/Vault: use o hex do endereço do token

---

**✅ Pronto! Use Sourcify para verificação rápida!**

