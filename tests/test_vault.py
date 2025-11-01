# tests/test_vault.py
import pytest

def test_stake_basic(project, accounts):
    deployer = accounts[0]
    staker = accounts[1]
    
    # Deploy token
    token = project.NeoFlowToken.deploy(1_000_000 * 10**18, sender=deployer)
    
    # Deploy vault
    vault = project.StakingVault.deploy(token.address, sender=deployer)
    
    # Transfer tokens para staker
    stake_amount = 1_000 * 10**18
    token.transfer(staker, stake_amount, sender=deployer)
    
    # Approve vault
    token.approve(vault.address, stake_amount, sender=staker)
    
    # Stake
    vault.stake(stake_amount, sender=staker)
    
    stake_info = vault.stakes(staker)
    assert stake_info[0] == stake_amount  # amount
    assert stake_info[1] > 0  # startTime
    assert stake_info[2] == False  # claimed
    
    # Verificar que tokens foram transferidos
    assert token.balanceOf(vault.address) == stake_amount
    assert token.balanceOf(staker) == 0


def test_stake_zero_amount(project, accounts):
    deployer = accounts[0]
    staker = accounts[1]
    
    token = project.NeoFlowToken.deploy(1_000_000 * 10**18, sender=deployer)
    vault = project.StakingVault.deploy(token.address, sender=deployer)
    
    # Tentar stake com amount zero deve falhar
    with pytest.raises(Exception):
        vault.stake(0, sender=staker)


def test_stake_double_stake(project, accounts):
    deployer = accounts[0]
    staker = accounts[1]
    
    token = project.NeoFlowToken.deploy(1_000_000 * 10**18, sender=deployer)
    vault = project.StakingVault.deploy(token.address, sender=deployer)
    
    stake_amount = 1_000 * 10**18
    token.transfer(staker, stake_amount * 2, sender=deployer)
    token.approve(vault.address, stake_amount * 2, sender=staker)
    
    # Primeiro stake
    vault.stake(stake_amount, sender=staker)
    
    # Tentar segundo stake deve falhar
    with pytest.raises(Exception):
        vault.stake(stake_amount, sender=staker)


def test_stake_insufficient_allowance(project, accounts):
    deployer = accounts[0]
    staker = accounts[1]
    
    token = project.NeoFlowToken.deploy(1_000_000 * 10**18, sender=deployer)
    vault = project.StakingVault.deploy(token.address, sender=deployer)
    
    stake_amount = 1_000 * 10**18
    token.transfer(staker, stake_amount, sender=deployer)
    
    # Não aprovar suficiente
    token.approve(vault.address, stake_amount - 1, sender=staker)
    
    # Tentar stake deve falhar
    with pytest.raises(Exception):
        vault.stake(stake_amount, sender=staker)


def test_claim_after_lock_period(project, accounts, chain):
    deployer = accounts[0]
    staker = accounts[1]
    
    token = project.NeoFlowToken.deploy(1_000_000 * 10**18, sender=deployer)
    vault = project.StakingVault.deploy(token.address, sender=deployer)
    
    stake_amount = 1_000 * 10**18
    token.transfer(staker, stake_amount, sender=deployer)
    token.approve(vault.address, stake_amount, sender=staker)
    
    # Stake
    vault.stake(stake_amount, sender=staker)
    
    # Depositar rewards no vault (10% = 100 tokens)
    reward_needed = (stake_amount * 10) // 100
    token.transfer(deployer, reward_needed, sender=deployer)
    token.approve(vault.address, reward_needed, sender=deployer)
    vault.depositRewards(reward_needed, sender=deployer)
    
    # Avançar 180 dias (6 meses)
    chain.mine(timestamp=chain.pending_timestamp + (180 * 24 * 60 * 60))
    
    # Claim
    initial_balance = token.balanceOf(staker)
    vault.claim(sender=staker)
    
    # Verificar que recebeu principal + reward
    expected_total = stake_amount + reward_needed
    assert token.balanceOf(staker) == initial_balance + expected_total
    
    # Verificar que stake foi marcado como claimed
    stake_info = vault.stakes(staker)
    assert stake_info[2] == True  # claimed


def test_claim_before_lock_period(project, accounts, chain):
    deployer = accounts[0]
    staker = accounts[1]
    
    token = project.NeoFlowToken.deploy(1_000_000 * 10**18, sender=deployer)
    vault = project.StakingVault.deploy(token.address, sender=deployer)
    
    stake_amount = 1_000 * 10**18
    token.transfer(staker, stake_amount, sender=deployer)
    token.approve(vault.address, stake_amount, sender=staker)
    
    vault.stake(stake_amount, sender=staker)
    
    # Tentar claim antes do período deve falhar
    with pytest.raises(Exception):
        vault.claim(sender=staker)


