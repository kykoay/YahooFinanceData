#############Illustration of how to use this module
from YFData import *


check = YahooPrice('2017-05-01','2017-05-20',"XCV.TO")

print check.ticker
print check.data
print check.df.tail(n=5) #Note if you remove .tail(n=5) you get all the data in a dataframe format for the range of date you specified

CADUSD = YahooFx("CAD=X") 
print CADUSD.headlinequote