# 🌐 Como Obter Sepolia ETH

## ⚠️ Diferença Importante

- **Ethereum Mainnet** = Rede real (ETH custa dinheiro real)
- **Sepolia Testnet** = Rede de testes (ETH grátis de faucets)

Você **NÃO pode usar** ETH da mainnet para fazer deploy em Sepolia!

## 🔧 Adicionar Rede Sepolia no MetaMask

1. Abra MetaMask
2. Clique na rede (topo, onde está "Ethereum Mainnet")
3. Role até o final → **"Add network"** ou procure por **"Sepolia"**
4. Se não tiver, adicione manualmente:
   - **Network Name**: `Sepolia`
   - **RPC URL**: `https://rpc.sepolia.org`
   - **Chain ID**: `11155111`
   - **Currency Symbol**: `ETH`
   - **Block Explorer**: `https://sepolia.etherscan.io`

5. Salve e mude para rede Sepolia

## 💧 Faucets Sepolia (ETH Grátis)

### 1. Alchemy Faucet (Recomendado - você já tem conta!)
```
https://www.alchemy.com/faucets/ethereum-sepolia
```
- Precisa login com Alchemy
- Dá ~0.5 Sepolia ETH

### 2. Sepolia Faucet
```
https://sepoliafaucet.com/
```
- Simples, sem login

### 3. QuickNode Faucet
```
https://faucet.quicknode.com/ethereum/sepolia
```
- Precisa criar conta grátis

### 4. Infura Faucet
```
https://www.infura.io/faucet/sepolia
```
- Precisa criar conta grátis

## 📝 Passo a Passo

1. **Mude MetaMask para rede Sepolia** (veja acima)
2. **Copie seu endereço**: `0x460F9D0cf3e6E84faC1A7Abc524ddfa66fb64f60`
3. **Abra um faucet** (recomendo Alchemy, você já tem conta)
4. **Cole o endereço** no faucet
5. **Resolva captcha** (se houver)
6. **Aguarde 1-2 minutos**
7. **Verifique no MetaMask** se recebeu Sepolia ETH

## ✅ Verificar Saldo

Depois de receber, verifique:

```bash
# No MetaMask, mude para rede Sepolia e veja seu saldo
# Ou use:
export ALCHEMY_API_KEY=h47p2nw-NDUbS0nQfSUuV
# Verificar saldo via API
```

## 🚀 Depois de Receber

Quando tiver Sepolia ETH suficiente (~0.01 ou mais):

```bash
export ALCHEMY_API_KEY=h47p2nw-NDUbS0nQfSUuV
npm run deploy:token
```

---

**Lembre-se**: ETH mainnet ≠ Sepolia ETH. São redes diferentes! 🌐

