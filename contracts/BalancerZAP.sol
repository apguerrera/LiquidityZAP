pragma solidity ^0.6.12;


import "../interfaces/IWETH9.sol";
import "../interfaces/IERC20.sol";
import "./Utils/SafeMath.sol";

contract BalancerZAP {

    using SafeMath for uint256;

    address public _token;
    address public _balancerPool;
    bool private initialized;

    function initBalancerZAP(address token, address balancerPool) public  {
        require(!initialized);
        _token = token;
        _balancerPool = balancerPool;
        // approve tokens from balancer
        initialized = true;
    }

    fallback() external payable {
        addLiquidityETHOnly(msg.sender);
    }
    receive() external payable {
        addLiquidityETHOnly(msg.sender);
    }

    function addLiquidityETHOnly(address payable to) public payable {
        require(to != address(0), "Invalid address");

        uint256 buyAmount = msg.value;
        require(buyAmount > 0, "Insufficient ETH amount");

        // Swap ETH for tokens        
        uint tokenAmount = buyAmount;

        _addLiquidity(tokenAmount, to);

    }

    function addLiquidityTokenOnly(uint256 tokenAmount, address payable to) public payable {
        require(to != address(0), "Invalid address");
        require(tokenAmount > 0, "Insufficient token amount");
        _addLiquidity(tokenAmount, to);

    }

    function _addLiquidity(uint256 /*tokenAmount*/, address payable /*to*/) internal {
        // transfer tokens to balancer pool

        //mint BPTs 
        
        //refund dust tokens

    }

}