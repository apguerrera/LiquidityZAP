from brownie import *
from .contract_addresses import *
import time


# Axia Protocol Constants
TOKEN_ADDRESS = '0x793786e2dd4cc492ed366a94b88a3ff9ba5e7546'
TOKEN_WETH_PAIR = '0x1e0693f129d05e5857a642245185ee1fca6a5096'
WETH_ADDRESS = '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2'
UNI_FACTORY = '0x5c69bee701ef814a2b6a3edd4b1652cb9cc5aa6f'

def deploy_uniswap_zap():
    uniswap_zap = UniswapZAP.deploy({"from": accounts[0]})
    # initUniswapZAP(address token, address WETH, address uniV2Factory, address tokenWethPair)
    uniswap_zap.initUniswapZAP(TOKEN_ADDRESS, WETH_ADDRESS, UNI_FACTORY, TOKEN_WETH_PAIR, {"from": accounts[0]})
    print("UniswapZAP contract deployed at: " + str(uniswap_zap))
    return uniswap_zap


def main():

    # Create Uniswap Liquidity Zap
    uniswap_zap = deploy_uniswap_zap()
    




