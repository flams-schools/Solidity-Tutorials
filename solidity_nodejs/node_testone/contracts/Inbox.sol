// SPDX-License-Identifier: MIT

pragma solidity ^0.4.17;

contract Inbox 
{
    string public message;

    // constructor -- am not sure if it has been changed to constructor
    function Inbox (string initialMessage) public
    {
        message = initialMessage;
    }

    function setMessage (string newMessage) public 
    {
        message = newMessage;
    }

    // view == function type && returns (string) == return type
    function getMessage () public view returns (string)
    {
        return message;
    }
}