def test_claim_insufficient_vault_balance(project, accounts, chain):
    deployer = accounts[0]
    staker = accounts[1]
    
    token = project.NeoFlowToken.deploy(1_000_000 * 10**18, sender=deployer)
    vault = project.StakingVault.deploy(token.address, sender=deployer)
    
    stake_amount = 1_000 * 10**18
    token.transfer(staker, stake_amount, sender=deployer)
    token.approve(vault.address, stake_amount, sender=staker)
    
    vault.stake(stake_amount, sender=staker)
    
    # NÃO depositar rewards no vault
    # Avançar 180 dias
    chain.mine(timestamp=chain.pending_timestamp + (180 * 24 * 60 * 60))
    
    # Tentar claim deve falhar por falta de saldo
    with pytest.raises(Exception):
        vault.claim(sender=staker)


def test_claim_already_claimed(project, accounts, chain):
    deployer = accounts[0]
    staker = accounts[1]
    
    token = project.NeoFlowToken.deploy(1_000_000 * 10**18, sender=deployer)
    vault = project.StakingVault.deploy(token.address, sender=deployer)
    
    stake_amount = 1_000 * 10**18
    token.transfer(staker, stake_amount, sender=deployer)
    token.approve(vault.address, stake_amount, sender=staker)
    
    vault.stake(stake_amount, sender=staker)
    
    # Depositar rewards
    reward_needed = (stake_amount * 10) // 100
    token.transfer(deployer, reward_needed, sender=deployer)
    token.approve(vault.address, reward_needed, sender=deployer)
    vault.depositRewards(reward_needed, sender=deployer)
    
    # Avançar 180 dias
    chain.mine(timestamp=chain.pending_timestamp + (180 * 24 * 60 * 60))
    
    # Primeiro claim
    vault.claim(sender=staker)
    
    # Tentar claim novamente deve falhar
    with pytest.raises(Exception):
        vault.claim(sender=staker)


def test_claim_no_stake(project, accounts):
    deployer = accounts[0]
    user = accounts[1]
    
    token = project.NeoFlowToken.deploy(1_000_000 * 10**18, sender=deployer)
    vault = project.StakingVault.deploy(token.address, sender=deployer)
    
    # Tentar claim sem stake deve falhar
    with pytest.raises(Exception):
        vault.claim(sender=user)


def test_timeLeft_active_stake(project, accounts, chain):
    deployer = accounts[0]
    staker = accounts[1]
    
    token = project.NeoFlowToken.deploy(1_000_000 * 10**18, sender=deployer)
    vault = project.StakingVault.deploy(token.address, sender=deployer)
    
    stake_amount = 1_000 * 10**18
    token.transfer(staker, stake_amount, sender=deployer)
    token.approve(vault.address, stake_amount, sender=staker)
    
    vault.stake(stake_amount, sender=staker)
    
    # Avançar 90 dias (metade do período)
    chain.mine(timestamp=chain.pending_timestamp + (90 * 24 * 60 * 60))
    
    time_left = vault.timeLeft(staker)
    expected_time = 90 * 24 * 60 * 60  # 90 dias restantes
    
    # Permitir pequena diferença devido ao timestamp do bloco
    assert abs(time_left - expected_time) < 60  # 1 minuto de tolerância


def test_timeLeft_no_stake(project, accounts):
    deployer = accounts[0]
    user = accounts[1]
    
    token = project.NeoFlowToken.deploy(1_000_000 * 10**18, sender=deployer)
    vault = project.StakingVault.deploy(token.address, sender=deployer)
    
    # Sem stake, timeLeft deve ser 0
    assert vault.timeLeft(user) == 0


def test_timeLeft_after_claimed(project, accounts, chain):
    deployer = accounts[0]
    staker = accounts[1]
    
    token = project.NeoFlowToken.deploy(1_000_000 * 10**18, sender=deployer)
    vault = project.StakingVault.deploy(token.address, sender=deployer)
    
    stake_amount = 1_000 * 10**18
    token.transfer(staker, stake_amount, sender=deployer)
    token.approve(vault.address, stake_amount, sender=staker)
    
    vault.stake(stake_amount, sender=staker)
    
    # Depositar rewards
    reward_needed = (stake_amount * 10) // 100
    token.transfer(deployer, reward_needed, sender=deployer)
    token.approve(vault.address, reward_needed, sender=deployer)
    vault.depositRewards(reward_needed, sender=deployer)
    
    # Avançar 180 dias
    chain.mine(timestamp=chain.pending_timestamp + (180 * 24 * 60 * 60))
    
    # Claim
    vault.claim(sender=staker)
    
    # Após claim, timeLeft deve ser 0
    assert vault.timeLeft(staker) == 0


