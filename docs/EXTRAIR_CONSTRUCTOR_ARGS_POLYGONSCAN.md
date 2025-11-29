# 🔍 Como Extrair Argumentos do Construtor no PolygonScan

**Contrato:** `NeoFlowToken`  
**Endereço:** `0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2`  
**Rede:** Polygon Mainnet

---

## 📋 Construtor do NeoFlowToken

```solidity
constructor(uint256 initialSupply) ERC20("NEOFlowOFF", "NEOFLW") {
    _mint(msg.sender, initialSupply);
}
```

**Argumentos:**

- `initialSupply` (uint256): Quantidade inicial de tokens em wei

**Valores hardcoded no construtor:**

- Nome: `"NEOFlowOFF"`
- Símbolo: `"NEOFLW"`

---

## 🎯 Passo a Passo: Extrair Argumentos no PolygonScan

### **1. Acessar o Contrato**

```
https://polygonscan.com/address/0x59aa4eae743d608fbdd4205eba59b38dca755dd2
```

### **2. Encontrar a Transação de Deploy**

1. Clique na aba **"Transactions"**
2. A primeira transação (mais antiga) é geralmente o deploy
3. Clique na transação para abrir os detalhes

### **3. Ver Argumentos do Construtor**

#### **Opção A: Se o contrato estiver verificado**

1. Na página da transação, procure por **"Constructor Arguments"** ou **"Decode Input Data"**
2. Os argumentos aparecerão decodificados automaticamente
3. Você verá algo como:
   ```
   initialSupply: 1000000000000000000000000000
   ```

#### **Opção B: Se o contrato NÃO estiver verificado**

1. Na página da transação, clique em **"Input Data"**
2. Você verá um hex longo começando com `0x...`
3. Copie esse hex completo

### **4. Decodificar Manualmente (se necessário)**

Se o PolygonScan não decodificar automaticamente:

1. **Use ferramenta online:**
   - https://lab.miguelmota.com/abi-decoder/
   - https://www.4byte.directory/
   - https://ethtx.info/

2. **Cole o ABI do construtor:**
   ```json
   [{
     "type": "constructor",
     "inputs": [{
       "type": "uint256",
       "name": "initialSupply"
     }]
   }]
   ```

3. **Cole o hex do Input Data**
4. Clique em "Decode"

---

## 📊 Valores Esperados para NeoFlowToken

### **Deploy Padrão (1 bilhão de tokens)**

**Valor decimal:**
```
1000000000000000000000000000
```

**Valor em formato legível:**
```
1,000,000,000 tokens × 10^18 = 1 bilhão de tokens
```

**Formato ABI-encoded (hex, 64 caracteres):**
```
0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000
```

---

## ✅ Usar na Verificação do PolygonScan

### **Método 1: Formato ABI-encoded (Recomendado)**

1. Acesse: https://polygonscan.com/address/0x59aa4eae743d608fbdd4205eba59b38dca755dd2
2. Clique em **"Contract"** → **"Verify and Publish"**
3. Escolha o método de verificação
4. No campo **"Constructor Arguments (ABI-encoded)"**, cole:
   ```
   0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000
   ```

### **Método 2: Formato Decodificado**

Se o PolygonScan pedir os argumentos decodificados:

1. No campo **"Constructor Arguments"**, digite:
   ```
   1000000000000000000000000000
   ```

2. O PolygonScan converterá automaticamente para ABI-encoded

---

## 🔧 Script para Calcular Argumentos

Você já tem um script pronto:

```bash
python scripts/utils/calculate_constructor_args.py
```

**Saída esperada:**
```
🔢 Calculando argumentos do construtor...

Valor decimal: 1,000,000,000,000,000,000,000,000,000
Valor em wei: 1000000000000000000000000000

✅ Formato ABI-encoded (hexadecimal):
   0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000
```

---

## 📝 Exemplo Completo de Verificação

### **Dados do Contrato:**

| Campo | Valor |
|-------|-------|
| **Endereço** | `0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2` |
| **Network** | Polygon Mainnet (Chain ID: 137) |
| **Compiler** | `v0.8.18+commit.87f61d96` |
| **License** | `MIT` |
| **Optimization** | `Yes` (200 runs) |
| **Constructor Args** | `0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000` |

### **Passos na PolygonScan:**

1. ✅ Acesse o endereço do contrato
2. ✅ Clique em **"Contract"** → **"Verify and Publish"**
3. ✅ Escolha: **"Via Standard JSON Input"** (recomendado)
4. ✅ Preencha:
   - **Compiler Version:** `v0.8.18+commit.87f61d96`
   - **License:** `MIT`
   - **Optimization:** `Yes` (200 runs)
5. ✅ Cole o **Standard JSON Input** (gerado pelo Ape)
6. ✅ Cole os **Constructor Arguments:**
   ```
   0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000
   ```
7. ✅ Clique em **"Verify and Publish"**

---

## 🔍 Verificar Argumentos Extraídos

### **Teste 1: Verificar se o valor está correto**

```python
# Converter hex para decimal
hex_value = "0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000"
decimal_value = int(hex_value, 16)
print(f"Valor: {decimal_value:,} wei")
print(f"Tokens: {decimal_value / 10**18:,.0f} NEOFLW")
```

**Saída esperada:**
```
Valor: 1,000,000,000,000,000,000,000,000,000 wei
Tokens: 1,000,000,000 NEOFLW
```

### **Teste 2: Comparar com o deploy**

Verifique se o valor extraído corresponde ao valor usado no deploy:

```bash
# Verificar no script de deploy
grep "initial_supply" scripts/deploy/deploy_token.py
```

**Deve mostrar:**
```python
initial_supply = 1_000_000_000 * 10**18  # 1 bilhão com 18 decimais
```

---

## 💡 Dicas Importantes

1. **Ordem dos Argumentos:**
   - O construtor do `NeoFlowToken` tem apenas **1 argumento**: `initialSupply`
   - Nome e símbolo são hardcoded no construtor

2. **Formato do Valor:**
   - Sempre em **wei** (menor unidade)
   - 1 token = 10^18 wei
   - 1 bilhão de tokens = 1,000,000,000 × 10^18 wei

3. **Padding:**
   - O valor ABI-encoded deve ter exatamente **64 caracteres hex** (32 bytes)
   - Se tiver menos, adicione zeros à esquerda

4. **Verificação:**
   - Se a verificação falhar, verifique se o valor está correto
   - Compare com o valor usado no deploy original

---

## 🚨 Problemas Comuns

### **Erro: "Constructor arguments mismatch"**

**Solução:**
- Verifique se o valor está em wei (não em tokens)
- Certifique-se de que o formato está correto (64 caracteres hex)

### **Erro: "Invalid constructor arguments"**

**Solução:**
- Use o script `calculate_constructor_args.py` para gerar o valor correto
- Verifique se não há espaços ou caracteres extras

### **Não consigo encontrar os argumentos**

**Solução:**
- Use o valor padrão do deploy: `1000000000000000000000000000`
- Ou calcule usando o script fornecido

---

## 📚 Recursos Úteis

- **PolygonScan:** https://polygonscan.com
- **ABI Decoder:** https://lab.miguelmota.com/abi-decoder/
- **Ethereum Unit Converter:** https://eth-converter.com/
- **Script de Cálculo:** `scripts/utils/calculate_constructor_args.py`

---

**Última atualização:** 2025-01-XX

