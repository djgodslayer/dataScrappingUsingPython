#%%
from bs4 import BeautifulSoup
import pandas as pd
import seaborn as sns
import requests

url="https://www.worldometers.info/coronavirus/"

r=requests.get(url)
htmlContent=r.content

soup=BeautifulSoup(htmlContent, "html.parser")

# print(soup.prettify())
# print(soup.find("table").get_text())

columns=soup.find_all("thead")
# print(columns)
columnsHead=[]
for i in columns:
    if i not in columnsHead:
        columnsHead.append(i.get_text())
    else: 
        pass

columns=columnsHead
columnsHead=columns[0]    
columns=columnsHead.split("\n")
columns[15]=columns[15]+columns[16]
columns[16]=columns[18]
columns[12]='Tot Cases/1M pop'
headers=[]
for i in range(3,17):
    headers.append(columns[i])

# print(headers)
covidStats=pd.DataFrame(columns= headers)
covidData={}
for i in headers:
    covidData[f'{i}']=[]

table=soup.find('tbody', {'class':''})

for j in table.find_all('tr'):
    rdata=j.find_all('td')
    row=[i.text for i in rdata]
    new=row[1:15]
    for m in range(len(new)):
        if new[m].strip()=="N/A" or new[m].strip()=="":
            covidData[f'{headers[m]}'].append("0")
        else:
            covidData[f'{headers[m]}'].append(new[m].strip())

for i in range(len(headers)):
    t=covidData[f'{headers[i]}']
    covidData[f'{headers[i]}']=t[8:]


covidStats=pd.DataFrame(covidData)
# print(covidStats)

covidStats.to_csv("Scrapping_2\\Covid_Data_2022.csv", index=False)

cstats=pd.read_csv("Scrapping_2\\Covid_Data_2022.csv")
print(cstats)
# %%
