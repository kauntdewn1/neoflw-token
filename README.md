# NEOFLOW Protocol

Repositório de contratos inteligentes do token **$NEOFLW** (NeoFlowOFF) com orquestração terminal padrão NEØ.

## 🚀 Quick Start

```bash
# Instalar plugins e dependências
npm run plugins

# Compilar contratos
npm run compile

# Executar testes
npm run test

# Deploy completo (plugins + compile + test + deploy)
npm run start:dev
```

## 📦 Contratos

- `NeoFlowToken.sol` — Token ERC20 com funções de queima
- `StakingVault.sol` — Vault de staking com lock de 6 meses e recompensas de 10%
- `NeoFlowClaim.sol` — Sistema de claim onde usuários pagam o próprio gas

### 💎 Token $NEOFLW

- **Nome**: NeoFlowOFF
- **Símbolo**: NEOFLW (6 caracteres)
- **Supply**: 1 bilhão (mint inicial)
- **Utilidade**: Staking, DAO, recompensas, integração com WebApp

## 🛠️ Comandos Disponíveis

### Setup Inicial

```bash
npm run init          # Inicializa projeto Ape
npm run plugins       # Instala plugins (solidity, alchemy, etherscan)
npm run account:import # Importa conta flowoff-admin
```

### Desenvolvimento

```bash
npm run compile       # Compila contratos Solidity
npm run test          # Executa testes
npm run console       # Abre console Ape interativo
npm run clean         # Limpa build e cache
```

### Deploy

```bash
npm run deploy:token      # Deploy token em Sepolia
npm run deploy:vault      # Deploy vault em Sepolia
npm run deploy:claim      # Deploy claim em Sepolia
npm run verify:token      # Verifica token no Etherscan
npm run verify:vault      # Verifica vault no Etherscan
npm run verify:claim      # Verifica claim no Etherscan
npm run deploy:local      # Deploy em rede local
npm run start:dev         # Pipeline completo (plugins + compile + test + deploy)
```

## 🔐 Configuração de Ambiente

1. Copie o arquivo de exemplo:

```bash
cp .env.example .env
```

2. Configure as variáveis no `.env`:

```env
ALCHEMY_API_KEY=your_alchemy_key_here
ETHERSCAN_API_KEY=your_etherscan_key_here
WALLET_LABEL=flowoff-admin
APE_NETWORK=ethereum:goerli
```

3. Exporte as variáveis (ou use `source .env`):

```bash
export ALCHEMY_API_KEY=...
export ETHERSCAN_API_KEY=...
```

## 🧪 Testes

```bash
# Via npm
npm run test

# Via Ape diretamente
ape test
```

## 🚀 Deploy

### Deploy em Goerli

```bash
# Configurar API key
export ALCHEMY_API_KEY=your-key

# Deploy
npm run deploy:token

# Verificar no Etherscan
npm run verify:token
```

### Deploy Local

```bash
npm run deploy:local
```

## 🛡️ Segurança

* ✅ Usa `Ownable` da OpenZeppelin (padrão auditado)
* ✅ Função de queima pública (`burn`) para controle de supply
* ✅ Sistema de claim com proteção CEI (Checks-Effects-Interactions)
* ✅ Contratos testados e verificados no Etherscan

## 📁 Estrutura do Projeto

```
neoflow/
├── contracts/
│   ├── NeoFlowToken.sol
│   ├── StakingVault.sol
│   └── NeoFlowClaim.sol
├── scripts/
│   ├── deploy_token.py
│   ├── deploy_vault.py
│   ├── deploy_claim.py
│   └── setup_claim.py
├── tests/
│   ├── test_token.py
│   ├── test_vault.py
│   └── test_claim.py
├── ape-config.yaml          # Configuração Ape Framework
├── package.json            # Orquestração terminal NEØ
├── .env.example            # Template de variáveis
├── neo-node.json           # Config NEØ para CI/CD
└── README.md
```

## 🌐 Roadmap

* [x] Token ERC20 com mint inicial
* [x] Orquestração terminal com npm scripts
* [x] Pipeline de deploy automatizado
* [x] Staking Vault (6 meses lock, 10% reward)
* [x] Sistema de Claim (usuários pagam próprio gas)
* [ ] Governança DAO
* [x] Integração com WebApp (Wagmi + Viem)

## 🤖 Integração CI/CD

O projeto está preparado para integração com:
- **GitHub Actions** — Use os scripts npm nos workflows
- **Vercel CLI** — Deploy automático via `npm run deploy:token`
- **Bots/IA Executora** — Interface padronizada via `package.json`
- **Docker** — Containerização com comandos npm

### Exemplo GitHub Actions

```yaml
- name: Deploy Token
  run: npm run deploy:token
  env:
    ALCHEMY_API_KEY: ${{ secrets.ALCHEMY_API_KEY }}
    ETHERSCAN_API_KEY: ${{ secrets.ETHERSCAN_API_KEY }}
```

## 🔗 Integração Frontend (Next.js + Wagmi + Viem)

O contrato `NeoFlowToken` está pronto para integração com WebApp.

### Gerar ABI

Após compilar o contrato, o ABI estará disponível em:
```
./build/contracts/NeoFlowToken.json
```

### Estrutura Recomendada

