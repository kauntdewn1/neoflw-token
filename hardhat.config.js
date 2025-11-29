// hardhat.config.js
// Configuração mínima do Hardhat APENAS para verificação no OKLink
// NOTA: Este projeto usa Ape Framework para deploy. Hardhat é usado apenas para verificação.

require("@nomicfoundation/hardhat-toolbox");
require("@okxweb3/hardhat-explorer-verify");
require("dotenv").config();

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: {
    version: "0.8.18", // Mesma versão usada no Ape Framework (ape-config.yaml)
    settings: {
      optimizer: {
        enabled: true,
        runs: 200 // Ajustar conforme configuração do Ape se necessário
      }
    }
  },
  
  networks: {
    polygon: {
      url: process.env.ALCHEMY_API_KEY 
        ? `https://polygon-mainnet.g.alchemy.com/v2/${process.env.ALCHEMY_API_KEY}`
        : "https://polygon-rpc.com",
      chainId: 137,
      accounts: process.env.PRIVATE_KEY ? [process.env.PRIVATE_KEY] : [],
    },
  },
  
  // Configuração do OKLink Explorer
  okxweb3explorer: {
    customChains: [
      {
        network: "Polygon Mainnet",
        chainId: 137,
        urls: {
          apiURL: "https://www.oklink.com/api/v5/explorer/contract/verify-source-code-plugin/POLYGON",
          browserURL: "https://www.oklink.com",
        }
      }
    ]
  },
  
  // Configuração alternativa usando etherscan (Method 2)
  etherscan: {
    customChains: [
      {
        network: "polygon",
        chainId: 137,
        urls: {
          apiURL: "https://www.oklink.com/api/v5/explorer/contract/verify-source-code-plugin/POLYGON",
          browserURL: "https://www.oklink.com",
        }
      }
    ]
  }
};

