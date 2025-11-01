# 📝 Guia Completo: Preencher Formulário de Token Info no Blockscout

## 🎯 Objetivo

Preencher o formulário "Token info application form" no Blockscout Sepolia para atualizar as informações do token, incluindo o logo.

---

## 📋 Informações do Token (Para Referência)

```
Endereço: 0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
Nome: NeoFlowOFF
Símbolo: NEOFLW
Logo URL: https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i
Website: neoflowoff.eth
```

---

## 📝 Passo a Passo - Preencher Cada Campo

### **✅ Seção 1: Campos Já Pre-preenchidos (Verificar)**

Estes campos já devem estar preenchidos automaticamente:

1. **✅ Token name\***: `NeoFlowOFF (NEOFLW)`
   - **Verificação:** Confirme que está correto
   - **Ação:** Se estiver errado, corrija

2. **✅ Token contract address\***: `0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87`
   - **Verificação:** Confirme que é o endereço correto
   - **Ação:** Se estiver errado, corrija

---

### **📝 Seção 2: Requester Information (Você Precisa Preencher)**

#### **Campo 3: Requester name\***

**O que preencher:**
- Seu nome completo, nickname ou nome do projeto
- Exemplos: `João Silva`, `@seu_nickname`, `NeoFlow Team`, `NeoFlow Dev`

**⚠️ Privacidade:**
- Esta informação **pode ficar pública** no Blockscout
- Você **pode usar um nickname** se preferir manter privacidade
- Alguns usuários usam: nickname, nome do projeto, ou nome genérico

**Instruções:**
- Digite seu nome, nickname ou nome do projeto no campo
- Este é o nome da pessoa/entidade que está solicitando a atualização
- Se quiser privacidade: use nickname como `@seu_nickname` ou `NeoFlow Dev`

**Recomendações:**
- ✅ Se quer privacidade: use nickname ou nome do projeto
- ✅ Se não se importa: pode usar nome completo
- ✅ Exemplos de nicknames aceitos: `@neoflw_dev`, `NeoFlow Team`, `NEOFLW`

---

#### **Campo 4: Requester email\***

**O que preencher:**
- Seu email válido (pode ser genérico)
- Exemplo: `contato@neoflowoff.eth` ou `seu.email@exemplo.com`

**⚠️ Privacidade:**
- Esta informação **pode ficar pública** no Blockscout
- Você **pode usar um email genérico** do projeto ao invés de pessoal
- Recomendado usar email do projeto se disponível

**Instruções:**
- Digite um email válido que você verifica regularmente
- Este email será usado para comunicação sobre o token
- **⚠️ IMPORTANTE:** Use um email que você realmente verifica!
- **💡 Dica:** Se tem privacidade, use email do projeto ao invés de pessoal

**Recomendações de Privacidade:**

- ✅ **Melhor opção:** Email do projeto (ex: `contato@neoflowoff.eth`)
- ✅ **Alternativa:** Email genérico criado só para isso
- ⚠️ **Evite:** Email pessoal muito pessoal se você quer privacidade
- ✅ Exemplo seguro: `info@neoflowoff.eth` ou `token@neoflowoff.eth`

---

### **📝 Seção 3: Project Info (Informações do Projeto)**

#### **Campo 5: Project name**

**O que preencher:**
```
NeoFlowToken
```

**Instruções:**

- Digite o nome completo do projeto
- Use exatamente: `NeoFlowToken` (sem espaços extras)

---

#### **Campo 6: Project industry**

**O que preencher:**

- Clique na seta do dropdown (▼)
- Selecione a indústria que melhor descreve seu projeto

**Opções comuns:**

- `DeFi` - Se for protocolo DeFi
- `Gaming` - Se for relacionado a jogos
- `Utility` - Se for token de utilidade
- `Governance` - Se for token de governança
- `Other` - Se nenhuma das anteriores se aplicar

**Recomendação para NeoFlowToken:**

- Se for protocolo DAO/governança: **`Governance`**
- Se for DeFi: **`DeFi`**
- Se não tiver certeza: **`Other`**

---

#### **Campo 7: Official project email address\***

**O que preencher:**

- Email oficial do projeto
- Pode ser o mesmo do requester ou diferente
- Exemplo: `contato@neoflowoff.eth` ou `info@neoflowoff.eth`

**Instruções:**

- Se você tem um domínio, use: `info@seudominio.com`
- Se não tem, pode usar um email pessoal ou criar um específico
- **⚠️ IMPORTANTE:** Este campo é obrigatório (tem asterisco `*`)

**Sugestões:**

- Se você não tem email oficial do projeto: use o mesmo email do requester
- Ou crie um email temporário específico para o projeto

---

#### **Campo 8: Official project website\***

**⚠️ Se aparecer "URL incorrect":**

