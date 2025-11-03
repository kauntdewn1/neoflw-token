# ✅ Como Verificar Contrato no BSCScan

## 🌐 Rede: Binance Smart Chain (BSC) Mainnet

**⚠️ IMPORTANTE:** Este token está deployado na **BSC Mainnet**.

- **Rede:** Binance Smart Chain (BSC) Mainnet
- **Chain ID:** 56
- **Explorer:** https://bscscan.com
- **Token Address:** `0xBc972E10Df612C7d65054BC67aBCA96B3C22a017`

---

## 🎯 Métodos de Verificação

### ✅ Método 1: Via Interface Web do BSCScan (Recomendado)

#### **Passo a Passo:**

1. **Acesse a página do contrato:**
   ```
   https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017#code
   ```

2. **Encontre a aba "Contract":**
   - Na página do contrato, clique na aba **"Contract"**
   - Você verá um botão **"Verify and Publish"** ou **"Verify Contract"**

3. **Preencha o formulário:**
   - **Compiler Version:** Selecione a versão usada no deploy (ex: `0.8.30+commit.87f61d96`)
   - **License:** Selecione a licença do contrato (ex: `MIT`)
   - **Contract Name:** Nome do contrato (ex: `BoxToken` ou similar)
   - **Optimization:** Marque se o contrato foi otimizado (ex: `Yes` ou `No`)
   - **Runs:** Número de runs de otimização (ex: `200`)

4. **Escolha o método de verificação:**
   - **Via Standard JSON Input** (recomendado para contratos com imports)
   - **Via Solidity (Single file)**
   - **Via Solidity (Multi-file)**

5. **Faça upload do código:**
   - Se escolheu **Standard JSON Input:** Faça upload do arquivo JSON completo
   - Se escolheu **Single file:** Cole todo o código do contrato
   - Se escolheu **Multi-file:** Use o formato de múltiplos arquivos

6. **Preencha Constructor Arguments:**
   - Se o contrato tem constructor, você precisa fornecer os argumentos
   - Use um script para calcular os argumentos codificados (ABI-encoded)

7. **Clique em "Verify and Publish"**

8. **Aguarde a verificação:**
   - Pode levar alguns minutos
   - Você receberá uma confirmação quando estiver pronto

---

### ✅ Método 2: Via API do BSCScan

#### **Pré-requisitos:**

1. **Obtenha uma API Key:**
   - Acesse: https://bscscan.com/myapikey
   - Crie uma conta (gratuita)
   - Gere uma API Key

2. **Use o script de verificação:**
   ```bash
   python scripts/verify_contract.py
   ```

---

### ✅ Método 3: Via Sourcify (Se Suportado)

O Sourcify suporta verificação para BSC:

1. **Acesse:** https://sourcify.dev/
2. **Selecione a rede:** Binance Smart Chain (BSC)
3. **Informe o endereço:** `0xBc972E10Df612C7d65054BC67aBCA96B3C22a017`
4. **Faça upload dos arquivos:**
   - Código fonte do contrato
   - Metadados JSON (se disponível)

---

## 📋 Informações Necessárias

Para verificar o contrato, você precisa ter:

- ✅ **Código fonte completo** do contrato
- ✅ **Versão do compilador** usada
- ✅ **Licença** do contrato
- ✅ **Constructor arguments** (se o contrato tiver constructor)
- ✅ **Configurações de otimização** (se usadas)

---

## 🔧 Troubleshooting

### **Problema 1: "Bytecode mismatch"**

**Causa:** Código compilado não corresponde ao bytecode na blockchain.

**Soluções:**
- ✅ Verifique a versão do compilador (deve ser exatamente a mesma)
- ✅ Verifique as configurações de otimização
- ✅ Verifique os constructor arguments
- ✅ Certifique-se de que está usando o código fonte correto

### **Problema 2: "Contract name does not match"**

**Causa:** Nome do contrato no código não corresponde ao esperado.

**Soluções:**
- ✅ Use o nome exato da classe/contrato
- ✅ Para contratos herdados, use o formato: `ContractFile.sol:ContractName`

### **Problema 3: "Constructor arguments not found"**

**Causa:** Constructor arguments não foram fornecidos ou estão incorretos.

**Soluções:**
- ✅ Calcule os constructor arguments usando um script
- ✅ Use o formato ABI-encoded correto
- ✅ Verifique a ordem dos parâmetros

---

## 📝 Script para Calcular Constructor Arguments

Se precisar calcular os constructor arguments, use:

```bash
python scripts/calculate_constructor_args.py
```

---

## 🔗 Links Úteis

- **Contrato no BSCScan:** https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017
- **BSCScan API Docs:** https://docs.bscscan.com/api-endpoints/contracts
- **Sourcify:** https://sourcify.dev/
- **Token no BSCScan:** https://bscscan.com/token/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017

---

## ✅ Checklist de Verificação

- [ ] Código fonte completo disponível
- [ ] Versão do compilador identificada
- [ ] Constructor arguments calculados (se necessário)
- [ ] Configurações de otimização conhecidas
- [ ] API Key do BSCScan obtida (se usar API)
- [ ] Contrato verificado no BSCScan
- [ ] Verificação confirmada na página do contrato

---

**Boa sorte com a verificação!** 🚀

