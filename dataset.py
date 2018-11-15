import numpy as np 
import os
import csv

Tainan_city_id = '467410'
Tainan_city_id2= '467411'
Tainan_county_id = '467420'
Dataset=[]
labellist=['stno','yyyymmdd', 'PS01', 'PS02', 'PS03', 'PS04', 'PS05', 'PS06', 'PS07', 'PS08', 'PS09', 'PS10', 'TX01', 'TX02', 'TX03', 'TX04', 'TX05', 'TX06', 'TD01', 'TD02', 'TD03', 'TD04', 'TX07', 'TX08', 'TX09', 'VP01', 'VP02', 'VP03', 'VP04', 'VP05', 'RH01', 'RH02', 'RH03', 'RH04', 'RH05', 'WD01', 'WD02', 'WD03', 'WD04', 'WD05', 'WD06', 'WD07', 'WD08', 'WD09', 'PP01', 'PP02', 'PP03', 'PP04', 'PP05', 'PP06', 'SS01', 'SS02', 'GR01', 'GR02', 'GR03', 'VS01', 'CD01', 'SD01', 'ST01', 'ST02', 'ST03', 'ST04', 'ST05', 'ST06', 'ST07', 'ST08', 'ST09', 'ST10', 'ST11', 'ST12', 'EP01', 'EP02', 'EP03', 'TG01', 'TS01', 'TS02', 'TS03', 'TS04', 'TS05', 'TS06', 'TS07', 'TS08', 'TS09', 'TS10']
for year in range(1958,2018):
    dir_path="C:\\Users\\User\\Desktop\\BS\\TyphoonData\\"+str(year)+"\\WeatherData"
    for file in os.listdir(dir_path):
        if file.find('_stn') == -1:
            Path=os.path.join(dir_path,file)
            with open(Path,'r') as f:
                with open('./label.txt','a') as wb:
                    label=[]
                    feature=[]
                    dic={}
                    data = f.readlines()
                    for Data in data:
                        if Data.find('stno') !=-1:
                            label=Data.split()
                            for d in label:
                                if d == 'ST02':
                                    label.remove('ST02')
                        if Data.find(Tainan_city_id) !=-1 or Data.find(Tainan_city_id2) !=-1:
                            feature=Data.split()
                            #for info in d_list:
                                #wb.write(info+" ")
                            #wb.write('0\n')
                    for i in range(1,len(label)):
                        dic[label[i]]=feature[i-1]
                    Dataset.append(dic)

with open('./newdata.txt','w') as dt:
    writer=csv.writer(dt,delimiter='\t')
    writer.writerow(labellist)
    for year in range(len(Dataset)):
        for label in labellist:
            if label in Dataset[year]:
                dt.write(Dataset[year][label]+'\t')
            else:
                dt.write('-9999\t')
        dt.write('\n')

#print(Dataset)