O Blockscout pode validar URLs de forma rigorosa. Tente estas opções:

**Opção 1: Com https:// para ENS (Tente primeiro):**
```
https://neoflowoff.eth
```
Alguns validadores aceitam ENS com `https://`

**Opção 2: Apenas o nome ENS (Se Opção 1 falhar):**
```
neoflowoff.eth
```

**Opção 3: Website temporário (Se nenhuma opção funcionar):**
```
https://example.com
```
Use um placeholder temporário se o Blockscout não aceitar ENS

**Opção 4: URL completa do ENS resolver (Mais técnico):**
Se você tem um resolver configurado, pode usar:
```
https://app.ens.domains/name/neoflowoff.eth
```

---

**Para website normal (se tiver):**
```
https://www.neoflowoff.com
https://neoflowoff.com
```
✅ Sempre precisa de `https://` para URLs normais

---

**Instruções detalhadas:**

1. **Primeiro, tente:** `https://neoflowoff.eth` (ENS com https)
2. **Se der erro:** Tente `neoflowoff.eth` (apenas ENS)
3. **Se ainda der erro:** Use placeholder `https://example.com` temporariamente
4. **Depois da aprovação:** Você pode solicitar atualização se necessário

**⚠️ IMPORTANTE:** Este campo é obrigatório (tem asterisco `*`)

**💡 Dica:** O Blockscout pode ter validação diferente - tente as opções acima na ordem até uma funcionar!

---

#### **Campo 9: Docs (Opcional, mas Recomendado)**

**O que preencher:**

**Opção 1: Se você tem repositório GitHub com docs:**
```
https://github.com/seu-usuario/neoflw-token/tree/main/docs
```
Substitua `seu-usuario` pelo seu usuário do GitHub

**Opção 2: Se você tem repositório GitHub geral:**
```
https://github.com/seu-usuario/neoflw-token
```
Link para o repositório principal

**Opção 3: Se você tem site de documentação:**
```
https://docs.neoflowoff.eth
https://docs.neoflowoff.com
```

**Opção 4: Se não tem nenhum (pode deixar vazio):**
- Deixe o campo em branco (não é obrigatório)
- Ou use: `https://github.com/neoflw` (se tiver organização GitHub)

**Instruções:**
- ✅ **Recomendado:** Link para documentação no GitHub (pasta `docs/`)
- ✅ **Alternativa:** Link para repositório GitHub principal
- ✅ **Opcional:** Site de docs dedicado
- ⚪ **Se não tiver:** Pode deixar vazio (não bloqueia o envio)

**Exemplo prático:**
- Se seu GitHub é `github.com/seuusuario`:
  ```
  https://github.com/seuusuario/neoflw-token/tree/main/docs
  ```

---

#### **Campo 10: Support URL or email**

**O que preencher:**
- URL do suporte ou email de suporte
- Exemplo de URL: `https://discord.gg/neoflow`
- Exemplo de email: `suporte@neoflowoff.eth`

**Instruções:**
- Se você tem Discord/Telegram: use o link
- Se você tem email de suporte: use o email
- Se não tem: pode deixar vazio (não é obrigatório)

**Sugestões:**
- Discord: `https://discord.gg/seu-servidor`
- Email: `suporte@neoflowoff.eth`
- Ou deixe vazio se não tiver

---

#### **Campo 11: Link to icon URL\* ⭐ (CAMPO MAIS IMPORTANTE)**

**Este é o campo do LOGO do token!**

**O que preencher:**
```
https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i
```

**Formato aceito:**
- ✅ SVG (recomendado): URL direta para arquivo SVG
- ✅ PNG 48x48: URL direta para arquivo PNG de 48x48 pixels
- ✅ Outros formatos de imagem

**Instruções detalhadas:**
1. **Cole esta URL exata:**
   ```
   https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i
   ```

2. **Verifique que a URL está correta:**
   - Deve começar com `https://`
   - Deve terminar com o hash IPFS correto
   - Não deve ter espaços ou caracteres extras

3. **Teste a URL antes de enviar:**
   - Copie a URL e cole no navegador
   - Deve carregar a imagem do logo
   - Se não carregar, verifique se está correta

**⚠️ IMPORTANTE:** Este campo é obrigatório (tem asterisco `*`)

**Alternativas (se o primeiro gateway falhar):**
```
https://ipfs.io/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i
https://cloudflare-ipfs.com/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i
```

---

#### **Campo 12: Project description\*** ⭐ (OBRIGATÓRIO)

**O que preencher:**
- Descrição completa e clara do projeto e token
- Explique o que é o token, para que serve, e o propósito do projeto

**Exemplo Recomendado (Baseado no metadata do token):**
```
Token oficial do protocolo NEOFLW - um protocolo modular DAO focado em governança descentralizada e crescimento sustentável. O NEOFLW token é utilizado para governança, staking e participação nas decisões da comunidade na rede Ethereum Sepolia (testnet).
```

