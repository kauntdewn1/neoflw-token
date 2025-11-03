# 🔑 Como Obter API Key do BSCScan / Etherscan API V2

## 🎯 Objetivo

Obter uma **API Key** para usar em scripts de automação. **⚠️ IMPORTANTE:** As APIs do BSCScan foram depreciadas e substituídas pela **Etherscan API V2**.

## ⚠️ ATENÇÃO: Mudança nas APIs

**As APIs do BSCScan foram depreciadas e substituídas pela Etherscan API V2.**

- ✅ **Para verificação de contratos:** Recomendamos usar **Sourcify** (gratuito, não requer API)
- ✅ **Para scripts que precisam de API:** Use a **Etherscan API V2** (suporta BSC)
- ⚠️ **BSCScan API antiga:** Não funciona mais para novos projetos

---

## ✅ Passo a Passo

### **1. Criar Conta no BSCScan**

1. **Acesse:** https://bscscan.com/register
2. **Preencha o formulário:**
   - Username
   - Email
   - Password
   - Confirme a password
   - Aceite os termos
3. **Clique em "Create Account"**
4. **Confirme seu email** (verifique a caixa de entrada)

---

### **2. Fazer Login**

1. **Acesse:** https://bscscan.com/login
2. **Entre com suas credenciais**

---

### **3. Gerar API Key**

1. **Acesse:** https://bscscan.com/myapikey
   - Ou vá em: **My Account** → **API-KEYs**

2. **Clique em "Add"** ou **"Create API Key"**

3. **Dê um nome para a API Key:**
   - Exemplo: `BoxToken-Verification`
   - Ou: `Personal-Project`

4. **Clique em "Create"**

5. **Copie a API Key gerada:**
   - ⚠️ **IMPORTANTE:** Guarde esta key com segurança!
   - Ela só será mostrada uma vez
   - Se perder, você precisará criar uma nova

---

### **4. Tipos de API Keys**

BSCScan oferece diferentes tipos:

- **Free Tier (Gratuito):**
  - 5 calls/second
  - Ideal para projetos pessoais
  - Recomendado para começar

- **Standard (Pago):**
  - Mais calls por segundo
  - Para projetos maiores

- **Professional (Pago):**
  - Máximo de calls
  - Para aplicações enterprise

**Para este projeto, o Free Tier é suficiente!** ✅

---

## 🔧 Usar a API Key

### **No arquivo .env:**

Adicione a API Key ao seu arquivo `.env`:

```env
BSCSCAN_API_KEY=sua_api_key_aqui
```

### **Em scripts Python:**

```python
import os
from dotenv import load_dotenv

load_dotenv()

bscscan_api_key = os.getenv('BSCSCAN_API_KEY')
```

### **Em requisições HTTP:**

```python
import requests

url = f"https://api.bscscan.com/api?module=account&action=balance&address=0xBc972E10Df612C7d65054BC67aBCA96B3C22a017&tag=latest&apikey={bscscan_api_key}"
response = requests.get(url)
```

---

## 📋 Limites da API

### **Free Tier:**
- **Rate Limit:** 5 calls/second
- **Daily Limit:** Sem limite específico mencionado
- **Endpoints disponíveis:** Todos os endpoints públicos

### **Dicas para evitar rate limiting:**
- ✅ Adicione delays entre chamadas (ex: 1 segundo)
- ✅ Use cache quando possível
- ✅ Não faça muitas chamadas simultâneas

---

## 🔗 Endpoints Úteis da API

### **Verificar Contrato:**
```
POST https://api.bscscan.com/api
```

### **Obter Informações do Token:**
```
GET https://api.bscscan.com/api?module=token&action=tokeninfo&contractaddress=0xBc972E10Df612C7d65054BC67aBCA96B3C22a017&apikey={API_KEY}
```

### **Obter Balance:**
```
GET https://api.bscscan.com/api?module=account&action=balance&address={ADDRESS}&tag=latest&apikey={API_KEY}
```

---

## 📖 Documentação Completa

Para ver todos os endpoints disponíveis:

**BSCScan API Docs:** https://docs.bscscan.com/api-endpoints/getting-started

---

## ⚠️ Segurança

### **Boas Práticas:**

1. ✅ **Nunca commite a API Key no Git**
   - Use `.env` e adicione ao `.gitignore`
   
2. ✅ **Não compartilhe a API Key publicamente**
   - Mantenha privada

3. ✅ **Use diferentes keys para diferentes projetos**
   - Facilita revogação se necessário

4. ✅ **Monitore o uso da API**
   - Verifique em: https://bscscan.com/myapikey

---

## 🔗 Links Úteis

- **BSCScan API Keys:** https://bscscan.com/myapikey
- **BSCScan API Docs:** https://docs.bscscan.com/api-endpoints/getting-started
- **BSCScan Register:** https://bscscan.com/register
- **BSCScan Login:** https://bscscan.com/login

---

## ✅ Checklist

- [ ] Conta criada no BSCScan
- [ ] Email confirmado
- [ ] Login realizado
- [ ] API Key gerada
- [ ] API Key copiada e guardada com segurança
- [ ] API Key adicionada ao `.env`
- [ ] `.env` adicionado ao `.gitignore` (se ainda não estiver)

---

**Pronto!** Agora você tem uma API Key do BSCScan para usar nos scripts! 🚀

