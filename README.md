# OrderUp-Crypto: Binance Futures Trading Bot

## Project Objective
This is a Python-based trading bot designed to place Market and Limit orders on the Binance Futures Testnet (USDT-M). It features a modular structure with dedicated layers for API interaction, CLI, logging, and error handling.

## Features
* Order Placement: Supports both BUY and SELL sides for Market and Limit orders.
* Robust Logging: All API requests, responses, and errors are logged to a file for auditing.
* Custom Exception Handling: Handles network failures and invalid user inputs gracefully.
* Professional Structure: Organized into `src` components for better reusability.

## Setup Instructions
1. **Clone the Repository**:
   git clone <https://github.com/Asmita-byte/OrderUp-Crypto.git>
   cd binance_testnet

2. Create Environment:
    conda activate testnet_env

3. Install Dependencies:
    pip install -r requirements.txt

4. API Keys:

    * Obtain API Key and Secret from Binance Futures Testnet.

    * (Optional: Set them as environment variables or in a      config file).

## How to Run
    Run the bot via CLI using the following format:
        python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001


## Project Structure

    src/components/: Contains core logic (client, orders).


    src/logger.py: Custom logging configuration.


    src/exception.py: Custom exception handling.


    requirements.txt: Project dependencies.

