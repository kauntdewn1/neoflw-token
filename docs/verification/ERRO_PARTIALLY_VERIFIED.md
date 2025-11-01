# ⚠️ Erro: "Cannot update partially verified smart contract with another partially verified contract"

## 🔍 O Problema

Ao tentar verificar no Blockscout, você recebeu este erro:

```
Cannot update partially verified smart contract with another partially verified contract
```

## 🎯 Causa

O Blockscout **já tem uma verificação "Partial Match"** do contrato e não permite substituir por outra verificação que também seria "Partial Match".

**Por que isso acontece:**
- O contrato já está verificado como "Partial Match" (pode ser do Sourcify ou tentativa anterior)
- Você está tentando verificar novamente, mas o resultado também seria "Partial Match"
- O Blockscout bloqueia para evitar loops de re-verificação

---

## ✅ Soluções

### **Solução 1: Garantir "Full Match" (Recomendado)**

Para conseguir "Full Match" e substituir o "Partial Match", você precisa:

#### **1.1. Verificar Configurações Exatas**

Certifique-se que **TODAS** as configurações estão idênticas ao deploy:

**Compilador:**
```
v0.8.30+commit.73712a01
```

**Optimization:**
```
Enabled: true
Runs: 200
```

**EVM Version:**
```
Default (ou "prague" se foi usado)
```

**Contract:**
```
Name: NeoFlowToken
Path: contracts/NeoFlowToken.sol
```

**Constructor Arguments (ABI-encoded):**
```
0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000
```

#### **1.2. Preencher TODOS os Campos no Formulário do Blockscout**

⚠️ **CRÍTICO:** Mesmo usando "Standard JSON Input", o Blockscout **AINDA EXIGE** alguns campos no formulário!

**Campos OBRIGATÓRIOS no formulário (mesmo com Standard JSON Input):**

1. **✅ Contract License:** `MIT License (MIT)` (já está preenchido ✅)

2. **✅ Verification Method:** `Solidity (Standard JSON input)` (já está selecionado ✅)

3. **✅ Compiler:** `v0.8.30+commit.73712a01` (já está selecionado ✅)

4. **✅ Standard JSON Input File:** `sourcify_standard_json.json` (já foi carregado ✅)

5. **❌ Constructor Arguments:** Você precisa preencher mesmo com Standard JSON Input!
   ```
   0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000
   ```
   **Ou use o valor decimal:**
   ```
   1000000000000000000000000000
   ```

6. **❌ Contract Name:** Você precisa especificar no formulário:
   ```
   NeoFlowToken
   ```

7. **❌ Contract File Path:** Especifique:
   ```
   contracts/NeoFlowToken.sol
   ```

8. **❌ Optimization:** Preencha no formulário (mesmo que esteja no JSON):
   - ✅ Optimization Enabled: `true` ou `Yes`
   - ✅ Optimization Runs: `200`

9. **❌ EVM Version:** Deixe como `default` ou conforme deploy

**⚠️ IMPORTANTE:** O Blockscout usa uma **combinação** dos campos do formulário + Standard JSON Input. Se algum campo estiver faltando ou diferente, pode resultar em "Partial Match"!

**📌 O QUE FAZER AGORA:**

1. **Role a página para baixo** - há mais campos abaixo que não aparecem na imagem!

2. **Procure por campos adicionais:**
   - **Contract Name** (obrigatório)
   - **Constructor Arguments** (obrigatório se o contrato tem construtor)
   - **Optimization Enabled** (checkbox ou dropdown)
   - **Optimization Runs** (número)
   - **EVM Version** (dropdown)
   - **Contract File Path** (caminho do arquivo)

3. **Preencha TODOS os campos**, mesmo que estejam no JSON!

4. **Depois, tente verificar novamente.**

#### **1.3. Verificar Constructor Arguments**

**Para NeoFlowToken:**
- **Constructor Arguments (ABI-encoded):**

  ```
  0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000
  ```
  
- **Ou valor decimal:** `1000000000000000000000000000`

Certifique-se que está usando o valor ABI-encoded correto no Blockscout.

#### **1.4. Verificar EVM Version**

**EVM Version:** Deixe como **"default"** ou selecione conforme foi usado no deploy (geralmente "default" para Solidity 0.8.x).

#### **1.5. Tentar Novamente**

Com **TODAS** as configurações exatas (compilador, optimizer, EVM, constructor args), você deve conseguir "Full Match" que substituirá o "Partial Match".

---

### **Solução 2: Limpar Verificação Existente (Se Possível)**

Alguns instances do Blockscout permitem limpar verificação:

1. **Procure por botão "Clear Verification" ou "Remove Verification"**
   - Pode estar na aba "Contract"
   - Ou no menu de opções do contrato

2. **Se encontrar, limpe e tente verificar novamente**

⚠️ **Nota:** Nem todos os instances do Blockscout permitem isso.

---

### **Solução 3: Usar Instance Diferente do Blockscout**

Se o instance atual não permite re-verificar:

1. **Tente outro instance do Blockscout Sepolia:**

   - <https://eth-sepolia.blockscout.com/>
   - Outros instances podem ter regras diferentes

2. **Ou aguarde e tente mais tarde:**
   - Às vezes há delays no sistema
   - Tente em horários diferentes

---

### **Solução 4: Deixar Como Está (Se Aceitável)**

