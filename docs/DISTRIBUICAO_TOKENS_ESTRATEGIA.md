# 💰 Estratégia de Distribuição de Tokens NEOFLW - Documento Completo

**Data de Criação:** 2025-01-XX  
**Status:** ✅ Contratos Deployados em Polygon Mainnet  
**Última Atualização:** Verificar com `git log docs/DISTRIBUICAO_TOKENS_ESTRATEGIA.md`

---

## 📊 STATUS ATUAL DOS DEPLOYS

### ✅ Contratos Deployados em Polygon Mainnet

| Contrato | Endereço | Status | Polygonscan |
|----------|----------|--------|-------------|
| **NeoFlowToken** | `0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2` | ✅ Deployado | [Ver](https://polygonscan.com/address/0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2) |
| **StakingVault** | `0x07E39107d4B35b64f9f2310B9A2B8e5262A4ee41` | ✅ Deployado | [Ver](https://polygonscan.com/address/0x07E39107d4B35b64f9f2310B9A2B8e5262A4ee41) |
| **NeoFlowClaim** | `0x407C037906d6441ECD4a3F9064eab2E6CF03b36b` | ✅ Deployado | [Ver](https://polygonscan.com/address/0x407C037906d6441ECD4a3F9064eab2E6CF03b36b) |

### 📝 Arquivos de Endereços

- `.token_address.txt` → `0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2`
- `.vault_address.txt` → `0x07E39107d4B35b64f9f2310B9A2B8e5262A4ee41`
- `.claim_address.txt` → `0x407C037906d6441ECD4a3F9064eab2E6CF03b36b`

### 👤 Wallet de Deploy

- **Label:** `neoflow-admin`
- **Endereço:** `0x460F9D0cf3e6E84faC1A7Abc524ddfa66fb64f60`
- **Status:** ✅ Configurada e com saldo de POL

---

## 💎 TOKENOMICS NEOFLW - Distribuição Completa

### 📈 Especificações Técnicas

| Parâmetro | Valor |
|-----------|-------|
| **Nome** | NEOFlowOFF |
| **Símbolo** | NEOFLW |
| **Decimais** | 18 |
| **Total Supply** | 1,000,000,000 NEOFLW (1 bilhão) |
| **Network** | Polygon Mainnet (Chain ID: 137) |
| **Padrão** | ERC-20 |
| **Burnable** | ✅ Sim |
| **Governança** | ✅ Sim (ERC20Votes para DAO) |

### 🎯 Distribuição Proposta (100% = 1,000,000,000 NEOFLW)

```
TOTAL SUPPLY: 1,000,000,000 NEOFLW (100%)

├─ 🎮 Gamificação & Rewards: 400M (40%)
│  ├─ Quest Rewards: 200M (20%) → GamificationController
│  ├─ Staking Rewards: 100M (10%) → StakingVault ⭐
│  ├─ Referral Program: 50M (5%) → GamificationController
│  └─ Badges & Achievements: 50M (5%) → GamificationController
│
├─ 👥 Comunidade & Airdrop: 250M (25%)
│  ├─ Initial Airdrop: 100M (10%) → NeoFlowClaim ⭐
│  ├─ Community Rewards: 75M (7.5%) → Wallet de Deploy
│  ├─ Early Adopters: 50M (5%) → Wallet de Deploy
│  └─ Marketing & Partnerships: 25M (2.5%) → Wallet de Deploy
│
├─ 🏛️ Governança DAO: 150M (15%)
│  ├─ Treasury: 100M (10%) → Wallet de Deploy (ou DAO quando criado)
│  ├─ Voting Rewards: 30M (3%) → Wallet de Deploy
│  └─ Proposals Fund: 20M (2%) → Wallet de Deploy
│
├─ 👨‍💼 Equipe & Desenvolvimento: 100M (10%)
│  ├─ Team: 60M (6%) → Wallet de Deploy (Vesting 4 anos)
│  ├─ Development: 25M (2.5%) → Wallet de Deploy
│  └─ Advisors: 15M (1.5%) → Wallet de Deploy (Vesting 2 anos)
│
├─ 💼 Reserva Estratégica: 50M (5%)
│  └─ Future Partnerships → Wallet de Deploy
│
└─ 🔥 Liquidity & Exchange: 50M (5%)
   ├─ DEX Liquidity: 30M (3%) → Wallet de Deploy
   └─ CEX Listing: 20M (2%) → Wallet de Deploy
```

---

## 🚀 SITUAÇÃO ATUAL APÓS DEPLOY

### ⚠️ IMPORTANTE: Distribuição Inicial

**Após o deploy do token, TODOS os 1 bilhão de tokens foram mintados para a wallet de deploy (`neoflow-admin`).**

A wallet de deploy atua como **treasury temporária** até que os tokens sejam distribuídos conforme a tokenomics.

### 📊 Status Atual da Distribuição

| Destino | Quantidade | Status | Observações |
|---------|------------|--------|-------------|
| **Wallet de Deploy** | 1,000M (100%) | ✅ Todos os tokens aqui | Treasury temporária |
| **NeoFlowClaim** | 0M (0%) | ⏳ Pendente | Precisa transferir 100M |
| **StakingVault** | 0M (0%) | ⏳ Pendente | Precisa transferir 100M |
| **GamificationController** | 0M (0%) | ⏳ Não deployado | Deployar e transferir 300M |

---

## 📋 ESTRATÉGIA DE DISTRIBUIÇÃO

### Fase 1: Distribuição para Contratos Deployados (200M)

#### 1.1. NeoFlowClaim - Initial Airdrop (100M)

**Objetivo:** Distribuir tokens para airdrop inicial da comunidade

**Quantidade:** 100,000,000 NEOFLW (10% do total supply)

**Como transferir:**

```bash
# Opção 1: Script automatizado (recomendado)
ape run scripts/setup/transfer_to_claim --network polygon:mainnet

# Opção 2: Quantidade customizada
ape run scripts/setup/transfer_to_claim -- 50 --network polygon:mainnet  # 50M tokens
```

**Após transferir:**

- Configurar whitelist de endereços elegíveis
- Usuários poderão fazer claim pagando seu próprio gas

**Script:** `scripts/setup/transfer_to_claim.py`

---

#### 1.2. StakingVault - Staking Rewards (100M)

**Objetivo:** Pool de rewards para staking (10% APY, 6 meses lock)

**Quantidade:** 100,000,000 NEOFLW (10% do total supply)

**Como transferir:**
```bash
# Criar script similar ou usar console do Ape
ape console --network polygon:mainnet

# No console:
>>> from ape import accounts, project
>>> acct = accounts.load("neoflow-admin")
>>> token = project.NeoFlowToken.at("0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2")
>>> vault = project.StakingVault.at("0x07E39107d4B35b64f9f2310B9A2B8e5262A4ee41")
>>> amount = 100_000_000 * 10**18
>>> token.transfer(vault.address, amount, sender=acct, auto_confirm=True)
```

**Após transferir:**

- Tokens estarão disponíveis para rewards de staking
- Usuários podem fazer stake e receber 10% APY após 6 meses

---

### Fase 2: Manter na Wallet de Deploy (800M)

**Estratégia:** Manter o restante na wallet de deploy para distribuição gradual conforme necessidade.

#### 2.1. Comunidade & Airdrop (150M restantes)

- **Community Rewards:** 75M (7.5%) - Distribuir gradualmente
- **Early Adopters:** 50M (5%) - Distribuir conforme onboarding
- **Marketing & Partnerships:** 25M (2.5%) - Usar para parcerias

#### 2.2. Governança DAO (150M)

- **Treasury:** 100M (10%) - Transferir para DAO quando criado
- **Voting Rewards:** 30M (3%) - Distribuir para votantes
- **Proposals Fund:** 20M (2%) - Financiar propostas aprovadas

#### 2.3. Equipe & Desenvolvimento (100M)

- **Team:** 60M (6%) - **Implementar vesting de 4 anos**
- **Development:** 25M (2.5%) - Usar para desenvolvimento
- **Advisors:** 15M (1.5%) - **Implementar vesting de 2 anos**

#### 2.4. Reserva Estratégica (50M)

- **Future Partnerships:** 50M (5%) - Manter para expansão

#### 2.5. Liquidity & Exchange (50M)

- **DEX Liquidity:** 30M (3%) - Criar pools quando necessário
- **CEX Listing:** 20M (2%) - Reservar para listing em exchanges

---

### Fase 3: GamificationController (300M) - Quando Deployado

**Objetivo:** Pool de rewards para gamificação

**Quantidade:** 300,000,000 NEOFLW (30% do total supply)

**Distribuição:**
- Quest Rewards: 200M (20%)
- Referral Program: 50M (5%)
- Badges & Achievements: 50M (5%)

**Como transferir (quando deployado):**
```bash
# Após deploy do GamificationController
ape console --network polygon:mainnet

# No console:
>>> from ape import accounts, project
>>> acct = accounts.load("neoflow-admin")
>>> token = project.NeoFlowToken.at("0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2")
>>> gamification = project.GamificationController.at("<endereço>")
>>> amount = 300_000_000 * 10**18
>>> token.transfer(gamification.address, amount, sender=acct, auto_confirm=True)
```

---

## 🛠️ SCRIPTS DISPONÍVEIS

### Scripts de Distribuição

#### 1. `scripts/setup/transfer_to_claim.py`
**Função:** Transferir tokens para o contrato de Claim

**Uso:**
```bash
# Padrão: 100M tokens (conforme tokenomics)
ape run scripts/setup/transfer_to_claim --network polygon:mainnet

# Customizado: 50M tokens
ape run scripts/setup/transfer_to_claim -- 50 --network polygon:mainnet
```

**Características:**
- Lê endereços de `.token_address.txt` e `.claim_address.txt`
- Verifica saldo antes de transferir
- Mostra percentual do total supply
- Confirma antes de executar

---

#### 2. `scripts/setup/distribute_initial_tokens.py`
**Função:** Distribuição completa e automatizada conforme tokenomics

**Uso:**
```bash
ape run scripts/setup/distribute_initial_tokens --network polygon:mainnet
```

**Características:**
- Verifica quais contratos estão deployados
- Distribui automaticamente para Claim e Vault
- Mostra o que fica na wallet de deploy
- Calcula percentuais corretos
- Resumo completo da distribuição

---

## 📝 CHECKLIST DE DISTRIBUIÇÃO

### ✅ Já Feito

- [x] Deploy do NeoFlowToken
- [x] Deploy do StakingVault
- [x] Deploy do NeoFlowClaim
- [x] Documentação da estratégia criada

### ⏳ Pendente

- [ ] Transferir 100M tokens para NeoFlowClaim
- [ ] Transferir 100M tokens para StakingVault
- [ ] Configurar whitelist no NeoFlowClaim
- [ ] Deploy do GamificationController
- [ ] Transferir 300M tokens para GamificationController
- [ ] Criar multi-sig wallet para treasury
- [ ] Implementar vesting para Team (60M)
- [ ] Implementar vesting para Advisors (15M)
- [ ] Transferir treasury para DAO quando criado

---

## 🔐 SEGURANÇA E BOAS PRÁTICAS

### ⚠️ IMPORTANTE

1. **Multi-Sig Wallet:** Criar multi-sig wallet para treasury no futuro
2. **Vesting:** Implementar contratos de vesting para Team e Advisors
3. **Backup:** Manter backup seguro das private keys
4. **Documentação:** Atualizar este documento após cada distribuição
5. **Verificação:** Verificar saldos após cada transferência

### 📊 Verificar Saldos

```bash
# Verificar saldo da wallet de deploy
ape console --network polygon:mainnet
>>> from ape import accounts, project
>>> acct = accounts.load("neoflow-admin")
>>> token = project.NeoFlowToken.at("0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2")
>>> token.balanceOf(acct.address) / 10**18

# Verificar saldo do Claim
>>> claim = project.NeoFlowClaim.at("0x407C037906d6441ECD4a3F9064eab2E6CF03b36b")
>>> token.balanceOf(claim.address) / 10**18

# Verificar saldo do Vault
>>> vault = project.StakingVault.at("0x07E39107d4B35b64f9f2310B9A2B8e5262A4ee41")
>>> token.balanceOf(vault.address) / 10**18
```

---

## 📚 REFERÊNCIAS

### Documentação Relacionada

- **Tokenomics Completa:** `docs/contracts/migr_mainnet_polygon.md`
- **Deploy Polygon:** `docs/deploy/MIGRACAO_POLYGON.md`
- **Claim Setup:** `docs/deploy/CLAIM_SETUP.md`
- **Status Deploy:** `docs/STATUS_ATUAL_DEPLOY.md`

### Contratos

- **Token:** `contracts/NeoFlowToken.sol`
- **Vault:** `contracts/StakingVault.sol`
- **Claim:** `contracts/NeoFlowClaim.sol`

### Scripts

- **Transfer to Claim:** `scripts/setup/transfer_to_claim.py`
- **Distribute Initial:** `scripts/setup/distribute_initial_tokens.py`

---

## 📞 PRÓXIMOS PASSOS

1. **Imediato:**
   - Executar distribuição para Claim (100M)
   - Executar distribuição para Vault (100M)

2. **Curto Prazo:**
   - Configurar whitelist no Claim
   - Deploy do GamificationController
   - Transferir 300M para GamificationController

3. **Médio Prazo:**
   - Criar multi-sig wallet
   - Implementar vesting contracts
   - Transferir treasury para DAO

4. **Longo Prazo:**
   - Distribuir Community Rewards gradualmente
   - Criar liquidity pools
   - Preparar para CEX listing

---

**⚠️ NOTA FINAL:** Este documento deve ser atualizado após cada distribuição de tokens para manter o registro preciso do estado atual.

