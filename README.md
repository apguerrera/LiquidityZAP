# LiquidityZAP

A tool to convert ETH to LP tokens

## Convert your ETH to Liquidity Provider (LP) tokens in a ZAP



# Developers

##  Setup 

Install Brownie, you'll love it

[`eth-brownie`](https://github.com/eth-brownie/brownie)

## Compiling the contracts

Compile updated contracts: `brownie compile`

Compile all contracts (even not changed ones): `brownie compile --all`

## Running tests

Run tests: `brownie test`

Run tests in verbose mode: `brownie test -v`

Check code coverage: `brownie test --coverage`

Check gas costs: `brownie test --coverage`

Check available fixtures: `brownie --fixtures .`


## Brownie commands

Run script: `brownie run <script_path>`

Run console (very useful for debugging): `brownie console`

## Deploying LiquidityZAP Contracts 

UniswapZAP: 

```bash
brownie run scripts/deploy_UniswapZAP.py
```

BalancerZAP:

```bash
brownie run scripts/deploy_BalancerZAP.py
```

