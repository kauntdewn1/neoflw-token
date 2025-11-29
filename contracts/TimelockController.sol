// contracts/TimelockController.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

import { TimelockController as OZTimelockController } from "@openzeppelin/contracts/governance/TimelockController.sol";

/**
 * @title NeoFlowTimelockController
 * @notice Wrapper local para expor o TimelockController da OpenZeppelin ao Ape Framework,
 *         evitando conflito de nome com o contrato da dependência.
 * @dev Necessário porque o Ape só enxerga contratos declarados neste projeto.
 */
contract NeoFlowTimelockController is OZTimelockController {
    constructor(
        uint256 minDelay,
        address[] memory proposers,
        address[] memory executors,
        address admin
    ) OZTimelockController(minDelay, proposers, executors, admin) {}
}


