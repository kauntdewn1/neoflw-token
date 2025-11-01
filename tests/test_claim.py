# tests/test_claim.py
import pytest

def test_deploy_claim(project, accounts):
    """Testa o deploy do contrato de claim"""
    deployer = accounts[0]
    
    # Deploy do token primeiro
    token = project.NeoFlowToken.deploy(1_000_000 * 10**18, sender=deployer)
    
    # Deploy do contrato de claim
    claim = project.NeoFlowClaim.deploy(token, sender=deployer)
    
    assert claim.tokenContract() == token.address
    assert claim.owner() == deployer.address


def test_set_whitelist(project, accounts):
    """Testa a configuração da whitelist"""
    deployer = accounts[0]
    user1 = accounts[1]
    user2 = accounts[2]
    
    token = project.NeoFlowToken.deploy(1_000_000 * 10**18, sender=deployer)
    claim = project.NeoFlowClaim.deploy(token, sender=deployer)
    
    # Configurar whitelist
    users = [user1.address, user2.address]
    amounts = [100 * 10**18, 200 * 10**18]
    
    claim.setWhitelist(users, amounts, sender=deployer)
    
    assert claim.claimableAmount(user1.address) == 100 * 10**18
    assert claim.claimableAmount(user2.address) == 200 * 10**18


def test_set_whitelist_only_owner(project, accounts):
    """Testa que apenas o owner pode configurar whitelist"""
    deployer = accounts[0]
    non_owner = accounts[1]
    user1 = accounts[2]
    
    token = project.NeoFlowToken.deploy(1_000_000 * 10**18, sender=deployer)
    claim = project.NeoFlowClaim.deploy(token, sender=deployer)
    
    users = [user1.address]
    amounts = [100 * 10**18]
    
    # Non-owner não pode configurar whitelist
    with pytest.raises(Exception):
        claim.setWhitelist(users, amounts, sender=non_owner)


def test_claim_tokens(project, accounts):
    """Testa o claim de tokens"""
    deployer = accounts[0]
    user = accounts[1]
    
    token = project.NeoFlowToken.deploy(1_000_000 * 10**18, sender=deployer)
    claim = project.NeoFlowClaim.deploy(token, sender=deployer)
    
    # Transferir tokens para o contrato
    claim_amount = 1000 * 10**18
    token.transfer(claim.address, claim_amount, sender=deployer)
    
    # Configurar whitelist
    claim.setWhitelist([user.address], [claim_amount], sender=deployer)
    
    # User faz claim
    initial_balance = token.balanceOf(user.address)
    claim.claimTokens(sender=user)
    
    # Verificar que user recebeu os tokens
    assert token.balanceOf(user.address) == initial_balance + claim_amount
    assert claim.hasClaimed(user.address) == True


def test_claim_ineligible_address(project, accounts):
    """Testa que endereço não elegível não pode fazer claim"""
    deployer = accounts[0]
    user = accounts[1]
    
    token = project.NeoFlowToken.deploy(1_000_000 * 10**18, sender=deployer)
    claim = project.NeoFlowClaim.deploy(token, sender=deployer)
    
    # Tentar claim sem estar na whitelist
    with pytest.raises(Exception):
        claim.claimTokens(sender=user)


def test_claim_already_claimed(project, accounts):
    """Testa que não é possível fazer claim duas vezes"""
    deployer = accounts[0]
    user = accounts[1]
    
    token = project.NeoFlowToken.deploy(1_000_000 * 10**18, sender=deployer)
    claim = project.NeoFlowClaim.deploy(token, sender=deployer)
    
    claim_amount = 1000 * 10**18
    token.transfer(claim.address, claim_amount, sender=deployer)
    claim.setWhitelist([user.address], [claim_amount], sender=deployer)
    
    # Primeiro claim deve funcionar
    claim.claimTokens(sender=user)
    
    # Segundo claim deve falhar
    with pytest.raises(Exception):
        claim.claimTokens(sender=user)


def test_claim_insufficient_contract_balance(project, accounts):
    """Testa que claim falha se contrato não tem saldo suficiente"""
    deployer = accounts[0]
    user = accounts[1]
    
    token = project.NeoFlowToken.deploy(1_000_000 * 10**18, sender=deployer)
    claim = project.NeoFlowClaim.deploy(token, sender=deployer)
    
    # Configurar whitelist com amount maior que o saldo do contrato
    claim_amount = 1000 * 10**18
    claim.setWhitelist([user.address], [claim_amount], sender=deployer)
    
    # Não transferir tokens para o contrato - deve falhar
    with pytest.raises(Exception):
        claim.claimTokens(sender=user)


def test_update_claimable_amount(project, accounts):
    """Testa atualização de amount para um usuário específico"""
    deployer = accounts[0]
    user = accounts[1]
    
    token = project.NeoFlowToken.deploy(1_000_000 * 10**18, sender=deployer)
    claim = project.NeoFlowClaim.deploy(token, sender=deployer)
    
    # Configurar amount inicial
    claim.setWhitelist([user.address], [100 * 10**18], sender=deployer)
    assert claim.claimableAmount(user.address) == 100 * 10**18
    
    # Atualizar amount
    claim.updateClaimableAmount(user.address, 500 * 10**18, sender=deployer)
    assert claim.claimableAmount(user.address) == 500 * 10**18


def test_emergency_withdraw(project, accounts):
    """Testa função de emergência para retirar tokens"""
    deployer = accounts[0]
    
    token = project.NeoFlowToken.deploy(1_000_000 * 10**18, sender=deployer)
    claim = project.NeoFlowClaim.deploy(token, sender=deployer)
    
    # Transferir tokens para o contrato
    amount = 10_000 * 10**18
    token.transfer(claim.address, amount, sender=deployer)
    
    initial_balance = token.balanceOf(deployer.address)
    
    # Owner faz emergency withdraw
    claim.emergencyWithdraw(amount, sender=deployer)
    
    # Verificar que tokens foram retirados
    assert token.balanceOf(deployer.address) == initial_balance + amount
    assert token.balanceOf(claim.address) == 0

