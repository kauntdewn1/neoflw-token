# 🚀 Plano Completo: Polygon Mainnet + IPFS + ENS + Embed Wallet

## 📋 Checklist de Implementação

### ✅ **FASE 1: Preparação e Configuração**

#### **1.1. Configurar Polygon Mainnet no Ape Framework**

- [ ] Adicionar Polygon mainnet no `ape-config.yaml`
- [ ] Configurar Alchemy API para Polygon
- [ ] Obter MATIC na wallet para gas fees
- [ ] Testar conexão com Polygon

#### **1.2. Atualizar Frontend para Polygon**

- [ ] Atualizar `frontend/src/config/token.ts` com Polygon mainnet
- [ ] Atualizar `frontend/src/app/providers.tsx` para suportar Polygon
- [ ] Adicionar chain Polygon no Wagmi config
- [ ] Atualizar `.env.example` com endereços Polygon

#### **1.3. Embed Wallet (Thirdweb)**

- [ ] Criar projeto no Thirdweb Dashboard
- [ ] Obter Client ID do Thirdweb
- [ ] Instalar `@thirdweb-dev/react` ou `@thirdweb-dev/sdk`
- [ ] Configurar embed wallet no frontend
- [ ] Testar conexão via embed wallet

---

### ✅ **FASE 2: Deploy dos Contratos**

#### **2.1. Deploy Token em Polygon**

- [ ] Compilar contratos
- [ ] Deploy `NeoFlowToken.sol` na Polygon mainnet
- [ ] Anotar endereço do contrato
- [ ] Verificar contrato no Polygonscan

#### **2.2. Deploy StakingVault**

- [ ] Deploy `StakingVault.sol` com endereço do token
- [ ] Anotar endereço do vault
- [ ] Verificar contrato no Polygonscan
- [ ] Testar stake/claim em Polygon

#### **2.3. Deploy NeoFlowClaim**

- [ ] Deploy `NeoFlowClaim.sol` com endereço do token
- [ ] Anotar endereço do claim
- [ ] Verificar contrato no Polygonscan
- [ ] Configurar whitelist inicial

#### **2.4. Deploy DAO (Opcional)**

- [ ] Deploy `NeoFlowTokenVotes.sol`
- [ ] Deploy `DaoGovernor.sol`
- [ ] Configurar parâmetros de governança

---

### ✅ **FASE 3: Frontend e IPFS**

#### **3.1. Build do Frontend**

- [ ] Atualizar todas as variáveis de ambiente
- [ ] Fazer build de produção: `npm run build`
- [ ] Testar build localmente
- [ ] Verificar que todas as funcionalidades funcionam

#### **3.2. Deploy em IPFS**

- [ ] Instalar IPFS CLI ou usar serviço (Pinata, Fleek, etc)
- [ ] Fazer upload do build para IPFS
- [ ] Obter CID/IPFS hash
- [ ] Testar acesso via gateway IPFS
- [ ] Configurar múltiplos gateways (redundância)

#### **3.3. Configurar ENS Domain**

- [ ] Verificar que `neoflowoff.eth` está configurado
- [ ] Configurar Content Hash (IPFS) no ENS
- [ ] Configurar Text Records (website, etc)
- [ ] Testar acesso via `neoflowoff.eth`

---

### ✅ **FASE 4: Integração com flowoff.xyz**

#### **4.1. Site da Agência (flowoff.xyz)**

- [ ] Criar página/componente com botão "Launch APP"
- [ ] Linkar botão para `neoflowoff.eth` ou IPFS gateway
- [ ] Adicionar seção "Partner" mencionando NEOFLW
- [ ] Implementar embed wallet (se necessário no site principal)

#### **4.2. Integração Partner**
- [ ] Adicionar logo/branding NEOFLW no site
- [ ] Criar página de parceiros mencionando NEOFLW
- [ ] Adicionar links para documentação
- [ ] Configurar tracking/analytics

---

### ✅ **FASE 5: Testes e Validação**

#### **5.1. Testes Funcionais**

- [ ] Testar conexão de wallet (MetaMask, WalletConnect, Embed)
- [ ] Testar todas as funcionalidades (Token, Staking, Claim)
- [ ] Testar em diferentes browsers
- [ ] Testar em mobile

