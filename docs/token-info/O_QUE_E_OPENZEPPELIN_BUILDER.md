# 🔧 OpenZeppelin Builder - O que é e Como Usar

## 📋 O que é o OpenZeppelin Builder?

O **OpenZeppelin Contracts UI Builder** é uma ferramenta para **criar interfaces front-end (UI)** para contratos inteligentes já deployados. 

**NÃO é para:**
- ❌ Atualizar metadados de token (logo, nome, descrição)
- ❌ Atualizar informações no Etherscan
- ❌ Gerenciar informações do token

**É para:**
- ✅ Criar interface web para interagir com seu contrato
- ✅ Gerar código React pronto para produção
- ✅ Criar formulários para chamar funções do contrato
- ✅ Conectar com carteiras (MetaMask, etc)

---

## 🎯 Quando Usar o OpenZeppelin Builder?

### **Use se você quer:**

1. **Criar uma interface web** para seu token
2. **Permitir usuários** interagirem com o contrato via interface
3. **Criar formulários** para funções como `burn()`, `transfer()`, etc
4. **Gerar código React** pronto para usar

### **NÃO use para:**

- ❌ Atualizar logo/nome no Etherscan
- ❌ Atualizar metadados do token
- ❌ Gerenciar informações do token

---

## 🔗 Como Funciona?

### **Passo a Passo:**

1. **Acesse:** https://builder.openzeppelin.com/
2. **Selecione a rede:** Sepolia Testnet (se disponível)
3. **Cole o endereço do contrato:**
   ```
   0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
   ```
4. **Se contrato verificado:** ABI será carregado automaticamente
5. **Selecione funções** para criar interface:
   - `burn(uint256 amount)` - Criar botão para queimar tokens
   - `transfer(address to, uint256 amount)` - Criar formulário de transferência
   - Etc.
6. **Personalize a interface:**
   - Campos do formulário
   - Restrições de execução
   - Kit de carteira (MetaMask, WalletConnect, etc)
7. **Exporte o projeto:**
   - Baixa código React pronto
   - Pronto para deploy ou personalização

---

## 💡 Exemplo de Uso para Seu Token

### **O que você pode criar:**

1. **Interface para queimar tokens:**
   - Campo: quantidade de tokens
   - Botão: "Burn Tokens"
   - Chama função `burn()` do contrato

2. **Interface para transferir:**
   - Campo: endereço destino
   - Campo: quantidade
   - Botão: "Transfer"
   - Chama função `transfer()` do contrato

3. **Dashboard do token:**
   - Mostrar saldo
   - Mostrar total supply
   - Interações com o contrato

---

## ⚠️ Limitações para Sepolia

- ⚠️ OpenZeppelin Builder pode não suportar Sepolia diretamente
- ✅ Mas você pode usar o ABI manualmente se necessário
- ✅ Funciona melhor com mainnets

---

## 📋 Informações do Seu Contrato para Usar no Builder

```
Endereço do Contrato: 0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
Rede: Sepolia Testnet
Contrato Verificado: Sim (Sourcify)
ABI: Disponível automaticamente (contrato verificado)
```

---

## 🔗 Links Úteis

- **OpenZeppelin Builder:** https://builder.openzeppelin.com/
- **Documentação:** https://docs.openzeppelin.com/contracts-ui-builder/1.0.x/
- **OpenZeppelin Wizard:** https://wizard.openzeppelin.com/ (para criar contratos)

---

## ✅ Resumo

### **OpenZeppelin Builder é para:**
- ✅ Criar interface web para seu contrato
- ✅ Gerar código React
- ✅ Criar formulários de interação

### **NÃO é para:**
- ❌ Atualizar metadados de token
- ❌ Atualizar informações no Etherscan
- ❌ Gerenciar logo/nome do token

### **Para atualizar metadados:**
- ✅ Use **Etherscan** (quando login voltar)
- ✅ Use **DeBank** (detecta automaticamente)
- ✅ Use **MetaMask** (adicionar token manualmente)

---

## 💡 Recomendação

**Se você quer:**

1. **Atualizar informações do token:** Foque no Etherscan
2. **Criar interface web para usuários:** Use o OpenZeppelin Builder
3. **Melhor dos dois mundos:** Faça ambos! 😊

---

**Conclusão:** OpenZeppelin Builder é uma ferramenta útil para criar interfaces, mas não substitui atualizar metadados no Etherscan ou outras plataformas! 🚀

