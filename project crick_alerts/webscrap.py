import requests
from bs4 import BeautifulSoup
url="https://www.bitdegree.org"

r= requests.get(url)
htmlContent=r.content
# print(htmlContent)
soup=BeautifulSoup(htmlContent,'html.parser')
# print(soup.prettify)
title=soup.title
print(type(title.string))
paras=soup.find('p')
print(soup.find('p')['class'])
print(soup.find_all("p",class_="text"))
print(soup.find('p').get_text())
anchor=soup.find_all('a')
all_links=set()
for link in anchor:
    if(link.get('href') !='#'):
        linktext=link.get('href')
        all_links.add(link)
        print(linktext)
comment= "<p> this is a comment</p> "
soup2=BeautifulSoup(comment)
print((soup2.p.string))
