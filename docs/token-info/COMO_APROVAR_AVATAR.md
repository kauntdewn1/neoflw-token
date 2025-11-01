# 🖼️ Como Aprovar a Imagem de Avatar do Token no Etherscan

## 🌐 Rede: Ethereum Sepolia (Testnet)

**⚠️ IMPORTANTE:** Este token está deployado na **Sepolia Testnet**, não na mainnet.

- **Rede:** Ethereum Sepolia (Testnet)
- **Explorer:** https://sepolia.etherscan.io
- **Chain ID:** 11155111
- **Token Address:** `0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87`

---

## ⚠️ Ape Framework, Remix e Sourcify NÃO Aprovam Imagens

### **Limitação do Etherscan (Testnet e Mainnet):**

Mesmo usando **Ape Framework** (`APE_NETWORK=ethereum:sepolia`), você **ainda precisa fazer manualmente** porque:

- ❌ **Ape Framework** e **ape-etherscan** só verificam código de contratos
- ❌ **Remix** e **Sourcify** só verificam código de contratos
- ❌ **Etherscan NÃO possui API pública** para atualizar logo/avatar de tokens
  - ⚠️ **Isso vale tanto para Sepolia Testnet quanto para Mainnet**
  - ⚠️ **Não é porque é testnet** - é uma limitação geral do Etherscan
- ✅ **A única forma** é através da interface web do Etherscan (manual)

**Isso é uma limitação do próprio Etherscan**, não das ferramentas ou da rede!

### **O que Ape Framework faz:**

✅ **Verificar código do contrato** via `ape etherscan verify`
✅ **Deploy de contratos**
✅ **Interagir com contratos** via `ape console`
❌ **NÃO atualiza logo/avatar** (não existe essa funcionalidade na API)

---

## 🎯 Resposta Direta

**Pergunta:** "Mesmo usando Ape Framework (`APE_NETWORK`), ainda preciso fazer manualmente? É porque é Sepolia Testnet?"

**Resposta:** **SIM, precisa fazer manualmente!** Mas **NÃO é porque é testnet**:

- ❌ A limitação existe **tanto em Sepolia quanto em Mainnet**
- ❌ O Etherscan **não oferece API** para atualizar logo em nenhuma rede
- ✅ O processo manual é **idêntico** em testnet e mainnet
- ✅ A diferença é apenas a URL: `sepolia.etherscan.io` vs `etherscan.io`

---

**Para aprovar o avatar, você precisa usar o Etherscan Sepolia diretamente:**
```
https://sepolia.etherscan.io/token/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
```

---

## 🎯 Método Mais Direto: Passo a Passo Detalhado

**📖 Para um guia passo a passo completo com screenshots e troubleshooting detalhado, veja:**
**[`PASSO_A_PASSO_ATUALIZAR_IMAGEM.md`](./PASSO_A_PASSO_ATUALIZAR_IMAGEM.md)**

---

## ✅ Método 1: Script Semi-Automatizado (Recomendado)

### **Executar o Script:**

```bash
python scripts/update_token_automated.py
```

**O script detecta automaticamente a rede do `APE_NETWORK`:**
- Se `APE_NETWORK=ethereum:sepolia` → usa Sepolia Etherscan
- Se `APE_NETWORK=ethereum:mainnet` → usa Mainnet Etherscan

**O script:**

- ✅ Detecta a rede automaticamente (usando `APE_NETWORK`)
- ✅ Abre o navegador automaticamente
- ✅ Navega para a página do token correto
- ✅ Tenta preencher os campos automaticamente
- ⚠️ Você ainda precisa fazer login e confirmar (não há como automatizar login)

**Requisitos:**
```bash

pip install playwright
playwright install chromium
```

**Nota:** O script **ajuda**, mas ainda requer interação manual (login e confirmação) porque o Etherscan não permite automação completa sem credenciais privadas.

---

## ✅ Método 2: Atualização Manual no Etherscan

### **Passo a Passo Detalhado:**

#### **1. Acesse a Página do Token (NÃO do Contrato)**

**URL:**
```
https://sepolia.etherscan.io/token/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
```

⚠️ **Importante:** Use `/token/` e não `/address/`

#### **2. Faça Login no Etherscan**

- **Clique em:** "Connect to Web3" ou "Login" (canto superior direito)
- **Conecte sua wallet** (MetaMask, WalletConnect, etc)
- **Use a mesma wallet** que fez o deploy do contrato
- **Certifique-se** de estar na rede **Sepolia Testnet**

