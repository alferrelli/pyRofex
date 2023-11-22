import secret
import pyRofex
import datetime
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

"""
Compra contado venta 48 Hs
"""
#pyRofex.initialize(user=secret.USER,
#                    password=secret.PASSWORD,
#                    account=secret.ACCOUNT,
#                    environment=pyRofex.Environment.LIVE)

pyRofex.initialize(user="20215883931",
                    password="148_Halcon_148",
                    account="38335",
                    environment=pyRofex.Environment.LIVE)

# logger = object


# tasa2d = {
#     'symbol': "MERV - XMEV - PESOS - 2D",
#     'marketData': {
#         'OF': [{'price': 0.0, 'size': 0}],
#         'BI': [{'price': 0.0, 'size': 0}]
#     }
# }

# instrument1 = {
#     'istrument_type':'bonds',
#     'symbol': 'MERV - XMEV - AL30 - CI',
#     'marketData': {
#         'OF': [{'price': 0.0, 'size': 0}],
#         'BI': [{'price': 0.0, 'size': 0}]
#     }
# }
# instrument2 = {
#     'istrument_type':'bonds',
#     'symbol': 'MERV - XMEV - AL30 - 48hs',
#     'marketData': {
#         'OF': [{'price': 0.0, 'size': 0}],
#         'BI': [{'price': 0.0, 'size': 0}]
#     }
# }


# def market_data_handler(message):

#     # print("Market Data Message Received----------: {0}".format(message))
#     # logger.info("Market DAta Received")
#     buy = message['marketData'][pyRofex.MarketDataEntry.BIDS.value]
#     sell = message['marketData'][pyRofex.MarketDataEntry.OFFERS.value]
    
    
#     if buy is None:
#         print("Nadie Compra None")
#         logger.info("Nadie Compra")
#         return
#     else:
#         if  len(buy)==0:
#             print("Nadie Compra Vacio")
#             logger.info("Nadie Compra Vacio")
#             return
    
#     if sell is None:
#         print("Nadie Vende")
#         logger.info("Nadie Vende")
#         return
#     else:
#         if  len(sell)==0:
#             print("Nadie Vende")
#             logging.info("Nadie Vende")
#             return



    




# def error_handler(message):
#     print("Error Message Received: {0}".format(message))


# def exception_handler(e):
#     print("Exception Occurred: {0}".format(e.msg))


# pyRofex.init_websocket_connection(market_data_handler=market_data_handler,
#                                   error_handler=error_handler,
#                                   exception_handler=exception_handler)


# # 4-Subscribes to receive market data messages
# instruments = [instrument1['symbol'],instrument2['symbol'],tasa2d['symbol']]  # Instruments list to subscribe
# entries = [pyRofex.MarketDataEntry.BIDS,
#            pyRofex.MarketDataEntry.OFFERS]

# pyRofex.market_data_subscription(tickers=instruments,
#                                  entries=entries)

# # Subscribes to an Invalid Instrument (Error Message Handler should be call)
# #pyRofex.market_data_subscription(tickers=["InvalidInstrument"],
#  #                                entries=entries)

scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name("c:/Users/Adrian/Documents/Adrian/Python/pyRofex/sheets/python-tablero.json",scope)
client = gspread.authorize(credentials)

# sheet = client.create("PrimeraBase")
# sheet.share("alferrelli@gmail.com",perm_type="user", role="writer")

sheet = client.open("PrimeraBase").sheet1


sheet.update([df.columns.tolist()] + df.values.tolist())
# time.sleep(20)
# pyRofex.close_websocket_connection()