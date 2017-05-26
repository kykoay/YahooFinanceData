# YahooFinanceData
Yahoo Finance data retrieval module that addresses May 16th 2017 changes that broke all existing Yahoo Finance modules.

## Description:
On May 16th 2017, Yahoo Finance made some changes that impacted the ability of various python modules that retrieves Yahoo Finance data. 
Thanks to the discussion on StackOverflow and the effort of Jev Kuznetsov, I am able to write this module that helped me retrieve Yahoo
Finance data. 

## What is contained in this repository
* YFData.py
### Description:
This is the module that has two classes. The first class is the YahooPrice class that allows the user to create objects containing tickets, 
time range to retrieve data. The user can then access the attributes of the object. Of particular interest is the df attribute, as that is
a data frame containing the date , open,close,adjusted close , high, low prices of the ticker along with the traded volume. 

The second class available on this module is the YahooFx class. Upon initiation, the user can access the bid price attribute of the foreign 
currency. Note that there are various data like previous close price, interday range etc. I will add those attributes in the future.
* Illustration.py
### Description:
Illustration.py is a script that shows how the YFData.py module is used.
