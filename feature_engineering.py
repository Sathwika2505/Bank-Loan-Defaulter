from data_preprocessing import data_preprocess
from sklearn.preprocessing import LabelEncoder
print("----------------------Feature engineering data ----------------")
def feature_engineering():
    data = data_preprocess()
    cols = ['Grade','Sub Grade','Verification Status','Loan Title','Application Type','Initial List Status']
    labelencoder = LabelEncoder()
    for column in cols:
        data[column] = labelencoder.fit_transform(data[column])
    data.to_csv("clean_artifact.csv", index=False)
    #print("=========================fffffffffffffffffffffffffffffffffffffffffff",data)
    return data
feature_engineering()