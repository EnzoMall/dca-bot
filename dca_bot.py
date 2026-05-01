from binance.client import Client
import time

API_KEY = "88LjyQmpM1MYZ6Qn7OZNlt8XVfblxTmMQS3W55fZo32F1ySV0QahPUHMWglkv0ac"
API_SECRET = "4WTtMBrY17uyEAY1DhLm9bs5im1XEcUx0LV4Pubid1aHSCEqHAhKTmSIsgrCSo2o"

#télécommande pour controler binance
client = Client(API_KEY, API_SECRET, testnet=True)
print("Connecté au testnet Binance !")

daily_money = 10

#boucle qui achete e l'infine
while True:
    #voir le compte (dictionnaire)
    compte = client.get_account()
    #clés pour optenir les tokens
    balances = compte["balances"]
    #boucle qui vient chercher le solde restant 
    for asset in balances:
        if asset["asset"]=="USDT":
            print(f"Solde USDT : {asset['free']} $")
    #achter btc
    order = client.order_market_buy(symbol="BTCUSDT", quoteOrderQty=daily_money)
    #visuel
    print(f"Achat éxécuté !")
    print(f"Prix BTC : {order['fills'][0]['price']} $")
    print(f"USDT dépensé : {order['cummulativeQuoteQty']} $")
    print("---------------------------------")
    #temps d'attente
    time.sleep(10)