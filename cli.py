import argparse
from src.components.client import BinanceClient
from src.components.orders import OrderManager

def main():
    parser = argparse.ArgumentParser(description="Binance Testnet Bot")
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True, choices=['BUY', 'SELL'])
    parser.add_argument("--type", required=True, choices=['MARKET', 'LIMIT'])
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    # Enter your Testnet API Keys here
    API_KEY = "dummy_key_123"
    API_SECRET = "secret123"

    try:
        bot_client = BinanceClient(API_KEY, API_SECRET)
        manager = OrderManager(bot_client)
        manager.place_order(args.symbol, args.side, args.type, args.quantity, args.price)
    except Exception as e:
        print(f"Process failed: {e}")

if __name__ == "__main__":
    main()