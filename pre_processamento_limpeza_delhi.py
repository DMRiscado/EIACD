import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

data_delhi = "datasetfiles/delhi_housing.csv"
df_delhi = pd.read_csv(data_delhi)

# substituir vazio nas colunas 'garage' e 'balcony' pela respetiva mediana
df_delhi['car_garage'] = df_delhi['car_garage'].fillna(df_delhi['car_garage'].median())
df_delhi['balcony'] = df_delhi['balcony'].fillna(df_delhi['balcony'].median())



# Reescrever os arquivos originais com os DataFrames modificados
df_delhi.to_csv(data_delhi, index=False)