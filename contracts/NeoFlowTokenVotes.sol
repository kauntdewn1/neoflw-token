// contracts/NeoFlowTokenVotes.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Votes.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title NeoFlowTokenVotes
 * @notice Versão do token NEOFLW com suporte a votação (snapshot-based voting)
 * @dev Herda de ERC20Votes para permitir governança DAO
 */
contract NeoFlowTokenVotes is ERC20Votes, Ownable {
    event Burned(address indexed account, uint256 amount);

    constructor(uint256 initialSupply) ERC20Votes("NEOFlowOFF", "NEOFLW") {
        _mint(msg.sender, initialSupply);
        _delegate(msg.sender, msg.sender); // Delegate inicial para o deployer
    }

    function burn(uint256 amount) public {
        require(amount > 0, "Amount must be greater than 0");
        _burn(msg.sender, amount);
        emit Burned(msg.sender, amount);
    }

    // Nota: ERC20Votes já gerencia automaticamente o voting power
    // através do hook _afterTokenTransfer. Não é necessário sobrescrever
    // transfer() e transferFrom() - eles funcionam corretamente por padrão.
}

