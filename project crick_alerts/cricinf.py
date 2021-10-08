import requests
import time
from bs4 import BeautifulSoup
t_end= time.time()+ 0.5
t_start=time.time() +6
url="https://www.espncricinfo.com"

r=requests.get(url)
htmlContent=r.content

soup=BeautifulSoup(htmlContent, 'html.parser')
tag=soup.find_all( "div",class_="score-detail fadeIn-enter-done")
while time.time() < t_start:
    k=[]
    # while time.time() < t_end:
    for i in range(0,5):
      new=  soup.find( "span",{'class':'score'}).text
      k.append(new)
      # print(k)
    for i in range(0,len(k)-2) :
        if(k[i]!=k[i+1]):
            print(k[i]) 
        else:print(k[i])    
      
     
 

