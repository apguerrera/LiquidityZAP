from brownie import *
from .settings import *
from .contract_addresses import *

def load_accounts():
    if network.show_active() == 'mainnet':
        # replace with your keys
        accounts.load("liquidityzap")
    # add accounts if active network is goerli
    if network.show_active() in ['goerli', 'ropsten','kovan','rinkeby']:
        # 0x2A40019ABd4A61d71aBB73968BaB068ab389a636
        accounts.add('4ca89ec18e37683efa18e0434cd9a28c82d461189c477f5622dae974b43baebf')
        # 0x1F3389Fc75Bf55275b03347E4283f24916F402f7
        accounts.add('fa3c06c67426b848e6cef377a2dbd2d832d3718999fbe377236676c9216d8ec0')


def deploy_uniswap_pool(tokenA, tokenB):
    uniswap_pool_address = CONTRACTS[network.show_active()]["lp_token"]
    if uniswap_pool_address == '':
        uniswap_factory = interface.IUniswapV2Factory(UNISWAP_FACTORY)
        tx = uniswap_factory.createPair(tokenA, tokenB, {'from': accounts[0]})
        assert 'PairCreated' in tx.events
        uniswap_pool = interface.IUniswapV2Pair(web3.toChecksumAddress(tx.events['PairCreated']['pair']))
    else:
        uniswap_pool = interface.IUniswapV2Pair(uniswap_pool_address)
    return uniswap_pool

def get_uniswap_pool():
    uniswap_pool_address = CONTRACTS[network.show_active()]["lp_token"]
    return interface.IUniswapV2Pair(uniswap_pool_address)

def deploy_erc20_token(symbol, name, initial_supply):
    erc20_token_address = CONTRACTS[network.show_active()]["erc20_token"]
    if erc20_token_address == '':
        decimals = 18
        erc20_token = ERC20.deploy(symbol, name, decimals, accounts[0], initial_supply, {'from': accounts[0]})
    else:
        erc20_token = ERC20.at(erc20_token_address)
    return erc20_token

def get_erc20_token():
    erc20_token_address = CONTRACTS[network.show_active()]["erc20_token"]
    return ERC20.at(erc20_token_address)

def deploy_weth_token():
    weth_token_address = CONTRACTS[network.show_active()]["weth_token"]
    if weth_token_address == '':
        weth_token = WETH9.deploy({'from': accounts[0]})
    else:
        weth_token = WETH9.at(weth_token_address)
    return weth_token

def get_weth_token():
    weth_token_address = web3.toChecksumAddress(CONTRACTS[network.show_active()]["weth_token"])
    return WETH9.at(weth_token_address)
