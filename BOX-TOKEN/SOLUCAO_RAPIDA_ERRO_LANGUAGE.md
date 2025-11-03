# ⚡ Solução Rápida: Erro "language field"

## ❌ Erro que Você Está Vendo

```
invalid_parameter: Standard JSON input must contain a language field
```

---

## ✅ Solução em 3 Passos

### **1. Abra o Seu Arquivo JSON**

Abra o arquivo JSON que você está tentando usar no BSCScan.

### **2. Adicione Esta Linha no Início**

Adicione esta linha **logo após o `{`**:

```json
{
  "language": "Solidity",
```

**Exemplo Completo:**

**ANTES (Errado - Sem language):**
```json
{
  "sources": {
    "contracts/BoxToken.sol": {
      "content": "..."
    }
  },
  "settings": {
    ...
  }
}
```

**DEPOIS (Correto - Com language):**
```json
{
  "language": "Solidity",
  "sources": {
    "contracts/BoxToken.sol": {
      "content": "..."
    }
  },
  "settings": {
    ...
  }
}
```

### **3. Salve e Cole no BSCScan**

Salve o arquivo JSON corrigido e cole o conteúdo no BSCScan.

---

## 🛠️ Solução Automática (Script)

Se você tem um arquivo JSON para corrigir, use o script:

```bash
cd BOX-TOKEN
python scripts/fix_json_language_field.py seu_arquivo.json
```

O script vai:
- ✅ Verificar se o campo `language` existe
- ✅ Adicionar se estiver faltando
- ✅ Criar um arquivo `seu_arquivo_fixed.json` corrigido

---

## 📋 O Que Precisa Estar no JSON

O JSON deve ter **no mínimo**:

```json
{
  "language": "Solidity",  // ← ESTE É O CAMPO QUE ESTÁ FALTANDO!
  "sources": {
    // Seus arquivos .sol aqui
  },
  "settings": {
    // Configurações de compilação aqui
  }
}
```

---

## ✅ Depois de Corrigir

1. **Cole o JSON corrigido** no BSCScan
2. **Preencha os outros campos:**
   - Compiler Version
   - License
3. **Clique em "Verify and Publish"**

---

## 🔗 Links Úteis

- **Guia Completo:** `docs/verification/CORRIGIR_ERRO_LANGUAGE_FIELD.md`
- **BSCScan:** https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017#code

---

**É só isso!** Adicione `"language": "Solidity",` no início do JSON e o erro será resolvido! 🚀

