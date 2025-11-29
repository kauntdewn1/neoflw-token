# ✅ Verificação do NeoFlowTokenVotes no PolygonScan

**Contrato:** `NeoFlowTokenVotes`  
**Rede:** Polygon Mainnet (Chain ID: 137)  
**Deploy script:** `scripts/deploy/deploy_token_votes.py`  
**Endereço:** (usar o valor salvo em `.token_votes_address.txt` após o deploy)

---

## 🎯 Passo a passo rápido

### 1. Descobrir o endereço do contrato

Após o deploy com:

```bash
ape run scripts/deploy/deploy_token_votes --network polygon:mainnet
```

Você terá:

- Log no terminal com o endereço
- Arquivo `.token_votes_address.txt` na raiz

Confirme o endereço:

```bash
cat .token_votes_address.txt
```

Use este endereço nos passos abaixo como `[ENDERECO_TOKEN_VOTES]`.

---

## 2. Acessar o contrato no PolygonScan

Abra no navegador:

```text
https://polygonscan.com/address/[ENDERECO_TOKEN_VOTES]#code
```

Exemplo (não real):  
`https://polygonscan.com/address/0xSEU_ENDERECO_AQUI#code`

---

## 3. Iniciar verificação

Na página do contrato:

1. Clique na aba **"Contract"**
2. Clique em **"Verify and Publish"**

---

## 4. Escolher método de verificação

Recomendo seguir o mesmo fluxo do token principal (`NeoFlowToken`):

- Método: **Flattened Source Code** ou **Standard JSON Input**
- Compiler: `v0.8.18+commit.87f61d96`
- License: `MIT License (MIT)`
- Optimization: **Yes**, 200 runs

### Opção A – Flattened (mais simples)

1. Gere/abra o arquivo flattened do `NeoFlowTokenVotes`  
   (ex.: `artifacts/flattened/NeoFlowTokenVotes_flattened.sol`, se você gerar).
2. Copie TODO o conteúdo do arquivo.
3. Na tela do PolygonScan:
   - **Compiler Version:** `v0.8.18+commit.87f61d96`
   - **License:** `MIT`
   - **Contract Name:** `NeoFlowTokenVotes`
   - **Optimization:** Yes (200)
   - **Constructor Arguments (ABI-encoded):**

Como o construtor é:

```solidity
constructor(uint256 initialSupply) ERC20Votes("NEOFlowOFF", "NEOFLW") {
    _mint(msg.sender, initialSupply);
    _delegate(msg.sender, msg.sender);
}
```

E usamos o mesmo `initialSupply` do token principal (`1_000_000_000 * 10**18`),  
você pode reutilizar o **mesmo valor ABI-encoded** já calculado para o token:

```text
0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000
```

Ou, se o PolygonScan permitir modo “Decoded”, use o valor decimal:

```text
1000000000000000000000000000
```

Depois clique em **“Verify and Publish”**.

---

## 5. Confirmar verificação

Após a verificação:

1. Volte para a aba **“Code”** do contrato.
2. Confirme que aparece:
   - **“Contract Source Code Verified”**
3. Teste a aba **“Read Contract”** e **“Write Contract”** para garantir que o ABI foi carregado.

---

## 📋 Resumo dos dados do NeoFlowTokenVotes

- **Nome do contrato:** `NeoFlowTokenVotes`
- **Compiler:** `v0.8.18+commit.87f61d96`
- **License:** `MIT`
- **Optimization:** Yes, 200 runs
- **Constructor:** `constructor(uint256 initialSupply)`
- **Constructor args (decimal):** `1000000000000000000000000000`
- **Constructor args (ABI-encoded):**  
  `0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000`