#### **3. Encontre o Botão de Atualização**

**Procure por um destes botões/links:**

- ✅ "Update Token Info"
- ✅ "Edit Token Info" 
- ✅ "Update" (ao lado do nome do token)
- ✅ Ícone de lápis ✏️ ou edição
- ✅ "More Info" → "Update Token Info"
- ✅ Menu "⋮" (três pontos) → "Update Token"

**Onde procurar:**

- **No topo da página** (próximo ao nome do token)
- **No final da página** (seção "Other Info")
- **No menu lateral** (se disponível)

#### **4. Se Não Encontrar o Botão:**

**Possíveis motivos:**

- ⚠️ Você precisa fazer login primeiro
- ⚠️ O serviço de login está temporariamente indisponível
- ⚠️ A interface mudou

**Soluções:**

- ✅ Tente fazer login primeiro
- ✅ Aguarde algumas horas se o login estiver indisponível
- ✅ Limpe o cache do navegador
- ✅ Tente outro navegador ou modo anônimo
- ✅ Verifique se está na rede correta (Sepolia)

#### **5. Preencha o Formulário**

Quando encontrar o formulário, preencha com:

**Token Logo (URL):**
```
https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i
```

**Token Name:**
```
NeoFlowOFF
```

**Token Symbol:**
```
NEOFLW
```

**Decimals:**
```
18
```

**Website (opcional):**
```
neoflowoff.eth
```

**Description (opcional):**
```
Token oficial do protocolo NEOFLW - um protocolo modular DAO focado em governança descentralizada e crescimento sustentável.
```

#### **6. Confirme e Envie**

- ✅ Verifique se todos os campos estão corretos
- ✅ Clique em "Submit" ou "Enviar"
- ✅ Confirme a transação na sua wallet
- ⚠️ **Não há custo de gas** para atualizar informações

#### **7. Aguarde a Aprovação**

- ⏳ Pode levar **alguns minutos** para aparecer
- ⏳ Atualize a página após alguns minutos
- ⏳ O logo deve aparecer no topo da página do token

---

## ✅ Método 3: Via My Account (Alternativa)

### **Se não encontrar na página do token:**

1. **Acesse My Account:**
   ```
   https://sepolia.etherscan.io/myaccount
   ```

2. **Faça login** (se ainda não fez)

3. **Procure por:**
   - "Token Management"
   - "My Tokens"
   - "Update Token Info"

4. **Selecione seu token** e atualize as informações

---

## ✅ Método 4: Script que Abre Direto na Página

```bash
python scripts/update_token_automated.py
```

**Escolha opção 3** (abrir página do token) para copiar as informações manualmente.

---

## 📋 Informações Completas do Token (para Copiar)

```
Endereço do Token: 0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
Rede: Ethereum Sepolia (Testnet)
Nome: NeoFlowOFF
Símbolo: NEOFLW
Decimals: 18

Logo URL:
https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i

Website: neoflowoff.eth

Descrição:
Token oficial do protocolo NEOFLW - um protocolo modular DAO focado em governança descentralizada e crescimento sustentável.
```

---

## ⚠️ Problemas Comuns e Soluções

### **1. "Account Login service is temporarily unavailable"**

**Solução:**

- ✅ Aguarde algumas horas
- ✅ Tente limpar cache do navegador
- ✅ Use outro navegador
- ✅ Tente modo anônimo
- ✅ Verifique se está na rede correta

### **2. Botão "Update Token Info" não aparece**

**Solução:**
- ✅ Certifique-se de estar **logado**
- ✅ Use a **mesma wallet** que fez o deploy
- ✅ Verifique se está na **página do token** (`/token/`) e não do contrato (`/address/`)
- ✅ Role a página até o final
- ✅ Procure no menu "More" ou "⋮"

### **3. Logo não aparece após atualizar**

**Solução:**
- ✅ Aguarde alguns minutos (pode demorar)
- ✅ Limpe o cache do navegador (Ctrl+Shift+R ou Cmd+Shift+R)
- ✅ Verifique se a URL do logo está acessível (abra no navegador)
- ✅ Certifique-se de que a URL começa com `https://`

### **4. Erro ao confirmar transação**

**Solução:**
- ✅ Verifique se sua wallet está conectada corretamente
- ✅ Verifique se está na rede Sepolia
- ✅ Tente desconectar e reconectar a wallet
- ⚠️ Lembre-se: **não deve haver custo de gas** para atualizar informações

---

## 🔗 Links Úteis

