import pandas as pd
import numpy as np

data_melbourne = "datasetfiles/melbourne_housing.csv"
df_melbourne = pd.read_csv(data_melbourne)

missing_values = df_melbourne.isnull().sum()
print(missing_values)

Remoção de linhas com valores nulos

def remover_linhas(df_melbourne, arquivo_csv):
    valores_falta = df_melbourne.isnull().sum(axis=1)
    indices_remover = valores_falta[valores_falta == 7].index
    df = df_melbourne.drop(indices_remover)
    df.to_csv(arquivo_csv, index=False)

#remover_linhas(df_melbourne, 'datasetfiles/melbourne_housing.csv')


colunas_em_falta = ["bedrooms", "bathrooms", "car_garage", "sqft_living", "year_built", "latitude", "longitude"]

#for col in df_melbourne.columns:
#    if df_melbourne[col].dtype != 'object':
#        median = df_melbourne[col].median()
#        df_melbourne[col].fillna(median, inplace=True)



#Remoção de outliers usando a técnica IQR 5/95

#Q1 = df_melbourne['year_built'].quantile(0.05)
#Q3 = df_melbourne['year_built'].quantile(0.95)
#IQR = Q3 - Q1
#outliers = df_melbourne[(df_melbourne['year_built'] >= Q1 - 1.5 * IQR) & (df_melbourne['year_built'] <= Q3 + 1.5 * IQR)]
#outliers.to_csv('datasetfiles/melbourne_housing.csv', index=False)

#Q1 = df_melbourne['sqft_living'].quantile(0.05)
#Q3 = df_melbourne['sqft_living'].quantile(0.95)
#IQR = Q3 - Q1
#outliers = df_melbourne[(df_melbourne['sqft_living'] >= Q1 - 1.5 * IQR) & (df_melbourne['sqft_living'] <= Q3 + 1.5 * IQR)]
#outliers.to_csv('datasetfiles/melbourne_housing.csv', index=False)

#Q1 = df_melbourne['bedrooms'].quantile(0.05)
#Q3 = df_melbourne['bedrooms'].quantile(0.95)
#IQR = Q3 - Q1
#outliers = df_melbourne[(df_melbourne['bedrooms'] >= Q1 - 1.5 * IQR) & (df_melbourne['bedrooms'] <= Q3 + 1.5 * IQR)]
#outliers.to_csv('datasetfiles/melbourne_housing.csv', index=False)

#Q1 = df_melbourne['bathrooms'].quantile(0.05)
#Q3 = df_melbourne['bathrooms'].quantile(0.95)
#IQR = Q3 - Q1
#outliers = df_melbourne[(df_melbourne['bathrooms'] >= Q1 - 1.5 * IQR) & (df_melbourne['bathrooms'] <= Q3 + 1.5 * IQR)]
#outliers.to_csv('datasetfiles/melbourne_housing.csv', index=False)

#Q1 = df_melbourne['car_garage'].quantile(0.05)
#Q3 = df_melbourne['car_garage'].quantile(0.95)
#IQR = Q3 - Q1
#outliers = df_melbourne[(df_melbourne['car_garage'] >= Q1 - 1.5 * IQR) & (df_melbourne['car_garage'] <= Q3 + 1.5 * IQR)]
#outliers.to_csv('datasetfiles/melbourne_housing.csv', index=False)

#Q1 = df_melbourne['price'].quantile(0.05)
#Q3 = df_melbourne['price'].quantile(0.95)
#IQR = Q3 - Q1
#outliers = df_melbourne[(df_melbourne['price'] >= Q1 - 1.5 * IQR) & (df_melbourne['price'] <= Q3 + 1.5 * IQR)]
#outliers.to_csv('datasetfiles/melbourne_housing.csv', index=False)

#Q1 = df_melbourne['zipcode'].quantile(0.05)
#Q3 = df_melbourne['zipcode'].quantile(0.95)
#IQR = Q3 - Q1
#outliers = df_melbourne[(df_melbourne['zipcode'] >= Q1 - 1.5 * IQR) & (df_melbourne['zipcode'] <= Q3 + 1.5 * IQR)]
#outliers.to_csv('datasetfiles/melbourne_housing.csv', index=False)