import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_delhi = "datasetfiles/delhi_housing.csv"
df_delhi = pd.read_csv(data_delhi)

#Substituir vazio nas colunas 'garage' e 'balcony' pela respetiva mediana
df_delhi['car_garage'] = df_delhi['car_garage'].fillna(df_delhi['car_garage'].median())
df_delhi['balcony'] = df_delhi['balcony'].fillna(df_delhi['balcony'].median())



#Reescrever os arquivos originais com os DataFrames modificados
df_delhi.to_csv(data_delhi, index=False)

#Remoção outliers

#price
#Q1 = df_delhi['price'].quantile(0.05)
#Q3 = df_delhi['price'].quantile(0.95)
#IQR = Q3 - Q1

#outliers = df_delhi[(df_delhi['price'] >= Q1 - 1.5 * IQR) & (df_delhi['price'] <= Q3 + 1.5 * IQR)]

#outliers.to_csv('datasetfiles/delhi_housing.csv', index=False)


#sqft living
#Q1 = df_delhi['sqft_living'].quantile(0.05)
#Q3 = df_delhi['sqft_living'].quantile(0.95)
#IQR = Q3 - Q1

#outliers = df_delhi[(df_delhi['sqft_living'] >= Q1 - 1.5 * IQR) & (df_delhi['sqft_living'] <= Q3 + 1.5 * IQR)]

#outliers.to_csv('datasetfiles/delhi_housing.csv', index=False)

#bedrooms
#Q1 = df_delhi['bedrooms'].quantile(0.05)
#Q3 = df_delhi['bedrooms'].quantile(0.95)
#IQR = Q3 - Q1

#outliers = df_delhi[(df_delhi['bedrooms'] >= Q1 - 1.5 * IQR) & (df_delhi['bedrooms'] <= Q3 + 1.5 * IQR)]

#outliers.to_csv('datasetfiles/delhi_housing.csv', index=False)

#bathrooms
#Q1 = df_delhi['bathrooms'].quantile(0.05)
#Q3 = df_delhi['bathrooms'].quantile(0.95)
#IQR = Q3 - Q1

#outliers = df_delhi[(df_delhi['bathrooms'] >= Q1 - 1.5 * IQR) & (df_delhi['bathrooms'] <= Q3 + 1.5 * IQR)]

#outliers.to_csv('datasetfiles/delhi_housing.csv', index=False)

#price sqft
#Q1 = df_delhi['price_sqft'].quantile(0.05)
#Q3 = df_delhi['price_sqft'].quantile(0.95)
#IQR = Q3 - Q1

#outliers = df_delhi[(df_delhi['price_sqft'] >= Q1 - 1.5 * IQR) & (df_delhi['price_sqft'] <= Q3 + 1.5 * IQR)]

#outliers.to_csv('datasetfiles/delhi_housing.csv', index=False)

#car garage
#Q1 = df_delhi['car_garage'].quantile(0.05)
#Q3 = df_delhi['car_garage'].quantile(0.95)
#IQR = Q3 - Q1

#outliers = df_delhi[(df_delhi['car_garage'] >= Q1 - 1.5 * IQR) & (df_delhi['car_garage'] <= Q3 + 1.5 * IQR)]

#outliers.to_csv('datasetfiles/delhi_housing.csv', index=False)

