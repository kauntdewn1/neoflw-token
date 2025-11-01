# NEOFLOW //  NEØ Protocol // Powered by MELLØ™

> `Infraestruturas vivas. Tokenização com propósito.`  
> *Orquestração terminal descentralizada do token $NEOFLW*

---

## 🧠 Essência do Projeto

- **Token:** `$NEOFLW` (NeoFlowOFF)  
- **Supply Inicial:** _1.000.000.000_  
- **Funções:** Staking · Claim descentralizado · DAO futura · WebApp-ready  
- **Smart Contracts:**  
  - `NeoFlowToken.sol` – ERC20 com queima  
  - `StakingVault.sol` – Staking 6 meses + 10%  
  - `NeoFlowClaim.sol` – Claim com gas pago pelo usuário

---

## ⚙️ Setup Rápido

```bash
npm run plugins     # Instala dependências
npm run compile     # Compila contratos
npm run test        # Executa testes
npm run start:dev   # Pipeline total
````

---

## 🧬 Orquestração NEØ

```bash
npm run init             # Inicia projeto Ape
npm run plugins          # Plugins Solidity, Alchemy, Etherscan
npm run account:import   # Importa conta flowoff-admin
```

---

## 🧪 Dev & Test

```bash
npm run compile     # Compilação
npm run test        # Testes unitários
npm run console     # Console interativo Ape
npm run clean       # Limpa cache
```

---

## 🚀 Deploy Terminal

```bash
npm run deploy:token      # Token – Sepolia
npm run deploy:vault      # Vault – Sepolia
npm run deploy:claim      # Claim – Sepolia
npm run verify:token      # Verifica no Etherscan
npm run deploy:local      # Deploy local
npm run start:dev         # Pipeline full
```

---

## 🔐 Configuração `.env`

```bash
cp .env.example .env
```

```env
ALCHEMY_API_KEY=...
ETHERSCAN_API_KEY=...
WALLET_LABEL=flowoff-admin
APE_NETWORK=ethereum:goerli
```

---

## 🧰 Estrutura NEØ

```
neoflow/
├── contracts/
│   ├── NeoFlowToken.sol
│   ├── StakingVault.sol
│   └── NeoFlowClaim.sol
├── scripts/
├── tests/
├── ape-config.yaml
├── neo-node.json
├── package.json
└── .env.example
```

---

## 🔁 Hooks WebApp (Wagmi + Viem)

### Balance + Burn – `$NEOFLW`

```ts
export function useNeoflow() {
  const { data: balance } = useContractRead({ functionName: 'balanceOf' })
  const { write: burn } = useContractWrite({ functionName: 'burn' })
  return { balance, burn }
}
```

---

### StakingVault – 6 Meses Lock / 10% Reward

```ts
export function useStakingVault() {
  const { data: stakeInfo } = useContractRead({ functionName: 'stakes' })
  const { write: stake } = useContractWrite({ functionName: 'stake' })
  const { write: claim } = useContractWrite({ functionName: 'claim' })
  return { stakeInfo, stake, claim }
}
```

> ***Aprovação obrigatória:***
> Antes do stake, execute `approve()` do token com o `VAULT_ADDRESS`.

---

## 🔄 Claim Inteligente

* Gas pago pelo usuário
* Whitelist configurável
* Claim único por wallet
* Proteção CEI (Checks-Effects-Interactions)

```bash
npm run deploy:claim
```

---

## 📦 Front Integration

* ✅ ABI disponível após build
* ✅ WebApp compatível com Wagmi / Viem
* ✅ `NeoFlowToken`, `StakingVault`, `Claim` integráveis

---

## 📈 CI/CD Ready

* GitHub Actions — Deploy automatizado
* Vercel CLI — WebApp integrado
* Docker — Imagem com scripts NPM
* Agentes IA — Executores padronizados

```yaml
- name: Deploy Token
  run: npm run deploy:token
```

---

## 🛡️ Segurança

* 🔐 `Ownable` (OpenZeppelin)
* 🔥 `burn()` público
* 🧠 Claim com CEI
* ✅ Verificado no Etherscan

---

## 🌍 Roadmap

* ✅ Token ERC20
* ✅ Deploy + Testes Automatizados
* ✅ Vault Staking 6m + 10%
* ✅ Claim com Gas pago
* [ ] DAO Governance Voting
* ✅ WebApp Hooks (Wagmi + Viem)

---

## 📚 Referências Vivas

* [Ape Framework](https://docs.apeworx.io/)
* [Solidity](https://docs.soliditylang.org/)
* [OpenZeppelin](https://docs.openzeppelin.com/)
* [Wagmi](https://wagmi.sh/)
* [Viem](https://viem.sh/)

---

## 🔖 Autoria

**MELLØ™** – Orquestração por NEØ Protocol
[flowoff.xyz](https://flowoff.xyz)

