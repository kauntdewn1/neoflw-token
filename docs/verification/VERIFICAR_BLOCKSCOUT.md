# ✅ Como Verificar Contrato no Blockscout (Full Match)

## 🎯 Objetivo

Verificar o contrato NeoFlowToken diretamente no Blockscout para garantir **"Full Match"** ao invés de "Partial Match".

---

## 📋 Informações do Contrato

```
Endereço: 0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
Rede: Ethereum Sepolia (Testnet)
Chain ID: 11155111
Contrato: NeoFlowToken
Compilador: 0.8.30+commit.73712a01
Optimization: Sim (200 runs)
```

---

## 🌐 URL do Blockscout Sepolia

```
https://eth-sepolia.blockscout.com/address/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
```

---

## 🚀 Método 1: Verificação Via Interface Web (Recomendado)

### **PASSO 1: Acesse a Página do Contrato**

1. **Acesse:**
   ```
   https://eth-sepolia.blockscout.com/address/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
   ```

2. **Vá para a aba "Contract"** (se não estiver já)

3. **Procure por:**
   - Botão "Verify & publish" ou "Verify contract"
   - Ou link "Verify contract source code"

---

### **PASSO 2: Escolha o Método de Verificação**

O Blockscout oferece vários métodos:

#### **Opção A: Standard JSON Input (Recomendado)**

**Melhor para:** Contratos com imports (OpenZeppelin)

**Vantagens:**
- ✅ Funciona com múltiplos arquivos
- ✅ Mantém imports corretos
- ✅ Geralmente resulta em "Full Match"

#### **Opção B: Flattened Source Code**

**Melhor para:** Contratos simples sem muitos imports

**Vantagens:**
- ✅ Mais simples
- ⚠️ Pode ter problemas com imports complexos

#### **Opção C: Via API (Avançado)**

**Melhor para:** Automação

---

### **PASSO 3: Preencha as Informações**

#### **Se escolher Standard JSON Input:**

1. **Compiler Version:**
   ```
   0.8.30+commit.73712a01
   ```
   ou apenas:
   ```
   v0.8.30+commit.73712a01
   ```

2. **Optimization:**
   - ✅ Habilitado
   - Runs: `200`

3. **Contract Name:**
   ```
   NeoFlowToken
   ```

4. **Contract File Path:**
   ```
   contracts/NeoFlowToken.sol
   ```

5. **Standard JSON Input:**
   - ✅ **Use:** `sourcify_standard_json.json` (já tem `language` e formato correto)
   - ❌ **NÃO use:** `etherscan_verification_fixed.json` (formato Ape, sem `language`)
   
   **Arquivo correto:**
   ```bash
   # O arquivo sourcify_standard_json.json já está no formato correto
   # Ele tem "language": "Solidity" e formato Standard JSON Input
   ```
   
   **Se precisar gerar novamente:**
   ```bash
   cd /Users/nettomello/CODIGOS/neoflw-token
   # Use o script que converte para formato correto
   python scripts/create_complete_json.py
   # Ou use sourcify_standard_json.json que já existe
   ```

#### **Se escolher Flattened Source Code:**

1. **Compiler Version:** `0.8.30+commit.73712a01`

2. **Optimization:** Sim, 200 runs

3. **Flattened Source:**
   - Use o arquivo `NeoFlowToken_flattened.sol`
   - Ou gere com: `ape compile --format flattened`

---

### **PASSO 4: Constructor Arguments**

**Constructor Arguments (ABI-encoded):**
```
0x0000000000000000000000000000000000000000000000000d3c21bcecceda1000000
```

**Ou decodificado:**
- Arg [0]: `1000000000000000000000000000` (initialSupply)

---

### **PASSO 5: Submeter e Aguardar**

1. **Clique em "Verify" ou "Submit"**

2. **Aguarde processamento:**
   - Pode levar alguns minutos
   - Blockscout compila e compara bytecode

3. **Resultado:**
   - ✅ **"Contract Source Code Verified (Full Match)"** = Sucesso!
   - ⚠️ Se aparecer "Partial Match", veja troubleshooting abaixo

---

## 🛠️ Método 2: Via Ape Framework (Automatizado)

### **Verificar se Ape tem plugin Blockscout:**

```bash
# Verificar plugins instalados
ape plugins list

# Se não tiver, instale (se disponível)
ape plugins install blockscout
```

### **Verificar Diretamente:**

```bash
# Verificar no Blockscout Sepolia
ape blockscout verify NeoFlowToken --network ethereum:sepolia
```