**Exemplo Alternativo (Mais Detalhado):**
```
NeoFlowOFF (NEOFLW) é o token ERC-20 oficial do protocolo NeoFlow, um protocolo modular DAO focado em governança descentralizada e crescimento sustentável. O token NEOFLW é utilizado para governança da comunidade, staking, e participação nas decisões do protocolo. Este contrato está implantado na rede Ethereum Sepolia (testnet) para testes e desenvolvimento.
```

**Exemplo Simples (Se Quiser Mais Curto):**
```
NeoFlowOFF (NEOFLW) é o token ERC-20 oficial do protocolo NeoFlow, utilizado para governança, staking e funcionalidades do protocolo na rede Ethereum Sepolia (testnet).
```

**O que incluir na descrição:**
1. ✅ Nome completo do token: NeoFlowOFF (NEOFLW)
2. ✅ Tipo: ERC-20 token
3. ✅ Propósito: governança, staking, etc.
4. ✅ Contexto: protocolo DAO/modular
5. ✅ Rede: Ethereum Sepolia (testnet)

**Instruções:**
- ✅ Seja claro e descritivo (2-4 frases é ideal)
- ✅ Explique o propósito do token
- ✅ Mencione que é testnet (Sepolia)
- ✅ Use português ou inglês (o que preferir)
- ✅ Não seja muito longo (máximo 200-300 palavras)
- **⚠️ IMPORTANTE:** Este campo é obrigatório (tem asterisco `*`)

**💡 Dica:** Copie e cole um dos exemplos acima e ajuste se necessário!

---

## ✅ Checklist Final Antes de Enviar

Antes de clicar em "Submit" ou "Apply", verifique:

### **Campos Obrigatórios (com `*`):**
- [ ] ✅ Token name está correto
- [ ] ✅ Token contract address está correto
- [ ] ✅ Requester name preenchido
- [ ] ✅ Requester email preenchido (email válido que você verifica)
- [ ] ✅ Official project email address preenchido
- [ ] ✅ Official project website preenchido
- [ ] ✅ Link to icon URL preenchido com a URL correta do logo
- [ ] ✅ Project description preenchida

### **Campos Opcionais (mas recomendados):**
- [ ] ✅ Project name preenchido
- [ ] ✅ Project industry selecionado
- [ ] ✅ Docs URL preenchida (se tiver)
- [ ] ✅ Support URL or email preenchido (se tiver)

### **Verificações Adicionais:**
- [ ] ✅ URL do logo foi testada no navegador (carrega a imagem)
- [ ] ✅ Todos os emails estão corretos e você tem acesso
- [ ] ✅ Website URL está correta (se aplicável)
- [ ] ✅ Descrição está clara e completa

---

## 🚀 Depois de Preencher

1. **Revise todos os campos** uma última vez
2. **Procure o botão "Submit" ou "Apply"** (geralmente no final do formulário)
3. **Clique para enviar**
4. **Aguarde confirmação** - pode levar alguns minutos para processar
5. **Verifique seu email** - pode receber confirmação por email

---

## ✅ Após Enviar o Formulário

**📖 Guia Completo:** Veja [`DEPOIS_DE_ENVIAR_BLOCKSCOUT.md`](./DEPOIS_DE_ENVIAR_BLOCKSCOUT.md)

### **O Que Esperar:**

1. **Status Inicial:**
   - Status aparecerá como **"In progress"** na página "My verified addresses"
   - Endereço: `https://eth-sepolia.blockscout.com/account/verified-addresses`

2. **Tempo de Processamento:**
   - ⏰ Típico: 24-72 horas
   - ⏰ Sepolia (testnet): Geralmente mais rápido

3. **Após Aprovação:**
   - ✅ Logo aparecerá automaticamente na página do token
   - ✅ Status mudará para "Approved"
   - ✅ Todas as informações ficarão públicas

4. **Como Acompanhar:**
   - Verifique a página "My verified addresses" periodicamente
   - Verifique seu email para atualizações
   - Quando aprovado, verifique a página do token

---

## 📧 O Que Esperar Depois

### **Após Enviar:**
1. ✅ Você pode receber um email de confirmação
2. ✅ O Blockscout pode revisar a solicitação
3. ✅ Pode levar algumas horas ou dias para aprovar
4. ✅ Você será notificado quando estiver aprovado

### **Como Verificar Aprovação:**
1. Acesse a página do token:
   ```
   https://eth-sepolia.blockscout.com/address/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
   ```
2. Verifique se o logo aparece
3. Verifique se as informações estão atualizadas

---

## 🔒 Privacidade: O Que Fica Público?

### **⚠️ Informações Que Podem Ficar Públicas:**

