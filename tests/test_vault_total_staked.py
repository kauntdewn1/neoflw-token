# tests/test_vault_total_staked.py
# Testes específicos para verificar getTotalStaked() otimizado
import pytest

def test_get_total_staked_single_stake(project, accounts):
    """Testa getTotalStaked com um único stake"""
    deployer = accounts[0]
    staker = accounts[1]
    
    token = project.NeoFlowToken.deploy(1_000_000 * 10**18, sender=deployer)
    vault = project.StakingVault.deploy(token.address, sender=deployer)
    
    stake_amount = 10_000 * 10**18  # 10k tokens
    expected_reward = (stake_amount * 10) // 100  # 10% = 1k tokens
    expected_total = stake_amount + expected_reward  # 11k tokens
    
    token.transfer(staker, stake_amount, sender=deployer)
    token.approve(vault.address, stake_amount, sender=staker)
    
    vault.stake(stake_amount, sender=staker)
    
    # Verificar tracking acumulado
    assert vault.totalStakedAmount() == stake_amount
    assert vault.totalRewardsReserved() == expected_reward
    assert vault.getTotalStaked() == expected_total


def test_get_total_staked_multiple_stakes(project, accounts):
    """Testa getTotalStaked com múltiplos stakes"""
    deployer = accounts[0]
    staker1 = accounts[1]
    staker2 = accounts[2]
    staker3 = accounts[3]
    
    token = project.NeoFlowToken.deploy(10_000_000 * 10**18, sender=deployer)
    vault = project.StakingVault.deploy(token.address, sender=deployer)
    
    stake1 = 5_000 * 10**18
    stake2 = 3_000 * 10**18
    stake3 = 2_000 * 10**18
    
    # Transferir e fazer stakes
    for staker, amount in [(staker1, stake1), (staker2, stake2), (staker3, stake3)]:
        token.transfer(staker, amount, sender=deployer)
        token.approve(vault.address, amount, sender=staker)
        vault.stake(amount, sender=staker)
    
    # Calcular total esperado
    total_staked = stake1 + stake2 + stake3
    total_rewards = (total_staked * 10) // 100
    expected_total = total_staked + total_rewards
    
    assert vault.totalStakedAmount() == total_staked
    assert vault.totalRewardsReserved() == total_rewards
    assert vault.getTotalStaked() == expected_total


def test_get_total_staked_after_claim(project, accounts, chain):
    """Testa getTotalStaked após um claim"""
    deployer = accounts[0]
    staker1 = accounts[1]
    staker2 = accounts[2]
    
    token = project.NeoFlowToken.deploy(10_000_000 * 10**18, sender=deployer)
    vault = project.StakingVault.deploy(token.address, sender=deployer)
    
    stake1 = 5_000 * 10**18
    stake2 = 3_000 * 10**18
    
    # Fazer dois stakes
    token.transfer(staker1, stake1, sender=deployer)
    token.approve(vault.address, stake1, sender=staker1)
    vault.stake(stake1, sender=staker1)
    
    token.transfer(staker2, stake2, sender=deployer)
    token.approve(vault.address, stake2, sender=staker2)
    vault.stake(stake2, sender=staker2)
    
    initial_total = vault.getTotalStaked()
    
    # Depositar rewards e fazer claim do primeiro
    reward1 = (stake1 * 10) // 100
    token.transfer(deployer, reward1, sender=deployer)
    token.approve(vault.address, reward1, sender=deployer)
    vault.depositRewards(reward1, sender=deployer)
    
    # Avançar tempo e claim
    chain.mine(timestamp=chain.pending_timestamp + (180 * 24 * 60 * 60))
    vault.claim(sender=staker1)
    
    # Verificar que total diminuiu
    reward2 = (stake2 * 10) // 100
    expected_total = stake2 + reward2
    
    assert vault.totalStakedAmount() == stake2
    assert vault.totalRewardsReserved() == reward2
    assert vault.getTotalStaked() == expected_total
    assert vault.getTotalStaked() < initial_total


def test_get_available_balance(project, accounts):
    """Testa getAvailableBalance usando getTotalStaked otimizado"""
    deployer = accounts[0]
    staker = accounts[1]
    
    token = project.NeoFlowToken.deploy(1_000_000 * 10**18, sender=deployer)
    vault = project.StakingVault.deploy(token.address, sender=deployer)
    
    stake_amount = 10_000 * 10**18
    expected_reward = (stake_amount * 10) // 100
    
    token.transfer(staker, stake_amount, sender=deployer)
    token.approve(vault.address, stake_amount, sender=staker)
    
    vault.stake(stake_amount, sender=staker)
    
    # Depositar mais tokens do que necessário (para testar available balance)
    # Note: depositRewards adiciona tokens ao saldo, mas não altera totalRewardsReserved
    extra_tokens = 5_000 * 10**18
    token.approve(vault.address, extra_tokens, sender=deployer)
    vault.depositRewards(extra_tokens, sender=deployer)
    
    # Verificar tracking
    total_staked = vault.getTotalStaked()  # stake_amount + expected_reward
    total_balance = token.balanceOf(vault.address)  # stake_amount + extra_tokens
    available = vault.getAvailableBalance()  # total_balance - total_staked
    
    # O available deve ser: (stake_amount + extra_tokens) - (stake_amount + expected_reward)
    # = extra_tokens - expected_reward (se extra_tokens > expected_reward)
    # Na prática: 15,000 - 11,000 = 4,000
    expected_available = total_balance - total_staked
    
    assert available == total_balance - total_staked
    assert available == expected_available
    # Available é extra_tokens menos o reward já reservado que não está no saldo extra
    # Mas como depositRewards não aumenta totalRewardsReserved, temos que considerar:
    # Balance total = stake_amount (10k) + extra_tokens (5k) = 15k
    # Total staked (reservado) = stake_amount (10k) + reward (1k) = 11k
    # Available = 15k - 11k = 4k
    assert available == extra_tokens - expected_reward

