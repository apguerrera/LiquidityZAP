from brownie import *
from .contract_addresses import *
import time


# Axia Protocol Constants
TOKEN_ADDRESS = '0x793786e2dd4cc492ed366a94b88a3ff9ba5e7546'
TOKEN_WETH_PAIR = '0x1e0693f129d05e5857a642245185ee1fca6a5096'
WETH_ADDRESS = '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2'


def deploy_uniswap_zap():
    uniswap_zap = UniswapZAP.deploy({"from": accounts[0]})
    # initUniswapZAP(address token, address WETH, address tokenWethPair)
    uniswap_zap.initUniswapZAP(TOKEN_ADDRESS, WETH_ADDRESS, TOKEN_WETH_PAIR, {"from": accounts[0]})
    print("UniswapZAP contract deployed at: " + str(uniswap_zap))
    return uniswap_zap


def main():
    if network.show_active() == 'mainnet':
        # replace with your keys
        accounts.load("dutchswap")

    # Create Uniswap Liquidity Zap
    uniswap_zap = deploy_uniswap_zap()
    