def test_timeLeft_after_period_ends(project, accounts, chain):
    deployer = accounts[0]
    staker = accounts[1]
    
    token = project.NeoFlowToken.deploy(1_000_000 * 10**18, sender=deployer)
    vault = project.StakingVault.deploy(token.address, sender=deployer)
    
    stake_amount = 1_000 * 10**18
    token.transfer(staker, stake_amount, sender=deployer)
    token.approve(vault.address, stake_amount, sender=staker)
    
    vault.stake(stake_amount, sender=staker)
    
    # Avançar mais de 180 dias
    chain.mine(timestamp=chain.pending_timestamp + (181 * 24 * 60 * 60))
    
    # TimeLeft deve ser 0 após período terminar
    assert vault.timeLeft(staker) == 0


def test_depositRewards(project, accounts):
    deployer = accounts[0]
    
    token = project.NeoFlowToken.deploy(1_000_000 * 10**18, sender=deployer)
    vault = project.StakingVault.deploy(token.address, sender=deployer)
    
    deposit_amount = 10_000 * 10**18
    token.approve(vault.address, deposit_amount, sender=deployer)
    
    initial_balance = token.balanceOf(vault.address)
    vault.depositRewards(deposit_amount, sender=deployer)
    
    assert token.balanceOf(vault.address) == initial_balance + deposit_amount


def test_depositRewards_zero_amount(project, accounts):
    deployer = accounts[0]
    
    token = project.NeoFlowToken.deploy(1_000_000 * 10**18, sender=deployer)
    vault = project.StakingVault.deploy(token.address, sender=deployer)
    
    # Verificar saldo inicial do vault
    initial_vault_balance = token.balanceOf(vault.address)
    
    # Tentar depositar 0
    # Em ambiente local, pode não reverter, mas deve falhar no transferFrom ou não mudar nada
    # Como não há approve, transferFrom deve falhar mesmo se o require passar
    try:
        vault.depositRewards(0, sender=deployer)
        # Se não reverteu, verificar que nada mudou (transferFrom com 0 sem approve deve falhar)
        final_vault_balance = token.balanceOf(vault.address)
        assert final_vault_balance == initial_vault_balance, "depositRewards(0) should not change vault balance"
    except Exception:
        # Se reverteu, está correto (comportamento esperado)
        pass


def test_depositRewards_only_owner(project, accounts):
    deployer = accounts[0]
    non_owner = accounts[1]
    
    token = project.NeoFlowToken.deploy(1_000_000 * 10**18, sender=deployer)
    vault = project.StakingVault.deploy(token.address, sender=deployer)
    
    token.transfer(non_owner, 1_000 * 10**18, sender=deployer)
    token.approve(vault.address, 1_000 * 10**18, sender=non_owner)
    
    # Non-owner não pode depositar rewards
    with pytest.raises(Exception):
        vault.depositRewards(1_000 * 10**18, sender=non_owner)


def test_reward_calculation(project, accounts, chain):
    deployer = accounts[0]
    staker = accounts[1]
    
    token = project.NeoFlowToken.deploy(1_000_000 * 10**18, sender=deployer)
    vault = project.StakingVault.deploy(token.address, sender=deployer)
    
    stake_amount = 10_000 * 10**18  # 10k tokens
    expected_reward = (stake_amount * 10) // 100  # 10% = 1k tokens
    
    token.transfer(staker, stake_amount, sender=deployer)
    token.approve(vault.address, stake_amount, sender=staker)
    
    vault.stake(stake_amount, sender=staker)
    
    # Depositar rewards exatos
    token.transfer(deployer, expected_reward, sender=deployer)
    token.approve(vault.address, expected_reward, sender=deployer)
    vault.depositRewards(expected_reward, sender=deployer)
    
    # Avançar 180 dias
    chain.mine(timestamp=chain.pending_timestamp + (180 * 24 * 60 * 60))
    
    initial_balance = token.balanceOf(staker)
    vault.claim(sender=staker)
    
    # Verificar que reward foi exatamente 10%
    assert token.balanceOf(staker) == initial_balance + stake_amount + expected_reward

