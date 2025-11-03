# 📋 Informações do Contrato InterboxCoin - BOX Token

## ✅ Análise do Arquivo

Arquivo: `InterboxCoin_Flattened_Final.sol`

---

## 📝 Informações Importantes para Verificação

### **1. Versão do Compilador:**
```
^0.8.24
```

**No BSCScan, selecione:**
- `0.8.24+commit.xxxxx` (ou versão compatível mais próxima)
- Exemplo: `0.8.24+commit.e11b9ed9` ou similar

### **2. Nome do Contrato:**
```
InterboxCoin
```

### **3. Constructor:**
```solidity
constructor(address _signer) ERC20("Interbox Token", "BOX") Ownable(0xbE90d7A34C8f38Ce5459609076d28C2e1E43925A)
```

**O contrato TEM constructor com 1 argumento:**
- Parâmetro: `address _signer`

**Para descobrir o valor do `_signer`:**
- Verifique a transação de deploy original no BSCScan
- Ou verifique se você tem essa informação em outro lugar
- O valor será um endereço (0x...)

**Como encontrar a transação de deploy:**
1. Acesse: https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017
2. Veja a seção "Contract Creator"
3. Clique no link da transação de criação
4. Veja os "Input Data" para encontrar o argumento do constructor

### **4. License:**
```
MIT
```
(O arquivo tem `// SPDX-License-Identifier: MIT`)

### **5. Otimização:**
Tente primeiro com:
- **Optimization:** `No`
- Se não funcionar, tente `Yes` com `Runs: 200`

---

## 🔍 Como Encontrar o Constructor Argument

### **Método 1: BSCScan**

1. **Acesse:**
   ```
   https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017
   ```

2. **Veja a seção "Contract Creator":**
   - Deve mostrar: `0x45f9C5Af...6E4D42A53`
   - E "Created: 111 days ago"

3. **Clique na transação de criação**

4. **Na página da transação:**
   - Veja "Input Data"
   - O último parâmetro (depois do código do contrato) é o argumento do constructor

### **Método 2: Verificar Função `signer()`**

Se o contrato já está deployado, você pode verificar o valor do `signer`:

1. Acesse: https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017#readContract
2. Procure pela função `signer()` (se visível)
3. Esse será o valor usado no constructor

### **Método 3: Deixar Vazio (Teste)**

Se não conseguir encontrar:
- Tente deixar o campo "Constructor Arguments" vazio
- Se não funcionar, você precisará encontrar o valor correto

---

## 📋 Resumo para Preencher no BSCScan

### **Formulário de Verificação:**

- **Compiler Type:** `Solidity (Single file)`
- **Compiler Version:** `0.8.24+commit.xxxxx` (ou versão compatível)
- **License:** `MIT License (MIT)`
- **Contract Code:** (Cole todo o conteúdo de `InterboxCoin_Flattened_Final.sol`)
- **Constructor Arguments:** (Endereço do signer em hexadecimal, sem 0x)
- **Optimization:** Tente `No` primeiro

---

## ⚠️ Importante sobre Constructor Arguments

O constructor precisa do endereço do `signer` em formato **ABI-encoded hexadecimal**.

**Formato esperado:**
- Sem `0x` no início
- 64 caracteres hexadecimais (32 bytes)
- Exemplo: `000000000000000000000000[64 chars do endereço]`

**Ferramenta para converter:**
- Você pode usar um conversor ABI online
- Ou calcular manualmente (pode ser complicado)

**Alternativa:**
- Se tiver dificuldade, tente o Sourcify que pode calcular automaticamente
- Ou deixe vazio e veja se funciona (pode não funcionar se for obrigatório)

---

## ✅ Checklist Final

- [x] Arquivo encontrado: `InterboxCoin_Flattened_Final.sol`
- [x] Versão do compilador identificada: `^0.8.24`
- [x] Nome do contrato identificado: `InterboxCoin`
- [x] Constructor identificado: Tem 1 argumento (`address _signer`)
- [ ] Valor do `_signer` encontrado (precisa descobrir)
- [ ] Código pronto para copiar e colar

---

## 🔗 Links Úteis

- **BSCScan Contrato:** https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017#code
- **BSCScan Token:** https://bscscan.com/token/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017
- **Verificar Contrato:** https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017#code

---

**Tudo pronto! Agora você tem todas as informações para verificar o contrato!** 🚀

