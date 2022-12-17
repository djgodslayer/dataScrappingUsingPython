#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests

url="https://www.cricketworld.com/cricket/series/asia-cup-2022/stats/batting-most-runs/125645"

page= requests.get(url)

soup= BeautifulSoup(page.text, 'html.parser')
# soup.find_all('table') - ALternate method for finding table tag
soup.table.find_all(string=True)

tabled= soup.find('table', {"class":"rankingTable batting_highest_strikerate"})


headers=[]
for i in tabled.find_all('th'):
    title=i.text
    if title not in headers:
        headers.append(title)
    else: pass



cricketStats=pd.DataFrame(columns= headers)
cricData={}

for i in headers:
    cricData[i]=[]

for j in tabled.find_all('tr')[1:]:
    rdata=j.find_all('td')
    row=[i.text for i in rdata]
    for m in range(len(row)):
        cricData[f'{headers[m]}'].append(row[m])
  
for j in range(len(cricData['Player'])):
    if "." in cricData['Player'][j]:
        n=cricData['Player'][j].replace(".","")    
    else: pass
    cricData['Player'][j]=n
    # print(j)

for j in range(len(cricData['Player'])):
    if j<=9:
        n=cricData['Player'][j][2:]    
    else: 
        n=cricData['Player'][j][3:]
    cricData['Player'][j]=n

# print(cricData["Player"])  
cricketStats=pd.DataFrame(cricData)
# print(cricketStats)

cricketStats.to_csv('C:\\Users\\divya\\OneDrive\\Documents\\Github\\Asia_Cup_2022_Batting_Stats.csv', index=False)

cstats= pd.read_csv('C:\\Users\\divya\\OneDrive\\Documents\\Github\\Asia_Cup_2022_Batting_Stats.csv')
print(cstats)


# Shows the indivdual total runs made by a player throughout the whole series 
sns.barplot(x ='Player', y ='RUNS', data = cstats,  
            palette ='plasma')


# Shows the number of times a particular number of players that have been not out throughout the whole series
sns.countplot(y ='NO', data = cstats) 


# %%
