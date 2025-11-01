# 🔍 Usando Blockscout para Visualizar Token (Alternativa ao Etherscan)

## 🌐 O que é Blockscout?

**Blockscout** é um explorer blockchain open-source que oferece funcionalidades similares ao Etherscan, mas com **suporte completo para tokens customizados em testnets**.

### **Vantagens sobre Etherscan:**

- ✅ **Suporte melhor para testnets** (incluindo Sepolia)
- ✅ **Open-source** - você pode rodar sua própria instância
- ✅ **Mais flexível** para tokens customizados
- ✅ **Interface similar** ao Etherscan (familiar)

---

## 🚀 Opção 1: Usar Blockscout Público (Mais Fácil)

### **Instances Públicos para Sepolia:**

1. **Sepolia Blockscout (oficial):**
   ```
   https://sepolia.blockscout.com/
   ```

2. **Alternativas:**
   - Busque por "sepolia blockscout" no navegador
   - Alguns projetos hospedam instances públicos

### **Como visualizar seu token:**

1. **Acesse:** https://sepolia.blockscout.com/
2. **Busque pelo endereço:**
   ```
   0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
   ```
3. **Visualize:**
   - Informações do token
   - Logo (se configurado)
   - Transações
   - Holders

### **Se o logo não aparecer:**

Blockscout pode requerer que você:
1. Faça login (se disponível)
2. Ou use a API para adicionar metadados
3. Ou o logo aparecerá automaticamente se os metadados estiverem no contrato

---

## 🏠 Opção 2: Deploy Local do Blockscout (Controle Total)

### **Prós:**
- ✅ **Controle completo** sobre visualização
- ✅ **Suporte total** a tokens custom
- ✅ **Testes ilimitados**
- ✅ **Customização** da interface

### **Contras:**
- ⚠️ Requer Docker e conhecimento técnico
- ⚠️ Configuração inicial mais complexa
- ⚠️ Requer infraestrutura (servidor/local)

### **Requisitos:**

- Docker e Docker Compose
- Node.js (para algumas partes)
- PostgreSQL (gerenciado via Docker)
- RPC URL do Sepolia (Alchemy, Infura, etc)

### **Instalação Rápida:**

```bash
# 1. Clone o repositório
git clone https://github.com/blockscout/blockscout.git
cd blockscout

# 2. Configure variáveis de ambiente
cp .env.example .env

# 3. Edite .env para Sepolia:
# ETHEREUM_JSONRPC_VARIANT=geth
# ETHEREUM_JSONRPC_HTTP_URL=https://sepolia.infura.io/v3/YOUR_KEY
# ETHEREUM_JSONRPC_WS_URL=wss://sepolia.infura.io/v3/YOUR_KEY
# CHAIN_ID=11155111
# DATABASE_URL=postgresql://postgres:@postgres:5432/blockscout

# 4. Inicie com Docker
docker-compose up -d

# 5. Aguarde alguns minutos para sincronizar
# 6. Acesse: http://localhost:4000
```

### **Configuração Detalhada:**

Veja documentação completa em:
- **GitHub:** https://github.com/blockscout/blockscout
- **Docs:** https://docs.blockscout.com/

---

## 📝 Configurando Token no Blockscout

### **Método 1: Via Interface Web (se disponível)**

1. **Acesse seu token no Blockscout**
2. **Procure por "Update Token Info" ou "Edit"**
3. **Preencha:**
   - Token Name: `NeoFlowOFF`
   - Token Symbol: `NEOFLW`
   - Token Logo: `https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i`
   - Decimals: `18`
   - Website: `neoflowoff.eth`

### **Método 2: Via API (se disponível)**

```bash
# Exemplo de requisição (ajuste conforme a API do Blockscout)
curl -X POST https://sepolia.blockscout.com/api/v1/tokens/update \
  -H "Content-Type: application/json" \
  -d '{
    "address": "0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87",
    "name": "NeoFlowOFF",
    "symbol": "NEOFLW",
    "logo_url": "https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i",
    "decimals": 18
  }'
```

**⚠️ Nota:** A API pode variar entre instances do Blockscout.

### **Método 3: Metadados do Contrato**

Se seu contrato implementa `tokenURI()` ou metadados ERC-721/ERC-1155, o Blockscout pode detectar automaticamente.

---

## 🔗 Informações do Token para Blockscout

```
Token Address: 0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
Network: Ethereum Sepolia (Chain ID: 11155111)
Name: NeoFlowOFF
Symbol: NEOFLW
Decimals: 18
Logo URL: https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i
Website: neoflowoff.eth
Description: Token oficial do protocolo NEOFLW - um protocolo modular DAO focado em governança descentralizada e crescimento sustentável.
```

---

## 📊 Comparação: Blockscout vs Etherscan

| Recurso | Blockscout | Etherscan |
|---------|------------|-----------|
| **Suporte Testnet** | ✅ Excelente | ⚠️ Limitado |
| **Open-Source** | ✅ Sim | ❌ Não |
| **Deploy Próprio** | ✅ Sim | ❌ Não |
| **API Pública** | ✅ Disponível | ✅ Disponível |
| **Atualização Logo** | ✅ Mais fácil | ⚠️ Manual apenas |
| **Popularidade** | ⭐⭐⭐ Bom | ⭐⭐⭐⭐⭐ Excelente |
| **UI Familiar** | ✅ Similar | ✅ Referência |

---

## 💡 Casos de Uso

### **Quando usar Blockscout:**

1. ✅ **Desenvolvimento em testnet** (Sepolia, Goerli, etc)
2. ✅ **Testes visuais** do token antes de produção
3. ✅ **Quando Etherscan login está indisponível**
4. ✅ **Quando precisa de controle total** (deploy próprio)
5. ✅ **Projetos open-source** que precisam de explorer próprio

### **Quando usar Etherscan:**

1. ✅ **Produção em mainnet** (padrão da indústria)
2. ✅ **Visibilidade máxima** (mais conhecido)
3. ✅ **Integração com outras ferramentas** que usam Etherscan

---

## 🔧 Troubleshooting

### **Token não aparece no Blockscout:**

1. **Verifique se está na rede correta** (Sepolia)
2. **Aguarde sincronização** (pode levar alguns minutos)
3. **Verifique se o endereço está correto**
4. **Tente usar RPC diferente** se estiver rodando localmente

### **Logo não aparece:**

1. **Verifique se a URL IPFS está acessível:**
   ```bash
   curl https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i
   ```
2. **Tente adicionar manualmente via interface**
3. **Verifique formato da imagem** (PNG, SVG, etc)
4. **Use gateway IPFS diferente** se necessário

---

## 🔗 Links Úteis

- **Blockscout Sepolia:** https://sepolia.blockscout.com/
- **GitHub Blockscout:** https://github.com/blockscout/blockscout
- **Documentação:** https://docs.blockscout.com/
- **Token no Etherscan:** https://sepolia.etherscan.io/token/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
- **Logo IPFS:** https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i

---

## ✅ Resumo Rápido

**Para visualização rápida:**
1. Acesse https://sepolia.blockscout.com/
2. Busque: `0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87`
3. Visualize o token com logo!

**Para deploy próprio:**
1. Clone: `git clone https://github.com/blockscout/blockscout`
2. Configure Docker
3. Execute: `docker-compose up`
4. Acesse: `http://localhost:4000`

---

**Blockscout é uma excelente alternativa ao Etherscan, especialmente para testnets!** 🚀

