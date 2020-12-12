
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
def weth_token(WETH9):
    weth_token = WETH9.deploy({'from': accounts[0]})
    return weth_token


@pytest.fixture(scope='module', autouse=True)
def erc20_token(ERC20):
    erc20_token = ERC20.deploy(
        "TKN",
        "Token",
        18,
        accounts[0],
        10000 * 10**18 ,
        {'from': accounts[0]})
    return erc20_token


@pytest.fixture(scope='module', autouse=True)
def uniswap_zap(UniswapZAP, weth_token, erc20_token):    
    token_owner = accounts[0]
    uniswap_zap = UniswapZAP.deploy({'from': token_owner})
    # uniV2Factory
    # tx = uniswap_zap.initUniswapZAP(erc20_token, weth_token, uniV2Factory, {'from': token_owner})
    return uniswap_zap

@pytest.fixture(scope='module', autouse=True)
def balancer_zap(BalancerZAP):
    token_owner = accounts[0]
    balancer_zap = BalancerZAP.deploy({'from': token_owner})
    tx = balancer_zap.init(token_owner, {'from': token_owner})
    return balancer_zap

