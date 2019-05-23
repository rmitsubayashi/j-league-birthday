from bs4 import BeautifulSoup
import requests
from os.path import split
import matplotlib.pyplot as plt
import numpy

def scrape(url, months): 
    result = requests.get(url)
    content = result.content
    
    soup = BeautifulSoup(content, "html5lib")
    
    allPlayerData = soup.find_all("dl","dl-base")
    
    for playerData in allPlayerData :
        # 5 = 国籍。日本国籍以外の場合のみ表示されている
        countryDataLabel = playerData.find("dt",string="5")
        if countryDataLabel is not None :
            continue
            
        birthdayDataLabel = playerData.find("dt",string="2")
        birthdayData = birthdayDataLabel.find_next("dd")
        birthday = birthdayData.contents[0].split("/")
        month = int(birthday[1])
        months[month-1] = months[month-1] + 1
        

months = [0] * 12        
for i in range(1,19):
    scrape("https://data.j-league.or.jp/SFIX02/search?displayId=SFIX02&selectValue=1&displayId=SFIX02&selectValueTeam=" + str(i), months)

x = numpy.arange(1,13)
y = numpy.array(months)   
plt.bar(x,y)
plt.show()