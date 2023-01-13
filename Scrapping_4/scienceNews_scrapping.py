import pandas as pd
from bs4 import BeautifulSoup
import requests 

url="https://www.sciencenews.org/"
r=requests.get(url)
htmlcontent=r.content
soup=BeautifulSoup(htmlcontent,"html.parser")
main=soup.find("main", class_={"site-main"})
link_count=0
links=[]

for link in main.find_all("a"):
    h=link.get("href")
    if h not in links and "article" in h:
        links.append(h)
   

df=pd.DataFrame(columns=["Article_Link"])
df["Article_Link"]=links

df.to_csv("scienceNews_articles.csv",index=False)




    

