



<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
## Table of Contents

- [Introduction](#introduction)
- [Quickstart](#quickstart)
- [Installation](#installation)
- [Features](#sniper)
- [Contact](#contact)



<!-- END doctoc generated TOC please keep comment here to allow auto update -->


# Introduction
The **FASTEST** and most profitable Solana bot on GitHub. Profits in excess of 100x achieved with this tool and the First Block Exploit.

<img src="https://files.catbox.moe/uvignr.gif" width="400" alt="image">

 
# Quickstart

This project has been made for Python.

## Installation

**Install [Python](https://www.python.org/downloads/)**

**IMPORTANT**: ***When installing Python, click the box "Add python to path" and "Use admin privileges when installing py.exe."***

💾 **Open your terminal/cmd**

<img src="https://www.lifewire.com/thmb/lZqO1iWs6LzvSYkXITCbNmTg2J4=/1305x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/windows-11-cmd-start-menu-a8c1d7d009f64856902c83e8e418563b.png" width="400" alt="image">

💾 **Download this repository & unzip**

<img src="https://files.catbox.moe/qextd1.png" width="400" alt="image">

💾 **Navigate to the directory you downloaded the repository to (often times Downloads)**
```sh
cd Downloads
```
```sh
cd solana-raydium-sniper-main
```
💻 **Install/upgrade pip**
```sh
python -m pip install --upgrade pip
```
💻 **Install the required libs**
```sh
pip install jupiter-python-sdk
```
```sh
pip install -r requirements.txt
```
▶️ **Start**
```sh
python main.py
```
![image](https://files.catbox.moe/654ggm.png)
![image](https://files.catbox.moe/l02bx1.png)

# Sniper

### 🆕 Add a token to snipe
- Add as many wallets as necessary
- Token/Project name
- Token Address
- Amount ($) to buy
- Take Profit ($)
- Stop Loss ($)
- Slippage (%)

If token has a launch date:
- Month
- Day
- Hours
- Minutes

### 🔭 Watch token
You can watch your trading position by selecting the token.<br>

### ✍🏻 Edit tokens
You can modify token info as follow:
- Name
- Address
- Selected Wallet
- Buy Amount
- Take Profit
- Stop Loss
- Slippage
- Launch date
- Delete


# MY OTHER PROJECT: Multichainsniper
Multi chain and multi wallet sniper that works on a variety of decentralized exchanges as well. Optimized methods are used in order to make this one of the fastest, if not the fastest sniper on the market

## Contact
Message me on telegram for more info
- [Telegram](https://t.me/nonlinearlogic)


### Supported chains and exchanges
- Ethereum
    - Uniswap
    - Sushiswap

- Binance smart chain
    - Pancakeswap
    - Sushiswap
    - Apeswap
    - Backeryswap

- Polygon Matic
    - Quickswap
    - Apeswap
    - Defyn

- Kucoin Community Chain
    - Kuswap
    - KoffeSwap

- Okex Chain
    - CherrySwap

- Avalanche Mainnet C-Chain
    - Pangolin
    - Trader Joe

- Fantom Opera
    - Spirit Swap
    - Spooky Swap
    - Protofi

- Cronos Mainnet beta
    - Meerkat
    - VVS Finance
    - Cronaswap

- Harmony chain shard 0
    - Viper

- Metis Andromeda Mainnet
    - Netswap
    - Tethys


### Innovative UI
The bot has a UI which runs in the terminal, this allows you to run the bot on remote servers without needing a display server or having to play with virtual displays as you would with normal UIs.

![Loading screen](https://i.imgur.com/Rave54x.png)
![Working screen](https://i.imgur.com/Kl8FY6u.png)

### Current features
- Multi wallet support
- Support for custom pairs (Tokens that are paired to a different coin than the default one of the exchange)
- Instant buy functionality, you can make the bot Instantly skipping it's normal flow in case something changes after you've started it.
- Automatically detect owner, max buy, trading open functions and sell triggering functions (ex. mint, blacklist and so on)
- Mempool scan for liquidity scanning & trading open scanning
- Option to send multiple buy transactions at the same time (99% all get in the same block at relatively near positions from each other, depends also on the node you use)
- Honeypot prevention, you can set the bot to check if the token is a honeypot before buying.
- Max buy tax and max sell tax prevention, the bot will only sell if the current tax is below the amount you set.
- Anti-bot prevention, options to skip blocks/seconds after liquidity detection, option to skip blocks/seconds after trading enable detection, minimum liquidity check (to be added in v1.0.1) 
- Anti rug

### Changelogs

#### Version 1.0.0
- Initial release
- Added TUI (Text user interface), it's like GUI but you can run your bot in the terminal)
- Added support for multiple wallets
- Added automatic trading enable function detection
- Added automatic bad functions (sell triggering) detection
- Added automatic owner address detection
- Improved mempool speed and overall performance
- Improved sending transactions speed
- Option to change secondary wallets on your own

#### Version 1.0.1
- Fix small bugs from version 1.0.0
- Add option to set gas price and gas limit also from UI rather than config only
- Add netswap and Tethys on Metis chain

#### Version 1.0.2
- Support for ethereum chain and it's new gas system
- Support for buying exact amount of tokens
- Add missing chains and exchanges
- Fix bugs from version 1.0.1

#### Version 1.0.3
- Add rug pull prevention (sell when liquidity is about to be removed or when a bad function is about to be called on the token contract)
- Add option to scroll the token functions table at startup screen
- Add IPC node connection support
- Added anti rug system
- Improvements to mempool scan

#### version 1.1.0
- Implement minimum liquidity option
- Add everything related to selling the tokens, sell certain % of tokens, certain amounts of tokens. Sell based on take profit and stop loss


#### version 1.2.0
- Telegram scrapper added (features in telegram)


#### version 1.3.0
- Contract buy mode added (anti blacklist)
- You will have to deploy a contract on each corresponding chain!

#### version 1.3.1 
- Refactoring/performance improvements
- 

## DISCLAIMER

> [!IMPORTANT]
> Use at your own risk. Loss of funds is the sole responsibility of the user.
