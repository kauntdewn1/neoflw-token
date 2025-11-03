# 🛠️ Como Usar o Script fix_json_language_field.py

## 🎯 O Que Este Script Faz

Este script corrige arquivos JSON adicionando o campo `"language": "Solidity"` que é obrigatório para verificação no BSCScan.

---

## 📋 Pré-requisitos

- Você precisa ter um arquivo JSON (Standard JSON Input) do seu contrato
- Python instalado na sua máquina

---

## 🚀 Como Usar

### **Opção 1: Usar Arquivo Existente**

Se você já tem um arquivo JSON do contrato BOX:

```bash
cd BOX-TOKEN
python scripts/fix_json_language_field.py caminho/para/seu_arquivo.json
```

**Exemplo:**
```bash
python scripts/fix_json_language_field.py box_token.json
```

Isso vai criar: `box_token_fixed.json`

---

### **Opção 2: Especificar Arquivo de Saída**

Você pode escolher o nome do arquivo de saída:

```bash
python scripts/fix_json_language_field.py box_token.json box_token_corrigido.json
```

---

## 📝 Exemplo Completo

### **Passo 1: Localize Seu Arquivo JSON**

Onde pode estar seu JSON:
- Se você tem o projeto original: `artifacts/build-info/*.json`
- Se você baixou de algum lugar: onde você salvou o arquivo
- Se você criou manualmente: onde você salvou

### **Passo 2: Execute o Script**

```bash
# Navegue para a pasta BOX-TOKEN
cd /Users/nettomello/CODIGOS/neoflw-token/BOX-TOKEN

# Execute o script
python scripts/fix_json_language_field.py seu_arquivo.json
```

### **Passo 3: Use o Arquivo Corrigido**

O script vai criar um arquivo `*_fixed.json` com o campo `language` adicionado.

Abra esse arquivo e:
1. Copie todo o conteúdo
2. Cole no BSCScan no campo "Standard JSON Input"

---

## 🔍 O Que o Script Faz

1. ✅ **Lê o arquivo JSON** que você especificou
2. ✅ **Verifica** se tem o campo `language`
3. ✅ **Adiciona** `"language": "Solidity"` se estiver faltando
4. ✅ **Salva** um novo arquivo `*_fixed.json`
5. ✅ **Valida** se tem todos os campos essenciais

---

## ⚠️ Se Você NÃO Tem um Arquivo JSON

Se você não tem o arquivo Standard JSON Input do contrato BOX, você tem algumas opções:

### **Opção A: Obter do Projeto Original**

Se o contrato BOX foi compilado em um projeto:
- Procure por arquivos JSON de compilação
- Geralmente em: `artifacts/`, `build/`, `out/`, `.build/`

### **Opção B: Usar Método "Single File" no BSCScan**

Ao invés de Standard JSON Input, use:
- **Compiler Type:** `Solidity (Single file)`
- Faça upload do arquivo `.sol` do contrato

### **Opção C: Usar Sourcify**

O Sourcify pode ser mais tolerante:
- Acesse: https://sourcify.dev/
- Selecione: Binance Smart Chain
- Siga o guia: `docs/verification/SOURCIFY_PASSO_A_PASSO_BSC.md`

---

## ✅ Checklist

- [ ] Tenho um arquivo JSON do contrato BOX
- [ ] Executei o script com o arquivo JSON
- [ ] Verifiquei que o arquivo `*_fixed.json` foi criado
- [ ] O arquivo corrigido tem o campo `"language": "Solidity"`
- [ ] Estou pronto para colar no BSCScan

---

## 🔗 Links Úteis

- **Guia Completo do Erro:** `docs/verification/CORRIGIR_ERRO_LANGUAGE_FIELD.md`
- **Solução Rápida:** `SOLUCAO_RAPIDA_ERRO_LANGUAGE.md`
- **BSCScan:** https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017#code

---

## 💡 Dica

Se você ainda não tem o arquivo JSON, talvez seja mais fácil usar o método "Single File" no BSCScan ou verificar via Sourcify, que são mais simples quando você não tem o Standard JSON Input pronto.

---

**Boa sorte!** 🚀