#### **5.2. Testes de Performance**

- [ ] Verificar tempo de carregamento via IPFS
- [ ] Testar com diferentes gateways
- [ ] Verificar que ENS resolve corretamente
- [ ] Testar fallbacks

#### **5.3. Validação Final**

- [ ] Verificar todos os contratos no Polygonscan
- [ ] Verificar que IPFS está acessível
- [ ] Verificar que ENS está configurado
- [ ] Testar fluxo completo: flowoff.xyz → Launch APP → neoflowoff.eth

---

## 📝 Detalhamento por Item

### **1. Configuração Polygon no Ape Framework**

**Arquivo:** `ape-config.yaml`

```yaml
networks:
  polygon:
    mainnet:
      default_provider: alchemy
      providers:
        alchemy:
          api_key: ${ALCHEMY_API_KEY}
          request_timeout: 60
```

**Variáveis de ambiente necessárias:**
```env
ALCHEMY_API_KEY=polygon-mainnet-key
APE_NETWORK=polygon:mainnet
```

---

### **2. Atualizar Frontend para Polygon**

**Arquivo:** `frontend/src/config/token.ts`

```typescript
export const TOKEN_CONFIG = {
  address: process.env.NEXT_PUBLIC_TOKEN_ADDRESS || "",
  name: "NeoFlowOFF",
  symbol: "NEOFLW",
  decimals: 18,
  
  network: {
    name: "Polygon",
    chainId: 137,
    rpcUrls: [
      `https://polygon-mainnet.g.alchemy.com/v2/${process.env.NEXT_PUBLIC_ALCHEMY_API_KEY}`,
      "https://polygon-rpc.com",
    ],
    explorer: "https://polygonscan.com",
  },
  // ... resto da config
};
```

**Arquivo:** `frontend/src/app/providers.tsx`

```typescript
import { polygon } from 'wagmi/chains';
import { createThirdwebClient, getRpcClient } from 'thirdweb';
import { ThirdwebProvider } from 'thirdweb/react';

// Adicionar Polygon chain
const config = createConfig({
  chains: [polygon],
  // ...
});
```

---

### **3. Embed Wallet (Thirdweb)**

**Instalação:**
```bash
cd frontend
npm install thirdweb @thirdweb-dev/react
```

**Configuração:**
```typescript
// frontend/src/app/providers.tsx
import { ThirdwebProvider } from 'thirdweb/react';

const client = createThirdwebClient({
  clientId: process.env.NEXT_PUBLIC_THIRDWEB_CLIENT_ID!,
});

export function Providers({ children }) {
  return (
    <ThirdwebProvider client={client}>
      <WagmiProvider config={config}>
        {/* ... */}
      </WagmiProvider>
    </ThirdwebProvider>
  );
}
```

**Componente Embed Wallet:**
```typescript
import { ConnectButton } from 'thirdweb/react';

<ConnectButton
  client={client}
  chains={[polygon]}
  connectModal={{
    size: "wide",
    title: "Conectar Wallet",
  }}
/>
```

---

### **4. Deploy em IPFS**

**Opção 1: Pinata**
```bash
# Instalar Pinata CLI
npm install -g pinata-cli

# Fazer upload
pinata-cli upload dist/ --name "neoflw-app"
```

**Opção 2: Fleek**
```bash
# Instalar Fleek CLI
npm install -g @fleek/cli

# Deploy
fleek deploy
```

**Opção 3: IPFS Desktop**
```bash
# Build do Next.js
cd frontend
npm run build

# Export estático (se necessário)
# Adicionar ao next.config.js:
output: 'export'

# Upload manual via IPFS Desktop
```

---

### **5. Configurar ENS Domain**

**Via ENS Manager (app.ens.domains):**
1. Conectar wallet que controla `neoflowoff.eth`
2. Ir em "My Account" → "neoflowoff.eth"
3. Em "Content Hash", adicionar:
   - Tipo: IPFS
   - Hash: `Qm...` (CID do IPFS)
4. Salvar transação

**Via Script:**
```javascript
// scripts/set_ens_contenthash.js
const { ethers } = require('ethers');
const { setContentHash } = require('@ensdomains/ensjs');

