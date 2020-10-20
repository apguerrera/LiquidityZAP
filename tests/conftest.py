
from brownie import accounts, web3, Wei, chain
from brownie.network.transaction import TransactionReceipt
from brownie.convert import to_address
import pytest
from brownie import Contract
from settings import *





##############################################
# Tokens
##############################################

@pytest.fixture(scope='module', autouse=True)
def uniswap_zap(UniswapZAP):    
    token_owner = accounts[0]
    uniswap_zap = UniswapZAP.deploy({'from': token_owner})
    # function initUniswapZAP(address token, address WETH, address uniV2Factory, address tokenWethPair) public  {

    tx = uniswap_zap.initUniswapZAP(token_owner, {'from': token_owner})
    return uniswap_zap

@pytest.fixture(scope='module', autouse=True)
def balancer_zap(BalancerZAP):
    token_owner = accounts[0]
    balancer_zap = BalancerZAP.deploy({'from': token_owner})
    tx = balancer_zap.init(token_owner, {'from': token_owner})
    return balancer_zap

