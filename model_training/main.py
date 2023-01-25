import pandas as pd
import os
import models

path = os.path.join(os.path.abspath('data_acquisition'), 'all_infos_processed.csv')
df = pd.read_csv(path)
df = df.dropna(subset=['Price','Living_Area'])
print(models.random_forest_model(df['Price'].array, df['Living_Area'].array))
print(models.linear_regression_model(df['Price'].array, df['Living_Area'].array))

'''X=df.drop('Price',axis=1) 
y=df['Price']

formated_columns = []

for column_name in X.columns :
    if(X[column_name].dtype == 'object') :
        print("column {} has been formated".format(column_name))
        formated_columns.append(column_name)
X = pd.get_dummies(df, prefix=formated_columns, columns=formated_columns)

print(X.shape)
print(X.head())'''




