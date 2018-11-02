# -*- coding: utf-8 -*-
import bs4
import requests
import re
from firebase import firebase
firebase=firebase.FirebaseApplication('https://sample1-ae95d.firebaseio.com/')
firebase.delete('/image',None)
res=requests.get('https://indianexpress.com/section/sports/')
soup=bs4.BeautifulSoup(res.text,'lxml')
title=soup.select('.title')
for articles in soup.select('.articles'):
    for title in articles.select('.title'):
        for p in articles.select('p'):
            for image in articles.select('.snaps'):
                for link in image.select('img'):
                    if link.get('src')=='https://s0.wp.com/wp-content/themes/vip/plugins/lazy-load-0.7/images/1x1.trans.gif':
                        continue
                    else:                        
                        print(link.get("src"))
                        print(title.text)
                        for i in title.find_all('a',href=True):
                            print(i['href'])
                        print(p.text)            
                        print('\n\n')
                        additem=firebase.post('/image',{'name':p.text,'uri':link.get("src"),'title':title.text,'link':i['href']})
res2=requests.get('http://www.espn.in/football/')
soup2=bs4.BeautifulSoup(res2.text,'lxml')
title2=soup2.select('section')
print(title2)
austeam=requests.get('http://www.espncricinfo.com/australia/content/player/country.html?country=2')
aussoup=bs4.BeautifulSoup(austeam.text,'lxml')

for player in aussoup.select('.playersTable'):
    for i in player.select('tr'):
        for j in i.select('td'):
            print(j.text)
    print(player.text)
                
