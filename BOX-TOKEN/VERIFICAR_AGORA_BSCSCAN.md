# ✅ Verificar Agora no BSCScan - Tudo Pronto!

## 🎯 Descoberta Importante!

Análise do **Input Data completo** revelou que o contrato foi deployado com **DOIS argumentos no constructor**, não apenas um!

---

## 📊 Constructor Arguments Completos

**Argumento 1 (uint256):** `1000000000000000000000000` (1 milhão de tokens)
**Argumento 2 (address):** `0x45f9c5af31678bc1dacddf348936a6a6e4d42a53` (signer)

**Constructor Arguments Completo (pronto para usar):**
```
00000000000000000000000000000000000000000000d3c21bcecceda100000000000000000000000000000045f9c5af31678bc1dacddf348936a6a6e4d42a53
```

⚠️ **Tamanho:** 128 caracteres hex (não apenas 64!)

---

## 🚀 Passo a Passo no BSCScan

### **Passo 1: Acesse a Página de Verificação**

**URL:**
```
https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017#code
```

**Clique em:** "Verify and Publish"

---

### **Passo 2: Preencha o Formulário**

#### **2.1. Compiler Type:**
```
Solidity (Single file)
```
⚠️ **IMPORTANTE:** Selecione **"Single file"**, NÃO "Standard JSON Input"!

#### **2.2. Compiler Version:**
```
0.8.24+commit.e11b9ed9
```
Ou tente versões próximas:
- `0.8.24+commit.xxxxx` (outras variantes)
- `0.8.23+commit.xxxxx`
- `0.8.25+commit.xxxxx`

#### **2.3. Open Source License Type:**
```
MIT License (MIT)
```

#### **2.4. EVM Version to target:**
```
default
```
**Ou se "default" não estiver disponível:** `london` ou `shanghai`

**⚠️ IMPORTANTE:** 
- Use **"default"** se disponível (recomendado)
- Se não tiver "default", use **"london"**
- **Evite "cancun"** (ainda não totalmente suportado na BSC)
- Veja guia completo: [`EERSION_EVM_BSCSCAN.md`](./EERSION_EVM_BSCSCAN.md)

#### **2.5. Enter the Solidity Contract Code below:**

**Copie TODO o conteúdo de:** `InterboxCoin_Flattened_Final.sol`

**Como fazer:**
1. Abra o arquivo: `BOX-TOKEN/InterboxCoin_Flattened_Final.sol`
2. Selecione tudo: `Ctrl+A` / `Cmd+A`
3. Copie: `Ctrl+C` / `Cmd+C`
4. Cole no campo do BSCScan

#### **2.6. Constructor Arguments:**

**Cole este valor COMPLETO (128 caracteres):**
```
00000000000000000000000000000000000000000000d3c21bcecceda100000000000000000000000000000045f9c5af31678bc1dacddf348936a6a6e4d42a53
```

⚠️ **Sem `0x` no início!** Apenas o valor hexadecimal completo.
⚠️ **Importante:** São DOIS argumentos concatenados (uint256 + address)

#### **2.7. Optimization Enabled:**
```
Yes
```

#### **2.8. Optimization Runs:**
```
200
```

---

### **Passo 3: Verifique e Envie**

**Antes de clicar em "Verify and Publish", verifique:**

- [ ] Compiler Type: Single file ✅
- [ ] Compiler Version: 0.8.24 (ou próxima) ✅
- [ ] License: MIT ✅
- [ ] EVM Version: default ou london ✅
- [ ] Código: Colado completamente ✅
- [ ] Constructor Arguments: `00000000000000000000000000000000000000000000d3c21bcecceda100000000000000000000000000000045f9c5af31678bc1dacddf348936a6a6e4d42a53` (128 chars) ✅
- [ ] Optimization: Yes, Runs: 200 ✅

**Clique em:** "Verify and Publish"

---

### **Passo 4: Aguarde**

- Pode levar alguns minutos
- Você verá uma mensagem de sucesso ou erro
- Se der erro, veja troubleshooting abaixo

---

## 🔧 Se Ainda Não Funcionar

### **Tente Estas Variações:**

**Variação 1:**
- Optimization: `No`
- Resto igual

**Variação 2:**
- Compiler Version: `0.8.23+commit.xxxxx`
- Resto igual

**Variação 3:**
- Optimization: `Yes`
- Runs: `100` (ao invés de 200)

---

## 📋 Resumo Rápido

**Constructor Arguments COMPLETO (copie e cole - 128 caracteres):**
```
00000000000000000000000000000000000000000000d3c21bcecceda100000000000000000000000000000045f9c5af31678bc1dacddf348936a6a6e4d42a53
```

**O que é cada parte:**
- Primeiros 64 chars: `uint256` = 1,000,000 tokens
- Últimos 64 chars: `address` = signer (`0x45f9c5af31678bc1dacddf348936a6a6e4d42a53`)

**Configurações Recomendadas:**
- Compiler: `0.8.24`
- License: `MIT`
- Optimization: `Yes`, Runs: `200`
- Constructor Arguments: (valor acima)

---

## 🔗 Links Úteis

- **BSCScan:** https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017#code
- **Token:** https://bscscan.com/token/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017

---

## ✅ Arquivos de Referência

- **Constructor Arguments Completo:** `CONSTRUCTOR_ARGS_COMPLETO.txt`
- **Solução Descoberta:** `SOLUCAO_DESCOBERTA.md`
- **Código do Contrato:** `InterboxCoin_Flattened_Final.sol`

---

## ⚠️ Nota Importante

O código fonte atual mostra apenas **1 parâmetro** no constructor (`address _signer`), mas o contrato deployado recebeu **DOIS parâmetros**:
1. `uint256` (1 milhão de tokens)
2. `address _signer`

Isso pode significar que o código fonte foi modificado após o deploy, ou foi usada uma versão diferente do contrato. Use o constructor argument completo acima para garantir a correspondência do bytecode!

---

**Tudo pronto! Agora é só preencher o formulário no BSCScan e verificar!** 🚀

