const path = require('path');
const fs = require('fs');
const solc = require('solc')

const inboxPath = path.resolve(__dirname, 'contracts', 'Inbox.sol');

const source = fs.readFileSync(inboxPath, 'utf8');

// const data = solc.compile(source, 1)

// console.log(data);

// Interface -> Bridge between solidity and js. can be use to call all callable function
// Bytecode -> can be deployed into solidity.
module.exports = solc.compile(source, 1).contracts[":Inbox"];