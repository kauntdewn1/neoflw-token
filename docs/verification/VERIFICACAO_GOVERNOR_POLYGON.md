# ✅ Verificação do DaoGovernor no PolygonScan

**Contrato:** `DaoGovernor`  
**Rede:** Polygon Mainnet (Chain ID: 137)  
**Deploy script:** `scripts/deploy/deploy_governor.py`  
**Endereços envolvidos:**  
- `NeoFlowTokenVotes` (token de votação)  
- `TimelockController` (criado no próprio script)  

> ⚠️ **Importante:** primeiro faça o deploy do `NeoFlowTokenVotes` e anote o endereço.  
> Em seguida, rode `deploy_governor.py` e anote **Governor** e **Timelock**.

---

## 1. Deploy (resumo)

```bash
# 1) Deploy do token de votação
ape run scripts/deploy/deploy_token_votes --network polygon:mainnet
cat .token_votes_address.txt  # endereço do NeoFlowTokenVotes

# 2) Deploy do sistema de governança (Governor + Timelock)
ape run scripts/deploy/deploy_governor --network polygon:mainnet
cat .governor_address.txt     # endereço do DaoGovernor
cat .timelock_address.txt     # endereço do TimelockController
```

Guarde o `[ENDERECO_GOVERNOR]` para usar no PolygonScan.

---

## 2. Acessar o contrato no PolygonScan

Abra no navegador:

```text
https://polygonscan.com/address/[ENDERECO_GOVERNOR]#code
```

Exemplo (não real):  
`https://polygonscan.com/address/0xSEU_ENDERECO_GOVERNOR#code`

---

## 3. Iniciar verificação

Na página do contrato `DaoGovernor`:

1. Clique na aba **“Contract”**
2. Clique em **“Verify and Publish”**

---

## 4. Escolher método de verificação

Para o `DaoGovernor`, recomendo usar **Standard JSON Input**:

- **Verification Method:** `Solidity (Standard JSON Input)`
- **Compiler:** `v0.8.18+commit.87f61d96` (mesma versão do projeto)
- **License:** `MIT`
- **Optimization:** Yes, 200 runs (mesma config dos demais contratos)

### 4.1. Gerar Standard JSON Input (se ainda não tiver)

No projeto:

```bash
ape compile --standard-json > artifacts/verification/standard-json-all.json
```

Ou gere um JSON só com o `DaoGovernor` se preferir.

Depois:

1. Abra o arquivo JSON gerado.
2. Use-o no campo **“Standard JSON Input”** do PolygonScan.

---

## 5. Constructor Arguments (DaoGovernor)

O construtor é:

```solidity
constructor(
    ERC20Votes _token,
    TimelockController _timelock,
    uint256 _votingDelay,
    uint256 _votingPeriod,
    uint256 _proposalThreshold,
    uint256 _quorumPercentage
) ...
```

Esses valores foram passados no deploy via `deploy_governor.py`.  
Para obter os argumentos exatos no formato esperado pelo PolygonScan:

### Método recomendado (via PolygonScan)

1. Vá na aba **“Transactions”** do endereço do `DaoGovernor`.
2. Clique na **transação de criação** (Contract Creation).
3. Na transação:
   - Vá em **“Input Data”**
   - Clique em **“Decode Input Data”**  
     ou **“Constructor Arguments”** (se disponível).
4. O PolygonScan mostrará os argumentos decodificados e/ou o campo **ABI-encoded**.
5. Copie a string de **Constructor Arguments (ABI-encoded)** e use no campo:

> **Constructor Arguments (ABI-encoded):**  
> cole exatamente o valor que o PolygonScan mostrar.

---

## 6. Finalizar verificação

Na tela de verificação:

1. Preencha:
   - **Compiler Version:** `v0.8.18+commit.87f61d96`
   - **License:** `MIT`
   - **Optimization:** Yes, 200
   - **Contract Name:** `DaoGovernor`
   - **Constructor Arguments (ABI-encoded):** (copiados da transação de deploy)
2. Clique em **“Verify and Publish”**.

---

## 7. Confirmar que deu certo

Depois da verificação:

1. Volte para a aba **“Code”** do `DaoGovernor`.
2. Confirme que aparece:
   - **“Contract Source Code Verified”**
3. Teste:
   - Aba **“Read as Proxy”** / **“Write as Proxy”** se tiver Proxy/Timelock integrado.

---

## 📋 Resumo (DaoGovernor)

- **Nome do contrato:** `DaoGovernor`
- **Rede:** Polygon Mainnet (`137`)
- **Compiler:** `v0.8.18+commit.87f61d96`
- **License:** `MIT`
- **Optimization:** Yes, 200
- **Constructor:**  
  `constructor(ERC20Votes _token, TimelockController _timelock, uint256 _votingDelay, uint256 _votingPeriod, uint256 _proposalThreshold, uint256 _quorumPercentage)`
- **Como obter constructor args:** via aba **“Input Data / Decode Input Data / Constructor Arguments”** da transação de deploy no PolygonScan.


