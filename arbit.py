from pybitx.api import BitX
import os
import pprint
import krakenex
import hmac

pp = pprint.PrettyPrinter(indent=4, width=80)

def format_call(name, results):
    print '-'*80
    print '%50s' % (name,)
    print '-'*80
    pp.pprint(results)
    print '-'*80

def runDemo():
    k = krakenex.API()
    k.load_key('kraken.key')
    f = open('bitx.key', "r")
    user = f.readline().strip()
    password = f.readline().strip()
    api = BitX(user, password)
    kind = 'auth'
    format_call('Krak Ticker   ', k.query_public('Ticker', {'pair': 'XXBTZGBP' }))
    raw_input("Press Enter to continue...")
    format_call('  Ticker   ', api.get_ticker(kind))
    format_call('All Tickers', api.get_all_tickers(kind))
    format_call('Order book ', api.get_order_book(5, kind))
    format_call('   Trades  ', api.get_trades(10, kind))
    format_call('   Orders  ', api.get_orders())
    format_call('Funding address', api.get_funding_address('XBT'))
    format_call('   Balance ', api.get_balance())
    a = raw_input("Press Enter to continue...")
	
if __name__ == '__main__':
    runDemo()
