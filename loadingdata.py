import  pandas as pd
import numpy as np

def loading_data():
    df = pd.read_csv("train.csv")
    print("df1 data : ", df)
    return df

loading_data()