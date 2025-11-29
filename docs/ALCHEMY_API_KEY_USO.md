# 🔑 Como o Ape Framework Usa a Alchemy API Key

## 📋 Situação Atual

### ✅ Configuração Correta

1. **`.env`** tem a chave:
   ```env
   ALCHEMY_API_KEY=F7WGOxare2E3WPbjGiBFQ
   ```

2. **`ape-config.yaml`** está configurado:
   ```yaml
   networks:
     polygon:
       mainnet:
         default_provider: alchemy
         providers:
           alchemy:
             api_key: ${ALCHEMY_API_KEY}  # ← Lê da variável de ambiente
   ```

### ⚠️ Problema

O Ape Framework **NÃO lê o arquivo `.env` automaticamente**. Ele precisa que a variável `ALCHEMY_API_KEY` esteja **exportada no shell** como variável de ambiente.

---

## ✅ Solução: Carregar Variáveis Antes de Usar

### **Opção 1: Usar o Script de Setup (Recomendado)**

```bash
# Carregar variáveis do .env
source scripts/shell/setup_env.sh

# Agora executar comandos do Ape
ape run check_contract_metadata --network polygon:mainnet
```

### **Opção 2: Exportar Manualmente**

```bash
# Exportar a chave manualmente
export ALCHEMY_API_KEY=F7WGOxare2E3WPbjGiBFQ

# Executar comandos
ape run check_contract_metadata --network polygon:mainnet
```

### **Opção 3: Usar em Uma Linha**

```bash
# Carregar e executar em uma linha
source scripts/shell/setup_env.sh && ape run check_contract_metadata --network polygon:mainnet
```

---

## 🔍 Verificar se Está Funcionando

### Teste 1: Verificar Variável Exportada

```bash
# Verificar se a variável está exportada
echo $ALCHEMY_API_KEY

# Deve mostrar: F7WGOxare2E3WPbjGiBFQ
```

### Teste 2: Verificar Conexão RPC

```bash
# Carregar variáveis
source scripts/shell/setup_env.sh

# Testar conexão (deve conectar via Alchemy)
ape run check_contract_metadata --network polygon:mainnet
```

Se conectar com sucesso, você verá:
```
INFO:     Connecting to existing Geth node at https://polygon-mainnet.g.alchemy.com/v2/[hidden].
```

---

## 📝 Variáveis no .env

### Para Backend (Ape Framework)

```env
# Usado pelo ape-config.yaml
ALCHEMY_API_KEY=F7WGOxare2E3WPbjGiBFQ
ETHERSCAN_API_KEY=WYII9Y7JICTMERA89H6P3X9C3JKTIW8V75
```

### Para Frontend (Next.js)

```env
# Usado pelo frontend (Next.js carrega .env automaticamente)
NEXT_PUBLIC_ALCHEMY_API_KEY=F7WGOxare2E3WPbjGiBFQ
NEXT_PUBLIC_ALCHEMY_POLYGON_MAINNET_API_KEY=https://polygon-mainnet.g.alchemy.com/v2/F7WGOxare2E3WPbjGiBFQ
NEXT_PUBLIC_ALCHEMY_MAINNET_API_KEY=https://eth-mainnet.g.alchemy.com/v2/F7WGOxare2E3WPbjGiBFQ
```

**Diferença:**
- **Backend (Ape)**: Precisa exportar manualmente ou usar `source scripts/shell/setup_env.sh`
- **Frontend (Next.js)**: Carrega automaticamente do `.env` (precisa do prefixo `NEXT_PUBLIC_`)

---

## 🚀 Comandos Prontos para Usar

### Verificar ContractMetadata

```bash
source scripts/shell/setup_env.sh && ape run check_contract_metadata --network polygon:mainnet
```

### Deploy Token

```bash
source scripts/shell/setup_env.sh && ape run scripts/deploy/deploy_token --network polygon:mainnet
```

### Deploy Vault

```bash
source scripts/shell/setup_env.sh && ape run scripts/deploy/deploy_vault --network polygon:mainnet
```

---

## 💡 Dica: Criar Alias no Shell

Adicione ao seu `~/.zshrc` ou `~/.bashrc`:

```bash
# Alias para carregar env e executar ape
alias ape-env='source /Users/nettomello/CODIGOS/TOKENS/neoflw-token/scripts/shell/setup_env.sh'
alias ape-run='source /Users/nettomello/CODIGOS/TOKENS/neoflw-token/scripts/shell/setup_env.sh && ape run'
```

Depois use:
```bash
ape-env
ape-run check_contract_metadata --network polygon:mainnet
```

---

## ✅ Resumo

| Item | Status |
|------|--------|
| `.env` tem `ALCHEMY_API_KEY` | ✅ Sim |
| `ape-config.yaml` configurado | ✅ Sim |
| Variável exportada no shell | ⚠️ Precisa carregar |
| **Solução** | `source scripts/shell/setup_env.sh` |

---

**Última atualização:** 2025-01-XX

