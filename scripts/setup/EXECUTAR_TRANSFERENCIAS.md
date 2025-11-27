# 🚀 Executar Transferências de Tokens

## Comando para Executar

```bash
cd /Users/nettomello/CODIGOS/TOKENS/neoflw-token
APE_NETWORK=polygon:mainnet python scripts/setup/transfer_100m_final.py
```

## O que vai acontecer:

1. **Script vai preparar as transferências:**
   - 100M NEOFLW para Claim
   - 100M NEOFLW para Vault

2. **Para cada transferência, você verá:**
   ```
   Sign:  [y/N]:
   ```
   - Digite `y` e pressione Enter
   - Digite a senha da wallet `neoflow-admin`
   - Confirme se quer deixar a wallet desbloqueada (recomendado `n`)

3. **Após cada transferência:**
   - Você verá a confirmação da transação
   - O script continuará para a próxima transferência

## ⚠️ IMPORTANTE:

- **Saldo de POL:** Certifique-se de ter pelo menos 0.02 POL na wallet
- **Senha:** Você precisará digitar a senha da wallet `neoflow-admin` duas vezes
- **Confirmação:** Confirme cada transação digitando `y`

## 📊 Endereços:

- **Token:** `0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2`
- **Claim:** `0x407C037906d6441ECD4a3F9064eab2E6CF03b36b`
- **Vault:** `0x07E39107d4B35b64f9f2310B9A2B8e5262A4ee41`

## 🔗 Verificar no Polygonscan:

Após as transferências, verifique:
- Claim: https://polygonscan.com/address/0x407C037906d6441ECD4a3F9064eab2E6CF03b36b
- Vault: https://polygonscan.com/address/0x07E39107d4B35b64f9f2310B9A2B8e5262A4ee41