```ts
// hooks/useNeoflow.ts
import { useAccount, useContractRead, useContractWrite } from 'wagmi'
import { NEOFLOW_ABI } from '@/lib/abi/neoflow'
import { parseEther, formatEther } from 'viem'

const NEOFLOW_ADDRESS = '0x...'; // Substituir após deploy

export function useNeoflow() {
  const { address } = useAccount()

  const { data: balance } = useContractRead({
    address: NEOFLOW_ADDRESS,
    abi: NEOFLOW_ABI,
    functionName: 'balanceOf',
    args: [address],
    watch: true,
  })

  const { write: burn } = useContractWrite({
    address: NEOFLOW_ADDRESS,
    abi: NEOFLOW_ABI,
    functionName: 'burn',
  })

  return { balance, burn }
}
```

### Funcionalidades Disponíveis

- ✅ Visualizar saldo de `$NEOFLW`
- ✅ Queimar tokens (`burn`)
- ✅ Airdrop (apenas owner)
- ✅ Staking com lock de 6 meses
- ✅ Claim de recompensas (10% reward)

## 🔒 StakingVault - Integração Frontend

### Funcionalidades do Contrato

- **Stake**: Trava tokens NEOFLW por 6 meses (180 dias)
- **Claim**: Retira tokens + 10% de reward após o período
- **Lock Duration**: 180 dias (6 meses)
- **Reward Rate**: 10% fixo

### ABI Mínima para Integração

```ts
// lib/abi/stakingVault.ts
export const STAKING_VAULT_ABI = [
  {
    "inputs": [{"internalType":"uint256","name":"_amount","type":"uint256"}],
    "name": "stake",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "claim",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [{"internalType":"address","name":"","type":"address"}],
    "name": "stakes",
    "outputs": [
      {"internalType":"uint256","name":"amount","type":"uint256"},
      {"internalType":"uint256","name":"startTime","type":"uint256"},
      {"internalType":"bool","name":"claimed","type":"bool"}
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [{"internalType":"address","name":"_user","type":"address"}],
    "name": "timeLeft",
    "outputs": [{"internalType":"uint256","name":"","type":"uint256"}],
    "stateMutability": "view",
    "type": "function"
  }
]
```

### Hook Recomendado (Wagmi)

```ts
// hooks/useStakingVault.ts
import {
  useAccount,
  useContractRead,
  useContractWrite,
  useWaitForTransaction,
} from 'wagmi'
import { parseEther } from 'viem'
import { STAKING_VAULT_ABI } from '@/lib/abi/stakingVault'

const VAULT_ADDRESS = '0x...'; // Substituir após deploy

export function useStakingVault() {
  const { address } = useAccount()

  const { data: stakeInfo } = useContractRead({
    address: VAULT_ADDRESS,
    abi: STAKING_VAULT_ABI,
    functionName: 'stakes',
    args: [address],
    watch: true,
  })

  const { data: timeLeft } = useContractRead({
    address: VAULT_ADDRESS,
    abi: STAKING_VAULT_ABI,
    functionName: 'timeLeft',
    args: [address],
    watch: true,
  })

  const { write: stake, data: stakeTx } = useContractWrite({
    address: VAULT_ADDRESS,
    abi: STAKING_VAULT_ABI,
    functionName: 'stake',
  })

  const { write: claim, data: claimTx } = useContractWrite({
    address: VAULT_ADDRESS,
    abi: STAKING_VAULT_ABI,
    functionName: 'claim',
  })

  const stakeConfirm = useWaitForTransaction({ hash: stakeTx?.hash })
  const claimConfirm = useWaitForTransaction({ hash: claimTx?.hash })

  return {
    stakeInfo,
    timeLeft,
    stake,
    claim,
    stakeConfirm,
    claimConfirm,
  }
}
```

### Importante: Aprovação do Token

Antes de fazer stake, o usuário precisa aprovar o vault:

```ts
// Approve vault para transferir tokens
const { write: approve } = useContractWrite({
  address: NEOFLOW_ADDRESS,
  abi: NEOFLOW_ABI,
  functionName: 'approve',
})

// Aprovar antes de stake
approve({ args: [VAULT_ADDRESS, parseEther(amount)] })
```

### Deploy do Vault

```bash
# 1. Deploy do token primeiro
npm run deploy:token

# 2. Atualizar token_address no deploy_vault.py

# 3. Deploy do vault
npm run deploy:vault

# 4. Verificar no Etherscan
npm run verify:vault
```

## 🎁 NeoFlowClaim - Sistema de Claim

Sistema eficiente de distribuição de tokens onde **usuários pagam o próprio gas** para reivindicar tokens elegíveis.

### Características

- ✅ Usuário paga o gas (distribuição eficiente)
- ✅ Whitelist configurável pelo owner
- ✅ Claim único por endereço
- ✅ Proteção CEI (Checks-Effects-Interactions)

### Deploy e Setup

```bash
# 1. Deploy do contrato de claim
npm run deploy:claim

# 2. Transferir tokens para o contrato
# 3. Configurar whitelist de endereços elegíveis
# 4. Usuários fazem claim pagando seu próprio gas
```

Para instruções completas, consulte: **[CLAIM_SETUP.md](./CLAIM_SETUP.md)**

### Deploy do Claim

```bash
# 1. Deploy do token primeiro (se ainda não feito)
npm run deploy:token

# 2. Deploy do claim
npm run deploy:claim

# 3. Verificar no Etherscan
npm run verify:claim
```

## 📚 Recursos

- [Ape Framework Documentation](https://docs.apeworx.io/)
- [OpenZeppelin Contracts](https://docs.openzeppelin.com/contracts)
- [Solidity Documentation](https://docs.soliditylang.org/)
- [Wagmi Documentation](https://wagmi.sh/)
- [Viem Documentation](https://viem.sh/)

## 👤 Autor

**MELLØ**

## 📄 Licença

MIT
