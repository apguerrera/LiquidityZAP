from brownie import *
import time


# Uniswap
#ZAP_ADDRESS = '0x2cbe8406380E784ea1a24aeEDFbf79788E2721AC'
# Balancer1
ZAP_ADDRESS = '0x575E0188cFC64d13107d00150dF5e495DFEDa664'
# Balancer2
#ZAP_ADDRESS = '0x3Cb74Cc99AEf86d6e2715015b3b80C69a5858190'


def get_zap():
    uniswap_zap = UniswapZAP.deploy({"from": accounts[0]})
    # initUniswapZAP(address token, address WETH, address tokenWethPair)
    uniswap_zap.initUniswapZAP(TOKEN_ADDRESS, WETH_ADDRESS, TOKEN_WETH_PAIR, {"from": accounts[0]})
    print("UniswapZAP contract deployed at: " + str(uniswap_zap))
    return uniswap_zap


def main():
    if network.show_active() == 'mainnet':
        # replace with your keys
        accounts.load("liquidityzap")

    # Create Uniswap Liquidity Zap
    liquidity_zap = get_zap()
    liquidity_zap.addLiquidityETHOnly(accounts[0], {"from": accounts[0]} )

# brownie run deploy_UniswapZAP.py --network mainnet      
#                                                                                                                             ─╯
# Brownie v1.11.0 - Python development framework for Ethereum
# LiquidityzapProject is the active project.

# Running 'scripts/deploy_UniswapZAP.py::main'...
# Enter the password to unlock this account:
# Transaction sent: 0xc219944451d240a7d5f880cf49d9a619baeb6a344a510ce2ba12929d12cd9e23
#   Gas price: 30.0 gwei   Gas limit: 935427
# Waiting for confirmation...
#   UniswapZAP.constructor confirmed - Block: 11096018   Gas used: 935427 (100.00%)
#   UniswapZAP deployed at: 0x2cbe8406380E784ea1a24aeEDFbf79788E2721AC

# Transaction sent: 0xc89eec30de8ab84fa122d255ae87656163c589927029a6eb066ccf6c35476097
#   Gas price: 31.0 gwei   Gas limit: 85828
# Waiting for confirmation...
#   UniswapZAP.initUniswapZAP confirmed - Block: 11096020   Gas used: 85828 (100.00%)

# UniswapZAP contract deployed at: 0x2cbe8406380E784ea1a24aeEDFbf79788E2721AC


