from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import auc
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
import numpy as np
import csv

def toF(list):
    output=[]
    for i in list:
        output.append(int(i))
    return output

featureData=[]
AnsData=[]

with open('newdatawithans.txt','r') as data:
    rows=csv.reader(data,delimiter='\t')
    switch=True
    for i in rows:
        if len(i)!=0:
            if switch:
                label= i
                switch=False
            else:
                featureData.append(i[2:83])
                AnsData.append(i[84])
"""
for r in featureData:
    for i in range(len(r)):
        if r[i]=='-9999':
            r[i]=None"""

train_data , test_data , train_label , test_label = train_test_split(featureData,AnsData,test_size=0.2)
Train_data=np.asarray(train_data)
Test_data=np.asarray(test_data)
Train_label=np.asarray(train_label)
Test_label=np.asarray(test_label)
#KNN
knn = KNeighborsClassifier()
knn.fit(Train_data,Train_label)
knn_pred=knn.predict(Test_data)
print('KNN_Acc:',accuracy_score(Test_label,knn_pred))
#XGB
XGB=XGBClassifier()
XGB.fit(Train_data,Train_label)
print('XGB_Acc:',XGB.score(Test_data, Test_label))
#RFC
rfc=RandomForestClassifier()
rfc.fit(Train_data,Train_label)
print('RFC_Acc:', rfc.score(Test_data, Test_label))
#SVM
svm=SVC(kernel='linear',probability=True)
svm.fit(Train_data,Train_label)
svm_pred=svm.predict(Test_data)
print('SVM_Acc',accuracy_score(Test_label,svm_pred))

