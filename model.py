from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import auc
from sklearn.metrics import f1_score
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE
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
count = [0, 0]
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
                if i[84] == '0':
                    count[0] += 1
                else:
                    count[1] += 1
print(count)

train_data , test_data , train_label , test_label = train_test_split(featureData,AnsData,test_size=0.2)
Train_data=np.asarray(train_data).astype(np.float64)
Test_data=np.asarray(test_data).astype(np.float64)
Train_label=np.asarray(train_label).astype(np.float64)
Test_label=np.asarray(test_label).astype(np.float64)
sm=SMOTE(random_state=42)
New_Data,New_Label = sm.fit_resample(Train_data,Train_label)
c=[0,0]
for i in New_Label:
    if i==0.0:
        c[0]+=1
    elif i==1.0:
        c[1]+=1
print(c)
#KNN
knn = KNeighborsClassifier()
knn.fit(Train_data,Train_label)
knn_pred=knn.predict(Test_data)
print('KNN_Acc:',accuracy_score(Test_label,knn_pred))
print('KNN_F1:',f1_score(Test_label,knn_pred,average='micro'))
knn.fit(New_Data,New_Label)
New_knn_pred=knn.predict(Test_data)
print('New_KNN_Acc:',accuracy_score(Test_label,New_knn_pred))
print('New_Knn_F1:',f1_score(Test_label,New_knn_pred,average='micro'))
#XGB
XGB=XGBClassifier()
XGB.fit(Train_data,Train_label)
print('XGB_Acc:',XGB.score(Test_data, Test_label))
print('XGB_F1:',f1_score(Test_label,XGB.predict(Test_data),average='micro'))
XGB.fit(New_Data,New_Label)
print('New_XGB_Acc:',XGB.score(Test_data,Test_label))
#RFC
rfc=RandomForestClassifier()
rfc.fit(Train_data,Train_label)
print('RFC_Acc:', rfc.score(Test_data, Test_label))
print('RFC_F1:',f1_score(Test_label,rfc.predict(Test_data),average='micro'))
rfc.fit(New_Data,New_Label)
print('New_Rfc_Acc:',rfc.score(Test_data,Test_label))
#SVM
svm=SVC(kernel='linear',probability=True)
svm.fit(Train_data,Train_label)
svm_pred=svm.predict(Test_data)
print('SVM_Acc',accuracy_score(Test_label,svm_pred))
svm.fit(New_Data,New_Label)
New_SVM_pred=svm.predict(Test_data)
print('New_Svm_Acc:',accuracy_score(Test_label,New_SVM_pred))

