# ⚡ Resumo Rápido - Frontend NEOFLW Token

## 🔑 Constantes Principais

```javascript
const TOKEN = {
  address: "0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87",
  name: "NeoFlowOFF",
  symbol: "NEOFLW",
  decimals: 18,
  chainId: 11155111, // Sepolia
  logoCid: "bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i"
};
```

## 🖼️ URL do Logo (com Fallbacks)

```javascript
// Gateway principal (recomendado)
const LOGO_URL = "https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i";

// Fallbacks (se o primeiro falhar)
const FALLBACK_GATEWAYS = [
  "https://ipfs.io/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i",
  "https://cloudflare-ipfs.com/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i",
  "/images/avatar_neoflow.png" // Local fallback
];
```

## 📄 Metadados

```javascript
// Carregar de arquivo local
const metadata = await fetch('/metadata/token-metadata.json').then(r => r.json());

// Ou usar diretamente:
const metadata = {
  name: "NeoFlowOFF",
  symbol: "NEOFLW",
  decimals: 18,
  image: "https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i",
  description: "Token oficial do protocolo NEOFLW..."
};
```

## ⚛️ React - Exemplo Mínimo

```jsx
import { useState } from 'react';

function TokenLogo() {
  const [src, setSrc] = useState("https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i");

  return (
    <img
      src={src}
      alt="NEOFLW Logo"
      onError={() => setSrc("https://ipfs.io/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i")}
    />
  );
}
```

## 🔗 Links Importantes

- **Explorer:** https://sepolia.etherscan.io/token/0x5AaCebca3f0CD9283401a83bC7BA5db48011CE87
- **Logo IPFS:** https://gateway.lighthouse.storage/ipfs/bafkreiboigewtuwih7cfnxppte64l3zkktrb52serzloa4vqfrw5f3zh3i
- **Metadados:** `metadata/token-metadata.json`

## ⚠️ Pontos Críticos

1. ✅ **Sempre use fallback** para logo (gateways podem falhar)
2. ✅ **Cache metadados** (localStorage ou memória)
3. ✅ **Tratamento de erros** em todas as requisições
4. ✅ **Loading states** para melhor UX
5. ✅ **Teste offline** (com fallbacks locais)

## 📚 Documentação Completa

Veja o guia completo em: [`GUIA_DESENVOLVIMENTO_FRONTEND.md`](./GUIA_DESENVOLVIMENTO_FRONTEND.md)

