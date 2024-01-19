from data_preprocessing import data_preprocess
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
print("----------------------Feature engineering data ----------------")

def feature_engineering():
    data = data_preprocess()
    cols = ['Grade','Sub Grade','Verification Status','Loan Title','Application Type','Initial List Status']
    labelencoder = LabelEncoder()
    for column in cols:
        data[column] = labelencoder.fit_transform(data[column])
    
    count_0, count_1 = data['Loan Status'].value_counts()
    class_0 = data[data['Loan Status'] == 0]
    class_1 = data[data['Loan Status'] == 1]
    Target_1_over = class_1.sample(count_0,replace=True)
    # print(Target_1_over)
    dataset_balanced = pd.concat([Target_1_over,class_0], axis=0)
    print('Target_1_over',Target_1_over.shape)
    print('class_0',class_0.shape)
    # print(dataset_balanced)
    data = dataset_balanced.copy()   

    data.to_csv("clean_artifact.csv", index=False)
    #print("=========================fffffffffffffffffffffffffffffffffffffffffff",data)
    return data
feature_engineering()