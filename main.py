#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns
##
#   Project: shoeBot
#   Filename: main.py
#   Author: Daniel Takyi
#   Purpose:
##
from bs4 import BeautifulSoup
from urllib.request import urlopen
from difflib import SequenceMatcher

from helper import *

import os
from time import sleep
from keys import *
from pprint import pprint
from airtable import Airtable


def similar(a,b):
    return SequenceMatcher(None, a, b).ratio()

url = "https://www.footlocker.ca/en/category/mens/shoes.html?query=mens%2Bshoes%3Aprice-desc%3AisNewarrival%3ANEW%2BARRIVALS&sort=newArrivals&currentPage=0"
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')
type(soup)

## Search parameters for wanted shoes' names
search_param1 = 'Jordan AJ 1'
search_param2 = 'Jordan Retro'
search_param3 = 'Nike Air'



## List of available shoes that are wanted
shoeRack = soup.find_all('span', attrs={'class': 'ProductName-primary'})
checklist, foundShoes = organizeShoes(search_param1, search_param2, search_param3, shoeRack)


## Find list of available wanted shoes and merge into tuple with shoe names
shoePriceList = soup.find_all('span', attrs={'class': 'ProductPrice'})
foundPrices = organizePrices(checklist, shoePriceList)
shoeCatalogue = conjoin(foundShoes, foundPrices)

i = 0
airtable = Airtable(base_key, table_name, api_key)
#for i in range(len(shoeCatalogue)):
#    airtable.insert({'binid': i, 'name': shoeCatalogue[i][0], 'price': shoeCatalogue[i][1]})
#    sleep(0.3)

## Compare current results with past results from database
pages = airtable.get_iter(sort=[("binid", 'asc')])
checkForUpdate(pages, shoeCatalogue)


 

#read from database to see if still in order (seach records in order 1 by 1)
#rewrite to csv or xml or database if not in order: the shoe, shoeprice, number of shoes

#send me notification if not in order
#(maybe this can be done in this script instead of a new one)
