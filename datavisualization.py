from data_preprocessing import data_preprocess
import pandas as pd
import plotly.express as px
from IPython.display import Image
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff
import plotly.io as pio
import io
from sklearn.preprocessing import LabelEncoder
from PIL import Image
a =[]
def data_visualization():
    data = data_preprocess()
    cols = ['Grade','Sub Grade','Verification Status','Loan Title','Application Type','Initial List Status']
    labelencoder = LabelEncoder()
    for column in cols:
        data[column] = labelencoder.fit_transform(data[column])
        print(data[column])
    col=list(data.columns)
    col.remove("Loan Status")
    print(col)
    for i in col:
        fig = px.box(data, y=i)
        fig.update_layout(template='plotly_dark')
        #fig.update_layout(plot_bgcolor = "plotly_dark")
        fig.update_xaxes(showgrid=False,zeroline=False)
        fig.update_yaxes(showgrid=False,zeroline=False)
        # fig.show()
        fig.write_image(f"{i}.jpg")
        # a.append(fig)
    for i in col:
        fig = ff.create_distplot([data[i].values],group_labels=[i])
        fig.update_layout(template='plotly_dark')
        #fig.update_layout(plot_bgcolor = "plotly_dark")
        fig.update_xaxes(showgrid=False,zeroline=False)
        fig.update_yaxes(showgrid=False,zeroline=False)
        fig.show()
        # a.append(fig)
    df=data.drop("Loan Status",axis=1)
    y=df.corr().columns.tolist()
    z=df.corr().values.tolist()
    z_text = np.around(z, decimals=4) # Only show rounded value (full value on hover)
    fig = ff.create_annotated_heatmap(z,x=y,y=y,annotation_text=z_text,colorscale=px.colors.sequential.Cividis_r,showscale=True)
    fig.update_layout(template='plotly_dark')
    # fig.show()
    fig.write_image("img.jpg")
    # a.append(fig)
    
    return data

data_visualization()

