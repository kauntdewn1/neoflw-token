# 📋 Como Obter o ABI do Contrato Verificado

Depois que o contrato BOX Token for verificado no BSCScan, você pode obter o ABI automaticamente usando a API do Etherscan (que também funciona para BSCScan).

---

## 🔑 Pré-requisitos

1. **API Key do Etherscan/BSCScan:**
   - Veja: [`docs/setup/BSCSCAN_API_SETUP.md`](../setup/BSCSCAN_API_SETUP.md)
   - A API do Etherscan funciona tanto para Ethereum quanto para BSC

2. **Contrato Verificado:**
   - O contrato deve estar verificado no BSCScan antes de obter o ABI

---

## 🌐 Endpoint da API

### **⚠️ IMPORTANTE: API V2 (V1 Depreciada)**

A API V1 foi depreciada em agosto de 2025. Use sempre a **API V2**:

### **URL Base:**
```
https://api.etherscan.io/v2/api
```

Para BSC (Binance Smart Chain), inclua `chainid=56` na URL.

---

## 📝 Parâmetros da Requisição

### **Query Parameters:**

| Parâmetro | Valor | Descrição |
|-----------|-------|-----------|
| `apikey` | `YourApiKeyToken` | Sua chave API do Etherscan |
| `chainid` | `56` | Chain ID do BSC Mainnet |
| `module` | `contract` | Módulo da API |
| `action` | `getabi` | Ação para obter o ABI |
| `address` | `0xBc972E10Df612C7d65054BC67aBCA96B3C22a017` | Endereço do contrato BOX Token |

---

## 🔗 URL Completa (API V2)

```
https://api.etherscan.io/v2/api?chainid=56&module=contract&action=getabi&address=0xBc972E10Df612C7d65054BC67aBCA96B3C22a017&apikey=YOUR_API_KEY
```

**⚠️ Diferença da V1:** O `chainid` agora vai na URL base (antes do `module`), não como parâmetro separado.

**Substitua:**
- `YOUR_API_KEY` pela sua chave API do Etherscan

---

## 📥 Resposta da API

### **Sucesso (Status 1):**

```json
{
  "status": "1",
  "message": "OK",
  "result": "[{\"constant\":false,\"inputs\":[{\"name\":\"_signer\",\"type\":\"address\"}],\"name\":\"constructor\",\"outputs\":[],\"payable\":false,\"stateMutability\":\"nonpayable\",\"type\":\"constructor\"},{\"constant\":true,\"inputs\":[],\"name\":\"name\",\"outputs\":[{\"name\":\"\",\"type\":\"string\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"}]"
}
```

O campo `result` contém o ABI como uma string JSON. Você precisa fazer parse dessa string.

### **Erro (Status 0):**

```json
{
  "status": "0",
  "message": "NOTOK",
  "result": "Contract source code not verified"
}
```

**Causa:** O contrato ainda não foi verificado no BSCScan.

---

## 🛠️ Métodos para Obter o ABI

### **Método 1: Usando o Script Python (Recomendado)**

Veja: [`scripts/get_contract_abi.py`](../../scripts/get_contract_abi.py)

**Uso:**
```bash
cd BOX-TOKEN
python scripts/get_contract_abi.py
```

O script vai:
- Solicitar sua API key (ou usar variável de ambiente)
- Fazer a requisição à API
- Salvar o ABI em um arquivo JSON formatado
- Mostrar o ABI na tela

---

### **Método 2: Usando cURL**

```bash
curl "https://api.etherscan.io/v2/api?chainid=56&module=contract&action=getabi&address=0xBc972E10Df612C7d65054BC67aBCA96B3C22a017&apikey=YOUR_API_KEY" | jq '.result' | jq 'fromjson' > contract_abi.json
```

**⚠️ Note:** URL mudou para `/v2/api` e `chainid` vem antes dos outros parâmetros.

**Requisitos:**
- `curl` instalado
- `jq` instalado (para formatar JSON)

**Sem jq:**
```bash
curl "https://api.etherscan.io/api?module=contract&action=getabi&address=0xBc972E10Df612C7d65054BC67aBCA96B3C22a017&chainid=56&apikey=YOUR_API_KEY"
```

Depois faça parse manual do campo `result`.

---

### **Método 3: Usando Python (Manual)**

```python
import requests
import json

api_key = "YOUR_API_KEY"
contract_address = "0xBc972E10Df612C7d65054BC67aBCA96B3C22a017"
chain_id = "56"  # BSC Mainnet

# API V2: chainid na URL base
url = f"https://api.etherscan.io/v2/api?chainid={chain_id}"
params = {
    "module": "contract",
    "action": "getabi",
    "address": contract_address,
    "apikey": api_key
}

response = requests.get(url, params=params)
data = response.json()

if data["status"] == "1":
    abi = json.loads(data["result"])
    print(json.dumps(abi, indent=2))
else:
    print(f"Erro: {data['message']}")
```

---

### **Método 4: Diretamente no BSCScan**

1. Acesse: https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017#code
2. Role até a seção "Contract ABI"
3. Clique em "Copy" para copiar o ABI
4. Cole em um arquivo JSON

---

## 🔍 Verificar se o Contrato Está Verificado

Antes de obter o ABI, verifique se o contrato está verificado:

1. **No BSCScan:**
   - Acesse a página do contrato
   - Veja se aparece "Contract Source Code Verified ✓"

2. **Via API (V2):**
   ```bash
   curl "https://api.etherscan.io/v2/api?chainid=56&module=contract&action=getsourcecode&address=0xBc972E10Df612C7d65054BC67aBCA96B3C22a017&apikey=YOUR_API_KEY"
   ```
   
   Se `SourceCode` não estiver vazio, o contrato está verificado.

---

## 📁 Onde Salvar o ABI

Recomendado salvar em:
```
BOX-TOKEN/abi/InterboxCoin_abi.json
```

Ou:
```
BOX-TOKEN/contracts/abi/InterboxCoin_abi.json
```

---

## ✅ Checklist

- [ ] Contrato verificado no BSCScan
- [ ] API Key do Etherscan configurada
- [ ] ABI obtido e salvo em arquivo JSON
- [ ] ABI formatado e validado

---

## 🔗 Links Úteis

- **API V2 Migration Guide:** https://docs.etherscan.io/v2-migration
- **API Documentation:** https://docs.etherscan.io/api-endpoints/contracts#get-contract-abi
- **BSCScan Contract:** https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017#code
- **Etherscan API Docs:** https://docs.etherscan.io/

---

## 💡 Dica

O ABI é útil para:
- Interagir com o contrato via Web3.js/Ethers.js
- Criar interfaces de usuário que interagem com o contrato
- Testes automatizados
- Análise de funções do contrato

---

**Após verificar o contrato, use o script para obter o ABI automaticamente!** 🚀

