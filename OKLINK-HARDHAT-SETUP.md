# 🔧 Configurar Hardhat + OKLink Plugin para Verificação

**Data**: 29 de Novembro de 2025

---

## ⚠️ IMPORTANTE

**Este projeto usa Ape Framework para deploy e testes.**  
Hardhat é configurado **APENAS** como ferramenta auxiliar para verificação de contratos no OKLink Explorer.

- **Framework Principal**: Ape Framework (`ape-config.yaml`)
- **Ferramenta de Verificação**: Hardhat (apenas para OKLink)

---

## 📋 Pré-requisitos

- **Repositório do contrato**: `github.com/kauntdewn1/neoflw-token`
- **Contrato**: `0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2`
- **Chain**: Polygon Mainnet (137)
- **Chain Short Name**: `POLYGON`
- **Solidity Version**: `0.8.18` (mesma do Ape Framework)

---

## 🚀 Passo a Passo

### **1. Clonar o Repositório do Contrato**

```bash
# Se ainda não tiver clonado
git clone https://github.com/kauntdewn1/neoflw-token.git
cd neoflw-token
```

### **2. Instalar Dependências**

```bash
npm install
```

### **3. Instalar Plugin do OKLink**

```bash
npm install @okxweb3/hardhat-explorer-verify --save-dev
```

### **4. Configurar hardhat.config.js**

O arquivo `hardhat.config.js` já está configurado no repositório. Ele usa:

- **Solidity 0.8.18** (mesma versão do Ape Framework)
- **Optimizer**: enabled, runs: 200
- **Rede Polygon Mainnet** configurada

Se precisar ajustar, edite `hardhat.config.js`:

```javascript
require("@nomicfoundation/hardhat-toolbox");
require("@okxweb3/hardhat-explorer-verify");
require("dotenv").config();

module.exports = {
  solidity: {
    version: "0.8.18", // Mesma versão usada no Ape Framework
    settings: {
      optimizer: {
        enabled: true,
        runs: 200
      }
    }
  },
  
  networks: {
    polygon: {
      url: process.env.POLYGON_RPC_URL || "https://polygon-mainnet.infura.io/v3/9afb8749df8f4370aded1dce851d13f4",
      accounts: process.env.PRIVATE_KEY ? [process.env.PRIVATE_KEY] : [],
      chainId: 137,
    },
  },
  
  // Configuração do OKLink Explorer
  okxweb3explorer: {
    customChains: [
      {
        network: "Polygon Mainnet",
        chainId: 137,
        urls: {
          apiURL: "https://www.oklink.com/api/v5/explorer/contract/verify-source-code-plugin/POLYGON",
          browserURL: "https://www.oklink.com",
        }
      }
    ]
  },
  
  // Configuração alternativa usando etherscan (Method 2)
  etherscan: {
    customChains: [
      {
        network: "polygon",
        chainId: 137,
        urls: {
          apiURL: "https://www.oklink.com/api/v5/explorer/contract/verify-source-code-plugin/POLYGON",
          browserURL: "https://www.oklink.com",
        }
      }
    ]
  }
};

export default config;
```

### **5. Configurar Variáveis de Ambiente**

Crie ou edite o arquivo `.env` no repositório do contrato:

```bash
# Polygon RPC (usado pelo Hardhat para verificação)
ALCHEMY_API_KEY=sua_alchemy_api_key_aqui

# Private Key (opcional, apenas se precisar fazer deploy via Hardhat)
PRIVATE_KEY=sua_private_key_aqui

# OKLink API Key (opcional - melhora rate limits)
# Obter em: https://www.oklink.com/docs/en/#quickstart-guide-getting-started
OKLINK_API_KEY=sua_oklink_api_key_aqui
```

**Nota:** A API Key do OKLink é **opcional**. A verificação funciona sem ela, mas ter uma API key pode melhorar os rate limits.

### **6. Verificar o Contrato**

Execute o comando de verificação básico:

```bash
npx hardhat okverify --network polygon 0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2
```

**Com nome do contrato específico** (recomendado para contratos com múltiplos arquivos):

```bash
npx hardhat okverify --network polygon --contract contracts/NeoFlowToken.sol:NeoFlowToken 0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2
```

**Outros contratos disponíveis:**

- `contracts/NeoFlowToken.sol:NeoFlowToken`
- `contracts/StakingVault.sol:StakingVault`
- `contracts/NeoFlowClaim.sol:NeoFlowClaim`
- `contracts/DaoGovernor.sol:DaoGovernor`
- `contracts/GamificationController.sol:GamificationController`
- `contracts/NeoFlowTokenVotes.sol:NeoFlowTokenVotes`

