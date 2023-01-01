import pandas as pd
import requests
from bs4 import BeautifulSoup

r=requests.get('https://markets.businessinsider.com/ajax/ExchangeRate_ListWithShortNameExcludes?currency=EUR')
htmlContent=r.content
soup= BeautifulSoup(htmlContent, 'html.parser')

# print(soup.prettify())

columns=soup.find_all('thead')
headers=[]

for i in columns:
    headers.append((i.get_text()).strip())
headers=headers[0]
columns=headers.split('\n')
columnHead=[]

for i in columns:
    columnHead.append(i.strip())
columns=[]    

for i in columnHead:
    if i=='':
        pass
    else:
        columns.append(i)

# print(columns)

CurrExcEuro=pd.DataFrame(columns=columns)

ExcData={}
for i in columns:
    ExcData[i]=[]
table=soup.find('table', {'class':'table table--col-1-font-color-black table--suppresses-line-breaks table--fixed'})

# print(table)

for j in table.find_all('tr'):
    rdata= j.find_all('td')
    row=[i.text for i in rdata]
    rowData=[]
    for i in row:
        rowData.append(i.strip())
    row=[]    
    for i in rowData:
        if i=='':
            pass
        else:
            row.append(i)
    if row==[]:
        pass
    else:
        for i in range(len(columns)):
            ExcData[f'{columns[i]}'].append(row[i])

CurrExcEuro=pd.DataFrame(ExcData)
print(CurrExcEuro)

CurrExcEuro.to_csv("C:\\Users\\divya\\OneDrive\\Documents\\Github\\Scrapping_3\\Euro_Currency_Exc_2023.csv", index=False)

Euro_Data=pd.read_csv("C:\\Users\\divya\\OneDrive\\Documents\\Github\\Scrapping_3\\Euro_Currency_Exc_2023.csv")
print(Euro_Data)
