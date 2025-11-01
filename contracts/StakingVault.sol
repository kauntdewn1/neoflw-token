// contracts/StakingVault.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract StakingVault is Ownable, ReentrancyGuard {
    IERC20 public token;
    
    uint256 public constant LOCK_DURATION = 180 days; // 6 meses
    uint256 public constant REWARD_RATE = 10; // 10% de reward após 6 meses
    
    struct StakeInfo {
        uint256 amount;
        uint256 startTime;
        bool claimed;
    }
    
    mapping(address => StakeInfo) public stakes;
    
    event Staked(address indexed user, uint256 amount);
    event Claimed(address indexed user, uint256 amount, uint256 reward, uint256 total);
    event RewardsDeposited(address indexed owner, uint256 amount);
    event EmergencyWithdrawn(address indexed owner, uint256 amount);
    
    constructor(address _token) {
        require(_token != address(0), "Invalid token address");
        token = IERC20(_token);
    }
    
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount == 0, "Already staking");
        require(
            token.transferFrom(msg.sender, address(this), _amount),
            "Transfer failed"
        );
        
        stakes[msg.sender] = StakeInfo({
            amount: _amount,
            startTime: block.timestamp,
            claimed: false
        });
        
        emit Staked(msg.sender, _amount);
    }
    
    function claim() external nonReentrant {
        StakeInfo storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake found");
        require(!userStake.claimed, "Already claimed");
        require(
            block.timestamp >= userStake.startTime + LOCK_DURATION,
            "Lock period not finished"
        );
        
        uint256 reward = (userStake.amount * REWARD_RATE) / 100;
        uint256 total = userStake.amount + reward;
        
        // ✅ VALIDAÇÃO CRÍTICA DE SEGURANÇA: Verificar saldo ANTES de marcar como claimed
        // Esta validação previne DoS e garante que o vault tem saldo suficiente
        // Ordem CEI: Checks (validações) → Effects (mudança de estado) → Interactions (transfer)
        require(
            token.balanceOf(address(this)) >= total,
            "Vault: Saldo insuficiente para rewards"
        );
        
        // Effects: Marcar como claimed ANTES da transferência (proteção CEI)
        userStake.claimed = true;
        
        // Interactions: Transferência após todas as validações e mudanças de estado
        require(
            token.transfer(msg.sender, total),
            "Transfer failed"
        );
        
        emit Claimed(msg.sender, userStake.amount, reward, total);
    }
    
    function timeLeft(address _user) external view returns (uint256) {
        StakeInfo memory userStake = stakes[_user];
        if (userStake.amount == 0 || userStake.claimed) {
            return 0;
        }
        
        uint256 endTime = userStake.startTime + LOCK_DURATION;
        if (block.timestamp >= endTime) {
            return 0;
        }
        
        return endTime - block.timestamp;
    }
    
    // Função para owner depositar tokens de reward no vault
    function depositRewards(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than 0");
        require(
            token.transferFrom(msg.sender, address(this), _amount),
            "Transfer failed"
        );
        emit RewardsDeposited(msg.sender, _amount);
    }
    
    /**
     * @dev Calcula o total de tokens comprometidos em stakes ativos (não reivindicados)
     * @return totalStaked Tokens em stakes ativos + rewards pendentes
     */
    function getTotalStaked() public view returns (uint256 totalStaked) {
        // Nota: Esta função requer iteração sobre todos os stakes, o que pode ser custoso.
        // Para produção, considere manter um mapeamento de total acumulado.
        // Por ora, retorna 0 como implementação simplificada.
        // Em produção, considere adicionar um counter para eficiência.
        return 0; // Implementação simplificada - requer redesign para eficiência
    }
    
    /**
     * @dev Calcula saldo disponível para emergency withdraw (balance - stakes ativos)
     * @return availableBalance Saldo que pode ser retirado sem afetar stakes
     */
    function getAvailableBalance() public view returns (uint256) {
        uint256 balance = token.balanceOf(address(this));
        uint256 totalStaked = getTotalStaked();
        
        // Se não conseguimos calcular, retorna 0 por segurança
        if (totalStaked == 0) {
            // Por segurança, assume que todo o saldo está comprometido
            // Owner deve verificar manualmente antes de usar emergencyWithdraw
            return 0;
        }
        
        if (balance >= totalStaked) {
            return balance - totalStaked;
        }
        return 0;
    }
    
    /**
     * @dev Função de emergência para owner retirar apenas saldo disponível
     * @param _amount Quantidade a retirar (deve ser <= getAvailableBalance())
     */
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than 0");
        
        uint256 availableBalance = getAvailableBalance();
        require(availableBalance >= _amount, "Insufficient available balance");
        
        require(
            token.transfer(owner(), _amount),
            "Transfer failed"
        );
        
        emit EmergencyWithdrawn(msg.sender, _amount);
    }
}

