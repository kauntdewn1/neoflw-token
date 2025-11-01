# 🔗 Recursos Oficiais - Sepolia Testnet

## 📋 Informações do Sepolia

- **Nome:** Sepolia
- **Chain ID:** `11155111`
- **Network ID:** `11155111`
- **Status:** Ativo (Launched)
- **Website Oficial:** https://sepolia.ethpandaops.io/
- **GitHub:** https://github.com/eth-clients/sepolia

---

## 🌐 Block Explorers

### **Etherscan (Oficial)**
- **URL:** https://sepolia.etherscan.io
- **Token:** https://sepolia.etherscan.io/token/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
- **Descrição:** Explorer oficial do Sepolia, mantido pela mesma equipe do Etherscan mainnet

### **Blockscout (Alternativa Open-Source)**
- **URL:** https://eth-sepolia.blockscout.com/
- **Vantagem:** Suporte melhor para tokens customizados
- **Token:** https://eth-sepolia.blockscout.com/address/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87

### **Otterscan (Open-Source)**
- **URL:** https://sepolia.otterscan.io
- **Vantagem:** Interface moderna e open-source

### **Beaconchain**
- **URL:** https://sepolia.beaconcha.in
- **Descrição:** Explorer para a beacon chain do Sepolia

---

## 🔌 RPC Endpoints (Públicos)

### **Endpoints Públicos (Sem API Key):**

1. **RPC Sepolia (Oficial)**
   ```
   https://rpc.sepolia.org
   ```
   - Status: https://status.sepolia.org

2. **RPC Sepolia Online**
   ```
   https://rpc.sepolia.online
   ```

3. **SepoliaRPC Space**
   ```
   https://www.sepoliarpc.space
   ```

4. **RockX**
   ```
   https://rpc-sepolia.rockx.com
   ```

5. **Bordel**
   ```
   https://rpc.bordel.wtf/sepolia
   ```

6. **ETH Panda Ops (Oficial)**
   ```
   https://rpc.sepolia.ethpandaops.io
   ```

### **Como usar no Frontend:**

```javascript
// Configuração para ethers.js
const provider = new ethers.JsonRpcProvider("https://rpc.sepolia.org");

// Configuração para viem
import { createPublicClient, http } from 'viem';
import { sepolia } from 'viem/chains';

const client = createPublicClient({
  chain: sepolia,
  transport: http("https://rpc.sepolia.org")
});

// MetaMask (adicionar rede)
const sepoliaNetwork = {
  chainId: '0xaa36a7', // 11155111 em hex
  chainName: 'Sepolia',
  nativeCurrency: {
    name: 'Ether',
    symbol: 'ETH',
    decimals: 18
  },
  rpcUrls: ['https://rpc.sepolia.org'],
  blockExplorerUrls: ['https://sepolia.etherscan.io']
};
```

---

## 💧 Faucets (ETH de Teste)

### **Faucets Recomendados:**

1. **Alchemy Faucet**
   - **URL:** https://sepoliafaucet.com/
   - **Requisitos:** Conta gratuita Alchemy

2. **Grabteeth**
   - **URL:** https://grabteeth.xyz
   - **Requisitos:** Conexão Twitter/Discord

3. **QuickNode**
   - **URL:** https://faucet.quicknode.com/ethereum/sepolia
   - **Requisitos:** Conta QuickNode

4. **PoW Faucet (PK910)**
   - **URL:** https://sepolia-faucet.pk910.de/
   - **Requisitos:** Resolver PoW (Proof of Work)

5. **RockX**
   - **URL:** https://faucet-sepolia.rockx.com/
   - **Requisitos:** Varia (pode precisar de conta)

6. **LearnWeb3**
   - **URL:** https://learnweb3.io/faucets/sepolia
   - **Requisitos:** Conta LearnWeb3

7. **Infura**
   - **URL:** https://infura.io/faucet
   - **Requisitos:** Conta Infura

8. **Unitap**
   - **URL:** https://unitap.app/gastap
   - **Requisitos:** Varia

### **Estratégia de Uso:**

Se um faucet estiver limitado ou offline, tente outro. Alguns têm limites diários.

---

## 📊 Status e Monitoramento

### **Status Dashboard:**
- **URL:** https://stats.noderpc.xyz
- **Descrição:** Monitoramento de status dos RPC endpoints

