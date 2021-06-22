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


import os
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
#search_param4 =


## List of available shoes that are wanted
shoeRack = soup.find_all('span', attrs={'class': 'ProductName-primary'})
i = 0
checklist = []
foundShoes = []
for shoeBox in shoeRack:
    shoe = shoeBox.text.strip()
    if search_param1 in shoe:
        print(shoe)
        checklist.append(1)
        foundShoes.append(shoe)
    elif search_param2 in shoe:
        print(shoe)
        checklist.append(1)
        foundShoes.append(shoe)
    elif search_param3 in shoe:
        print(shoe)
        checklist.append(1)
        foundShoes.append(shoe)
    else:
        checklist.append(0)
    i += 1

## Find list of available wanted shoes and merge into tuple with shoe names
shoePriceList = soup.find_all('span', attrs={'class': 'ProductPrice'})
i = 0
j = 0
for shoePrice in shoePriceList:
    if checklist[i] == 1:
        price = shoePrice.text.strip()
        print(price)
        foundShoes[j] = tuple((foundShoes[j], price))
        j += 1
    
    i += 1

i = 0
for i in range(j):
    print(foundShoes[i])

airtable = Airtable(base_key, table_name, api_key)
print(airtable)

#read from database to see if still in order
#write to csv or xml or database if not in order: the shoe, shoeprice, number of shoes

#send me notification if not in order
#(maybe this can be done in this script instead of a new one)
