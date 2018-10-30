import os
import sys
import urllib.request

user="Rollens"
password="rollens0429"

path="C:\\Users\\User\\Desktop\\BS\\TyphoonData\\"
url="http://rdc28.cwb.gov.tw/TDB/ctrl_download_area/download_file/year/2013/2013.Data.zip"

for i in range (1958,2018):
    Year=str(i)
    Path=path+Year
    os.mkdir(Path)
    """url="http://rdc28.cwb.gov.tw/TDB/ctrl_download_area/download_file/year/"+Year+"/"+Year+".Data.zip"
    filedata=urllib.request.urlopen(url)
    data=filedata.read()
    with open(Path,'wb')as f:
        f.write(data)"""