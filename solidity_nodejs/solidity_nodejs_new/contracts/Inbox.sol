// SPDX-License-Identifier: MIT

pragma solidity ^0.8.9;

contract Inbox 
{
    string public message;

    // constructor -- am not sure if it has been changed to constructor
    constructor (string memory initialMessage)
    {
        message = initialMessage;
    }

    function setMessage (string memory newMessage) public 
    {
        message = newMessage;
    }

    // view == function type && returns (string) == return type
    function getMessage () public view returns (string memory)
    {
        return message;
    }
}
