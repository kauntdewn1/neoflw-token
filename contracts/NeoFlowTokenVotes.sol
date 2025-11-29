// contracts/NeoFlowTokenVotes.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Permit.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Votes.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "./ContractMetadata.sol";

/**
 * @title NeoFlowTokenVotes
 * @notice Versão do token NEOFLW com suporte a votação (snapshot-based voting)
 * @dev Herda de ERC20 + ERC20Permit + ERC20Votes para permitir governança DAO
 */
contract NeoFlowTokenVotes is ERC20, ERC20Permit, ERC20Votes, Ownable, ContractMetadata {
    event Burned(address indexed account, uint256 amount);

    constructor(uint256 initialSupply)
        ERC20("NEOFlowOFF", "NEOFLW")
        ERC20Permit("NEOFlowOFF")
    {
        _mint(msg.sender, initialSupply);
        _delegate(msg.sender, msg.sender); // Delegate inicial para o deployer
    }

    function burn(uint256 amount) public {
        require(amount > 0, "Amount must be greater than 0");
        _burn(msg.sender, amount);
        emit Burned(msg.sender, amount);
    }

    /// @dev Returns whether contract metadata can be set in the given execution context.
    function _canSetContractURI() internal view override returns (bool) {
        return msg.sender == owner();
    }

    // ===== Overrides necessários para múltipla herança (ERC20 + ERC20Votes) =====

    function _afterTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override(ERC20, ERC20Votes) {
        super._afterTokenTransfer(from, to, amount);
    }

    function _mint(address to, uint256 amount)
        internal
        override(ERC20, ERC20Votes)
    {
        super._mint(to, amount);
    }

    function _burn(address account, uint256 amount)
        internal
        override(ERC20, ERC20Votes)
    {
        super._burn(account, amount);
    }
}


