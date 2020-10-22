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
    



# brownie run deploy_BalancerZAP.py --network mainnet      
#                                                                                                                             ─╯
# Brownie v1.11.0 - Python development framework for Ethereum
# LiquidityzapProject is the active project.

# Running 'scripts/deploy_BalancerZAP.py::main'...
# Enter the password to unlock this account:
# Transaction sent: 0xc219944451d240a7d5f880cf49d9a619baeb6a344a510ce2ba12929d12cd9e23
#   Gas price: 30.0 gwei   Gas limit: 935427
# Waiting for confirmation...
#   BalancerZAP.constructor confirmed - Block: 11096018   Gas used: 935427 (100.00%)
#   BalancerZAP deployed at: 0x2cbe8406380E784ea1a24aeEDFbf79788E2721AC

# Transaction sent: 0xc89eec30de8ab84fa122d255ae87656163c589927029a6eb066ccf6c35476097
#   Gas price: 31.0 gwei   Gas limit: 85828
# Waiting for confirmation...
#   BalancerZAP.initBalancerZAP confirmed - Block: 11096020   Gas used: 85828 (100.00%)

# BalancerZAP contract deployed at: 0x2cbe8406380E784ea1a24aeEDFbf79788E2721AC


