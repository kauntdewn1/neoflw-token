# ⚡ Atualizar Imagem do Token - Guia Rápido

## ⚠️ ERRO COMUM: "Account Login service is temporarily unavailable"

**Se você está vendo este erro no Etherscan:**

- "Sorry, the Account Login service is temporarily unavailable. Please try again later."

**Soluções:**

1. ✅ **Aguarde algumas horas** e tente novamente (manutenção temporária)
2. ✅ **Use Blockscout** (funciona agora mesmo) - Veja abaixo
3. ✅ **Tente em horários diferentes** (madrugada pode estar menos carregado)
4. ✅ **Limpe cache do navegador** e tente novamente

---

## 🎯 3 Passos Principais (Quando Etherscan Funciona)

### 1️⃣ **Acesse a Página do Token**

```
https://sepolia.etherscan.io/token/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
```

⚠️ **Importante:** Use `/token/` e não `/address/`

---

### 2️⃣ **Conecte Sua Wallet e Procure "Update Token Info"**

**Onde procurar:**

- Topo da página (próximo ao nome do token)
- Menu "More" ou "⋮" (três pontos)
- Final da página (seção "Other Info")
- "My Account" → "Token Management"

---

### 3️⃣ **Cole Esta URL do Logo**

```
https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i
```

**Outras informações para preencher:**

- Name: `NeoFlowOFF`
- Symbol: `NEOFLW`
- Decimals: `18`
- Website: `neoflowoff.eth`

---

## ❗ Se Não Encontrar o Botão

1. ✅ Verifique se está na página `/token/` (não `/address/`)
2. ✅ Certifique-se que conectou a wallet
3. ✅ Verifique se está na rede Sepolia
4. ✅ Use a mesma wallet que fez o deploy
5. ✅ Tente limpar cache do navegador
6. ✅ Aguarde algumas horas se login estiver indisponível

---

## 🔗 Links Rápidos

- **Página do Token:** https://sepolia.etherscan.io/token/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
- **My Account:** https://sepolia.etherscan.io/myaccount
- **Guia Completo:** [`PASSO_A_PASSO_ATUALIZAR_IMAGEM.md`](./PASSO_A_PASSO_ATUALIZAR_IMAGEM.md)

---

## 🔄 Alternativa Imediata: Blockscout (Funciona Agora!)

**Se o Etherscan está com erro de login, use Blockscout:**

### **Opção 1: Blockscout Público (Mais Fácil)**

1. **Acesse (SEM `?tab=contract`):**
   ```
   https://eth-sepolia.blockscout.com/address/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
   ```
   ⚠️ **IMPORTANTE:** Remova `?tab=contract` se estiver na URL! Você precisa da página do TOKEN, não do contrato.

2. **Encontre o formulário "Token info application form":**
   - Procure por link "Update Token Info" ou "Edit Token Info"
   - Ou menu de opções do token
   - Ou botão "Submit Token Info"

3. **Preencha o formulário completo:**
   - 📖 **Guia detalhado:** Veja [`PREENCHER_FORMULARIO_BLOCKSCOUT.md`](./PREENCHER_FORMULARIO_BLOCKSCOUT.md)
   - ✅ Todos os campos obrigatórios precisam ser preenchidos
   - ⭐ **Campo mais importante:** Link to icon URL (logo do token)

4. **Após enviar - O que esperar:**
   - 📖 **Guia pós-envio:** Veja [`DEPOIS_DE_ENVIAR_BLOCKSCOUT.md`](./DEPOIS_DE_ENVIAR_BLOCKSCOUT.md)
   - ⏳ Status inicial: "In progress"
   - ⏰ Tempo típico: 24-72 horas para aprovação

### **Vantagens do Blockscout:**
- ✅ **Funciona mesmo quando Etherscan está com erro**
- ✅ **Suporte melhor para testnets**
- ✅ **Interface similar ao Etherscan**
- ✅ **Open-source** (mais confiável)

### **Outros Explorers Alternativos:**
- **Otterscan:** https://sepolia.otterscan.io/address/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
- **Etherscan (quando voltar):** https://sepolia.etherscan.io/token/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87

---

## ⏰ Estratégia Recomendada

1. **Agora (Etherscan com erro):**
   - ✅ Use Blockscout para visualizar/atualizar
   - ✅ Use Otterscan como alternativa

2. **Quando Etherscan voltar:**
   - ✅ Tente novamente no Etherscan (mais popular)
   - ✅ Mantenha Blockscout como backup

---

**Boa sorte!** 🚀