**⚠️ Nota:** Nem todas as versões do Ape têm suporte nativo ao Blockscout. Pode precisar fazer manualmente.

---

## 🔧 Método 3: Via API (Avançado)

### **Configuração:**

```bash
# Obter API key do Blockscout (se necessário)
# Alguns instances públicos não requerem API key
```

### **Usar cURL:**

```bash
curl -X POST https://eth-sepolia.blockscout.com/api \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "eth_verify",
    "params": [
      "0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87",
      "...standard_json_input..."
    ],
    "id": 1
  }'
```

**⚠️ Nota:** A API pode variar entre instances do Blockscout.

---

## 📄 Arquivos Necessários

### **1. Standard JSON Input (OBRIGATÓRIO - Use Este!):**

⚠️ **CRÍTICO:** Use o arquivo correto ou você terá erro "missing field `language`"!

**✅ ARQUIVO CORRETO:**
```
sourcify_standard_json.json
```

**Este arquivo:**
- ✅ Tem `"language": "Solidity"` (obrigatório para Blockscout)
- ✅ Formato Standard JSON Input válido
- ✅ Já foi usado com sucesso no Sourcify
- ✅ Pronto para usar no Blockscout

**❌ NÃO USE:**
```
etherscan_verification_fixed.json
```

**Este arquivo:**
- ❌ Formato do Ape Framework (sem `language`)
- ❌ Tem `"compilers"` ao invés de formato padrão
- ❌ **NÃO funciona no Blockscout!**

**Como usar:**
```bash
# O arquivo já existe e está correto
cat sourcify_standard_json.json

# Copie o conteúdo completo e cole no Blockscout
```

**Se precisar gerar/corrigir:**
```bash
cd /Users/nettomello/CODIGOS/neoflw-token

# Opção 1: Use o arquivo que já existe (sourcify_standard_json.json)

# Opção 2: Corrigir formato Ape para Blockscout
python scripts/fix_json_for_blockscout.py

# Opção 3: Gerar novo do zero
python scripts/create_complete_json.py
```

### **2. Flattened Source (Alternativa):**

Arquivo: `NeoFlowToken_flattened.sol`

**Gerar (se necessário):**
```bash
ape compile --format flattened
```

---

## 🔍 Informações Técnicas Completas

### **Compilador:**

```
Compiler: v0.8.30+commit.73712a01
EVM Version: Default
Optimization Enabled: true
Optimization Runs: 200
```

### **Contrato:**

```
Name: NeoFlowToken
Path: contracts/NeoFlowToken.sol
License: MIT
```

### **Constructor:**
```solidity
constructor(uint256 initialSupply) ERC20("NeoFlowOFF", "NEOFLW")
```

**Argumentos:**
- `initialSupply`: `1000000000000000000000000000` (1000000000 tokens com 18 decimais)

---

## ⚠️ Troubleshooting

### **Problema 1: Ainda Aparece "Partial Match"**

**Possíveis causas:**
1. Diferenças em configurações de compilação
2. Versão do compilador ligeiramente diferente
3. Diferenças em como bibliotecas são linkadas

**Soluções:**
- ✅ Verifique se está usando exatamente a mesma versão do compilador
- ✅ Use Standard JSON Input ao invés de Flattened
- ✅ Certifique-se que optimization settings são idênticos
- ✅ Verifique se todos os imports estão incluídos

### **Problema 2: Erro "missing field `language`"**

**Erro comum:**
```
content is not a valid standard json: missing field `language` at line X column 1
```

**Causa:**
- ❌ Usou `etherscan_verification_fixed.json` (formato Ape, sem `language`)
- ❌ JSON não está no formato Standard JSON Input correto

**Solução:**
- ✅ Use `sourcify_standard_json.json` (tem `language` e formato correto)
- ✅ Ou execute: `python scripts/fix_json_for_blockscout.py` para corrigir

**📖 Guia completo do erro:** Veja [`ERRO_JSON_BLOCKSCOUT.md`](./ERRO_JSON_BLOCKSCOUT.md)

### **Problema 3: Erro "Compilation Failed"**

**Soluções:**
- ✅ Verifique versão do compilador
- ✅ Certifique-se que todos os imports estão no Standard JSON
- ✅ Verifique se constructor arguments estão corretos
- ✅ Tente Flattened Source se Standard JSON falhar

### **Problema 4: Botão "Verify" Não Aparece**

**Soluções:**
- ✅ Certifique-se que está na aba "Contract"
- ✅ Conecte sua wallet (alguns instances requerem)
- ✅ Tente fazer login no Blockscout
- ✅ Verifique se o contrato já não está verificado

