# 🔑 Como Configurar a API Key para Obter o ABI

## ⚡ Método Rápido (Temporário)

Quando o script pedir a API Key, você pode:

1. **Digitar diretamente no terminal** (a key não será salva)
2. **Ou pressionar Ctrl+C para cancelar** e configurar antes

---

## ✅ Método Permanente (Recomendado)

### **Opção 1: Variável de Ambiente (Temporária)**

No terminal, antes de rodar o script:

```bash
export ETHERSCAN_API_KEY=sua_api_key_aqui
```

Depois execute o script normalmente:

```bash
cd BOX-TOKEN
python scripts/get_contract_abi.py
```

### **Opção 2: Arquivo .env (Permanente)**

1. **Crie um arquivo `.env` na raiz do projeto BOX-TOKEN:**

```bash
cd BOX-TOKEN
touch .env
```

2. **Adicione a API key no arquivo:**

```env
ETHERSCAN_API_KEY=sua_api_key_aqui
```

3. **Adicione `.env` ao `.gitignore`** (se ainda não estiver):

```bash
echo ".env" >> .gitignore
```

4. **O script detectará automaticamente** (já está configurado para ler do .env via `os.getenv()`)

---

## 🔍 Como Obter a API Key

1. **Acesse:** https://etherscan.io/register (ou https://bscscan.com/register)
2. **Crie uma conta** (se ainda não tiver)
3. **Acesse:** https://etherscan.io/myapikey (ou https://bscscan.com/myapikey)
4. **Crie uma nova API Key**
5. **Copie a key** (ela só aparece uma vez!)

---

## 📝 Nota Importante

A mesma API Key do Etherscan funciona para:
- ✅ Ethereum Mainnet
- ✅ BSC (Binance Smart Chain)
- ✅ Polygon
- ✅ E outras redes suportadas pela API V2

Você **NÃO precisa** de uma API Key separada para BSC!

---

## ✅ Após Configurar

Depois de configurar a API key, você pode rodar:

```bash
cd BOX-TOKEN
python scripts/get_contract_abi.py
```

O script vai:
1. ✅ Usar a API key automaticamente
2. ✅ Verificar se o contrato está verificado
3. ✅ Obter o ABI
4. ✅ Salvar em `abi/InterboxCoin_abi.json`

---

## 🔗 Links Úteis

- **Etherscan API Keys:** https://etherscan.io/myapikey
- **BSCScan API Keys:** https://bscscan.com/myapikey
- **API V2 Migration:** https://docs.etherscan.io/v2-migration

---

**Configure a API key e rode o script novamente!** 🚀

