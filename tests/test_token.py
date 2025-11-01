# tests/test_token.py
import pytest

def test_initial_supply(project, accounts):
    deployer = accounts[0]
    token = project.NeoFlowToken.deploy(1_000_000 * 10**18, sender=deployer)
    assert token.totalSupply() == 1_000_000 * 10**18
    assert token.balanceOf(deployer) == 1_000_000 * 10**18


def test_burn_tokens(project, accounts):
    deployer = accounts[0]
    user = accounts[1]
    
    token = project.NeoFlowToken.deploy(1_000_000 * 10**18, sender=deployer)
    initial_supply = token.totalSupply()
    
    # Transfer tokens para user
    burn_amount = 100 * 10**18
    token.transfer(user, burn_amount, sender=deployer)
    
    # User queima tokens
    token.burn(burn_amount, sender=user)
    
    assert token.totalSupply() == initial_supply - burn_amount
    assert token.balanceOf(user) == 0


def test_burn_zero_amount(project, accounts):
    deployer = accounts[0]
    token = project.NeoFlowToken.deploy(1_000_000 * 10**18, sender=deployer)
    
    # Tentar queimar 0 tokens deve falhar
    with pytest.raises(Exception):
        token.burn(0, sender=deployer)


def test_burn_insufficient_balance(project, accounts):
    deployer = accounts[0]
    user = accounts[1]
    
    token = project.NeoFlowToken.deploy(1_000_000 * 10**18, sender=deployer)
    
    # User tenta queimar mais do que tem
    with pytest.raises(Exception):
        token.burn(100 * 10**18, sender=user)

