const assert = require('assert');
const ganache = require('ganache-cli')
const Web3 = require('web3');
const { interface, bytecode } = require('../compile')

const web3 = new Web3(ganache.provider());


let accounts;
let inbox;
const INITIAL_STRING = 'Hi there!'

beforeEach(async () => {
  // Get all accounts
  accounts = await web3.eth.getAccounts()
  // .then(fetchedAccounts => { console.log(fetchedAccounts);})

  // use one of these accounts to deploy the contracts
  inbox = await new web3.eth.Contract(JSON.parse(interface))
    .deploy({ data: bytecode, arguments: ['Hi there!']})
    .send({ from: accounts[0], gas: '1000000'})
})

describe('Inbox', () => {
  it('deploys a contract', () => {
    // console.log(inbox)

    // makes sure that whatever is in that function is a value that exists
    assert.ok(inbox.options.address)
  })

  it('has a default message', async () => {
    const message = await inbox.methods.message().call();
    assert.equal(message, 'Hi there!')
  })

  it('can change the message on the contract', async () => {
    await inbox.methods.setMessage('bye').send({ from: accounts[0] });

    const message = await inbox.methods.message().call();
    assert.equal(message, 'bye');
  })
})