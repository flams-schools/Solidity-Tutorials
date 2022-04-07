import os
from brownie import Contract, accounts
from dotenv import load_dotenv

load_dotenv()

# maij is only what infura speaks with
def main():
    account = accounts.add(os.getenv("PRIVATE_KEY"))
    usdc_contract = Contract("usdc account from build");
    defi_contract = Contract("defi account from build")

    print(f"Before function call Current usdc tokn deposit balance is {defi_contract.depositBalance(account)}")

    usdc_contract.approve(defi_contract, 100, {"from": account})
    defi_contract.depositToken(100, {"from": account})

    print(f"After function call Current usdc token deposit balance is {defi_contract.depositBalance(account)}")

    # test for withdraw function

    defi_contract.withdraw(100, {"from": account})

    print(f"Current balance after withdraw usdc token deposit balance is {defi_contract.depositBalance(account)}")

    #  run script now