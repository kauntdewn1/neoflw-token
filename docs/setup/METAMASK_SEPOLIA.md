# 🦊 Configurar Sepolia no MetaMask

## ⚠️ Problema: "Não foi possível obter o ID da cadeia"

O RPC público (`https://rpc.sepolia.org`) pode estar instável. Use o RPC da Alchemy que já temos configurado!

## ✅ Configuração Recomendada (Alchemy RPC)

### No MetaMask:

1. **Abra MetaMask**
2. **Clique na rede** (topo, onde está "Ethereum Mainnet")
3. **Role até o final** → **"Add network"** ou **"Add network manually"**
4. **Preencha os campos:**

```
Network Name: Sepolia Test Network
RPC URL: https://eth-sepolia.g.alchemy.com/v2/SUA_API_KEY_AQUI
Chain ID: 11155111
Currency Symbol: ETH
Block Explorer URL: https://sepolia.etherscan.io
```

5. **Clique em "Save"**
6. **Mude para rede Sepolia**

## 🔄 RPCs Alternativos (se Alchemy não funcionar)

### Opção 1: PublicNode (público, sem key)

```
Network Name: Sepolia Test Network
RPC URL: https://ethereum-sepolia-rpc.publicnode.com
Chain ID: 11155111
Currency Symbol: ETH
Block Explorer URL: https://sepolia.etherscan.io
```

### Opção 2: Ankr (público)

```
Network Name: Sepolia Test Network
RPC URL: https://rpc.ankr.com/eth_sepolia
Chain ID: 11155111
Currency Symbol: ETH
Block Explorer URL: https://sepolia.etherscan.io
```

### Opção 3: QuickNode (público)

```
Network Name: Sepolia Test Network
RPC URL: https://ethereum-sepolia-rpc.publicnode.com
Chain ID: 11155111
Currency Symbol: ETH
Block Explorer URL: https://sepolia.etherscan.io
```

## ✅ Depois de Adicionar

1. **Mude para rede Sepolia** no MetaMask
2. **Verifique se aparece "Sepolia Test Network"** no topo
3. **Seu endereço**: `0x460F9D0cf3e6E84faC1A7Abc524ddfa66fb64f60`
4. **Saldo deve aparecer como 0 ETH** (ainda)
5. **Obtenha Sepolia ETH** de um faucet

## 💧 Faucets Sepolia

- **Alchemy**: https://www.alchemy.com/faucets/ethereum-sepolia
- **Sepolia Faucet**: https://sepoliafaucet.com/
- **QuickNode**: https://faucet.quicknode.com/ethereum/sepolia

---

**Dica**: Use sempre o RPC da Alchemy se possível - é mais rápido e confiável! 🚀

