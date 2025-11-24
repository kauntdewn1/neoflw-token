# 🐚 Scripts Shell do Projeto NEOFLW

## 📁 Scripts Disponíveis

### **1. setup_env.sh**
Exporta variáveis de ambiente do `.env` para o shell atual.

**Uso:**
```bash
source scripts/shell/setup_env.sh
```

**O que faz:**
- Carrega variáveis do `.env`
- Exporta `ALCHEMY_API_KEY`, `ETHERSCAN_API_KEY`
- Configura variáveis WEB3 para Ape Framework

---

### **2. setup_wallet.sh**
Script interativo para configurar wallet e verificar setup.

**Uso:**
```bash
bash scripts/shell/setup_wallet.sh
```

**O que faz:**
- Verifica/cria arquivo `.env`
- Exporta variáveis de ambiente
- Verifica se conta `neoflow-admin` existe
- Verifica saldo na rede
- Oferece opções para importar/criar conta

---

### **3. deploy.sh**
Script simplificado para deploy do token.

**Uso:**
```bash
bash scripts/shell/deploy.sh
```

**O que faz:**
- Carrega variáveis do `.env`
- Verifica API keys
- Verifica conta configurada
- Compila contratos
- Faz deploy do token

**Nota:** Usa `APE_NETWORK` do `.env` ou padrão `polygon:mainnet`

---

### **4. RETRY_DEPLOY.sh**
Script para retentar deploy com delay (evita rate limiting).

**Uso:**
```bash
bash scripts/shell/RETRY_DEPLOY.sh
```

**O que faz:**
- Aguarda 30 segundos
- Carrega variáveis do `.env`
- Tenta deploy novamente

---

### **5. recuperar_senha.sh**
Script interativo para recuperar/redefinir senha da conta APE.

**Uso:**
```bash
bash scripts/shell/recuperar_senha.sh
```

**O que faz:**
- Oferece opções para recuperar senha
- Permite reimportar conta com nova senha
- Permite criar nova conta

---

## ⚠️ Segurança

**IMPORTANTE:** Todos os scripts foram atualizados para:
- ✅ **NÃO** conter API keys hardcoded
- ✅ Carregar variáveis do `.env`
- ✅ Verificar se `.env` existe antes de executar

**Antes de usar:**
1. Certifique-se de ter um arquivo `.env` configurado
2. Use `source scripts/shell/setup_env.sh` para exportar variáveis
3. Nunca commite o arquivo `.env` (está no `.gitignore`)

---

## 📋 Exemplos de Uso

### **Setup Completo:**
```bash
# 1. Configurar wallet
bash scripts/shell/setup_wallet.sh

# 2. Exportar variáveis
source scripts/shell/setup_env.sh

# 3. Deploy
make deploy-token
```

### **Deploy Rápido:**
```bash
# Carregar variáveis e fazer deploy
source scripts/shell/setup_env.sh && make deploy-token
```

### **Retentar Deploy:**
```bash
# Se o deploy falhar por rate limiting
bash scripts/shell/RETRY_DEPLOY.sh
```

---

## 🔄 Migração de Comandos Antigos

Se você estava usando comandos antigos na raiz:

| Antigo | Novo |
|--------|------|
| `source setup_env.sh` | `source scripts/shell/setup_env.sh` |
| `bash deploy.sh` | `bash scripts/shell/deploy.sh` |
| `bash setup_wallet.sh` | `bash scripts/shell/setup_wallet.sh` |

---

**✅ Scripts organizados e seguros!**

