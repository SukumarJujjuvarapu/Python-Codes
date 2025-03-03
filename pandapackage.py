import pandas as pd
import numpy as np
df= pd.read_csv('heart.csv')
df.pop('Age')
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.columns) 
print(df.T) 
new_df=df.sort_values('Gender')
print(new_df)
print(df[5:9])




