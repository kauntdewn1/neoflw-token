# 🔄 Token na Uniswap - Guia Completo

## ⚠️ Limitação Importante

**Uniswap não suporta Sepolia Testnet!**

A Uniswap funciona apenas com **mainnets** (redes principais):
- ✅ Ethereum Mainnet
- ✅ Arbitrum
- ✅ Polygon
- ✅ Base
- ✅ Optimism
- ✅ BNB Smart Chain
- ✅ E outras mainnets
- ❌ **NÃO suporta Sepolia** (testnet)

---

## 🎯 Como Funciona na Uniswap (Mainnet)

### **Para tokens em Mainnet:**

1. **Token aparece automaticamente** quando há liquidez
2. **Não precisa de formulário** para listar
3. **Logo/nome** vem de:
   - Token lists (Uniswap, CoinGecko, etc)
   - Dados on-chain do contrato
   - Sincronização com Etherscan

### **Passo a Passo (quando em Mainnet):**

1. **Adicione Liquidez:**
   - Acesse: https://app.uniswap.org/
   - Vá em "Pool" → "Add Liquidity"
   - Crie um par (ex: ETH/SEU_TOKEN)
   - Forneça liquidez

2. **Token aparecerá automaticamente** para swap

3. **Para atualizar logo/nome:**
   - Atualize no **Etherscan** primeiro
   - Uniswap sincroniza automaticamente
   - Ou atualize em **Token Lists** públicas

---

## 📋 Token Lists (Método para Atualizar Informações)

### **O que são Token Lists?**

Token Lists são arquivos JSON públicos que contêm informações de tokens que a Uniswap usa como referência.

### **Principais Token Lists:**

1. **Uniswap Default Token List:**
   - https://tokens.uniswap.org/
   - Gerenciada pela Uniswap Labs

2. **CoinGecko Token List:**
   - Usada por muitos serviços

3. **Token Lists públicas:**
   - Hospedadas em GitHub ou IPFS
   - Uniswap pode usar se configurado

### **Como Criar/Atualizar Token List:**

1. **Criar arquivo JSON** com formato Token List:
```json
{
  "name": "NeoFlow Token List",
  "timestamp": "2025-11-01T00:00:00.000Z",
  "version": {
    "major": 1,
    "minor": 0,
    "patch": 0
  },
  "tags": {},
  "logoURI": "https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i",
  "keywords": ["neoflow", "dao"],
  "tokens": [
    {
      "chainId": 1,
      "address": "0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87",
      "name": "NeoFlowOFF",
      "symbol": "NEOFLW",
      "decimals": 18,
      "logoURI": "https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i"
    }
  ]
}
```

2. **Hospedar publicamente** (GitHub, IPFS, etc)

3. **Solicitar inclusão** na lista da Uniswap (se qualificar)

---

## ✅ Solução para Sepolia Testnet

### **Opção 1: Aguardar Migração para Mainnet**

Quando migrar para Ethereum Mainnet:
1. ✅ Atualize no Etherscan primeiro
2. ✅ Adicione liquidez na Uniswap
3. ✅ Token aparecerá automaticamente
4. ✅ Logo/nome serão sincronizados do Etherscan

### **Opção 2: Usar Uniswap em Testnet Alternativo**

Uniswap tem versões em algumas testnets:
- ❌ Não inclui Sepolia
- ✅ Mas pode ter outras testnets suportadas

### **Opção 3: Focar em Etherscan Agora**

Para **testnet**, o mais importante é:
- ✅ **Etherscan** (quando login voltar)
- ✅ Outras plataformas são secundárias

---

## 🔗 Links Úteis

- **Uniswap App:** https://app.uniswap.org/
- **Uniswap Token Lists:** https://tokens.uniswap.org/
- **Suporte Uniswap:** https://support.uniswap.org/
- **Rede Suportadas:** https://support.uniswap.org/hc/pt-br/articles/40074184880525-Redes-no-Uniswap

---

## 📋 Informações do Token (para quando migrar para Mainnet)

```
Endereço: 0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
Nome: NeoFlowOFF
Símbolo: NEOFLW
Decimals: 18
Logo: https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i
Website: neoflowoff.eth
Rede: Ethereum Mainnet (quando migrar)
```

---

## 💡 Resumo

### **Para Sepolia Testnet (Agora):**
- ❌ Uniswap não suporta
- ✅ Foque em Etherscan (quando login voltar)
- ✅ Adicione na MetaMask para usar em outras plataformas

### **Para Mainnet (Depois):**
- ✅ Atualize no Etherscan primeiro
- ✅ Adicione liquidez na Uniswap
- ✅ Token aparecerá automaticamente
- ✅ Logo/nome serão sincronizados

---

## 🎯 Recomendação

**Para agora (Sepolia Testnet):**
1. ✅ **Etherscan** é a prioridade (quando login voltar)
2. ✅ **MetaMask** para adicionar o token
3. ✅ **DeBank** pode detectar automaticamente

**Para depois (Mainnet):**
1. ✅ **Etherscan** primeiro
2. ✅ **Uniswap** aparecerá automaticamente com liquidez
3. ✅ **Outras plataformas** seguirão

---

**Conclusão:** Uniswap não funciona para Sepolia agora, mas será fácil quando migrar para mainnet! 🚀