- **Página do Token:** https://sepolia.etherscan.io/token/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
- **My Account:** https://sepolia.etherscan.io/myaccount
- **Logo IPFS:** https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i
- **Contrato Verificado:** https://repo.sourcify.dev/11155111/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87

---

## ✅ Checklist Rápido

- [ ] Acessei a página do token (não do contrato)
- [ ] Fiz login no Etherscan (conectei minha wallet)
- [ ] Encontrei o botão "Update Token Info"
- [ ] Preenchi o campo "Token Logo" com a URL IPFS
- [ ] Preenchi os outros campos (nome, símbolo, decimals)
- [ ] Cliquei em "Submit" ou "Enviar"
- [ ] Confirmei na minha wallet (se solicitado)
- [ ] Aguardei alguns minutos
- [ ] Atualizei a página e verifiquei se o logo apareceu

---

## 💡 Dica Final

**O Remix/Sourcify são apenas para verificação de código.**

**Para aprovar avatar/logo, você DEVE usar o Etherscan diretamente:**

1. ✅ Login no Etherscan
2. ✅ Acessar página do token
3. ✅ Clicar em "Update Token Info"
4. ✅ Preencher URL do logo
5. ✅ Confirmar

**Não há atalho - precisa ser feito manualmente no Etherscan!**

---

## 🎯 Resumo Executivo

| Ferramenta | Serve Para | Não Serve Para |
|------------|------------|----------------|
| **Ape Framework** | ✅ Verificar código via `ape etherscan verify` | ❌ Aprovar imagens (não há API) |
| **Remix/Sourcify** | ✅ Verificar código do contrato | ❌ Aprovar imagens |
| **Etherscan API** | ✅ Ler informações | ❌ Atualizar logo (não existe endpoint) |
| **Etherscan Web** | ✅ Aprovar logo/avatar (manual) | ❌ Verificar código (já está verificado) |

### **Por que não há automação completa?**

1. ❌ **Etherscan não oferece API pública** para atualizar logo
   - ⚠️ **Vale para Sepolia E Mainnet** - não é porque é testnet!
2. ❌ **Requer autenticação Web3** (conectar wallet)
3. ❌ **Requer confirmação manual** (segurança)

### **⚠️ É porque é Sepolia Testnet?**

**NÃO!** A limitação é a mesma em todas as redes:
- ✅ **Sepolia Testnet:** Processo manual
- ✅ **Ethereum Mainnet:** Processo manual (idêntico)
- ✅ **Outras redes:** Todas requerem processo manual

**Única diferença entre Sepolia e Mainnet:**
- URL: `sepolia.etherscan.io` vs `etherscan.io`
- Processo: **Exatamente o mesmo**

**Solução:** Use Etherscan Web → Login → Update Token Info → Preencher logo URL → Confirmar

**O Ape Framework ajuda detectando a rede automaticamente, mas o processo ainda é manual em qualquer rede.**

---

## 🎨 Alternativas para Visualização do Logo (Quando Etherscan não Funciona)

### **Por que usar alternativas?**

- ✅ **Testes visuais** durante desenvolvimento
- ✅ **Visualização completa** mesmo sem aprovação no Etherscan
- ✅ **Branding consistente** em todas as interfaces
- ✅ **Funciona para testnets** sem limitações

---

## ✅ Alternativa 1: Blockscout (Explorer Open-Source)

### **O que é Blockscout?**

**Blockscout** é um explorer blockchain open-source que suporta tokens customizados com logo e metadados, mesmo em testnets.

### **Como usar:**

#### **Opção A: Blockscout Público (Sepolia)**

1. **Acesse um instance público do Blockscout:**
   ```
   https://sepolia-blockscout.com/
   ```
   ou
   ```
   https://explorer.sepolia.dev/
   ```

2. **Busque seu token:**
   - Digite: `0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87`

3. **Visualize o token:**
   - O Blockscout geralmente mostra metadados automaticamente
   - Se não aparecer, pode adicionar via interface

#### **Opção B: Deploy Local do Blockscout**

**Prós:**
- ✅ Controle total sobre visualização
- ✅ Suporte completo a tokens custom
- ✅ Testes visuais ilimitados

**Contras:**
- ⚠️ Requer infraestrutura (Docker/Kubernetes)
- ⚠️ Configuração mais complexa

**Passos básicos:**
```bash
# Clone o repositório
git clone https://github.com/blockscout/blockscout
cd blockscout

# Configure para Sepolia
# Edite docker-compose.yml para usar Sepolia RPC

# Inicie com Docker
docker-compose up

# Acesse: http://localhost:4000
```