### **7. Verificar Contrato Proxy**

**Para TransparentUpgradeableProxy (OpenZeppelin):**

```bash
npx hardhat okverify --network polygon --contract contracts/NeoFlowToken.sol:NeoFlowToken --proxy 0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2
```

**⚠️ IMPORTANTE**: Se usar contrato **EIP-897** (Proxy pattern), **NÃO** adicione `--proxy`, use diretamente:

```bash
npx hardhat okverify --network polygon --contract contracts/NeoFlowToken.sol:NeoFlowToken 0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2
```

### **8. Verificar Resultado da Verificação**

Após executar o comando, você receberá um **GUID**. O tempo médio de processamento é **30-60 segundos**.

Você pode verificar o status no OKLink Explorer:

```
https://www.oklink.com/polygon/address/0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2
```

**Status possíveis:**
- ✅ **Success**: Contrato verificado com sucesso
- ⏳ **Pending**: Verificação em processamento
- ❌ **Fail**: Verificação falhou (verificar logs)

---

## 📝 Exemplo Completo de hardhat.config.js

O arquivo `hardhat.config.js` já está configurado no repositório. Exemplo:

```javascript
require("@nomicfoundation/hardhat-toolbox");
require("@okxweb3/hardhat-explorer-verify");
require("dotenv").config();

module.exports = {
  solidity: {
    version: "0.8.18", // Mesma versão do Ape Framework
    settings: {
      optimizer: {
        enabled: true,
        runs: 200
      }
    }
  },
  networks: {
    polygon: {
      url: process.env.POLYGON_RPC_URL || "https://polygon-mainnet.infura.io/v3/9afb8749df8f4370aded1dce851d13f4",
      accounts: process.env.PRIVATE_KEY ? [process.env.PRIVATE_KEY] : [],
      chainId: 137,
    },
  },
  okxweb3explorer: {
    customChains: [
      {
        network: "Polygon Mainnet",
        chainId: 137,
        urls: {
          apiURL: "https://www.oklink.com/api/v5/explorer/contract/verify-source-code-plugin/POLYGON",
          browserURL: "https://www.oklink.com",
        }
      }
    ]
  }
};
```

---

## 🔍 Verificar Resultado

Após a verificação bem-sucedida, você pode ver o contrato verificado em:

```
https://www.oklink.com/polygon/address/0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2
```

**Tempo de processamento:** 30-60 segundos em média.

**Verificar status via API** (opcional):

Se você recebeu um GUID, pode verificar o status via API:

```bash
curl -X POST https://www.oklink.com/api/v5/explorer/contract/check-verify-result \
  -H "Content-Type: application/json" \
  -d '{
    "chainShortName": "POLYGON",
    "guid": "SEU_GUID_AQUI"
  }'
```

**Resposta esperada:**
- `"Success"` - Verificação concluída
- `"Pending"` - Ainda processando
- `"Fail"` - Falhou (verificar logs)

---

## ⚠️ Troubleshooting

### **Erro: "Contract not found"**

- Verifique se o endereço do contrato está correto
- Confirme que está na rede correta (Polygon Mainnet)

### **Erro: "Compiler version mismatch"**

- Use exatamente a mesma versão do compilador usada no deploy
- Verifique em `hardhat.config.js` ou nos artifacts

### **Erro: "Optimization settings mismatch"**

- Use as mesmas configurações de otimização do deploy
- Verifique `optimizer.enabled` e `optimizer.runs`

### **Erro: "Source code not found"**

- Certifique-se de que os arquivos de contrato estão no caminho correto
- Se usar imports, pode precisar fazer flatten do código

---

## 📚 Recursos

- **Plugin GitHub**: https://github.com/okx/hardhat-explorer-verify
- **OKLink Explorer**: https://www.oklink.com/
- **Documentação API**: https://www.oklink.com/docs/en/
- **Lista de Chains Suportadas**: https://www.oklink.com/docs/zh/#quickstart-guide-list-of-supported-chains
- **Obter API Key**: https://www.oklink.com/docs/en/#quickstart-guide-getting-started

---

## 🎯 Comandos Rápidos

```bash
# 1. Instalar plugin
npm install @okxweb3/hardhat-explorer-verify --save-dev

# 2. Verificar contrato
npx hardhat okverify --network polygon 0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2

# 3. Verificar com nome específico
npx hardhat okverify --network polygon --contract contracts/NeoFlowToken.sol:NeoFlowToken 0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2

# 4. Verificar proxy
npx hardhat okverify --network polygon --contract contracts/NeoFlowToken.sol:NeoFlowToken --proxy 0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2
```

---

**Última atualização**: 29 de Novembro de 2025

