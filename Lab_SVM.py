from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from imblearn.over_sampling import SMOTE
from rd import ReadData
import numpy as np
from goGoogle import goGoogle
import time

switch=True
C=0.5

while switch:
    Aac=0
    NAac=0
    for i in range(30):
        train_data , test_data , train_label , test_label = ReadData(i)
        Train_data=np.asarray(train_data).astype(np.float64)
        Test_data=np.asarray(test_data).astype(np.float64)
        Train_label=np.asarray(train_label).astype(np.float64)
        Test_label=np.asarray(test_label).astype(np.float64)
        sm=SMOTE(random_state=42)
        New_Data,New_Label = sm.fit_resample(Train_data,Train_label)
        svm=SVC(kernel='linear',probability=True)
        svm.fit(Train_data,Train_label)
        svm_pred=svm.predict(Test_data)
        print('SVM_Acc',accuracy_score(Test_label,svm_pred))
        ac=accuracy_score(Test_label,svm_pred)
        svm.fit(New_Data,New_Label)
        New_SVM_pred=svm.predict(Test_data)
        print('New_Svm_Acc:',accuracy_score(Test_label,New_SVM_pred))
        nac=accuracy_score(Test_label,New_SVM_pred)
        goGoogle(i,C,ac,nac,'svm')
        Aac=Aac+ac
        NAac=NAac+nac
    goGoogle('Avg',C,Aac/30,NAac/30,'svm')
    C=C+0.1
    if C>1:
        switch=False