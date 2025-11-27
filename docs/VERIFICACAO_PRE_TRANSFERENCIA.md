# 🔍 Verificação Pré-Transferência de Tokens

**Data:** 2025-11-27  
**Status:** ⚠️ **AÇÃO NECESSÁRIA ANTES DE PROSSEGUIR**

---

## ⚠️ PROBLEMAS IDENTIFICADOS

### 1. **Endereços Divergentes**

Os endereços nos arquivos são **diferentes** dos endereços na documentação:

| Contrato | Arquivo | Documentação | Status |
|----------|---------|--------------|--------|
| **Token** | `0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87` | `0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2` | ❓ Divergente |
| **Claim** | `0xEE96C0813e84bb7Ea162b1594b8Bff61dB79A7Ca` | `0x407C037906d6441ECD4a3F9064eab2E6CF03b36b` | ❓ Divergente |
| **Vault** | `0x7A3109a7A978473142c655C3DBbfad4e5Bc37aeD` | `0x07E39107d4B35b64f9f2310B9A2B8e5262A4ee41` | ❓ Divergente |

**⚠️ CRÍTICO:** Precisamos confirmar qual conjunto de endereços está correto antes de fazer qualquer transferência!

---

### 2. **Saldo de POL Insuficiente**

- **Saldo atual:** 0.0005 POL
- **Necessário:** ~0.01-0.02 POL (para 2 transferências)
- **Status:** ⚠️ Saldo muito baixo

**Ação necessária:** Adicionar POL à wallet antes de fazer transferências.

---

### 3. **Contratos Não Encontrados**

A verificação não conseguiu confirmar se os contratos existem nos endereços dos arquivos:

- Token: Contrato não encontrado/verificado
- Claim: Código não encontrado
- Vault: Código não encontrado

**Possíveis causas:**

- Contratos não foram deployados nesses endereços
- Contratos não estão verificados no Polygonscan
- Endereços incorretos nos arquivos

---

## ✅ VERIFICAÇÕES REALIZADAS

### 1. Network

- ✅ Polygon Mainnet (Chain ID: 137)
- ✅ Provider: Alchemy

### 2. Wallet

- ✅ Wallet `neoflow-admin` carregada
- ✅ Endereço: `0x460F9D0cf3e6E84faC1A7Abc524ddfa66fb64f60`

### 3. Arquivos de Endereços

- ✅ Arquivos existem em `artifacts/addresses/`
- ✅ Formato dos endereços válido

---

## 🔍 PRÓXIMOS PASSOS - VERIFICAÇÃO MANUAL

### Passo 1: Confirmar Endereços Corretos

Verifique manualmente no Polygonscan qual conjunto de endereços está correto:

#### **Opção A: Endereços dos Arquivos**

- Token: https://polygonscan.com/address/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
- Claim: https://polygonscan.com/address/0xEE96C0813e84bb7Ea162b1594b8Bff61dB79A7Ca
- Vault: https://polygonscan.com/address/0x7A3109a7A978473142c655C3DBbfad4e5Bc37aeD

#### **Opção B: Endereços da Documentação**

- Token: https://polygonscan.com/address/0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2
- Claim: https://polygonscan.com/address/0x407C037906d6441ECD4a3F9064eab2E6CF03b36b
- Vault: https://polygonscan.com/address/0x07E39107d4B35b64f9f2310B9A2B8e5262A4ee41

**O que verificar:**

1. Qual endereço tem o contrato deployado?
2. Qual endereço tem o código verificado?
3. Qual endereço corresponde ao deploy mais recente?

---

### Passo 2: Atualizar Arquivos (Se Necessário)

Se os endereços da documentação estiverem corretos, atualize os arquivos:

```bash
# Atualizar endereço do Token
echo "0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2" > artifacts/addresses/.token_address.txt

# Atualizar endereço do Claim
echo "0x407C037906d6441ECD4a3F9064eab2E6CF03b36b" > artifacts/addresses/.claim_address.txt

# Atualizar endereço do Vault
echo "0x07E39107d4B35b64f9f2310B9A2B8e5262A4ee41" > artifacts/addresses/.vault_address.txt
```

---

### Passo 3: Adicionar POL à Wallet

**Wallet:** `0x460F9D0cf3e6E84faC1A7Abc524ddfa66fb64f60`

**Necessário:** ~0.02 POL (para 2 transferências + gas)

**Como adicionar:**

1. Comprar POL em exchange (Binance, Coinbase, etc)
2. Transferir para a wallet acima
3. Ou fazer bridge de outra rede

**Verificar saldo:**

- Polygonscan: https://polygonscan.com/address/0x460F9D0cf3e6E84faC1A7Abc524ddfa66fb64f60

---

### Passo 4: Verificar Saldo de Tokens

Após confirmar os endereços corretos, verificar:

1. **Saldo na wallet de deploy:**
   - Deve ser ~1,000,000,000 NEOFLW (1 bilhão)
   - Verificar no Polygonscan no contrato do Token

2. **Saldo nos contratos:**
   - Claim: Deve ser 0 NEOFLW (ainda não transferido)
   - Vault: Deve ser 0 NEOFLW (ainda não transferido)

---

## 📋 CHECKLIST ANTES DE TRANSFERIR

- [ ] Confirmar qual conjunto de endereços está correto
- [ ] Atualizar arquivos de endereços (se necessário)
- [ ] Verificar saldo de POL (mínimo 0.02 POL)
- [ ] Verificar saldo de tokens na wallet (1B NEOFLW)
- [ ] Confirmar que contratos existem nos endereços corretos
- [ ] Executar script de verificação novamente
- [ ] Se tudo OK, executar transferências

---

## 🚀 APÓS VERIFICAÇÃO

Quando tudo estiver confirmado:

```bash
# Executar verificação novamente
APE_NETWORK=polygon:mainnet python -c "
from ape import networks
with networks.polygon.mainnet.use_provider('alchemy'):
    from scripts.setup.verify_before_transfer import _verify
    _verify()
"

# Se verificação OK, executar transferências
# (script será criado após confirmação dos endereços)
```

---

## 📚 SCRIPTS DISPONÍVEIS

- **Verificação:** `scripts/setup/verify_before_transfer.py`
- **Transfer para Claim:** `scripts/setup/transfer_to_claim.py` (atualizado)
- **Transfer para Vault:** `scripts/setup/transfer_to_vault.py` (criado)
- **Transfer ambos:** `scripts/setup/transfer_100m_to_claim_and_vault.py` (criado)

---

**⚠️ IMPORTANTE:** Não execute transferências até confirmar os endereços corretos!

