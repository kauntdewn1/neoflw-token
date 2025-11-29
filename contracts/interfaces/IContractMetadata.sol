// SPDX-License-Identifier: Apache-2.0
pragma solidity ^0.8.18;

/**
 * @dev Interface mínima de metadata de contrato compatível com thirdweb.
 * Mantém a mesma assinatura usada em `ContractMetadata.sol`.
 */
interface IContractMetadata {
    /// @notice Retorna a URI de metadata do contrato.
    function contractURI() external view returns (string memory);

    /**
     * @notice Define a URI de metadata do contrato.
     * @param _uri Nova URI.
     */
    function setContractURI(string memory _uri) external;

    /// @dev Emitido quando a URI de metadata do contrato é atualizada.
    event ContractURIUpdated(string prevURI, string newURI);
}


