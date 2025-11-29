# 🔍 Auditoria de Endereços de Contratos

**Objetivo:** Encontrar todos os endereços de contratos deployados e identificar em qual rede cada um está.

---

## 🚀 Como Executar a Auditoria

### **Método 1: Script Automático (Recomendado)**

```bash
# Carregar variáveis de ambiente
source scripts/shell/setup_env.sh

# Executar auditoria
ape run audit_contract_addresses
```

O script vai:
1. ✅ Ler todos os arquivos de endereços
2. ✅ Ler endereços do `.env`
3. ✅ Verificar on-chain em múltiplas redes (Polygon, Sepolia, Ethereum)
4. ✅ Gerar relatório completo

### **Método 2: Verificação Manual**

Verifique cada endereço no explorer correspondente:

**Polygon Mainnet:**
- https://polygonscan.com/address/[ENDERECO]

**Sepolia (Testnet):**
- https://sepolia.etherscan.io/address/[ENDERECO]

---

## 📋 Arquivos Verificados

O script verifica os seguintes arquivos:

### **Arquivos de Endereços:**

1. `.token_address.txt` (raiz)
2. `artifacts/addresses/.token_address.txt`
3. `.vault_address.txt` (raiz)
4. `artifacts/addresses/.vault_address.txt`
5. `.claim_address.txt` (raiz)
6. `artifacts/addresses/.claim_address.txt`

### **Arquivos de Configuração:**

1. `.env` (variáveis `NEXT_PUBLIC_*_ADDRESS`)

---

## 📊 Resultado Esperado

O script gera um relatório mostrando:

### ✅ **Contratos no Polygon Mainnet**
- Endereços válidos para produção
- Onde cada endereço foi encontrado

### ⚠️ **Contratos no Sepolia (Testnet)**
- Endereços de teste (devem ser removidos ou marcados)

### ❌ **Contratos Não Encontrados**
- Endereços inválidos ou de outras redes

---

## 🔧 Após a Auditoria

### **1. Atualizar Arquivos Corretos**

Após identificar os endereços corretos do Polygon:

```bash
# Atualizar token
echo "0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2" > .token_address.txt
echo "0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2" > artifacts/addresses/.token_address.txt

# Atualizar vault (substituir pelo endereço correto)
echo "0x[ENDERECO_VAULT_POLYGON]" > .vault_address.txt
echo "0x[ENDERECO_VAULT_POLYGON]" > artifacts/addresses/.vault_address.txt

# Atualizar claim (substituir pelo endereço correto)
echo "0x[ENDERECO_CLAIM_POLYGON]" > .claim_address.txt
echo "0x[ENDERECO_CLAIM_POLYGON]" > artifacts/addresses/.claim_address.txt
```

### **2. Atualizar .env**

```env
# Polygon Mainnet (produção)
NEXT_PUBLIC_TOKEN_ADDRESS=0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2
NEXT_PUBLIC_VAULT_ADDRESS=0x[ENDERECO_VAULT_POLYGON]
NEXT_PUBLIC_CLAIM_ADDRESS=0x[ENDERECO_CLAIM_POLYGON]
```

### **3. Remover Endereços de Sepolia**

Se encontrar endereços de Sepolia, remova ou marque claramente:

```bash
# Criar arquivo de backup
mkdir -p docs/temp/old_addresses
mv .token_address.txt docs/temp/old_addresses/token_sepolia.txt  # se for Sepolia
```

---

## 📝 Checklist de Limpeza

Após a auditoria:

- [ ] Identificar endereços corretos do Polygon
- [ ] Atualizar arquivos `.txt` com endereços corretos
- [ ] Atualizar `.env` com endereços corretos
- [ ] Remover ou marcar endereços de Sepolia
- [ ] Verificar se frontend está usando endereços corretos
- [ ] Documentar endereços finais

---

## 🐛 Troubleshooting

### **Erro: "Network not found"**

**Solução:** Verifique se as redes estão configuradas no `ape-config.yaml`

### **Erro: "Provider not available"**

**Solução:** 
```bash
# Carregar variáveis de ambiente
source scripts/shell/setup_env.sh
```

### **Contrato não encontrado em nenhuma rede**

**Possíveis causas:**
- Endereço inválido
- Contrato deployado em rede não verificada
- Contrato foi destruído (selfdestruct)

---

## 📄 Relatório Gerado

O script salva um relatório em:
```
artifacts/addresses/AUDIT_REPORT.txt
```

Este arquivo contém:
- Lista de endereços por rede
- Onde cada endereço foi encontrado
- Recomendações

---

**Última atualização:** 2025-01-XX

