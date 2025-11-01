// contracts/NeoFlowClaim.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NeoFlowClaim is Ownable {
    IERC20 public tokenContract;
    
    // Whitelist de endereços elegíveis
    mapping(address => uint256) public claimableAmount;
    
    // Controle de claims realizados
    mapping(address => bool) public hasClaimed;
    
    constructor(IERC20 _tokenAddress) {
        require(address(_tokenAddress) != address(0), "Invalid token address");
        tokenContract = _tokenAddress;
    }
    
    // Função para carregar whitelist (apenas owner)
    function setWhitelist(
        address[] calldata _users, 
        uint256[] calldata _amounts
    ) external onlyOwner {
        require(_users.length == _amounts.length, "Arrays incompativeis");
        require(_users.length > 0, "Arrays vazios");
        
        for(uint256 i = 0; i < _users.length; i++) {
            require(_users[i] != address(0), "Endereco invalido");
            claimableAmount[_users[i]] = _amounts[i];
        }
        
        emit WhitelistUpdated(_users.length);
    }
    
    // Função para atualizar amount de um endereço específico
    function updateClaimableAmount(address _user, uint256 _amount) external onlyOwner {
        require(_user != address(0), "Endereco invalido");
        require(!hasClaimed[_user], "Usuario ja fez claim");
        claimableAmount[_user] = _amount;
        emit ClaimableAmountUpdated(_user, _amount);
    }
    
    // Função principal de claim (usuário paga o gas)
    function claimTokens() external {
        uint256 amountToClaim = claimableAmount[msg.sender];
        
        require(amountToClaim > 0, "Claim: Endereco nao elegivel");
        require(!hasClaimed[msg.sender], "Claim: Tokens ja reivindicados");
        
        // Proteção CEI (Checks-Effects-Interactions)
        hasClaimed[msg.sender] = true;
        
        require(
            tokenContract.transfer(msg.sender, amountToClaim),
            "Claim: Falha na transferencia"
        );
        
        emit TokensClaimed(msg.sender, amountToClaim);
    }
    
    // Função para verificar saldo disponível do contrato
    function contractBalance() external view returns (uint256) {
        return tokenContract.balanceOf(address(this));
    }
    
    // Função de emergência para retirar tokens (apenas owner)
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(
            tokenContract.transfer(owner(), _amount),
            "Emergency withdraw failed"
        );
        emit EmergencyWithdraw(owner(), _amount);
    }
    
    event TokensClaimed(address indexed user, uint256 amount);
    event WhitelistUpdated(uint256 userCount);
    event ClaimableAmountUpdated(address indexed user, uint256 amount);
    event EmergencyWithdraw(address indexed to, uint256 amount);
}

