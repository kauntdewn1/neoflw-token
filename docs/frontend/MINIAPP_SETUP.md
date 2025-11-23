# 📱 Setup MiniApp - Telegram & Farcaster

## 🎯 Resumo Rápido

O DApp NEOFLW está configurado para funcionar como **MiniApp** no Telegram e **Frame** no Farcaster.

---

## ✅ O Que Foi Configurado

### **1. Frontend**

- ✅ `src/utils/miniapp.ts` - Utilitários de detecção
- ✅ `src/hooks/useTelegram.ts` - Hook para Telegram
- ✅ `src/hooks/useFarcaster.ts` - Hook para Farcaster
- ✅ `src/components/MiniAppLayout.tsx` - Layout adaptativo
- ✅ `src/app/providers.tsx` - WalletConnect adicionado
- ✅ `src/app/layout.tsx` - Meta tags para Telegram/Farcaster
- ✅ `next.config.js` - Headers para permitir iframe

### **2. Documentação**

- ✅ `docs/frontend/MINIAPP_TELEGRAM_FARCASTER.md` - Guia completo
- ✅ `docs/frontend/MINIAPP_SETUP.md` - Este arquivo

---

## 🚀 Próximos Passos

### **1. Instalar Dependências**

```bash
cd frontend
npm install @walletconnect/web3modal
```

**Nota:** Thirdweb pode ser adicionado depois se necessário para embed wallet.

### **2. Obter WalletConnect Project ID**

1. Acesse: https://cloud.walletconnect.com/
2. Crie projeto
3. Copie Project ID
4. Adicione ao `.env`:
   ```env
   NEXT_PUBLIC_WALLETCONNECT_PROJECT_ID=seu-project-id
   ```

### **3. Configurar Telegram Bot**

1. Abra BotFather no Telegram: https://t.me/botfather
2. Criar bot: `/newbot`
3. Obter token
4. Criar MiniApp: `/newapp`
5. Definir URL: `https://neoflowoff.eth` (ou seu domínio)
6. Configurar permissões

### **4. Testar em Telegram**

```bash
# Desenvolver
cd frontend
npm run dev

# Testar localmente com ngrok
ngrok http 3002

# Usar URL do ngrok no BotFather
```

### **5. Deploy para IPFS**

```bash
# Build
npm run build

# Deploy (Pinata)
npx pinata-cli upload .next/

# Configurar ENS
# neoflowoff.eth → ipfs://CID
```

---

## 📋 Checklist Rápido

- [ ] Instalar WalletConnect
- [ ] Obter Project ID
- [ ] Configurar Telegram Bot
- [ ] Testar em Telegram
- [ ] Deploy em IPFS
- [ ] Configurar ENS
- [ ] Testar em Farcaster

---

## 🎯 Vantagens

✅ **Telegram**: 1B+ usuários, acesso nativo  
✅ **Farcaster**: Comunidade Web3, on-chain  
✅ **Polygon**: Gas baixo = viável para microtransações  
✅ **Mobile-First**: Otimizado para mobile  

---

**Pronto para MiniApp! 📱🚀**

