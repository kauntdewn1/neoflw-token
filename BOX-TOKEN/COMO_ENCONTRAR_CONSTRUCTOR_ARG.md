# 🔍 Como Encontrar o Constructor Argument

## 🎯 Problema

O erro de bytecode mismatch geralmente é causado por **Constructor Arguments incorretos ou ausentes**.

O contrato `InterboxCoin` tem constructor:
```solidity
constructor(address _signer)
```

Você precisa descobrir qual endereço foi usado como `_signer` no deploy.

---

## ✅ Método 1: Na Transação de Deploy (Mais Confiável)

### **Passo a Passo:**

1. **Acesse a página do contrato:**
   ```
   https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017
   ```

2. **Veja a seção "Contract Creator":**
   - Deve mostrar algo como: `0x45f9C5Af...6E4D42A53`
   - E "Created: 111 days ago"
   - **CLIQUE no endereço do creator OU no link da transação**

3. **Na página da transação de criação:**
   - Role até a seção **"Input Data"**
   - Você verá um código hexadecimal longo

4. **Como identificar o signer:**
   - O Input Data tem esta estrutura:
     ```
     [Bytecode do contrato][Constructor Arguments]
     ```
   - O contrato InterboxCoin tem 1 argumento: `address _signer`
   - Um endereço tem 40 caracteres hex (20 bytes)
   - Procure pelos últimos caracteres do Input Data
   - O signer é um endereço completo (0x seguido de 40 caracteres hex)

5. **Exemplo:**
   - Se Input Data termina com: `...000000000000000000000000A1B2C3D4E5F6A7B8C9D0E1F2A3B4C5D6E7F8A9B0`
   - O signer seria: `0xA1B2C3D4E5F6A7B8C9D0E1F2A3B4C5D6E7F8A9B0`
   - (Os zeros à esquerda são padding ABI)

---

## ✅ Método 2: Verificar Função `signer()` no Contrato

Se o contrato tem uma função pública `signer()`:

1. **Acesse:**
   ```
   https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017#readContract
   ```

2. **Procure pela função:**
   - `signer()` ou `signer`
   - Execute a função (clique em "Read")
   - O valor retornado é o `_signer` usado no constructor

3. **Se encontrar:** Use esse valor como constructor argument

---

## ✅ Método 3: Usar Script Automatizado

Depois de encontrar o endereço do signer, use o script:

```bash
cd BOX-TOKEN
python scripts/calculate_constructor_args_box.py 0x[ENDEREÇO_DO_SIGNER]
```

**Exemplo:**
```bash
python scripts/calculate_constructor_args_box.py 0x1234567890123456789012345678901234567890
```

O script vai calcular o ABI-encoded automaticamente.

---

## 📋 Formato do Constructor Argument no BSCScan

No campo "Constructor Arguments" do BSCScan:

- ❌ **NÃO coloque:** `0x1234...5678`
- ✅ **Cole apenas:** `0000000000000000000000001234...5678`
- ✅ **Sem o `0x`**
- ✅ **Com zeros à esquerda** (total de 64 caracteres hex)

**Exemplo:**
- Se o signer é: `0xABC123DEF456789012345678901234567890ABCD`
- No BSCScan coloque: `000000000000000000000000ABC123DEF456789012345678901234567890ABCD`

---

## ⚠️ Se Não Encontrar o Constructor Argument

**Opções:**

1. **Tente deixar vazio primeiro**
   - Às vezes funciona se o BSCScan consegue inferir
   - Mas geralmente não funciona para contratos com constructor

2. **Use o Sourcify**
   - O Sourcify pode calcular automaticamente
   - Acesse: https://sourcify.dev/
   - Método: "Solidity Files"
   - Faça upload do arquivo `InterboxCoin_Flattened_Final.sol`
   - O Sourcify pode conseguir mesmo sem o constructor argument explícito

3. **Entre em contato com quem fez o deploy**
   - O deployer é: `0x45f9C5Af...6E4D42A53`
   - Peça o valor do `_signer` usado

---

## 🎯 Quick Start

1. **Encontre o signer** (Método 1 ou 2 acima)
2. **Use o script:**
   ```bash
   python scripts/calculate_constructor_args_box.py [SIGNER_ADDRESS]
   ```
3. **Copie o resultado** e cole no BSCScan
4. **Tente verificar novamente**

---

## ✅ Checklist

- [ ] Acessei a página do contrato no BSCScan
- [ ] Encontrei a transação de deploy
- [ ] Identifiquei o Input Data
- [ ] Extraí o endereço do signer dos últimos bytes
- [ ] Usei o script para calcular ABI-encoded
- [ ] Colei no campo Constructor Arguments (sem 0x)
- [ ] Tentei verificar novamente

---

**O constructor argument é muito provável que seja o problema! Encontre o signer e tente novamente!** 🚀