**Links:**
- GitHub: https://github.com/blockscout/blockscout
- Docs: https://docs.blockscout.com/

---

## ✅ Alternativa 2: Fork Local do Etherscan UI

### **O que é?**

Existem forks open-source da interface do Etherscan que você pode rodar localmente para testes visuais.

### **Repositórios Disponíveis:**

1. **Etherscan-like UI (Comunidade):**
   - Busque por "etherscan ui fork" no GitHub
   - Alguns projetos mantêm forks atualizados

2. **Ethplorer Open-Source:**
   - Interface similar ao Etherscan
   - GitHub: https://github.com/EverexIO/Ethplorer

### **Como usar:**

```bash
# Exemplo genérico (ajuste conforme o repositório)
git clone <repositorio-etherscan-ui>
cd etherscan-ui

# Instale dependências
npm install

# Configure para Sepolia
# Edite .env com:
# REACT_APP_NETWORK=sepolia
# REACT_APP_RPC_URL=https://sepolia.infura.io/...

# Execute
npm start

# Acesse: http://localhost:3000
```

**⚠️ Nota:** Verifique a licença antes de usar forks.

---

## ✅ Alternativa 3: IPFS + Metadados JSON (Já Configurado!)

### **Status Atual:**

✅ **Logo já está no IPFS via Lighthouse:**
```
https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i
```

✅ **Metadados JSON disponíveis:**
```json
{
  "name": "NeoFlowOFF",
  "symbol": "NEOFLW",
  "image": "https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i",
  "logo": "https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i"
}
```

### **Como usar:**

1. **Wallets (MetaMask, etc):**
   - Adicione o token manualmente
   - Use a URL IPFS do logo
   - O logo aparecerá na carteira

2. **DApps e Interfaces:**
   - Consulte o metadata JSON
   - Use a URL IPFS do logo diretamente
   - Funciona em qualquer interface que suporte IPFS

3. **Gateways IPFS Disponíveis:**
   ```
   - Lighthouse: https://gateway.lighthouse.storage/ipfs/...
   - IPFS.io: https://ipfs.io/ipfs/...
   - Cloudflare: https://cloudflare-ipfs.com/ipfs/...
   - Pinata: https://gateway.pinata.cloud/ipfs/...
   ```

### **Visualização Completa:**

Mesmo sem aprovação no Etherscan, você pode:

- ✅ **Ver o logo em wallets** (adicionando manualmente)
- ✅ **Usar em DApps** (usando URL IPFS)
- ✅ **Visualizar em Blockscout** (se disponível)
- ✅ **Usar em interfaces custom** (usando metadados JSON)

---

## 📊 Comparação das Alternativas

| Alternativa | Complexidade | Controle | Funciona em Testnet | Melhor Para |
|-------------|-------------|----------|---------------------|-------------|
| **Etherscan Manual** | ⭐ Fácil | ⭐⭐ Médio | ⚠️ Limitado | Produção |
| **Blockscout Público** | ⭐ Muito Fácil | ⭐ Baixo | ✅ Sim | Visualização rápida |
| **Blockscout Local** | ⭐⭐⭐ Difícil | ⭐⭐⭐ Total | ✅ Sim | Desenvolvimento |
| **Fork Etherscan UI** | ⭐⭐ Médio | ⭐⭐⭐ Total | ✅ Sim | Testes visuais |
| **IPFS + Metadados** | ⭐ Muito Fácil | ⭐⭐ Médio | ✅ Sim | Wallets/DApps |

---

## 💡 Recomendação

### **Para Desenvolvimento/Testes:**

1. **Use Blockscout público** para visualização rápida
2. **Use IPFS diretamente** em wallets e DApps
3. **Consulte `metadata/token-metadata.json`** para metadados completos

### **Para Produção:**

1. **Tente Etherscan manual** primeiro (padrão da indústria)
2. **Use Blockscout como backup** se Etherscan não funcionar
3. **Mantenha IPFS atualizado** (já está configurado ✅)

---

## 🔗 Links Úteis

- **Logo IPFS:** https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i
- **Metadados:** `metadata/token-metadata.json`
- **Blockscout:** https://github.com/blockscout/blockscout
- **Lighthouse Storage:** https://lighthouse.storage/
- **Token no Etherscan Sepolia:** https://sepolia.etherscan.io/token/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87

---

**Pronto!** Agora você tem várias alternativas para visualizar o logo! 🚀

