import requests
import bs4


name=input('who are you looking for?\n')
res=requests.get('https://www.instadp.com/profile/{}'.format(name))
soup=bs4.BeautifulSoup(res.text,'lxml')
s1=soup.find('img').get('src')
download=requests.get(s1)
with open(name+'.jpg',"wb") as f:
    f.write(download.content)