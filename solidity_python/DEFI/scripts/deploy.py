import os
from brownie import accounts, USDC, AUSD, DefiBank
from dotenv import load_dotenv

# please make sure you import the contract name 
# not the file name
# loadenv will load all env in that script

load_dotenv()

def main():
    account = accounts.add(os.getenv("PRIVATE_KEY"))
    usdc_addr = USDC.deploy({"from": account})
    ausd_addr = AUSD.deploy({"from": account})
    DefiBank.deploy(usdc_addr, ausd_addr, {"from": account})
