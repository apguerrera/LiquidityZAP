from brownie import *
from .settings import *
from .contracts import *
from .contract_addresses import *
import time



def main():
    load_accounts()

    # Create Uniswap Liquidity Zap
    uniswap_zap = deploy_uniswap_zap()
    
