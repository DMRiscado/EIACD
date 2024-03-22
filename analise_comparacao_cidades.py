import pandas as pd
import numpy as np


# importar dataset
df_analise = pd.read_csv("datasetfiles/full_housing.csv")

# mediana dos metros quarados disponiveis
median_sqft = df_analise['sqft_living'].median()
print("Mediana de metros quadrados disponíveis: ", median_sqft)
