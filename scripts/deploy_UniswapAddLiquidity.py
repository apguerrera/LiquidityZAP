from brownie import *
from .settings import *
from .contracts import *
from .contract_addresses import *
import time


def main():
    load_accounts()

    # Deploy Contracts 
    weth_token = get_weth_token()
    erc20_token = get_erc20_token()

    # Deploy Uniswap Pool
    uniswap_pool = deploy_uniswap_pool(erc20_token, weth_token)

    weth_token.deposit({'from': accounts[0], 'value': 0.11*10**18})
    erc20_token.transfer(uniswap_pool, 20 * 10**18, {'from':accounts[0]})
    weth_token.transfer( uniswap_pool,0.1 * 10**18,{'from':accounts[0]})
    uniswap_pool.mint(accounts[0] ,{'from':accounts[0]})
    print(str(uniswap_pool))


