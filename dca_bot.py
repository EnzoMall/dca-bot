from binance.client import Client
import time

API_KEY = "..."
API_SECRET = "..."

client = Client(API_KEY, API_SECRET, testnet=True)
print("Connecté au testnet Binance !")
daily_money = 10

while True:
    compte = client.get_account()
    balances = compte["balances"]

    for asset in balances:
        if asset["asset"]=="USDT":
            print(f"Solde USDT : {asset['free']} $")
    
    order = client.order_market_buy(symbol="BTCUSDT", quoteOrderQty=daily_money)
    
    print(f"Achat éxécuté !")
    print(f"Prix BTC : {order['fills'][0]['price']} $")
    print(f"USDT dépensé : {order['cummulativeQuoteQty']} $")
    print("---------------------------------")
    
    time.sleep(86400)
