# 🔍 Encontrar Signer Quando Contrato Não Está Verificado

## ❌ Situação

O contrato **não está verificado**, então a aba "Read Contract" está vazia.

Não conseguimos ver a função `signer()` porque o código não está público ainda.

---

## ✅ Solução: Procurar na Transação de Criação

### **Método Visual Passo a Passo:**

#### **Passo 1: Na Página Atual**

Você está em:
```
bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017#readContract
```

Na seção **"More Info"**, você vê:

- **"CONTRACT CREATOR"** → `0x45f9C5Af...6E4D42A53`
- **"Created: 111 days ago"**

#### **Passo 2: Clique no Endereço do Creator**

**CLIQUE em:** `0x45f9C5Af...6E4D42A53`

Isso abre a página do endereço que criou o contrato.

#### **Passo 3: Na Página do Creator**

Na nova página, procure por:
- **"Contract Creation"**
- Ou uma lista de contratos criados
- Deve mostrar: `0xBc972E10Df612C7d65054BC67aBCA96B3C22a017`

#### **Passo 4: Clique na Transação**

Clique na **transação** (não no endereço do contrato) que criou o BOX Token.

**Você vai ver:**
- Transaction Hash
- Block Number
- **Input Data** ← **ESTE É O QUE PROCURAMOS!**

#### **Passo 5: Encontre o Input Data**

Na página da transação:
- Procure por **"Input Data"** (pode estar mais abaixo, role a página)
- É uma seção com um código hexadecimal muito longo
- Parece algo como: `0x608060405234801561001057600080fd5b506...`

#### **Passo 6: Identifique o Signer**

O Input Data tem esta estrutura:
```
[Bytecode completo do contrato][Constructor Arguments]
```

**Para encontrar o signer:**
- O contrato InterboxCoin tem constructor: `constructor(address _signer)`
- Um endereço tem 20 bytes = 40 caracteres hex
- O signer está nos **últimos bytes** do Input Data

**Como fazer:**
1. Copie TODO o Input Data
2. Os últimos caracteres são o constructor argument
3. Procure por um padrão que parece endereço (após muito código hex)
4. Geralmente aparece algo como: `...000000000000000000000000[40_CHARS_DO_ENDERECO]`

**Exemplo:**
- Se Input Data termina com: `...000000000000000000000000A1B2C3D4E5F6789012345678901234567890ABCD`
- O signer é: `0xA1B2C3D4E5F6789012345678901234567890ABCD`

---

## ✅ Alternativa: Link Direto para Input Data

Se você souber o hash da transação de criação, pode acessar diretamente:

```
https://bscscan.com/tx/[HASH_DA_TRANSACAO]
```

**Como descobrir o hash:**
- Na página do creator, veja as transações
- Procure pela transação que criou o contrato BOX
- O hash é uma string longa começando com `0x`

---

## 🔧 Outra Opção: Usar Sourcify (Recomendado!)

O Sourcify **pode calcular o constructor argument automaticamente** mesmo sem você fornecer!

### **Passo a Passo:**

1. **Acesse:** https://sourcify.dev/

2. **Selecione:**
   - **Network:** `Binance Smart Chain`
   - **Chain ID:** `56`

3. **Informe o endereço:**
   ```
   0xBc972E10Df612C7d65054BC67aBCA96B3C22a017
   ```

4. **Escolha método:**
   - **"Solidity Files"** (não JSON)

5. **Faça upload:**
   - Arquivo: `InterboxCoin_Flattened_Final.sol`
   - Ou cole o código diretamente

6. **Preencha:**
   - **Compiler Version:** `0.8.24`
   - **Contract Name:** `InterboxCoin`

7. **Clique em "Verify"**

O Sourcify vai tentar calcular o constructor argument automaticamente comparando bytecodes!

---

## 📋 Checklist - Método Transação de Criação

- [ ] Estou na página do contrato no BSCScan
- [ ] Vi "Contract Creator": `0x45f9C5Af...6E4D42A53`
- [ ] Cliquei no endereço do creator
- [ ] Encontrei a transação que criou o contrato
- [ ] Cliquei na transação (não no endereço)
- [ ] Encontrei a seção "Input Data"
- [ ] Copiei o Input Data completo
- [ ] Identifiquei os últimos bytes (40 chars hex)
- [ ] Identifiquei o endereço do signer

---

## 💡 Dica: Decodificador de Input Data

Se você conseguir copiar o Input Data completo, posso criar um script para extrair o signer automaticamente!

**O que preciso:**
- O Input Data completo da transação de criação

**Posso criar um script que:**
- Lê o Input Data
- Extrai o constructor argument automaticamente
- Calcula o ABI-encoded formatado

---

## 🎯 Recomendação Imediata

**Tente PRIMEIRO o Sourcify** - é muito mais fácil e pode calcular automaticamente!

1. Acesse: https://sourcify.dev/
2. Binance Smart Chain
3. Endereço: `0xBc972E10Df612C7d65054BC67aBCA96B3C22a017`
4. Upload: `InterboxCoin_Flattened_Final.sol`
5. Verify!

**O Sourcify pode conseguir mesmo sem você fornecer o constructor argument!** ✅

---

## 🔗 Links Úteis

- **Sourcify:** https://sourcify.dev/
- **Contrato:** https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017
- **Creator:** (Clique no endereço `0x45f9C5Af...6E4D42A53` para ver as transações)

---

**Recomendação: Use o Sourcify primeiro! É mais fácil e pode funcionar sem o constructor argument!** 🚀

