from bs4 import BeautifulSoup

cityName=[]

with open("nds.html",encoding="utf8") as page:
    soup=BeautifulSoup(page,features="html.parser")
    for txt in soup.find_all("td",{"headers":"city_Name"}):
        cityName.append(txt.text)

print(cityName)