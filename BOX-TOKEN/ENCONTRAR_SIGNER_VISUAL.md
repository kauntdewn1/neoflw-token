# 🔍 Como Encontrar o Signer - Passo a Passo Visual

## 🎯 Você Está na Página do Contrato

URL atual: `bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017`

---

## ✅ Método 1: Verificar Função `signer()` (MAIS FÁCIL!)

### **Passo a Passo:**

#### **Passo 1: Vá para a Aba "Contract"**

Na página atual, você está na aba **"Transactions"**.

**Clique na aba:** **"Contract"** (ao lado de "Token Transfers", "Other Transactions", etc)

#### **Passo 2: Veja a Seção "Read Contract"**

Dentro da aba "Contract", você verá duas seções:
- **"Read Contract"** ← Clique aqui
- "Write Contract"

#### **Passo 3: Procure pela Função `signer`**

Na seção "Read Contract", procure por:
- `signer` ou `signer()`
- Pode estar listada junto com outras funções públicas

#### **Passo 4: Execute a Função**

- Clique na função `signer` ou no botão ao lado
- Clique em **"Read"** ou **"Query"**
- O valor retornado é o endereço do signer usado no constructor!

#### **Passo 5: Use o Valor**

Copie o endereço retornado e use no script ou cole diretamente no BSCScan.

---

## ✅ Método 2: Na Transação de Criação

### **Passo a Passo:**

#### **Passo 1: Encontre "Contract Creator"**

Na página atual (Overview), procure na seção **"More Info"**:
- **"CONTRACT CREATOR"** mostra: `0x45f9C5Af...6E4D42A53`
- E diz: "Created: 111 days ago"

#### **Passo 2: Clique no Endereço do Creator**

**Clique no endereço:** `0x45f9C5Af...6E4D42A53`

Isso vai abrir a página de perfil/endereço do creator.

#### **Passo 3: Veja "Contract Creation"**

Na página do creator, procure por:
- **"Contract Creation"** ou **"Contracts Created"**
- Deve mostrar o contrato `0xBc972E10Df612C7d65054BC67aBCA96B3C22a017`

#### **Passo 4: Clique na Transação de Criação**

Clique na transação que criou o contrato BOX Token.

#### **Passo 5: Veja "Input Data"**

Na página da transação:
- Procure a seção **"Input Data"**
- Role a página se necessário
- O Input Data mostra todo o código hexadecimal

#### **Passo 6: Identifique o Signer**

O Input Data tem esta estrutura:
```
[Bytecode do contrato compilado][Constructor Arguments]
```

Para o contrato InterboxCoin:
- O constructor precisa de: `address _signer`
- Um endereço tem 20 bytes (40 caracteres hex)
- O signer está nos **últimos bytes** do Input Data

**Como identificar:**
- Procure pelos últimos caracteres do Input Data
- Procure por um padrão que parece um endereço (0x seguido de 40 chars hex)
- O signer geralmente aparece após muito código hexadecimal

---

## ✅ Método 3: Direto no Hash da Transação (Alternativa)

### **Passo a Passo:**

1. **Na página do contrato**, veja **"Contract Creator"**
2. **Anote o endereço:** `0x45f9C5Af...6E4D42A53`
3. **Acesse diretamente:** 
   ```
   https://bscscan.com/address/0x45f9C5Af...6E4D42A53
   ```
   (Substitua `...` pelo endereço completo)
4. **Procure por transações** que criaram contratos
5. **Clique na transação** que criou `0xBc972E10Df612C7d65054BC67aBCA96B3C22a017`
6. **Veja Input Data** na página da transação

---

## 🎯 Método Mais Rápido: Aba "Contract"

**Recomendado:** Use o Método 1 acima (aba "Contract" → "Read Contract" → função `signer`)

É o mais simples porque:
- ✅ Não precisa procurar transação
- ✅ Não precisa decodificar hexadecimal
- ✅ O valor está diretamente acessível

---

## 📋 Checklist - Método 1 (Recomendado)

- [ ] Estou na página do contrato no BSCScan
- [ ] Cliquei na aba **"Contract"**
- [ ] Cliquei em **"Read Contract"**
- [ ] Procurei pela função `signer` ou `signer()`
- [ ] Cliquei em "Read" ou "Query"
- [ ] Copiei o endereço retornado
- [ ] Usei no script ou no BSCScan

---

## 🔧 Usar o Script com o Signer

Depois de encontrar o signer pelo Método 1:

```bash
cd BOX-TOKEN
python scripts/calculate_constructor_args_box.py 0x[ENDEREÇO_DO_SIGNER]
```

**Exemplo:**
```bash
python scripts/calculate_constructor_args_box.py 0x1234567890123456789012345678901234567890
```

O script retorna o valor para colar no BSCScan.

---

## 💡 Se Não Encontrar a Função `signer()`

**Alternativas:**

1. **Tente ver outras funções públicas:**
   - Na aba "Read Contract", veja todas as funções listadas
   - Procure por qualquer função que possa retornar o signer

2. **Use o Método 2** (procurar na transação de criação)

3. **Use o Sourcify:**
   - O Sourcify pode calcular automaticamente
   - Acesse: https://sourcify.dev/
   - Faça upload do arquivo `.sol`
   - Ele pode conseguir mesmo sem o constructor argument explícito

---

## 🔗 Links Diretos

- **Contrato (Aba Contract):** 
  ```
  https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017#readContract
  ```
  (Este link leva direto para "Read Contract"!)

- **Creator:**
  ```
  https://bscscan.com/address/0x45f9C5Af...6E4D42A53
  ```
  (Substitua pelos caracteres completos do endereço)

---

## ✅ Quick Action - Agora Mesmo

**Clique neste link direto:**
```
https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017#readContract
```

Isso vai abrir direto na seção "Read Contract". Procure por `signer` e clique em "Read"!

---

**Tente primeiro o Método 1 (aba Contract → Read Contract) - é o mais fácil!** 🚀

