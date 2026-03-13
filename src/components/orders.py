import sys
from binance.enums import *
from src.logger import logging
from src.exception import CustomException
import sys

class OrderManager:
    def __init__(self, binance_client):
        self.client = binance_client.client

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            logging.info(f"Order Request: {side} {quantity} {symbol} ({order_type})")
            
            params = {
                'symbol': symbol.upper(),
                'side': side.upper(),
                'type': order_type.upper(),
                'quantity': quantity
            }

            if order_type.upper() == 'LIMIT':
                if not price:
                    raise ValueError("LIMIT order ke liye price dena zaroori hai.")
                params['price'] = str(price)
                params['timeInForce'] = TIME_IN_FORCE_GTC

            # Binance Futures API call..
            response = self.client.futures_create_order(**params)
            
            logging.info(f"Order Success! ID: {response['orderId']}")
            print(f"Success: {side} order placed for {symbol}")
            return response

        except Exception as e:
            logging.error(f"Error in Order placement: {str(e)}")
            raise CustomException(e, sys)