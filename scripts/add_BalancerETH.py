from brownie import *
import time


# Axia Protocol Constants
TOKEN_ADDRESS = '0x793786e2dd4cc492ed366a94b88a3ff9ba5e7546'
TOKEN_WETH_PAIR = '0x1e0693f129d05e5857a642245185ee1fca6a5096'
WETH_ADDRESS = '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2'
TENPOW18 = 10 ** 18


# Balancer1: 60% WETH 10% AXIA BAL COMP SNX
ZAP_ADDRESS = '0x575E0188cFC64d13107d00150dF5e495DFEDa664'
# Balancer2: 60% LINK 10% TRB ZAP AXIA BAND
#ZAP_ADDRESS = '0x3Cb74Cc99AEf86d6e2715015b3b80C69a5858190'


def get_zap():
    balancer_zap = BalancerZAP.at(ZAP_ADDRESS)
    print("BalancerZAP contract deployed at: " + str(balancer_zap))
    return balancer_zap


def main():
    if network.show_active() == 'mainnet':
        # replace with your keys
        accounts.load("liquidityzap")

    liquidity_to_add = 0.001 * TENPOW18

    # Create Uniswap Liquidity Zap
    liquidity_zap = get_zap()
    liquidity_zap.addLiquidityETHOnly(accounts[0], {"from": accounts[0], "value": liquidity_to_add} )
