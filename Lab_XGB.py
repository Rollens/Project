from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
from imblearn.over_sampling import SMOTE
from rd import ReadData
import numpy as np
from goGoogle import goGoogle
import time

switch=True
eta=0.01

while switch:
    for i in range(30):
        train_data , test_data , train_label , test_label = ReadData(i)
        Train_data=np.asarray(train_data).astype(np.float64)
        Test_data=np.asarray(test_data).astype(np.float64)
        Train_label=np.asarray(train_label).astype(np.float64)
        Test_label=np.asarray(test_label).astype(np.float64)
        sm=SMOTE(random_state=42)
        New_Data,New_Label = sm.fit_resample(Train_data,Train_label)
        XGB=XGBClassifier()
        XGB.fit(Train_data,Train_label)
        print('XGB_Acc:',XGB.score(Test_data, Test_label))
        XGB.fit(New_Data,New_Label)
        New_XGB_pred=XGB.predict(Test_data)
        print('New_XGB_Acc:',accuracy_score(Test_label,New_XGB_pred))
        goGoogle(i,eta,XGB.score(Test_data, Test_label),accuracy_score(Test_label,New_XGB_pred))
        time.sleep(2)
    eta=eta+0.02
    if eta>0.2:
        switch=False