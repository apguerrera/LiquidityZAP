from brownie import *
import time


# Axia Protocol Constants
TOKEN_ADDRESS = '0x793786e2dd4cc492ed366a94b88a3ff9ba5e7546'
TOKEN_WETH_PAIR = '0x1e0693f129d05e5857a642245185ee1fca6a5096'
WETH_ADDRESS = '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2'

# 60% LINK 10% TRB ZAP AXIA BAND
BALANCER_POOL = '0xa1ec308f05bca8acc84eaf76bc9c92a52ac25415'

def deploy_balancer_zap():
    balancer_zap = BalancerZAP.deploy({"from": accounts[0]})
    # initBalancerZAP(address token, address balancerPool, address WETH, address tokenWethPair)
    balancer_zap.initBalancerZAP(TOKEN_ADDRESS, BALANCER_POOL, WETH_ADDRESS, TOKEN_WETH_PAIR, {"from": accounts[0]})
    print("BalancerZAP contract deployed at: " + str(balancer_zap))
    return balancer_zap


def main():
    if network.show_active() == 'mainnet':
        # replace with your keys
        accounts.load("liquidityzap")

    # Create Uniswap Liquidity Zap
    balancer_zap = deploy_balancer_zap()
    



# brownie run deploy_BalancerZAP.py --network mainnet      
#                                                                                                                             ─╯
# Brownie v1.11.0 - Python development framework for Ethereum
# LiquidityzapProject is the active project.

# Running 'scripts/deploy_BalancerZAP2.py::main'...
# Enter the password to unlock this account:
# Transaction sent: 0x4f8fe23d19ac52b21e163674854ac8e89f789720407052b8b9ec155602424273
#   Gas price: 68.697 gwei   Gas limit: 743090
# Waiting for confirmation...
#   BalancerZAP.constructor confirmed - Block: 11103510   Gas used: 743090 (100.00%)
#   BalancerZAP deployed at: 0x3Cb74Cc99AEf86d6e2715015b3b80C69a5858190
