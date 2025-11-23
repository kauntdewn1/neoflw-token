// contracts/NeoFlowClaim.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

contract NeoFlowClaim is Ownable, Pausable {
    IERC20 public tokenContract;
    
    // Whitelist de endereços elegíveis
    mapping(address => uint256) public claimableAmount;
    
    // Controle de claims realizados
    mapping(address => bool) public hasClaimed;
    
    // Tracking de total comprometido em claims pendentes
    uint256 public totalClaimable;
    
    // Array para rastrear usuários whitelisted (para cálculo de saldo comprometido)
    address[] private whitelistedUsers;
    mapping(address => bool) private isWhitelisted;
    
    constructor(IERC20 _tokenAddress) {
        require(address(_tokenAddress) != address(0), "Invalid token address");
        tokenContract = _tokenAddress;
    }
    
    // Função para carregar whitelist (apenas owner)
    function setWhitelist(
        address[] calldata _users, 
        uint256[] calldata _amounts
    ) external onlyOwner whenNotPaused {
        require(_users.length == _amounts.length, "Arrays incompativeis");
        require(_users.length > 0, "Arrays vazios");
        
        // Reset total claimable
        totalClaimable = 0;
        
        // Limpar array anterior (apenas se não for update incremental)
        // Para update incremental, usar updateClaimableAmount
        
        for(uint256 i = 0; i < _users.length; i++) {
            require(_users[i] != address(0), "Endereco invalido");
            
            // Se usuário não estava na whitelist, adicionar ao array
            if (!isWhitelisted[_users[i]]) {
                whitelistedUsers.push(_users[i]);
                isWhitelisted[_users[i]] = true;
            }
            
            // Atualizar amount (pode ser novo ou update)
            claimableAmount[_users[i]] = _amounts[i];
            
            // Adicionar ao total apenas se não foi reivindicado
            if (!hasClaimed[_users[i]]) {
                totalClaimable += _amounts[i];
            }
        }
        
        emit WhitelistUpdated(_users.length);
    }
    
    // Função para atualizar amount de um endereço específico
    function updateClaimableAmount(address _user, uint256 _amount) external onlyOwner whenNotPaused {
        require(_user != address(0), "Endereco invalido");
        require(!hasClaimed[_user], "Usuario ja fez claim");
        
        // Atualizar total claimable
        if (isWhitelisted[_user] && !hasClaimed[_user]) {
            totalClaimable -= claimableAmount[_user];
        }
        
        claimableAmount[_user] = _amount;
        
        // Adicionar ao total se não estava whitelisted
        if (!isWhitelisted[_user]) {
            whitelistedUsers.push(_user);
            isWhitelisted[_user] = true;
        }
        
        if (!hasClaimed[_user]) {
            totalClaimable += _amount;
        }
        
        emit ClaimableAmountUpdated(_user, _amount);
    }
    
    // Função principal de claim (usuário paga o gas)
    function claimTokens() external whenNotPaused {
        uint256 amountToClaim = claimableAmount[msg.sender];
        
        require(amountToClaim > 0, "Claim: Endereco nao elegivel");
        require(!hasClaimed[msg.sender], "Claim: Tokens ja reivindicados");
        
        // ✅ CORREÇÃO: Verificar saldo antes de marcar como claimed
        uint256 currentBalance = tokenContract.balanceOf(address(this));
        require(
            currentBalance >= amountToClaim,
            "Claim: Saldo insuficiente no contrato"
        );
        
        // Proteção CEI (Checks-Effects-Interactions)
        hasClaimed[msg.sender] = true;
        
        // Atualizar total claimable
        totalClaimable -= amountToClaim;
        
        // Interactions: Transferência
        bool success = tokenContract.transfer(msg.sender, amountToClaim);
        require(success, "Claim: Falha na transferencia");
        
        emit TokensClaimed(msg.sender, amountToClaim);
    }
    
    // Função para verificar saldo disponível do contrato
    function contractBalance() external view returns (uint256) {
        return tokenContract.balanceOf(address(this));
    }
    
    /**
     * @dev Retorna o total de tokens comprometidos em claims pendentes
     */
    function getTotalCommitted() public view returns (uint256) {
        return totalClaimable;
    }
    
    /**
     * @dev Retorna saldo disponível para emergency withdraw
     */
    function getAvailableBalance() public view returns (uint256) {
        uint256 balance = tokenContract.balanceOf(address(this));
        uint256 committed = getTotalCommitted();
        
        if (balance >= committed) {
            return balance - committed;
        }
        return 0;
    }
    
    // Função de emergência para retirar tokens (apenas owner)
    // ✅ CORREÇÃO CRÍTICA: Proteção contra retirada de tokens comprometidos
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than 0");
        
        uint256 availableBalance = getAvailableBalance();
        require(
            availableBalance >= _amount,
            "Cannot withdraw committed tokens"
        );
        
        bool success = tokenContract.transfer(owner(), _amount);
        require(success, "Emergency withdraw failed");
        
        emit EmergencyWithdraw(owner(), _amount);
    }
    
    /**
     * @dev Pausa o contrato em caso de emergência
     */
    function pause() external onlyOwner {
        _pause();
    }
    
    /**
     * @dev Despausa o contrato
     */
    function unpause() external onlyOwner {
        _unpause();
    }
    
    event TokensClaimed(address indexed user, uint256 amount);
    event WhitelistUpdated(uint256 userCount);
    event ClaimableAmountUpdated(address indexed user, uint256 amount);
    event EmergencyWithdraw(address indexed to, uint256 amount);
    // Paused e Unpaused eventos já vêm do Pausable do OpenZeppelin
}

