import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium

data_perth = "datasetfiles/perth_housing.csv"

df_perth = pd.read_csv(data_perth)

media_preco = df_perth['price'].mean()
mediana_preco = df_perth['price'].median()
print(f"Média dos preços em Melbourne: {media_preco:.2f} €")
print(f"Mediana dos preços em Melbourne: {mediana_preco:.2f} €\n")


media_quartos = df_perth["bedrooms"].mean()
mediana_quartos = df_perth["bedrooms"].median()
print(f"Média de quartos em Melbourne: {int(media_quartos)}")
print(f"Mediana de quartos em Melbourne: {mediana_quartos}\n")

media_wc = df_perth["bathrooms"].mean()
mediana_wc = df_perth["bathrooms"].median()
print(f"Média de casas de banho em Melbourne: {int(media_wc)}")
print(f"Mediana de casas de banho em Melbourne: {mediana_wc}\n")

media_carros = df_perth["car_garage"].mean()
mediana_carros = df_perth["car_garage"].median()
print(f"Média de carros na garagem em Melbourne: {int(media_carros)}")
print(f"Mediana de carros na garagem em Melbourne: {mediana_carros}\n")