async function setENSContentHash() {
  const provider = new ethers.providers.JsonRpcProvider('https://eth-mainnet.g.alchemy.com/v2/YOUR_KEY');
  const signer = provider.getSigner();
  
  await setContentHash({
    name: 'neoflowoff.eth',
    contentHash: 'ipfs://Qm...', // CID do IPFS
    signer,
  });
}
```

---

### **6. Integração flowoff.xyz**

**HTML/React no site da agência:**
```html
<!-- Botão Launch APP -->
<a 
  href="https://neoflowoff.eth" 
  target="_blank"
  rel="noopener noreferrer"
  className="launch-app-button"
>
  🚀 Launch APP
</a>

<!-- Seção Partner -->
<section className="partners">
  <h2>Nossos Parceiros</h2>
  <div className="partner-card">
    <img src="neoflw-logo.png" alt="NEOFLW" />
    <h3>NEOFLW Protocol</h3>
    <p>Tokenização com propósito</p>
    <a href="https://neoflowoff.eth">Acessar Protocolo</a>
  </div>
</section>
```

---

## 🔧 Arquivos que Precisam ser Criados/Atualizados

### **Novos Arquivos:**
1. `docs/deploy/POLYGON_MAINNET_PLANO_COMPLETO.md` (este arquivo)
2. `scripts/deploy_polygon.py` - Script de deploy em Polygon
3. `frontend/.env.polygon` - Variáveis de ambiente para Polygon
4. `scripts/set_ens_contenthash.js` - Script para configurar ENS

### **Arquivos a Atualizar:**
1. `ape-config.yaml` - Adicionar Polygon network
2. `frontend/src/config/token.ts` - Configurar Polygon
3. `frontend/src/app/providers.tsx` - Adicionar Polygon + Thirdweb
4. `frontend/package.json` - Adicionar dependências Thirdweb
5. `frontend/next.config.js` - Configurar para export estático (se IPFS)
6. `.env.example` - Adicionar variáveis Polygon

---

## 📊 Status Atual vs Necessário

| Item | Status Atual | Necessário |
|------|--------------|------------|
| **Rede** | Sepolia Testnet | Polygon Mainnet |
| **Frontend Chain** | Sepolia | Polygon |
| **Embed Wallet** | ❌ Não implementado | ✅ Thirdweb |
| **IPFS Deploy** | ❌ Não feito | ✅ IPFS + ENS |
| **ENS Domain** | ✅ Configurado (não aponta) | ✅ Apontar para IPFS |
| **flowoff.xyz** | ❌ Não integrado | ✅ Botão + Partner |

---

## 🎯 Próximos Passos Imediatos

### **Prioridade ALTA:**
1. ✅ Configurar Polygon no `ape-config.yaml`
2. ✅ Atualizar frontend para Polygon
3. ✅ Instalar e configurar Thirdweb embed wallet
4. ✅ Fazer deploy dos contratos em Polygon

### **Prioridade MÉDIA:**
5. ✅ Fazer build e deploy em IPFS
6. ✅ Configurar ENS para apontar para IPFS
7. ✅ Testar tudo funcionando

### **Prioridade BAIXA:**
8. ✅ Integrar botão no flowoff.xyz
9. ✅ Criar seção Partner
10. ✅ Finalizar documentação

---

## 💰 Custos Estimados

| Item | Custo Estimado |
|------|----------------|
| **Polygon Gas Fees** | ~$5-20 USD (MATIC) |
| **ENS Renewal** | ~$5 USD/ano (se necessário) |
| **IPFS Hosting** | Gratuito (Pinata free tier) ou ~$10-20/mês |
| **Thirdweb** | Gratuito (free tier) |
| **Total** | **~$20-50 USD** |

---

## 📚 Recursos e Links

- **Polygon Docs:** https://docs.polygon.technology/
- **Thirdweb Docs:** https://portal.thirdweb.com/
- **IPFS Docs:** https://docs.ipfs.tech/
- **ENS Manager:** https://app.ens.domains/
- **Polygonscan:** https://polygonscan.com/

---

**✅ Checklist completo para implementação em Polygon Mainnet!**