"Partial Match" já é suficiente:

- ✅ Contrato está verificado
- ✅ Código está público
- ✅ Funcionalidade não é afetada
- ✅ Explorers reconhecem como verificado

**Você pode deixar como está** se não precisar obrigatoriamente de "Full Match".

---

### **Solução 5: Verificar Diretamente no Etherscan**

Quando o Etherscan voltar ao normal:

1. **Verifique diretamente no Etherscan:**

   ```bash
   ape etherscan verify NeoFlowToken --network ethereum:sepolia
   ```

2. **Ou use a interface web do Etherscan:**
   - Acesse: 
   https://sepolia.etherscan.io/address/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87#code
   - Clique em "Verify and Publish"
   - Use Standard JSON Input

**Vantagem:** Etherscan pode aceitar mesmo com "Partial Match" existente no Blockscout.

---

## 🔍 Verificar Status Atual

### **Como Verificar Se Já Está Verificado:**

1. **Acesse:**
   ```
   https://eth-sepolia.blockscout.com/address/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
   ```

2. **Vá para aba "Contract"**

3. **Veja o status:**
   - ✅ "Contract Source Code Verified (Full Match)" = Já verificado, não precisa fazer nada
   - ⚠️ "Contract Source Code Verified (Partial Match)" = Verificado parcialmente, pode tentar melhorar

---

## 📋 Checklist Para Conseguir "Full Match"

Antes de tentar verificar novamente:

**Configurações do Compilador:**
- [ ] ✅ Versão do compilador EXATA: `0.8.30+commit.73712a01` (ou `0.8.30` se não houver opção com commit)
- [ ] ✅ Optimization: enabled: **true**, runs: **200** (EXATO)
- [ ] ✅ EVM version: **default** (ou conforme deploy)

**Constructor Arguments:**
- [ ] ✅ Constructor args ABI-encoded: `0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000`
- [ ] ✅ Ou valor decimal: `1000000000000000000000000000`

**Standard JSON Input:**
- [ ] ✅ Usei `sourcify_standard_json.json` (formato correto)
- [ ] ✅ JSON tem campo `"language": "Solidity"`
- [ ] ✅ Todos os arquivos fonte estão no JSON
- [ ] ✅ outputSelection está completo
- [ ] ✅ Settings têm optimizer correto (enabled: true, runs: 200)

**Verificações Finais:**
- [ ] ✅ Contrato compila localmente sem erros
- [ ] ✅ Verifiquei no Blockscout que NÃO estou tentando substituir "Partial Match" por outro "Partial Match"
- [ ] ✅ Todas as configurações estão IDÊNTICAS ao deploy original

---

## 💡 Estratégia Recomendada

### **⚠️ ESTÁ EM LOOP? Veja Estratégia Específica:**

Se você está recebendo o erro repetidamente mesmo com todas as configurações corretas, veja o guia específico:

**📖 Guia Completo:** [`SAIR_LOOP_PARTIAL_MATCH.md`](./SAIR_LOOP_PARTIAL_MATCH.md)

### **Se "Partial Match" é Aceitável (Recomendado para Testnet):**

1. ✅ **Deixe como está** - já é suficiente para Sepolia
2. ✅ Já está verificado e funcional
3. ✅ Foque em atualizar a imagem do token
4. ✅ Para mainnet, aí sim se preocupe com "Full Match"

### **Se Você Precisa "Full Match":**

**Se o erro persiste em loop:**

1. ✅ **Tente limpar verificação existente** (se Blockscout permitir)
2. ✅ **Contate suporte do Blockscout** (GitHub Issues)
3. ✅ **Aguarde Etherscan voltar** e verifique lá (não tem essa limitação)
4. ✅ **Aceite "Partial Match"** se for testnet - já é suficiente

**Se ainda não tentou com configurações exatas:**

1. ✅ **Verifique todas as configurações** (checklist acima)
2. ✅ **Use Standard JSON Input correto** (`sourcify_standard_json.json`)
3. ✅ **Certifique-se que tudo está idêntico** ao deploy
4. ✅ **Preencha TODOS os campos do formulário** (veja [`CAMPOS_BLOCKSCOUT_STANDARD_JSON.md`](./CAMPOS_BLOCKSCOUT_STANDARD_JSON.md))
5. ✅ **Tente novamente** - deve resultar em "Full Match"

---

## 🔗 Links Úteis

- **Blockscout Sepolia:** https://eth-sepolia.blockscout.com/address/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
- **Sourcify (Já verificado):** https://repo.sourcify.dev/11155111/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
- **Etherscan:** https://sepolia.etherscan.io/address/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87#code

---

## ✅ Resumo

**Erro:** "Cannot update partially verified smart contract..."

**Causa:** Blockscout já tem "Partial Match" e não permite substituir por outro "Partial Match"

**Soluções:**
1. ✅ Garantir configurações exatas para conseguir "Full Match"
2. ✅ Limpar verificação existente (se permitido)
3. ✅ Tentar outro instance ou aguardar
4. ✅ Deixar como está (se aceitável)
5. ✅ Verificar no Etherscan quando voltar

**Recomendação:** Se "Partial Match" já funciona, pode deixar assim. Se precisa "Full Match", verifique todas as configurações e tente novamente com Standard JSON Input correto.

---

**Boa sorte na verificação!** 🚀

