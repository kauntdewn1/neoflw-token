# 🎁 BOX TOKEN - Binance Smart Chain (BSC)

> Gerenciamento e documentação do token BOX na BSCScan Mainnet

---

## 📋 Informações do Token

- **Endereço:** `0xBc972E10Df612C7d65054BC67aBCA96B3C22a017`
- **Rede:** Binance Smart Chain (BSC) Mainnet
- **Chain ID:** 56
- **Explorer:** https://bscscan.com
- **Token URL:** https://bscscan.com/token/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017

### 🖼️ Logo do Token

- **URL:** https://gateway.lighthouse.storage/ipfs/bafybeia34i4ey5a7hd7odmazmyts4m6dasnceqtqky5gozrqbqylevjg6e
- **CID:** `bafybeia34i4ey5a7hd7odmazmyts4m6dasnceqtqky5gozrqbqylevjg6e`
- **Gateway:** Lighthouse Storage
- **📄 Detalhes:** Veja [`AVATAR_INFO.md`](./AVATAR_INFO.md)

---

## 🚀 Próximos Passos

Este projeto replica o processo feito com o token NEOFLW na testnet, mas agora para o token BOX na BSC mainnet.

### ✅ Checklist de Tarefas

1. **Verificação do Contrato** 🔍
   - [ ] Verificar contrato no BSCScan
   - [ ] Verificar no Sourcify (se suportado)
   - [ ] Documentar processo de verificação

2. **Atualização de Metadados** 📝
   - [ ] Obter/criar logo do token
   - [ ] Fazer upload do logo para IPFS
   - [ ] Atualizar informações no BSCScan
   - [ ] Preencher nome, símbolo, descrição

3. **Integração com Plataformas** 🔗
   - [ ] Adicionar no GeckoTerminal (se aplicável)
   - [ ] Atualizar informações em wallets
   - [ ] Configurar para DEXs (PancakeSwap, etc)

---

## 📁 Estrutura do Projeto

```
BOX-TOKEN/
├── README.md                    # Este arquivo
├── docs/                        # Documentação
│   ├── verification/           # Guias de verificação
│   ├── token-info/             # Guias de atualização de metadados
│   └── setup/                  # Guias de configuração
├── scripts/                    # Scripts de automação
│   ├── verify_contract.py     # Verificação de contrato
│   └── update_metadata.py     # Atualização de metadados
└── metadata/                   # Metadados do token
    └── token-metadata.json    # JSON com informações do token
```

---

## 🔧 Configuração

### Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto ou use o `.env` existente:

```env
# BSCScan API (obtenha em https://bscscan.com/myapikey)
BSCSCAN_API_KEY=your_bscscan_api_key_here

# Token Address
BOX_TOKEN_ADDRESS=0xBc972E10Df612C7d65054BC67aBCA96B3C22a017

# Network
BSC_NETWORK=bsc:mainnet
BSC_RPC_URL=https://bsc-dataseed.binance.org/
```

---

## 📖 Documentação

### Verificação do Contrato

- **⭐ SEM JSON? Comece Aqui:** [`VERIFICAR_SEM_JSON.md`](./VERIFICAR_SEM_JSON.md) 🚀
- **Guia Completo Sem JSON:** [`docs/verification/SEM_JSON_VERIFICAR.md`](./docs/verification/SEM_JSON_VERIFICAR.md)
- **Sourcify (Recomendado):** [`docs/verification/SOURCIFY_PASSO_A_PASSO_BSC.md`](./docs/verification/SOURCIFY_PASSO_A_PASSO_BSC.md)
- **Sourcify (Geral):** [`docs/verification/SOURCIFY_BSC.md`](./docs/verification/SOURCIFY_BSC.md)
- **BSCScan (Manual):** [`docs/verification/VERIFICAR_BSCSCAN.md`](./docs/verification/VERIFICAR_BSCSCAN.md)

**⚠️ Nota sobre APIs:** BSCScan APIs foram depreciadas e substituídas pela Etherscan API V2. O Sourcify é uma excelente alternativa que não depende de APIs.

**💡 Não tem JSON?** Use o método "Single File" no BSCScan ou Sourcify com arquivos `.sol` - muito mais simples!

### Atualização de Metadados

- **Como Atualizar Logo:** [`docs/token-info/ATUALIZAR_LOGO_BSCSCAN.md`](./docs/token-info/ATUALIZAR_LOGO_BSCSCAN.md)
- **Informações do Token:** [`docs/token-info/COMO_PREENCHER_TOKEN_INFO.md`](./docs/token-info/COMO_PREENCHER_TOKEN_INFO.md)

### Setup

- **Configurar BSC na MetaMask:** [`docs/setup/METAMASK_BSC.md`](./docs/setup/METAMASK_BSC.md)
- **Obter BSCScan API Key:** [`docs/setup/BSCSCAN_API_SETUP.md`](./docs/setup/BSCSCAN_API_SETUP.md)

---

## 🛠️ Scripts Disponíveis

### Verificar Contrato

```bash
python scripts/verify_contract.py
```

### Atualizar Metadados

```bash
python scripts/update_metadata.py
```

---

## 🔗 Links Úteis

- **Token no BSCScan:** https://bscscan.com/token/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017
- **BSCScan Explorer:** https://bscscan.com
- **BSCScan API Docs:** https://docs.bscscan.com/
- **BSC RPC Endpoints:** https://docs.binance.org/smart-chain/developer/rpc.html

---

## 📝 Notas

- Este projeto é baseado na estrutura do token NEOFLW
- Adaptações foram feitas para BSCScan (ao invés de Etherscan)
- Processos são similares, mas URLs e APIs são diferentes
- BSC usa BNB como gas, não ETH

---

## 🔖 Autoria

Estrutura baseada no projeto **NEOFLW Token** - adaptada para **BOX TOKEN** na BSC Mainnet.

