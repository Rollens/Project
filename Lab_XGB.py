from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
from imblearn.over_sampling import SMOTE
from rd import ReadData
import numpy as np
from goGoogle import goGoogle
import time
"""
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
        XGB=XGBClassifier(eta=eta)
        XGB.fit(Train_data,Train_label)
        print('XGB_Acc:',XGB.score(Test_data, Test_label))
        XGB.fit(New_Data,New_Label)
        New_XGB_pred=XGB.predict(Test_data)
        print('New_XGB_Acc:',accuracy_score(Test_label,New_XGB_pred))
        goGoogle(i,eta,XGB.score(Test_data, Test_label),accuracy_score(Test_label,New_XGB_pred),'xgb')
        time.sleep(2)
    eta=eta+0.02
    if eta>0.2:
        switch=False"""
eta_switch=True
maxdeep_switch=True
mds_switch=True
spw_switch=True
eta=0.1
while eta_switch:
    max_deep=0
    while maxdeep_switch:
        max_delta_step=6
        while mds_switch:
            scale_pos_weight=1
            while spw_switch:
                for i in range(30):
                    train_data , test_data , train_label , test_label = ReadData(i)
                    Train_data=np.asarray(train_data).astype(np.float64)
                    Test_data=np.asarray(test_data).astype(np.float64)
                    Train_label=np.asarray(train_label).astype(np.float64)
                    Test_label=np.asarray(test_label).astype(np.float64)
                    sm=SMOTE(random_state=42)
                    New_Data,New_Label = sm.fit_resample(Train_data,Train_label)
                    XGB=XGBClassifier(eta=eta,max_delta_step=max_delta_step,max_deep=max_deep,scale_pos_weight=scale_pos_weight)
                    XGB.fit(Train_data,Train_label)
                    Unbalanced_Pred=XGB.predict(Test_data)
                    Unbalanced_Acc=XGB.score(Test_data,Test_label)
                    XGB.fit(New_Data,New_Label)
                    Balanced_Pred=XGB.predict(Test_label)
                    Balanced_Acc=accuracy_score(Test_label,Balanced_Pred)
                    Parameters=(eta,max_deep,max_delta_step,scale_pos_weight)
                    Accuracy=(Unbalanced_Acc,Balanced_Acc)
                    goGoogle(i,'XGB',Parameters,Accuracy)
                    time.sleep(2)
                scale_pos_weight=scale_pos_weight+0.1
                if scale_pos_weight>3:
                    spw_switch=False
            max_delta_step=max_delta_step+1
            if maxdeep_switch>15:
                mds_switch=False
        max_deep=max_deep+1
        if max_deep>40:
            maxdeep_switch=False
    eta=eta+0.1
    if eta>5:
        eta_switch=False


    