### **Problema 5: "Cannot update partially verified smart contract with another partially verified contract"**

**Erro:**
```
Cannot update partially verified smart contract with another partially verified contract
```

**Causa:**
- ⚠️ Blockscout já tem verificação "Partial Match"
- ⚠️ Tentando verificar novamente, mas também resultaria em "Partial Match"
- ⚠️ Blockscout bloqueia para evitar loops

**Soluções:**
1. ✅ **Garantir "Full Match":** Certifique-se que TODAS as configurações estão exatas
   - Compilador: `0.8.30+commit.73712a01` (exato)
   - Optimization: enabled, 200 runs (exato)
   - EVM Version: default/prague (conforme deploy)
   - Constructor args: corretos
   - Standard JSON Input: completo e correto
2. ✅ **Limpar verificação existente** (se o Blockscout permitir)
3. ✅ **Aguardar e tentar mais tarde**
4. ✅ **Deixar como está** (se "Partial Match" é aceitável)
5. ✅ **Verificar no Etherscan** quando voltar ao normal

**📖 Guia completo do erro:** Veja [`ERRO_PARTIALLY_VERIFIED.md`](./ERRO_PARTIALLY_VERIFIED.md)

### **Problema 6: "Contract Already Verified"**

**Solução:**
- ✅ Isso é bom! O contrato já está verificado
- ✅ Se mostra "Partial Match" e você quer "Full Match", veja Problema 5 acima

---

## 📊 Comparação: Sourcify vs Blockscout

| Aspecto | Sourcify | Blockscout |
|---------|----------|------------|
| **Método** | Metadados + Código | Bytecode Comparison |
| **Rigor** | Flexível | Mais rigoroso |
| **Resultado** | ✅ Fully Verified | ⚠️ Partial Match → ✅ Full Match |
| **Reconhecimento** | ✅ Aceito por Etherscan | ✅ Próprio explorer |

---

## ✅ Checklist de Verificação

Antes de verificar:

- [ ] ✅ Tenho acesso ao Standard JSON Input correto (`sourcify_standard_json.json`)
- [ ] ✅ Versão do compilador está correta e EXATA (0.8.30+commit.73712a01)
- [ ] ✅ Optimization settings estão corretos e EXATOS (200 runs)
- [ ] ✅ EVM Version está correto (default/prague, conforme deploy)
- [ ] ✅ Constructor arguments estão corretos e ABI-encoded
- [ ] ✅ Standard JSON Input tem campo `"language": "Solidity"`
- [ ] ✅ Contrato compila sem erros localmente
- [ ] ✅ Wallet conectada no Blockscout (se necessário)
- [ ] ⚠️ Se já tem "Partial Match", preparei para conseguir "Full Match"

Durante verificação:

- [ ] Escolhi método correto (Standard JSON recomendado)
- [ ] Preenchi todas as informações
- [ ] Constructor arguments estão corretos
- [ ] Submeti e aguardei processamento

Após verificação:

- [ ] Verifiquei status (Full Match ou Partial Match)
- [ ] Código fonte está visível no Blockscout
- [ ] Contrato aparece como "Verified"

---

## 🔗 Links Úteis

- **Blockscout Sepolia:** https://eth-sepolia.blockscout.com/
- **Contrato:** https://eth-sepolia.blockscout.com/address/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
- **Sourcify (já verificado):** https://repo.sourcify.dev/11155111/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
- **Documentação Blockscout:** https://docs.blockscout.com/

---

## 💡 Dica Final

**Recomendação:**
1. ✅ Use **Standard JSON Input** correto (`sourcify_standard_json.json`)
2. ✅ Certifique-se que TODAS as configurações estão EXATAS (compilador, optimizer, EVM)
3. ✅ Se der erro "Cannot update partially verified...", veja [`ERRO_PARTIALLY_VERIFIED.md`](./ERRO_PARTIALLY_VERIFIED.md)
4. ✅ "Full Match" garante máxima confiança, mas "Partial Match" também funciona

**⚠️ Se Receber Erro "Cannot update partially verified...":**
- O contrato já está verificado como "Partial Match"
- Para conseguir "Full Match", todas as configurações precisam estar EXATAS
- Veja o guia de erro para detalhes completos

**Por que verificar em ambos?**
- ✅ Sourcify: Reconhecido automaticamente pelo Etherscan (já feito ✅)
- ✅ Blockscout: Garante "Full Match" no próprio explorer (opcional)
- ✅ Máxima transparência e confiança

---

**Boa sorte na verificação!** Com isso você terá "Full Match" garantido! 🚀

