from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from imblearn.over_sampling import SMOTE
from rd import ReadData
import numpy as np
from goGoogle import goGoogle
import time

for k in range(5,15):
    for i in range(30):
        train_data , test_data , train_label , test_label = ReadData(i)
        Train_data=np.asarray(train_data).astype(np.float64)
        Test_data=np.asarray(test_data).astype(np.float64)
        Train_label=np.asarray(train_label).astype(np.float64)
        Test_label=np.asarray(test_label).astype(np.float64)
        sm=SMOTE(random_state=42)
        New_Data,New_Label = sm.fit_resample(Train_data,Train_label)
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(Train_data,Train_label)
        knn_pred=knn.predict(Test_data)
        print('KNN_Acc:',accuracy_score(Test_label,knn_pred))
        knn.fit(New_Data,New_Label)
        New_knn_pred=knn.predict(Test_data)
        print('New_KNN_Acc:',accuracy_score(Test_label,New_knn_pred))
        goGoogle(i,k,accuracy_score(Test_label,knn_pred),accuracy_score(Test_label,New_knn_pred),'Knn')
        time.sleep(2)