from bs4 import BeautifulSoup
from tabulate import tabulate
import matplotlib.pyplot as plt
import pandas as pd
import requests

page=requests.get("https://www.imdb.com/search/title/?countries=in&sort=moviemeter&title_type=tv_series")
soup=BeautifulSoup(page.content,'html.parser')

# print(soup)
# print()
# print(soup.find_all('a'))
tv=soup.find(id="main")
article=soup.find('div',class_="lister-item-content")
hd=article.h3.a.text
print(hd)

print(tv.find('p').get_text())
print()
# print(week)
items=tv.find_all(class_="lister-item mode-advanced")
an=tv.find('a')['class']

compact=soup.find_all('p',class_='text-muted')
print(compact)
# print(an)

# print(items[0])
print(items[0].find(class_="lister-item-header").get_text())
print(items[0].find(class_="inline-block ratings-imdb-rating").get_text())
print(items[0].find(class_="sort-num_votes-visible").get_text())
print()
name=[item.find('div',class_="lister-item-content").h3.a.text for item in items ]
ratin=[item.find(class_="inline-block ratings-imdb-rating").get_text() for item in items]
vote=[item.find('p',class_="sort-num_votes-visible",name='nv').p.text for item in items]
# new_content = names.replace('\n', '')
rep="'Votes:','\n'"

rating = [sub.replace('\n', ' ') for sub in ratin]
votes = [sub.replace(rep, ' ') for sub in vote]

print(name)
print(rating)
print(votes)
print()
popularity=pd.DataFrame(
    {'show name':name,
     'rating':rating,
     'votes':votes,}
 )
print(popularity)
popularity.to_csv('tvshow.csv')
print()

headers=['sno','show-name','rating','votes']

print(tabulate(popularity,headers=headers,tablefmt='grid'))
