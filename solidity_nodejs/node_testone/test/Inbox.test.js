const assert = require('assert');
const ganache = require('ganache-cli')
const Web3 = require('web3');

const web3 = new Web3(ganache.provider());


let accounts;

beforeEach(async () => {
  // Get all accounts
  accounts = await web3.eth.getAccounts()
  // .then(fetchedAccounts => { console.log(fetchedAccounts);})

  // use one of these accounts to deploy the contracts
})

describe('Inbox', () => {
  it('deploys a contract', () => {
    console.log(accounts)
  })
})