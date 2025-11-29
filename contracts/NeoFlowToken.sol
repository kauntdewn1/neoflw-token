// contracts/NeoFlowToken.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "./ContractMetadata.sol";

contract NeoFlowToken is ERC20, Ownable, ContractMetadata {
    event Burned(address indexed account, uint256 amount);

    constructor(uint256 initialSupply) ERC20("NEOFlowOFF", "NEOFLW") {
        _mint(msg.sender, initialSupply);
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
}

