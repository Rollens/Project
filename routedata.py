import numpy as np 
import pandas as pd 

path="C:\\Users\\User\\Desktop\\BS\\TyphoonData\\2017\\TrackData\\2017.HAITANG.Track.txt"
Path="C:\\Users\\User\\Desktop\\BS\\TyphoonData\\2017\\WeatherData\\HAITANG.txt"
data=pd.read_csv(path,sep=" ")
#Data=pd.read_csv(Path,sep=" ")
print(data)