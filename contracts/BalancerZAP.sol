pragma solidity ^0.6.12;


//:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
//
// LiquidityZAP - BalancerZAP
//   Copyright (c) 2020 deepyr.com
//
// BalancerZAP takes ETH and converts to a Balancer Pool Tokens (BTP). 
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.  
// If not, see <https://github.com/apguerrera/LiquidityZAP/>.
//
// The above copyright notice and this permission notice shall be included 
// in all copies or substantial portions of the Software.
//
// Authors:
// * Adrian Guerrera / Deepyr Pty Ltd
//
// ---------------------------------------------------------------------
// SPDX-License-Identifier: GPL-3.0-or-later                        
// ---------------------------------------------------------------------

import "../interfaces/IWETH9.sol";
import "../interfaces/IERC20.sol";
import "../interfaces/IBPool.sol";
import "../interfaces/IUniswapV2Pair.sol";
import "./Utils/SafeMath.sol";
import "./Utils/UniswapV2Library.sol";

contract BalancerZAP {

    using SafeMath for uint256;

    address public _token;
    address public _balancerPool;
    address public _tokenWETHPair;
    IWETH public _WETH;
    bool private initialized;

    function initBalancerZAP(address token, address balancerPool, address WETH, address tokenWethPair) public  {
        require(!initialized);
        _token = token;
        _balancerPool = balancerPool;
        require(IERC20(_token).approve(balancerPool, uint(-1)));
        _WETH = IWETH(WETH);
        _tokenWETHPair = tokenWethPair;
        initialized = true;
    }

    fallback() external payable {
        if(msg.sender != address(_WETH)){
             addLiquidityETHOnly(msg.sender);
        }
    }

    /**
     * @dev Converts ETH to Balancer Pool Tokens (BPT)
     */
    function addLiquidityETHOnly(address payable to) public payable {
        require(to != address(0), "Invalid address");

        uint256 buyAmount = msg.value;
        require(buyAmount > 0, "Insufficient ETH amount");
        _WETH.deposit{value : msg.value}();

        (uint256 reserveWeth, uint256 reserveTokens) = getPairReserves();
        uint256 outTokens = UniswapV2Library.getAmountOut(buyAmount, reserveWeth, reserveTokens);
        
        _WETH.transfer(_tokenWETHPair, buyAmount);

        (address token0, address token1) = UniswapV2Library.sortTokens(address(_WETH), _token);
        IUniswapV2Pair(_tokenWETHPair).swap(_token == token0 ? outTokens : 0, _token == token1 ? outTokens : 0, address(this), "");

        _addLiquidity(outTokens, to);

    }

    /**
     * @dev User needs to have approved this contract to transferFrom tokens
     */
    function addLiquidityTokenOnly(uint256 tokenAmount, address to) public  {
        require(to != address(0), "Invalid address");
        require(tokenAmount > 0, "Insufficient token amount");

        require(IERC20(_token).transferFrom(msg.sender, address(this), tokenAmount)); 
        _addLiquidity(tokenAmount, to);

    }

    function _addLiquidity(uint256 tokenAmount, address to) internal {

        //mint BPTs 
        uint256 bptTokens = IBPool(_balancerPool).joinswapExternAmountIn( _token, tokenAmount, 0);
        require(bptTokens > 0, "Insufficient BPT amount");
    
        //transfer tokens to user
        require(IBPool(_balancerPool).transfer(to, bptTokens));

    }

    function getPairReserves() internal view returns (uint256 wethReserves, uint256 tokenReserves) {
        (address token0,) = UniswapV2Library.sortTokens(address(_WETH), _token);
        (uint256 reserve0, uint reserve1,) = IUniswapV2Pair(_tokenWETHPair).getReserves();
        (wethReserves, tokenReserves) = token0 == _token ? (reserve1, reserve0) : (reserve0, reserve1);
    }


}