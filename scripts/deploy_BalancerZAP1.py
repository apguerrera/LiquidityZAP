from brownie import *
import time


# Axia Protocol Constants
TOKEN_ADDRESS = '0x793786e2dd4cc492ed366a94b88a3ff9ba5e7546'
TOKEN_WETH_PAIR = '0x1e0693f129d05e5857a642245185ee1fca6a5096'
WETH_ADDRESS = '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2'

# 60% WETH 10% AXIA BAL COMP SNX
BALANCER_POOL = '0x4833e8b56fc8e8a777fcc5e37cb6035c504c9478'

def deploy_balancer_zap():
    balancer_zap = BalancerZAP.deploy({"from": accounts[0]})
    # initBalancerZAP(address token, address WETH, address tokenWethPair)
    balancer_zap.initBalancerZAP(TOKEN_ADDRESS, BALANCER_POOL, WETH_ADDRESS, TOKEN_WETH_PAIR, {"from": accounts[0]})
    print("BalancerZAP contract deployed at: " + str(balancer_zap))
    return balancer_zap


def main():
    if network.show_active() == 'mainnet':
        # replace with your keys
        accounts.load("liquidityzap")

    # Create Uniswap Liquidity Zap
    balancer_zap = deploy_balancer_zap()
    



# ╰─ brownie run deploy_BalancerZAP1.py --network mainnet                      ─╯
# Brownie v1.11.0 - Python development framework for Ethereum

# LiquidityzapProject is the active project.

# Running 'scripts/deploy_BalancerZAP1.py::main'...
# Enter the password to unlock this account:
# Transaction sent: 0x689500fa3a725772746ad0eff1b19266e4d0e1115cc911bad001fc964caf49bd
#   Gas price: 66.0 gwei   Gas limit: 743090
# Waiting for confirmation...
#   BalancerZAP.constructor confirmed - Block: 11103424   Gas used: 743090 (100.00%)
#   BalancerZAP deployed at: 0x575E0188cFC64d13107d00150dF5e495DFEDa664

# Transaction sent: 0x9e562f8f618bd673d7a1e3b2f02c17f61bafacd43fb7da4ccabab1297a785e1d
#   Gas price: 65.0 gwei   Gas limit: 131111
# Waiting for confirmation...
#   BalancerZAP.initBalancerZAP confirmed - Block: 11103430   Gas used: 131111 (100.00%)

# BalancerZAP contract deployed at: 0x575E0188cFC64d13107d00150dF5e495DFEDa664
