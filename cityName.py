from bs4 import BeautifulSoup
import os

cityName=[]
GovData={}
def OnlyCharNum(s,oth=''):
	fomart = '0123456789'
	for c in s:
	    if not c in fomart:
	        s = s.replace(c,'')
	return s
def CleanN(s,oth=''):
    for c in s:
        if c in '\n':
            s=s.replace(c,'')
    return s

for file in os.listdir("C:\\Users\\User\\Desktop\\BS\\govdata"):
    if file.endswith(".html"):
        Path=os.path.join("C:\\Users\\User\\Desktop\\BS\\govdata",file)
        with open(Path,'rb') as page:
            soup=BeautifulSoup(page,features="html.parser")
            for txt in soup.find_all("td",{"headers":"city_Name"}):
                cityName.append(CleanN(txt.text))
        print(OnlyCharNum(Path),cityName)
        #GovData[OnlyCharNum(Path)]=cityName
        cityName.clear()
print(GovData)