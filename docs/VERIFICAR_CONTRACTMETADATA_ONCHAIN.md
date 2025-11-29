# 🔍 Verificar ContractMetadata On-Chain (Sem PolygonScan)

**Objetivo:** Verificar se o contrato deployado já tem `ContractMetadata` antes de verificar no PolygonScan

---

## ✅ SITUAÇÃO ATUAL

### Código Fonte
O código atual **JÁ TEM** `ContractMetadata` implementado:

```9:9:contracts/NeoFlowToken.sol
contract NeoFlowToken is ERC20, Ownable, ContractMetadata {
```

O contrato herda de:
- ✅ `ContractMetadata` (que expõe `contractURI()` e `setContractURI()`)
- ✅ Implementa `_canSetContractURI()` corretamente

### Contrato Deployado
O contrato deployado em `0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87` pode ter sido deployado:
- ❓ **ANTES** de adicionar `ContractMetadata` → Precisa novo deploy
- ✅ **DEPOIS** de adicionar `ContractMetadata` → Já tem, só precisa verificar

---

## 🚀 SOLUÇÃO: Verificar On-Chain

**NÃO precisa verificar no PolygonScan primeiro!** Podemos verificar diretamente on-chain se o contrato tem a função `contractURI()`.

### Script Criado

**Forma 1: Usando arquivo `.token_address.txt` (Recomendado)**

```bash
# Salvar endereço no arquivo
echo "0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87" > .token_address.txt

# Executar script
ape run check_contract_metadata --network polygon:mainnet
```

**Forma 2: Passar endereço diretamente (se o Ape suportar)**

```bash
ape run check_contract_metadata --network polygon:mainnet
# (O script tentará ler de .token_address.txt automaticamente)
```

---

## 📋 O QUE O SCRIPT FAZ

1. ✅ Conecta à rede (Polygon Mainnet)
2. ✅ Acessa o contrato no endereço especificado
3. ✅ Tenta chamar `contractURI()` on-chain
4. ✅ Verifica se `setContractURI()` existe
5. ✅ Retorna resultado claro:
   - ✅ **TEM** → Não precisa novo deploy, só configurar metadata
   - ❌ **NÃO TEM** → Precisa novo deploy

---

## 🎯 RESULTADOS POSSÍVEIS

### ✅ Caso 1: Contrato JÁ TEM ContractMetadata

```
✅ RESULTADO: Contrato JÁ TEM ContractMetadata!

💡 Próximos passos:
   1. Você pode configurar contractURI usando:
      token.setContractURI('https://...', sender=acct)
   2. NÃO precisa fazer novo deploy!
   3. Basta verificar o contrato no PolygonScan
```

**Ação:** Apenas verificar no PolygonScan e configurar `contractURI` se necessário.

---

### ❌ Caso 2: Contrato NÃO TEM ContractMetadata

```
❌ RESULTADO: Contrato NÃO tem ContractMetadata

💡 Próximos passos:
   1. Você precisa fazer NOVO deploy do contrato
   2. O código atual JÁ tem ContractMetadata implementado
   3. Use: ape run scripts/deploy/deploy_token --network polygon:mainnet
```

**Ação:** Fazer novo deploy seguindo `docs/deploy/DEPLOY_COM_CONTRACTMETADATA.md`

---

## 🔧 USO PRÁTICO

### Verificar Contrato Específico

```bash
# 1. Salvar endereço no arquivo
echo "0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87" > .token_address.txt

# 2. Executar script (Polygon Mainnet)
ape run check_contract_metadata --network polygon:mainnet
```

### Verificar Contrato do Arquivo Existente

```bash
# Se já tiver .token_address.txt com o endereço
ape run check_contract_metadata --network polygon:mainnet
```

---

## 💡 VANTAGENS

✅ **Evita trabalho duplicado:**
- Não precisa verificar no PolygonScan primeiro
- Não precisa fazer novo deploy se já tiver

✅ **Resultado imediato:**
- Script retorna resultado em segundos
- Sabemos exatamente o que fazer

✅ **Confiança:**
- Verificação on-chain é 100% confiável
- Não depende de indexadores ou verificação de código

---

## 📝 NOTAS

- O script usa o ABI do contrato compilado localmente
- Se o contrato não tiver `ContractMetadata`, a chamada falhará
- Se tiver, retornará a URI atual (pode ser vazia se não configurada)

---

**Última atualização:** 2025-01-XX

