import urllib
from datetime import datetime, timedelta
import requests
import datetime as dt
import string
import time
import numpy as np
import pandas as pd
import re
import json
import io

######################################
### Reference: 
### https://github.com/sjev/trading-with-python/blob/master/scratch/get_yahoo_data.ipynb
### Jev Kuznetsov described what happened and provided an excellent tutorial on how to retrieve the data.
### Foreign currency prices are accessed differently as historical data is not provided. 
#####################################

class YahooPrice(object):
	def __init__(self,datefrom,dateto,ticker):
		self.datefrom = np.datetime64(datefrom)  #Date from must be in tuple format. Eg 2017 May 21st is 
		self.dateto = np.datetime64(dateto)
		self.ticker = ticker
		self.datefromsec = int((self.datefrom - np.datetime64('1970-01-01T00:00:00Z')) / np.timedelta64(1, 's') )
		self.datetosec = int((self.dateto - np.datetime64('1970-01-01T00:00:00Z')) / np.timedelta64(1, 's')  )
		self.url = requests.get('https://finance.yahoo.com/quote/'+ self.ticker +'/history')
		self.crumb = self.url.text.split('"CrumbStore"')[1].split('"crumb":')[1].split(',')[0].replace('}','').replace('"','')
		self.cookie = self.url.cookies['B']
		self.data = requests.get('https://query1.finance.yahoo.com/v7/finance/download/' + self.ticker +'?period1={0}&period2={1}&interval=1d&events=history&crumb={2}'.format(self.datefromsec,self.datetosec,self.crumb),cookies={'B':self.cookie})
		self.buf = io.StringIO(self.data.text)
		self.df = pd.read_csv(self.buf,index_col = 0 )

class YahooFx(object):
	def __init__ (self,fxticker):
		self.fxticker = fxticker
		self.url = urllib.urlopen('https://ca.finance.yahoo.com/quote/{0}/?p={1}'.format(self.fxticker,self.fxticker)).read()
		self.headlinequote = self.url.split('"symbol":"{0}"'.format(self.fxticker)+',"price":{"regularMarketOpen":{"raw":')[1].split(',"regularMarketPrice":{"raw":')[1].split(',"fmt"')[0]
		self.bid = self.url.split('"symbol":"{0}"'.format(self.fxticker)+',"price":{"regularMarketOpen":{"raw":')[1].split('"bid":{"raw":')[1].split(',"fmt"')[0]
		self.ask = self.url.split('"symbol":"{0}"'.format(self.fxticker)+',"price":{"regularMarketOpen":{"raw":')[1].split('"ask":{"raw":')[1].split(',"fmt"')[0]

