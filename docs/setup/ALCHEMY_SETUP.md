# 🔧 Como Configurar Alchemy API Key

## 📍 Onde encontrar sua API Key

### Opção 1: Pelo App Dashboard (Recomendado)

1. No painel da Alchemy, clique em **"App Dashboard"** (menu lateral)
2. Selecione seu app (ex: "Neo's First App")
3. Procure por **"API Key"** ou **"View Key"**
4. Copie a chave completa

### Opção 2: Pela URL do Endpoint

Se você ver uma URL como:
```
https://eth-sepolia.g.alchemy.com/v2/h47p2nw-NDUbS0nQfSUuV
```

A parte após `/v2/` é sua API key:
```
h47p2nw-NDUbS0nQfSUuV
```

## ⚠️ IMPORTANTE: Node API vs Token API

- ✅ **Node API** → Use para deploy (RPC endpoint)
- ❌ **Token API** → É só para dados de tokens, não serve para deploy

Você está vendo a **Token API** na imagem, mas precisa da **Node API**!

## 🔑 Criar App para Sepolia (se não tiver)

1. No painel da Alchemy, clique em **"Create App"**
2. **Name**: `neoflow-sepolia`
3. **Chain**: `Ethereum`
4. **Network**: `Sepolia` (ou `Goerli` se preferir)
5. Clique em **"Create App"**
6. Copie a **API Key** do app criado

## 📝 Configurar no .env.local

1. Abra `.env.local`
2. Cole sua API key:
```env
ALCHEMY_API_KEY=h47p2nw-NDUbS0nQfSUuV
```

3. Exporte a variável:
```bash
export ALCHEMY_API_KEY=h47p2nw-NDUbS0nQfSUuV
```

## ✅ Verificar se funciona

```bash
# Testar conexão
curl -X POST https://eth-sepolia.g.alchemy.com/v2/SUA_API_KEY \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}'
```

Se retornar um número de bloco, está funcionando! ✅

