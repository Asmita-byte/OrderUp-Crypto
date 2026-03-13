from binance.client import Client
import sys
from src.logger import logging
from src.exception import CustomException
import sys

class BinanceClient:
    def __init__(self, api_key, api_secret):
        try:
            logging.info("Binance Testnet Client is initializing...")
            # testnet=True is important here
            self.client = Client(api_key, api_secret, testnet=True)
            
            # To check Connection..
            self.client.futures_account_balance()
            logging.info("Binance Testnet se connection successful!")
            
        except Exception as e:
            raise CustomException(e, sys)