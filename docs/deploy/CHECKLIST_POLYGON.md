# ✅ Checklist: O que Falta Preencher - Polygon Mainnet

## 🎯 Resumo Rápido

### **O QUE VOCÊ PRECISA FAZER:**

---

## 1️⃣ **CONFIGURAÇÕES QUE FALTAM**

### **A. Variáveis de Ambiente (.env)**

#### **Raiz do projeto:**

```env
# Polygon Alchemy API Key
ALCHEMY_API_KEY=polygon-mainnet-key-aqui

# Network para deploy
APE_NETWORK=polygon:mainnet

# Wallet para deploy
WALLET_LABEL=neoflow-admin
```

#### **Frontend (.env):**
```env
# Contratos Polygon (preencher após deploy)
NEXT_PUBLIC_TOKEN_ADDRESS=
NEXT_PUBLIC_VAULT_ADDRESS=
NEXT_PUBLIC_CLAIM_ADDRESS=
NEXT_PUBLIC_GOVERNOR_ADDRESS=

# Thirdweb Client ID (obter em thirdweb.com)
NEXT_PUBLIC_THIRDWEB_CLIENT_ID=

# Alchemy para frontend
NEXT_PUBLIC_ALCHEMY_API_KEY=
```

---

## 2️⃣ **ARQUIVOS QUE PRECISAM SER ATUALIZADOS**

### **A. `ape-config.yaml`**
```yaml
# ADICIONAR esta seção:
networks:
  polygon:
    mainnet:
      default_provider: alchemy
      providers:
        alchemy:
          api_key: ${ALCHEMY_API_KEY}
          request_timeout: 60
```

### **B. `frontend/src/config/token.ts`**
```typescript
// MUDAR de Sepolia para Polygon:
network: {
  name: "Polygon",
  chainId: 137,  // Polygon mainnet
  rpcUrls: [
    `https://polygon-mainnet.g.alchemy.com/v2/${process.env.NEXT_PUBLIC_ALCHEMY_API_KEY}`,
    "https://polygon-rpc.com",
  ],
  explorer: "https://polygonscan.com",
}
```

### **C. `frontend/src/app/providers.tsx`**
```typescript
// MUDAR de sepolia para polygon:
import { polygon } from 'wagmi/chains';

const config = createConfig({
  chains: [polygon],  // Era [sepolia]
  // ...
});
```

---

## 3️⃣ **DEPENDÊNCIAS QUE FALTAM INSTALAR**

### **Frontend:**
```bash
cd frontend
npm install thirdweb @thirdweb-dev/react
```

---

## 4️⃣ **SERVIÇOS QUE PRECISAM SER CONFIGURADOS**

### **A. Thirdweb Dashboard**
- [ ] Criar conta em https://thirdweb.com
- [ ] Criar novo projeto
- [ ] Obter Client ID
- [ ] Adicionar ao `.env` do frontend

### **B. Alchemy (Polygon)**
- [ ] Criar app Polygon Mainnet no Alchemy
- [ ] Obter API Key
- [ ] Adicionar ao `.env` (raiz e frontend)

### **C. IPFS (Pinata ou Fleek)**
- [ ] Criar conta no Pinata (https://pinata.cloud) OU
- [ ] Criar conta no Fleek (https://fleek.co)
- [ ] Preparar para fazer upload do build

### **D. ENS Domain**
- [ ] Verificar que você controla `neoflowoff.eth`
- [ ] Acessar https://app.ens.domains
- [ ] Configurar Content Hash (após ter CID do IPFS)

---

## 5️⃣ **DEPLOY QUE PRECISA SER FEITO**

### **A. Contratos em Polygon:**
```bash
# 1. Token
ape run scripts/deploy_token.py --network polygon:mainnet

# 2. Vault
ape run scripts/deploy_vault.py --network polygon:mainnet

# 3. Claim
ape run scripts/deploy_claim.py --network polygon:mainnet
```

**⚠️ IMPORTANTE:** Anotar todos os endereços e atualizar `.env` do frontend!

---

## 6️⃣ **BUILD E DEPLOY IPFS**

### **A. Build do Frontend:**
```bash
cd frontend
npm run build
```

### **B. Deploy IPFS:**
```bash
# Opção 1: Pinata
pinata-cli upload .next/out/

# Opção 2: Fleek
fleek deploy

# Opção 3: IPFS Desktop (manual)
```

**⚠️ IMPORTANTE:** Anotar o CID/IPFS hash!

---

## 7️⃣ **CONFIGURAR ENS**

### **Via ENS Manager:**
1. Acessar https://app.ens.domains
2. Conectar wallet que controla `neoflowoff.eth`
3. Ir em "My Account" → `neoflowoff.eth`
4. Em "Content Hash", adicionar:
   - Tipo: **IPFS**
   - Hash: `Qm...` (CID do IPFS)
5. Confirmar transação

---

## 8️⃣ **INTEGRAÇÃO flowoff.xyz**

### **No site da agência, adicionar:**

```html
<!-- Botão Launch APP -->
<a href="https://neoflowoff.eth" class="launch-app-btn">
  🚀 Launch APP
</a>

<!-- Seção Partner -->
<section class="partners">
  <div class="partner-card">
    <h3>NEOFLW Protocol</h3>
    <p>Parceiro oficial</p>
    <a href="https://neoflowoff.eth">Acessar</a>
  </div>
</section>
```

---

## 📋 CHECKLIST RESUMIDO

### **Configuração:**
- [ ] Alchemy API Key (Polygon)
- [ ] Thirdweb Client ID
- [ ] Atualizar `ape-config.yaml`
- [ ] Atualizar `frontend/src/config/token.ts`
- [ ] Atualizar `frontend/src/app/providers.tsx`
- [ ] Instalar dependências Thirdweb

### **Deploy:**
- [ ] Deploy Token em Polygon
- [ ] Deploy Vault em Polygon
- [ ] Deploy Claim em Polygon
- [ ] Anotar endereços e atualizar `.env`

### **Frontend:**
- [ ] Build do frontend
- [ ] Deploy em IPFS
- [ ] Obter CID/IPFS hash

### **ENS:**
- [ ] Configurar Content Hash no ENS
- [ ] Testar acesso via `neoflowoff.eth`

### **Integração:**
- [ ] Adicionar botão no flowoff.xyz
- [ ] Criar seção Partner
- [ ] Testar fluxo completo

---

## 🚨 PRIORIDADES

### **URGENTE (fazer primeiro):**
1. ✅ Obter Alchemy API Key (Polygon)
2. ✅ Obter Thirdweb Client ID
3. ✅ Atualizar arquivos de configuração
4. ✅ Fazer deploy dos contratos

### **IMPORTANTE (fazer depois):**
5. ✅ Build e deploy IPFS
6. ✅ Configurar ENS
7. ✅ Testar tudo

### **FINALIZAÇÃO:**
8. ✅ Integrar no flowoff.xyz
9. ✅ Documentar tudo

---

## 💡 DICAS

- **Gas Fees:** Polygon é muito mais barato que Ethereum (~$0.01 por transação)
- **Teste primeiro:** Use Polygon Mumbai testnet antes de mainnet
- **Backup:** Sempre anote endereços e CIDs em local seguro
- **Verificação:** Verifique todos os contratos no Polygonscan

---

**✅ Use este checklist como guia passo a passo!**

