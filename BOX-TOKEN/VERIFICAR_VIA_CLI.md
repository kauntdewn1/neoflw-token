# 🚀 Verificar Contrato via CLI (Terminal)

## ✅ Método Automatizado via Script Python

Agora você pode verificar o contrato **InterboxCoin** diretamente pelo terminal!

---

## 📋 Pré-requisitos

1. **API Key do Etherscan/BSCScan:**
   - Configure no `.env` ou variável de ambiente:
     ```bash
     export ETHERSCAN_API_KEY=sua_api_key_aqui
     ```
   - Ou adicione ao `.env` do projeto raiz:
     ```env
     ETHERSCAN_API_KEY=sua_api_key_aqui
     ```

2. **Python 3** instalado

3. **Bibliotecas Python:**
   ```bash
   pip install requests python-dotenv
   ```

---

## 🚀 Como Usar

### **Método 1: Executar o Script Direto**

```bash
cd BOX-TOKEN
python scripts/verify_contract_cli.py
```

### **Método 2: Com API Key Temporária**

```bash
export ETHERSCAN_API_KEY=sua_api_key_aqui
cd BOX-TOKEN
python scripts/verify_contract_cli.py
```

---

## 📊 O Que o Script Faz

1. ✅ Lê automaticamente o código fonte (`InterboxCoin_Flattened_Final.sol`)
2. ✅ Usa os constructor arguments corretos (já configurados)
3. ✅ Envia requisição de verificação via API V2
4. ✅ Monitora o status da verificação automaticamente
5. ✅ Mostra o resultado final

---

## ⚙️ Configurações do Script

O script já vem com as configurações corretas:

| Configuração | Valor |
|--------------|-------|
| **Contrato** | `0xBc972E10Df612C7d65054BC67aBCA96B3C22a017` |
| **Compiler** | `0.8.24+commit.e11b9ed9` |
| **EVM Version** | `default` |
| **Optimization** | `Yes`, Runs: `200` |
| **License** | `MIT` |
| **Constructor Args** | `00000000000000000000000000000000000000000000d3c21bcecceda100000000000000000000000000000045f9c5af31678bc1dacddf348936a6a6e4d42a53` |

---

## 📝 Exemplo de Execução

```bash
$ cd BOX-TOKEN
$ python scripts/verify_contract_cli.py

📄 Lendo código fonte...
   ✅ Código fonte lido (XXXX caracteres)

======================================================================
  🚀 Verificando Contrato via CLI - BSCScan API V2
======================================================================

📍 Contrato: 0xBc972E10Df612C7d65054BC67aBCA96B3C22a017
🌐 Rede: BSC Mainnet (Chain ID: 56)
📝 Compiler: 0.8.24+commit.e11b9ed9
⚙️  Optimization: Yes, Runs: 200

📤 Enviando requisição de verificação...
   ✅ Requisição enviada com sucesso!
   📋 GUID: [guid-aqui]

   ⏳ Aguardando processamento...
   (Isso pode levar alguns minutos)

   Tentativa 1/20: Pending in queue
   Tentativa 2/20: Pending in queue
   Tentativa 3/20: Pass - Verified
   
======================================================================
  ✅ CONTRATO VERIFICADO COM SUCESSO!
======================================================================

   🌐 Veja em: https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017#code
```

---

## ⚠️ Troubleshooting

### **Erro: API Key não encontrada**

**Solução:**
```bash
export ETHERSCAN_API_KEY=sua_api_key_aqui
```

Ou adicione ao `.env`:
```env
ETHERSCAN_API_KEY=sua_api_key_aqui
```

### **Erro: Arquivo não encontrado**

**Solução:**
Certifique-se de que o arquivo existe:
```bash
ls BOX-TOKEN/InterboxCoin_Flattened_Final.sol
```

### **Erro na API**

O script mostrará a mensagem de erro da API. Verifique:
- ✅ API Key válida
- ✅ Contrato ainda não verificado
- ✅ Parâmetros corretos (já configurados no script)

### **Timeout ou Aguardando Muito**

Se o script aguardar muito tempo:
- Pare o script (Ctrl+C)
- Verifique manualmente em: https://bscscan.com/address/0xBc972E10Df612C7d65054BC67aBCA96B3C22a017#code
- A verificação pode estar processando (normal levar alguns minutos)

---

## 🔧 Personalizar Configurações

Se precisar alterar alguma configuração, edite o script:

```python
# Em scripts/verify_contract_cli.py
COMPILER_VERSION = "0.8.24+commit.e11b9ed9"  # Altere aqui
EVERSION = "default"  # ou "london"
OPTIMIZATION = "1"  # "1" = Yes, "0" = No
OPTIMIZATION_RUNS = "200"
```

---

## ✅ Após Verificação

Depois que o contrato for verificado:

1. **Obter o ABI:**
   ```bash
   python scripts/get_contract_abi.py
   ```

2. **Atualizar logo do token:**
   - Veja: `docs/token-info/ATUALIZAR_LOGO_BSCSCAN.md`

---

## 📋 Comparação: CLI vs Manual

| Método | Vantagens |
|--------|-----------|
| **CLI (Script)** | ✅ Automático, rápido, repetível |
| **Manual (Web)** | ✅ Mais controle, vê formulário completo |

**Recomendação:** Use o CLI para agilizar! 🚀

---

**Pronto para usar! Execute o script e verifique automaticamente!** 🎉

