import secret
import pyRofex

pyRofex.initialize(user=secret.USER,
                   password=secret.PASSWORD,
                   account=secret.ACCOUNT,
                   environment=pyRofex.Environment.REMARKET)


instrument = "MERV - XMEV - GGAL - 48hs"

entries = [pyRofex.MarketDataEntry.BIDS, pyRofex.MarketDataEntry.OFFERS, pyRofex.MarketDataEntry.LAST]
market_data = pyRofex.get_market_data(instrument, entries, depth=2)

print("Market Data Response for {0}: {1}".format(instrument, market_data))