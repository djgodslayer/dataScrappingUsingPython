import pandas as pd
from bs4 import BeautifulSoup
import requests

df=pd.read_csv("scienceNews_articles.csv")
num=len(df.index)
def text_extract(url):
    print("\nConnecting to Server.......")
    r=requests.get(url)
    if r.status_code==200:
        print("\nGetting your file ready......")
        htmlcontent=r.content
        soup=BeautifulSoup(htmlcontent,"html.parser")
        h=soup.find("h1",class_={"header-default__title___2wL7r"})
        t=soup.find("div",class_="rich-text single__rich-text___BlzVF")
        try:      
            paras=t.find_all("p")
            article=""
            for i in paras:
                article=article+"\n"+i.text
            try:
                title=h.text
                try:
                    with open(f"scienceNews_Articles/{title}.txt","w") as f:
                        f.write(article)
                except OSError:
                    pass
            except AttributeError:
                pass    
        except AttributeError:
            pass    
        



    else:
        print("\nProblem connecting to server......")
        print("\nError Code: ",r.status_code)

for i in range(num):
    text_extract(df["Article_Link"][i])
    
