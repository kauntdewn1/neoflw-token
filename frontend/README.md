# NEOFLW Frontend

WebApp para interação com o protocolo NEOFLW.

## 🚀 Setup

```bash
# Instalar dependências
npm install

# Copiar variáveis de ambiente
cp .env.example .env
# Editar .env com os endereços dos contratos

# Desenvolver (porta 3002 para evitar conflito)
npm run dev
# Acessar: http://localhost:3002

# Build
npm run build

# Produção
npm start
```

## 📁 Estrutura

```
frontend/
├── src/
│   ├── app/           # Next.js App Router
│   ├── components/    # Componentes React
│   ├── hooks/         # Hooks Wagmi/Viem
│   └── config/        # Configurações
├── public/           # Arquivos estáticos
└── package.json
```

## 🔧 Configuração

Edite `.env` com os endereços dos contratos após deploy:

```env
NEXT_PUBLIC_TOKEN_ADDRESS=0x...
NEXT_PUBLIC_VAULT_ADDRESS=0x...
NEXT_PUBLIC_CLAIM_ADDRESS=0x...
NEXT_PUBLIC_GOVERNOR_ADDRESS=0x...
```

## 🎯 Funcionalidades

- ✅ Balance do token
- ✅ Queimar tokens
- ✅ Staking (lock 6 meses, 10% reward)
- ✅ Claim de tokens elegíveis
- ✅ Integração com MetaMask/WalletConnect

## 📚 Hooks Disponíveis

- `useNeoflow()` - Token balance, burn
- `useStakingVault()` - Stake, claim, aprovação
- `useClaim()` - Claim de tokens

