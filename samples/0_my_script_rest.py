import secret
import pyRofex
import time

pyRofex.initialize(user=secret.USER,
                   password=secret.PASSWORD,
                   account=secret.ACCOUNT,
                   environment=pyRofex.Environment.REMARKET)



instrument1 = "MERV - XMEV - GGAL - 48hs"
instrument2 = "MERV - XMEV - GGAL - CI"

entries = [pyRofex.MarketDataEntry.BIDS, pyRofex.MarketDataEntry.OFFERS, pyRofex.MarketDataEntry.LAST]
market_data = pyRofex.get_market_data(instrument1,entries)



status=pyRofex.send_order(instrument1,10,pyRofex.OrderType.LIMIT,pyRofex.Side.BUY,price=90)
estado=status['status']

if status['status']=='OK':
    print ("ESTADO OKKKKKKKKKKKKKK")

