import requests
from bs4 import BeautifulSoup
import pandas as pd


r=requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')
soup=BeautifulSoup(r.text,'html.parser')
results=soup.find_all('span',attrs={'class':'short-desc'})
first_results=results[0]
#print (first_results.find('strong').text)
#print (first_results.contents[1])
#print(first_results.contents[1][1:-2])
#print(first_results.find('a').text[1:-1])
#print(first_results.find('a')['href'])
records=[]
for result in results:
    date=result.find('strong').text[0:-1] + ',2017'
    lie=result.contents[1][1:-2]
    explanation=result.find('a').text[1:-1]
    url=result.find('a')['href']
    records.append((date,lie,explanation,url))

df=pd.DataFrame(records,columns=['date','lie','explanation','url'])
#print(df.head())
#df['date']=pd.to_datetime[df['date']]
df.to_csv('trump_lies.csv', index=False, encoding='utf-8')
#print(records[0])