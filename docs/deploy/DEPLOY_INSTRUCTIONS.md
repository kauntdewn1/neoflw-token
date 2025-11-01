# 🚀 Instruções de Deploy - $NEOFLW

## 📋 Pré-requisitos

1. **Conta criptografada**: Importe ou crie a conta `neoflow-admin`
2. **API Key Alchemy**: Configure no `.env`
3. **Rede de teste**: Sepolia (recomendado) ou Goerli

---

## ✅ Passo 1: Criar/Importar Conta

```bash
# Opção A: Importar conta existente
ape accounts import neoflow-admin
# Cole sua private key e defina senha

# Opção B: Gerar nova conta (não recomendado para produção)
ape accounts generate neoflow-admin
```

---

## ✅ Passo 2: Configurar API Keys

1. Copie `.env.example` para `.env`:
```bash
cp .env.example .env
```

2. Edite `.env` e adicione suas keys:
```env
ALCHEMY_API_KEY=your_alchemy_key_here
ETHERSCAN_API_KEY=your_etherscan_key_here
```

3. Exporte as variáveis:
```bash
export ALCHEMY_API_KEY=your_key
export ETHERSCAN_API_KEY=your_key
```

---

## ✅ Passo 3: Deploy do Token

```bash
# Em Sepolia (recomendado)
npm run deploy:token -- --network ethereum:sepolia

# Ou em Goerli (se ainda funcionar)
npm run deploy:token
```

**IMPORTANTE**: Após o deploy, copie o endereço do token!

Exemplo de output:
```
NEOFLW Token deployed at: 0x1234567890123456789012345678901234567890
```

---

## ✅ Passo 4: Atualizar e Deploy do Vault

1. Edite `scripts/deploy_vault.py`:
```python
token_address = "0x1234567890123456789012345678901234567890"  # 👈 Cole o endereço do token
```

2. Faça deploy do vault:
```bash
npm run deploy:vault -- --network ethereum:sepolia
```

---

## ✅ Passo 5: Verificar Contratos no Etherscan

```bash
# Verificar token
npm run verify:token -- --network ethereum:sepolia

# Verificar vault
npm run verify:vault -- --network ethereum:sepolia
```

---

## 🔗 Links Úteis

- **Alchemy**: https://www.alchemy.com/ (criar conta e obter API key)
- **Etherscan Sepolia**: https://sepolia.etherscan.io/
- **Sepolia Faucet**: https://sepoliafaucet.com/

---

## ⚠️ Notas

- Sepolia é a rede de teste atual recomendada (Goerli foi desativado)
- Certifique-se de ter Sepolia ETH na conta para gas
- Guarde os endereços dos contratos deployados!

