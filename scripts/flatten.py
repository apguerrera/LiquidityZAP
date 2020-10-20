import subprocess

# run  `python scripts/flatten.py`

CONTRACT_DIR = "contracts/"

def flatten(mainsol, outputsol):
    pipe = subprocess.call("scripts/solidityFlattener.pl --contractsdir={} --mainsol={} --outputsol={} --verbose"
                           .format(CONTRACT_DIR, mainsol, outputsol), shell=True)
    print(pipe)

def flatten_contracts():
    flatten("BalancerZAP.sol", "flattened/BalancerZAP_flattened.sol")
    flatten("UniswapZAP.sol", "flattened/UniswapZAP_flattened.sol")


flatten_contracts()