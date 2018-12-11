from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import auc
import numpy as np
import csv

def toF(list):
    output=[]
    for i in list:
        output.append(int(i))
    return output

featureData=[]
AnsData=[]
with open('newdata.txt','r') as data:
    rows=csv.reader(data,delimiter='\t')
    switch=True
    for i in rows:
        if switch:
            label= i
            switch=False
        else:
            featureData.append(i[0:83])
            AnsData.append(i[84])

train_data , test_data , train_label , test_label = train_test_split(featureData,AnsData,test_size=0.2)
knn = KNeighborsClassifier()
knn.fit(train_data,train_label)
pred=knn.predict(test_data)
print("Acc:",accuracy_score(test_label,pred))
#print(knn.predict(test_data))
#rint(test_label)