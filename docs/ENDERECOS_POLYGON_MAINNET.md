# 📍 Endereços Oficiais – Polygon Mainnet (NEOFLW)

**Rede:** Polygon Mainnet (Chain ID: 137)  
**Explorer:** `https://polygonscan.com`

---

## 1. Contratos Principais (Já Deployados)

### 1.1 Token ERC20 – NeoFlowToken

- **Nome:** `NeoFlowToken`
- **Símbolo:** `NEOFLW`
- **Endereço:** `0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2`
- **Contrato:**  
  `https://polygonscan.com/address/0x59aa4eae743d608fbdd4205eba59b38dca755dd2`

---

### 1.2 StakingVault

- **Nome:** `StakingVault`
- **Função:** Vault de staking (lock 6 meses, 10% reward)
- **Endereço:** `0x07E39107d4B35b64f9f2310B9A2B8e5262A4ee41`
- **Contrato:**  
  `https://polygonscan.com/address/0x07E39107d4B35b64f9f2310B9A2B8e5262A4ee41`

---

### 1.3 NeoFlowClaim

- **Nome:** `NeoFlowClaim`
- **Função:** Claim descentralizado (whitelist)
- **Endereço:** `0x407C037906d6441ECD4a3F9064eab2E6CF03b36b`
- **Contrato:**  
  `https://polygonscan.com/address/0x407C037906d6441ECD4a3F9064eab2E6CF03b36b`

---

## 2. Governança e Gamificação

### 2.1 NeoFlowTokenVotes (Token de Votação)

- **Contrato:** `NeoFlowTokenVotes`
- **Script de deploy:** `scripts/deploy/deploy_token_votes.py`
- **Arquivo de endereço (após deploy):** `.token_votes_address.txt`
- **Endereço:** `0xEce94d3719fc6FDe7275051a54caf1F7d5098d59`
- **Contrato (PolygonScan):**  
  `https://polygonscan.com/address/0xEce94d3719fc6FDe7275051a54caf1F7d5098d59`

---

### 2.2 DaoGovernor

- **Contrato:** `DaoGovernor`
- **Script de deploy:** `scripts/deploy/deploy_governor.py`
- **Arquivo de endereço (após deploy):** `.governor_address.txt`
- **Endereço:** `0xeA6cedF9eD5d67fd2785Dd1cb34F434477927bB0`
- **Contrato (PolygonScan):**  
  `https://polygonscan.com/address/0xeA6cedF9eD5d67fd2785Dd1cb34F434477927bB0`

---

### 2.3 TimelockController (Governança)

- **Contrato:** `NeoFlowTimelockController`
- **Criado junto com o `DaoGovernor` no script de deploy**
- **Arquivo de endereço (após deploy):** `.timelock_address.txt`
- **Endereço:** `0xCe47c1045f41bF80d7bbDB7ff725fab03A471e5F`
- **Contrato (PolygonScan):**  
  `https://polygonscan.com/address/0xCe47c1045f41bF80d7bbDB7ff725fab03A471e5F`

---

### 2.4 GamificationController

- **Contrato:** `GamificationController`
- **Script de deploy:** `scripts/deploy/deploy_gamification.py`
- **Arquivo de endereço (sugerido após deploy):** `.gamification_address.txt`
- **Endereço:** `0xfbD4b4e0Cd08d871042Db1D4CC47e7bb66d1aDE3`
- **Contrato (PolygonScan):**  
  `https://polygonscan.com/address/0xfbD4b4e0Cd08d871042Db1D4CC47e7bb66d1aDE3`
  
---

## 3. Onde esses endereços também estão salvos

### 3.1 Arquivos de endereços

- `./.token_address.txt` → Token (`NeoFlowToken`)
- `./.vault_address.txt` → `StakingVault`
- `./.claim_address.txt` → `NeoFlowClaim`
- `./artifacts/addresses/.token_address.txt`
- `./artifacts/addresses/.vault_address.txt`
- `./artifacts/addresses/.claim_address.txt`

### 3.2 Variáveis de ambiente (`.env`)

```env

NEXT_PUBLIC_TOKEN_ADDRESS=0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2
NEXT_PUBLIC_VAULT_ADDRESS=0x07E39107d4B35b64f9f2310B9A2B8e5262A4ee41
NEXT_PUBLIC_CLAIM_ADDRESS=0x407C037906d6441ECD4a3F9064eab2E6CF03b36b
NEXT_PUBLIC_GOVERNOR_ADDRESS=0xeA6cedF9eD5d67fd2785Dd1cb34F434477927bB0
NEXT_PUBLIC_GAMIFICATION_ADDRESS=0xfbD4b4e0Cd08d871042Db1D4CC47e7bb66d1aDE3
---

## 4. Referências rápidas

- **Token (NEOFLW):**  
  `https://polygonscan.com/address/0x59aa4eae743d608fbdd4205eba59b38dca755dd2`
- **Vault:**  
  `https://polygonscan.com/address/0x07E39107d4B35b64f9f2310B9A2B8e5262A4ee41`
- **Claim:**  
  `https://polygonscan.com/address/0x407C037906d6441ECD4a3F9064eab2E6CF03b36b`

---

**Última atualização:** 2025-11-29


