# 🔐 Como Encontrar sua Private Key

## 📍 Onde encontrar sua Private Key

### Opção 1: MetaMask (Mais comum)

1. Abra o MetaMask
2. Clique no menu (3 linhas) → **Settings** → **Security & Privacy**
3. Role até **"Show Private Key"** ou **"Export Private Key"**
4. Digite sua senha do MetaMask
5. **COPIE a private key** (começa com `0x` e tem 66 caracteres)
6. **⚠️ NUNCA compartilhe essa chave!**

### Opção 2: Outras Wallets

- **Trust Wallet**: Settings → Wallets → (seu wallet) → Show Private Key
- **Coinbase Wallet**: Settings → Security → Show Recovery Phrase (depois derive private key)
- **Ledger/Trezor**: Não expõem private key (use outra wallet para deploy)

### Opção 3: Criar Nova Wallet Apenas para Deploy (Recomendado)

Se você não quer usar sua wallet principal:

1. Instale MetaMask (se não tiver)
2. Crie uma **nova conta** apenas para testes
3. Anote/exporte a private key dessa nova conta
4. Use apenas essa conta para deploy em testnets

## ⚠️ SEGURANÇA IMPORTANTE

- ❌ **NUNCA** compartilhe sua private key
- ❌ **NUNCA** cole em locais públicos
- ❌ **NUNCA** commite no Git (está no .gitignore)
- ✅ Use apenas em testnets (Sepolia/Goerli)
- ✅ Para mainnet, use hardware wallet

## 🚀 Como Importar no Ape

Depois de ter sua private key:

```bash
ape accounts import neoflow-admin
```

O comando vai pedir:

1. Cole sua private key (`0x...`)
2. Defina uma senha forte (você precisará dela para deploy)
3. Confirme a senha

## 💡 Dica: Criar Wallet de Teste

Se preferir criar uma wallet nova só para deploy:

1. **MetaMask**: Criar nova conta → Exportar private key
2. **Anotar em local seguro** (não commit no Git!)
3. **Usar apenas para testnets**

---

**FORMATO DA PRIVATE KEY:**
```
0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef
```
(66 caracteres, começa com `0x`)

