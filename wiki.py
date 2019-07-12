import requests
import bs4
while True:
    usr=input('what are you trying to find?\n')
    res=requests.get('https://en.wikipedia.org/wiki/{}'.format(usr))
    soup=bs4.BeautifulSoup(res.text,'lxml')
    try:
        s1=soup.find('div',attrs={'class':'mw-parser-output'})
        s2=s1.find('p')
        s3=s2.find_next_sibling('p')
        if s3==None:
            s4=s3.find_next_sibling('p')
            print(s4.get_text())
        else:
            print(s3.get_text())
    except AttributeError:
        print('the term you are looking for is undefined\nTry again please...')
    usr=input('would you like to try again?\n')
    if usr=='yes':
        continue
    if usr=='no':
        print('thank you!')
        break
