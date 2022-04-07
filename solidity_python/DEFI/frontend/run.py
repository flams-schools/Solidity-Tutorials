import os
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import SelectField
from brownie import accounts, Contract, network
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = "not easy to guess key"

# Declare he address as global scope
# usdc_contratcAddress = 'get from build/deployments/map.json'
usdc_Address = Contract('get from build/deployments/map.json')
defi_contract = Contract('get from build/deployments/map.json')
account = account.add(os.getenv("PRIVATE_KEY"))


class Form(FlaskForm):
    Faccounts = SelectField('Account', choices=['address account', 'address account', 'address account'])

@app.route('/')
def index():
    # return "<h1>Home Page</h1>"
    return render_template('index.html')

@app.route('/'deposit)
def deposit():
    form = Form()
    AvalableBal = SC_getAccountbal() 10 ** 18
    return render_template('deposit.html', form = form, AvailableBal = AvailableBal)

@app.route('/FundMe')
def  FundMe():
    return render_template('index.html')


@app.route('/depositButton', methods=['GET', 'POST'])
def depositButton():
    if request.method == 'POST':
        depositAmount = request.form.get("depositValue", type=int) * (10 ** 18)
        SC_depositBal(depositAmount)
        DepositedAmount = defi_contract.depositBalance(account) / (10 ** 18)
        AvailableBal = balance = usdcAddress.balanceOf('put in an address balance')
    return render_template('deposit.html', )

def SC_getAccountbal():
    # pass
    # usdcAddress = Contract(usdc_contractAddress)
    balance = usdcAddress.balanceOf('put in an address balance')
    return balance

def SC_depositBal(depositAmount):
    usdc_Address.approve(defi_Address, depositAmount, {"from": account})
    defi_contract.depositToken(depositAmount, {"from": account})

if __name__ == "__main__":
    network.connect('rinkeby')
    app.run()
    network.disconnect()