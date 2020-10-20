from brownie import accounts, web3, Wei, reverts, chain
from brownie.network.transaction import TransactionReceipt
from brownie.convert import to_address
import pytest
from brownie import Contract
from settings import *



# reset the chain after every test case
@pytest.fixture(autouse=True)
def isolation(fn_isolation):
    pass


def test_uniswap_zap_init(uniswap_zap):
    assert uniswap_zap._WETH({'from': accounts[0]}) == WETH_ADDRESS

