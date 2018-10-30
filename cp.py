import shutil

for i in range (1958,1960):
    path="C:\\Users\\User\\Desktop\\BS\\Station_daily_man_1958_1959\\"+str(i)
    des="C:\\Users\\User\\Desktop\\BS\\TyphoonData\\"+str(i)+"\\WeatherData"
    shutil.copytree(path,des)

