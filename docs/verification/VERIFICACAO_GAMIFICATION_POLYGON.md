# ✅ Verificação do GamificationController no PolygonScan

**Contrato:** `GamificationController`  
**Rede:** Polygon Mainnet (Chain ID: 137)  
**Deploy script:** `scripts/deploy/deploy_gamification.py`  
**Parâmetro de construtor:** endereço do token NEOFLW (`address _neoflwToken`)

---

## 1. Deploy (resumo)

```bash
ape run scripts/deploy/deploy_gamification --network polygon:mainnet
```

O script irá pedir:

- `Enter NEOFLW Token address:` → use `0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2`

Anote o endereço retornado (ex.: `0xSEU_ENDERECO_GAMIFICATION`) e, se quiser, salve manualmente em um arquivo:

```bash
echo "0xSEU_ENDERECO_GAMIFICATION" > .gamification_address.txt
```

---

## 2. Acessar o contrato no PolygonScan

Abra no navegador:

```text
https://polygonscan.com/address/0xSEU_ENDERECO_GAMIFICATION#code
```

Substitua `0xSEU_ENDERECO_GAMIFICATION` pelo endereço real do contrato.

---

## 3. Iniciar verificação

Na página do `GamificationController`:

1. Clique na aba **“Contract”**
2. Clique em **“Verify and Publish”**

---

## 4. Escolher método de verificação

Recomendado: **Standard JSON Input** (mais confiável para contratos com imports).

Configurações:

- **Compiler:** `v0.8.18+commit.87f61d96`
- **License:** `MIT`
- **Optimization:** Yes, 200 runs

### 4.1. Gerar Standard JSON Input (se ainda não tiver)

```bash
ape compile --standard-json > artifacts/verification/standard-json-all.json
```

Na tela do PolygonScan:

1. Selecione **“Solidity (Standard JSON Input)”**
2. Cole o conteúdo de `artifacts/verification/standard-json-all.json`
3. Defina:
   - **Contract Name:** `GamificationController`

---

## 5. Constructor Arguments (GamificationController)

O construtor é:

```solidity
constructor(address _neoflwToken) {
    require(_neoflwToken != address(0), "Invalid token address");
    neoflwToken = IERC20(_neoflwToken);
    _setupDefaultQuests();
}
```

No deploy, você passou o endereço do token NEOFLW (`0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2`).

### Maneira simples de obter o valor correto:

1. Vá na aba **“Transactions”** do endereço do `GamificationController`.
2. Clique na **transação de criação** (Contract Creation).
3. Na transação:
   - Vá em **“Input Data”**
   - Clique em **“Decode Input Data”** ou **“Constructor Arguments”**
4. O PolygonScan mostrará o argumento `_neoflwToken` já decodificado.
5. Use esse endereço como argumento de construtor na verificação.

Se o PolygonScan pedir o **constructor ABI-encoded**, você pode:

1. Copiar diretamente o campo **“Constructor Arguments (ABI-encoded)”** que ele mostrar.
2. Colar no campo correspondente na tela de verificação.

---

## 6. Finalizar verificação

Na tela de verificação:

1. Preencha:
   - **Compiler Version:** `v0.8.18+commit.87f61d96`
   - **License:** `MIT`
   - **Optimization:** Yes, 200
   - **Contract Name:** `GamificationController`
   - **Constructor Arguments:** endereço do token NEOFLW (ou string ABI-encoded, se for o caso)
2. Clique em **“Verify and Publish”**.

---

## 7. Confirmar que deu certo

Depois da verificação:

1. Volte à aba **“Code”** do contrato.
2. Verifique se aparece **“Contract Source Code Verified”**.
3. Use as abas **“Read Contract”** e **“Write Contract”** para validar o ABI.

---

## 📋 Resumo (GamificationController)

- **Nome do contrato:** `GamificationController`
- **Rede:** Polygon Mainnet (`137`)
- **Compiler:** `v0.8.18+commit.87f61d96`
- **License:** `MIT`
- **Optimization:** Yes, 200
- **Constructor:** `constructor(address _neoflwToken)`
- **Parâmetro:** endereço do token NEOFLW (`0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2`)


