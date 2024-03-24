import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_delhi = "datasetfiles/delhi_housing.csv"

df_delhi = pd.read_csv(data_delhi)

media_preco = df_delhi['price'].mean()
print(f"Média dos preços em Delhi: {media_preco:.2f} €")

media_quartos = df_delhi["bedrooms"].mean()
print(f"Média de quartos em Delhi: {int(media_quartos)}")

media_wc = df_delhi["bathrooms"].mean()
print(f"Média de casas de banho em Delhi: {int(media_wc)}")

media_carros = df_delhi["car_garage"].mean()
print(f"Média de carros na garagem em Delhi: {int(media_carros)}")

def sqft_living_price(df_delhi):
    plt.figure(figsize=(10, 6))
    plt.scatter("sqft_living", "price", data=df_delhi, color='blue', alpha=0.5)
    plt.title('Comparação entre Área Construída e Preço')
    plt.xlabel('Área Construída (em m²)')
    plt.ylabel('Preço (em €)')
    plt.grid(True)
    plt.xticks(ticks=range(0, int(df_delhi['sqft_living'].max()) + 1000, 1000))
    plt.yticks(ticks=range(0, int(df_delhi['price'].max()) + 1000000, 10000000))
    plt.ticklabel_format(style='plain', axis='y')
    plt.show()

sqft_living_price(df_delhi)


