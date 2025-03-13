## Loading required libraries
import numpy as np
import pandas as pd

import requests
from bs4 import BeautifulSoup

## Identify the URL
URL='https://yasaswithachowdary28.github.io/WebScraping/'

## Loading the WebPage in Memory using requests library
page=requests.get(URL)

#Check the Status Code of the Page
page.status_code

## Extracting the HTML code of the Webpage
htmlcode=page.text
soup=BeautifulSoup(htmlcode)
htmlcode

content =soup.find('div', attrs={'class':"product-container"})
text=content.text
#print(text)

r1=text.split("\n")
# print(r1)
r2=[]
for i in r1:
   if i!='' and i!='\r':
     r2.append(i)
# print(r2)
r3=[]
for i in r2:
   k=i.strip()
   r3.append(k)
# print(r3)
r4=[]
for i in r3:
  if i!='' and i!='\r':
    r4.append(i)
# print(r4)

names=[]
prices=[]
stock=[]
for i in range(0,len(r4),3):
   names.append(r4[i])
   x=r4[i+1].replace("Price:","")
   x=x.strip()

   prices.append(x)
   y=r4[i+2].replace("Stock:","")
   y=y.strip()
   stock.append(y)

#print(names)
#print(prices)
#print(stock)

## Create a DataFrame and save it in CSV file
df=pd.DataFrame({'Name':names,'Price':prices,'Stock':stock})
print(df)

## saving the dataframe
df.to_csv('products.csv',header=True,index=False)

from google.colab import files
files.download('products.csv')