1. **Requester name:**
   - ✅ **Pode ficar público** no Blockscout
   - ✅ **Pode usar nickname** se preferir privacidade
   - ✅ Aceita: nome completo, nickname, nome do projeto

2. **Requester email:**
   - ✅ **Pode ficar público** no Blockscout
   - ✅ **Recomendado:** usar email do projeto ao invés de pessoal
   - ✅ Exemplo: `info@neoflowoff.eth` ao invés de email pessoal

3. **Official project email address:**
   - ✅ **Provavelmente fica público** (é email oficial do projeto)
   - ✅ Já deve ser um email público/empresarial mesmo

4. **Official project website:**
   - ✅ **Fica público** (é informação do projeto)
   - ✅ Normal ser público

5. **Project description:**
   - ✅ **Fica público** (descrição do token)
   - ✅ Normal ser público

### **✅ Estratégias de Privacidade:**

**Se você quer manter privacidade:**

1. **Requester name:**
   - Use nickname: `@neoflw_dev`, `NeoFlow Dev`, `NEOFLW Team`
   - Ou nome genérico: `NeoFlow Contributor`

2. **Requester email:**
   - Use email do projeto: `info@neoflowoff.eth`, `contato@neoflowoff.eth`
   - Ou crie email temporário só para isso
   - Evite email pessoal muito pessoal

3. **Lembre-se:**
   - Informações do projeto (website, description) são normalmente públicas
   - Requester info pode ser minimizada mas ainda visível

---

## ⚠️ Dicas Importantes

### **1. URL do Logo:**
- ✅ Use sempre `https://` (não `http://`)
- ✅ Teste a URL antes de enviar
- ✅ Prefira SVG ou PNG 48x48 para melhor qualidade
- ✅ Gateway IPFS pode levar alguns segundos para carregar

### **2. Emails:**
- ✅ Use emails que você realmente verifica
- ✅ Verifique se os emails estão corretos (sem erros de digitação)
- ✅ Alguns campos podem aceitar o mesmo email

### **3. Website (⚠️ Se aparecer "URL incorrect"):**
- ⚠️ **Primeiro tente:** `https://neoflowoff.eth` (ENS com https)
- ⚠️ **Se falhar, tente:** `neoflowoff.eth` (apenas ENS)
- ⚠️ **Se ainda falhar:** Use `https://example.com` temporariamente
- ✅ Para URLs normais, sempre use `https://` completo
- ✅ O Blockscout pode ter validação rigorosa de URL

### **4. Descrição:**
- ✅ Seja claro e objetivo
- ✅ Mencione que é testnet (Sepolia)
- ✅ Explique o propósito do token
- ✅ Evite texto muito longo ou muito curto

---

## 🔗 Links Úteis

- **URL do Logo (Principal):**
  ```
  https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i
  ```

- **Página do Token no Blockscout:**
  ```
  https://eth-sepolia.blockscout.com/address/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
  ```

- **Metadados do Token:**
  ```
  metadata/token-metadata.json
  ```

---

## ✅ Valores Sugeridos para Copiar e Colar

### **Logo URL (Cole Este Valor Exato):**
```
https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i
```

### **Project Name:**
```
NeoFlowToken
```

### **Project Website - Tente nesta ordem se der "URL incorrect":**

**Opção 1 (Tente primeiro - ENS com https):**
```
https://neoflowoff.eth
```

**Opção 2 (Se Opção 1 falhar - apenas ENS):**
```
neoflowoff.eth
```

**Opção 3 (Se ainda falhar - placeholder temporário):**
```
https://example.com
```

**Se for website normal:**
```
https://www.neoflowoff.com
```

### **Docs (Opcional - pode deixar vazio ou usar GitHub):**
```
https://github.com/seu-usuario/neoflw-token/tree/main/docs
```
**Ou deixe vazio** se não tiver documentação pública

### **Project Description (OBRIGATÓRIO - Cole este texto):**
```
Token oficial do protocolo NEOFLW - um protocolo modular DAO focado em governança descentralizada e crescimento sustentável. O NEOFLW token é utilizado para governança, staking e participação nas decisões da comunidade na rede Ethereum Sepolia (testnet).
```

**Ou versão mais detalhada (se preferir):**
```
NeoFlowOFF (NEOFLW) é o token ERC-20 oficial do protocolo NeoFlow, um protocolo modular DAO focado em governança descentralizada e crescimento sustentável. O token NEOFLW é utilizado para governança da comunidade, staking, e participação nas decisões do protocolo. Este contrato está implantado na rede Ethereum Sepolia (testnet) para testes e desenvolvimento.
```

---

**Boa sorte preenchendo o formulário!** 🚀

**Lembre-se:** Preencha com cuidado, especialmente os campos obrigatórios (marcados com `*`) e teste a URL do logo antes de enviar!