### **Status RPC Sepolia:**
- **URL:** https://status.sepolia.org
- **Descrição:** Status específico do RPC oficial

---

## 🛠️ Configuração no Frontend

### **Variáveis de Ambiente:**

```bash
# .env
VITE_SEPOLIA_RPC_URL=https://rpc.sepolia.org
VITE_SEPOLIA_CHAIN_ID=11155111
VITE_SEPOLIA_EXPLORER=https://sepolia.etherscan.io
VITE_TOKEN_ADDRESS=0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
```

### **Configuração Completa:**

```javascript
// config/sepolia.js
export const SEPOLIA_CONFIG = {
  chainId: 11155111,
  chainIdHex: '0xaa36a7',
  name: 'Sepolia',
  networkId: 11155111,
  
  // RPC URLs (fallbacks)
  rpcUrls: [
    'https://rpc.sepolia.org',
    'https://rpc.sepolia.online',
    'https://www.sepoliarpc.space',
    'https://rpc-sepolia.rockx.com',
    'https://rpc.bordel.wtf/sepolia'
  ],
  
  // Block Explorers
  blockExplorers: [
    {
      name: 'Etherscan',
      url: 'https://sepolia.etherscan.io'
    },
    {
      name: 'Blockscout',
      url: 'https://eth-sepolia.blockscout.com/'
    },
    {
      name: 'Otterscan',
      url: 'https://sepolia.otterscan.io'
    }
  ],
  
  // Currency
  nativeCurrency: {
    name: 'Ether',
    symbol: 'ETH',
    decimals: 18
  },
  
  // Faucets
  faucets: [
    'https://sepoliafaucet.com/',
    'https://grabteeth.xyz',
    'https://faucet.quicknode.com/ethereum/sepolia',
    'https://sepolia-faucet.pk910.de/'
  ],
  
  // Info
  testnet: true,
  officialWebsite: 'https://sepolia.ethpandaops.io/'
};
```

### **Helper para Detectar Rede:**

```javascript
// utils/network.js
export function isSepolia(chainId) {
  return chainId === 11155111 || chainId === '0xaa36a7';
}

export function getSepoliaRPC() {
  // Retorna RPC aleatório para distribuir carga
  const rpcs = SEPOLIA_CONFIG.rpcUrls;
  return rpcs[Math.floor(Math.random() * rpcs.length)];
}

export async function checkRPCHealth(rpcUrl) {
  try {
    const response = await fetch(rpcUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        jsonrpc: '2.0',
        method: 'eth_blockNumber',
        params: [],
        id: 1
      })
    });
    return response.ok;
  } catch {
    return false;
  }
}
```

---

## 🔗 Links Úteis para Desenvolvimento

### **Token NEOFLW:**
- **Etherscan:** https://sepolia.etherscan.io/token/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
- **Blockscout:** https://eth-sepolia.blockscout.com/address/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87

### **Recursos Gerais:**
- **Website Oficial:** https://sepolia.ethpandaops.io/
- **GitHub:** https://github.com/eth-clients/sepolia
- **Status Dashboard:** https://stats.noderpc.xyz

---

## ✅ Checklist para Desenvolvimento

### **Configuração Inicial:**
- [ ] RPC endpoint configurado (com fallbacks)
- [ ] Chain ID verificado (`11155111`)
- [ ] Block explorer configurado
- [ ] Testnet ETH obtido via faucet
- [ ] Rede Sepolia adicionada no MetaMask

### **Desenvolvimento:**
- [ ] Token address correto
- [ ] Logo IPFS funcionando
- [ ] Metadados carregando
- [ ] Tratamento de erros de rede
- [ ] Fallbacks para RPC

### **Testes:**
- [ ] Transações funcionando
- [ ] Consultas de saldo funcionando
- [ ] Eventos sendo ouvidos
- [ ] Interface responsiva
- [ ] Testes em diferentes exploradores

---

## 💡 Dicas Importantes

1. **Sempre use fallbacks de RPC** - Endpoints públicos podem ficar sobrecarregados
2. **Teste com diferentes faucets** - Se um estiver offline, use outro
3. **Monitore status** - Verifique https://status.sepolia.org antes de reportar bugs
4. **Use Blockscout como alternativa** - Se Etherscan estiver lento
5. **Mantenha ETH de teste** - Faucets têm limites diários

---

**Recursos atualizados conforme:** https://sepolia.ethpandaops.io/ 🚀

