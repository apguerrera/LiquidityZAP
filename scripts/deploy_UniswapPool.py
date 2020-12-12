from brownie import *
from .settings import *
from .contracts import *
from .contract_addresses import *
import time


def main():
    load_accounts()

    # Deploy Contracts 
    erc20_token = deploy_erc20_token(ERC20_SYMBOL, ERC20_NAME, ERC20_INITIAL_SUPPLY)
    weth_token = deploy_weth_token()

    # Deploy Uniswap Pool
    uniswap_pool = deploy_uniswap_pool(erc20_token, weth_token)
    
    print(str(uniswap_pool))


