import secret
import pyRofex
import datetime
import time
import logging
import calculos as calc

"""
Compra contado venta 48 Hs
"""

pyRofex.initialize(user=secret.USER,
                   password=secret.PASSWORD,
                   account=secret.ACCOUNT,
                   environment=pyRofex.Environment.LIVE)


logger = object


tasa2d = {
    'symbol': "MERV - XMEV - PESOS - 2D",
    'marketData': {
        'OF': [{'price': 0.0, 'size': 0}],
        'BI': [{'price': 0.0, 'size': 0}]
    }
}

instrument1 = {
    'istrument_type':'bonds',
    'symbol': 'MERV - XMEV - AL30 - CI',
    'marketData': {
        'OF': [{'price': 0.0, 'size': 0}],
        'BI': [{'price': 0.0, 'size': 0}]
    }
}
instrument2 = {
    'istrument_type':'bonds',
    'symbol': 'MERV - XMEV - AL30 - 48hs',
    'marketData': {
        'OF': [{'price': 0.0, 'size': 0}],
        'BI': [{'price': 0.0, 'size': 0}]
    }
}


def market_data_handler(message):

    # print("Market Data Message Received----------: {0}".format(message))
    # logger.info("Market DAta Received")
    buy = message['marketData'][pyRofex.MarketDataEntry.BIDS.value]
    sell = message['marketData'][pyRofex.MarketDataEntry.OFFERS.value]
    
    
    if buy is None:
        print("Nadie Compra None")
        logger.info("Nadie Compra")
        return
    else:
        if  len(buy)==0:
            print("Nadie Compra Vacio")
            logger.info("Nadie Compra Vacio")
            return
    
    if sell is None:
        print("Nadie Vende")
        logger.info("Nadie Vende")
        return
    else:
        if  len(sell)==0:
            print("Nadie Vende")
            logging.info("Nadie Vende")
            return



    




def error_handler(message):
    print("Error Message Received: {0}".format(message))


def exception_handler(e):
    print("Exception Occurred: {0}".format(e.msg))


pyRofex.init_websocket_connection(market_data_handler=market_data_handler,
                                  error_handler=error_handler,
                                  exception_handler=exception_handler)


# 4-Subscribes to receive market data messages
instruments = [instrument1['symbol'],instrument2['symbol'],tasa2d['symbol']]  # Instruments list to subscribe
entries = [pyRofex.MarketDataEntry.BIDS,
           pyRofex.MarketDataEntry.OFFERS]

pyRofex.market_data_subscription(tickers=instruments,
                                 entries=entries)

# Subscribes to an Invalid Instrument (Error Message Handler should be call)
#pyRofex.market_data_subscription(tickers=["InvalidInstrument"],
 #                                entries=entries)

def set_my_log():
            logger = logging.getLogger("log")
            formatter = logging.Formatter(
                '%(asctime)s | %(name)s |  %(levelname)s: %(message)s')
            logger.setLevel(logging.DEBUG)

            #stream_handler = logging.StreamHandler()
            #stream_handler.setLevel(logging.INFO)
            #stream_handler.setFormatter(formatter)

            logFilePath = "my.log"
            file_handler = logging.FileHandler(filename=logFilePath)
            file_handler.setFormatter(formatter)
            file_handler.setLevel(logging.DEBUG)

            logger.addHandler(file_handler)
            #logger.addHandler(stream_handler)

            logger.info("Started");
            return (logger)
            

# Wait 5 sec then close the connection
logger = set_my_log()
time.sleep(20)
pyRofex.close_websocket_connection()