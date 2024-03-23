import pandas as pd
import numpy as np


# importar dataset
data_total= "datasetfiles\concatenated_housing.csv"
#df_analise = pd.read_csv(r"C:\Users\Administrator\Documents\GitHub\EIACD\datasetfiles\concatenated_housing.csv")

# mediana dos metros quarados disponiveis
median_sqft = df_analise['sqft_living'].median()
print("Mediana de metros quadrados disponíveis: ", median_sqft)

# mediana dos preços
median_price = df_analise['price'].median()
print("Mediana dos preços: ", median_price)

#média dos preços
mean_price = df_analise['price'].mean()
print("Média dos preços: ", mean_price)

#média dos quartos disponíveis arredondada
mean_bedrooms = round(df_analise['bedrooms'].mean())
print("Média dos quartos disponíveis: ", mean_bedrooms)
