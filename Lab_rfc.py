from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from imblearn.over_sampling import SMOTE
from rd import ReadData
import numpy as np
from goGoogle import goGoogle
import time
        
for i in range(30):
    train_data , test_data , train_label , test_label = ReadData(i)
    Train_data=np.asarray(train_data).astype(np.float64)
    Test_data=np.asarray(test_data).astype(np.float64)
    Train_label=np.asarray(train_label).astype(np.float64)
    Test_label=np.asarray(test_label).astype(np.float64)
    sm=SMOTE(random_state=42)
    New_Data,New_Label = sm.fit_resample(Train_data,Train_label)
    rfc=RandomForestClassifier(n_estimators=100)
    rfc.fit(Train_data,Train_label)
    print('RFC_Acc:', rfc.score(Test_data, Test_label))
    ac=rfc.score(Test_data, Test_label)
    rfc.fit(New_Data,New_Label)
    print('New_Rfc_Acc:',rfc.score(Test_data,Test_label))
    nac=rfc.score(Test_data,Test_label)
    goGoogle(i,1,ac,nac,'rfc')
    time.sleep(2)