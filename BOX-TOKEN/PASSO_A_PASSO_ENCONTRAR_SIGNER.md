# ⚡ Passo a Passo Rápido: Encontrar o Signer

## 🎯 Método Mais Simples (5 Segundos)

### **Clique neste link:**
```
https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017#readContract
```

### **O Que Você Vai Ver:**

1. Página abre direto na seção **"Read Contract"**
2. Procure por uma função chamada: **`signer`**
3. Clique no botão **"Read"** ou **"Query"** ao lado
4. **Copie o endereço** que aparece (será algo como `0x1234...5678`)

### **Pronto! Esse é o valor do signer!** ✅

---

## 📋 O Que Fazer Depois

### **Opção 1: Usar no Script**

```bash
cd BOX-TOKEN
python scripts/calculate_constructor_args_box.py 0x[COLE_O_ENDERECO_AQUI]
```

**O script vai calcular o constructor argument automaticamente.**

### **Opção 2: Calcular Manualmente**

Se o signer é: `0xABC123DEF456...`

No BSCScan, no campo "Constructor Arguments", cole:
```
000000000000000000000000ABC123DEF456...
```

(Sem o `0x`, e com zeros à esquerda até 64 caracteres)

---

## 🆘 Se Não Aparecer a Função `signer`

**Tente:**

1. **Verifique se está na aba "Contract"**
   - Não na aba "Transactions"
   - Não na aba "Token Transfers"
   - Deve estar em **"Contract"**

2. **Verifique se está em "Read Contract"**
   - Não em "Write Contract"
   - Deve estar em **"Read Contract"**

3. **Role a página para baixo**
   - As funções podem estar mais abaixo
   - Procure por qualquer coisa relacionada a "signer"

4. **Se realmente não aparecer:**
   - Use o Método 2: Procurar na transação de criação
   - Ou use o Sourcify (pode calcular automaticamente)

---

## ✅ Resumo Super Rápido

1. ✅ Clique: https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017#readContract
2. ✅ Procure: `signer`
3. ✅ Clique: "Read"
4. ✅ Copie: O endereço retornado
5. ✅ Use: No script ou no BSCScan

**É isso! Muito simples!** 🚀

