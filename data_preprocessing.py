import numpy as np
from loadingdata import loading_data

def data_preprocess():
    data = loading_data()
    data =  data.drop(['ID', 'Payment Plan', 'Accounts Delinquent','Batch Enrolled','Employment Duration','Home Ownership'], axis = 1)
    #print(data.columns)
    data['Funded Amount Investor'] = data['Funded Amount Investor'].astype('int')
    #print("----------------------data_preprocess------------------",data)
    return data

data_preprocess()