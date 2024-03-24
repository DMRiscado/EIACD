import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

def price_sqft_living(df_delhi):
    plt.figure(figsize=(10, 6))
    plt.scatter("sqft_living", "price", data=df_delhi, color='blue', alpha=0.5)
    plt.title('Comparação entre Área Construída e Preço')
    plt.xlabel('Área Construída (em m²)')
    plt.ylabel('Preço (em €)')
    plt.grid(True)
    plt.xticks(ticks=range(0, int(df_delhi['sqft_living'].max()) + 1000, 1000))
    plt.yticks(ticks=range(0, int(df_delhi['price'].max()) + 100000, 100000))
    plt.ticklabel_format(style='plain', axis='y')
    plt.show()

def price_type_of_building(df_delhi):
    preco_por_tipo = df_delhi.groupby('type_of_building')['price'].mean()
    plt.figure(figsize=(10, 6))
    preco_por_tipo.plot(kind='bar', color='blue')
    plt.title('Preço Médio por Tipo de Construção')
    plt.xlabel('Tipo de Construção')
    plt.ylabel('Preço Médio (em €)')
    plt.xticks(rotation=1)
    plt.grid(axis='y')
    plt.show()

def price_balcony(df_delhi):
    preco_por_varanda = df_delhi.groupby('balcony')['price'].mean()
    plt.figure(figsize=(10, 6))
    preco_por_varanda.plot(kind='bar', color='blue')
    plt.title('Preço Médio por Varanda')
    plt.xlabel('Varanda')
    plt.ylabel('Preço Médio (em €)')
    plt.xticks(rotation=1)
    plt.grid(axis='y')
    plt.show()

def price_latitude_longitude(df_delhi):
    plt.figure(figsize=(10, 6))
    plt.scatter(df_delhi['longitude'], df_delhi['latitude'], c=df_delhi['price'], cmap='viridis', s=50, alpha=0.5)
    plt.clim(df_delhi['price'].min(), df_delhi['price'].max()*1)
    plt.title('Preço em relação à Localização Geográfica')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.colorbar(label='Preço (em €)')
    plt.grid(True)
    plt.show()

def price_bedrooms_bathrooms(df_delhi):
    plt.figure(figsize=(10, 6))
    plt.scatter(df_delhi['bedrooms'], df_delhi['bathrooms'], c=df_delhi['price'], cmap='viridis', s=50, alpha=0.5)
    plt.clim(df_delhi['price'].min(), df_delhi['price'].max() * 1)
    plt.title('Relação entre Preço, Quartos e Casas de Banho')
    plt.xlabel('Quartos')
    plt.ylabel('Casas de Banho')
    plt.colorbar(label='Preço (em €)')
    plt.grid(True)
    plt.show()


def price_car_garage(df_delhi):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(df_delhi['longitude'], df_delhi['latitude'], df_delhi['price_sqft'], c='blue', marker='o', alpha=0.5)
    ax.set_title('Relação entre Preço por metro quadrado, Latitude e Longitude')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_zlabel('Preço por metro quadrado (em €/m²)')
    plt.show()

def type_of_building_latitude_longitude(df_delhi):
    plt.figure(figsize=(10, 6))
    colors = {'Flat': 'blue', 'Individual House': 'green'}
    for building_type, color in colors.items():
        data = df_delhi[df_delhi['type_of_building'] == building_type]
        plt.scatter(data['longitude'], data['latitude'], color=color, label=building_type, alpha=0.5)
    plt.title('Localização por Tipo de Construção')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend()
    plt.grid(True)
    plt.show()

def price_sqft_latitude_longitude(df_delhi):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='longitude', y='latitude', hue='price_sqft', palette='viridis', data=df_delhi)
    plt.title('Preço por metro quadrado em relação à Localização Geográfica')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    scatter = plt.scatter([], [], c=[], cmap='viridis')
    plt.colorbar(scatter, label='Preço por metro quadrado (em €/m²)')
    plt.grid(True)
    plt.show()


price_sqft_living(df_delhi)
price_type_of_building(df_delhi)
price_balcony(df_delhi)
price_latitude_longitude(df_delhi)
price_bedrooms_bathrooms(df_delhi)
price_car_garage(df_delhi)
type_of_building_latitude_longitude(df_delhi)
price_sqft_latitude_longitude(df_delhi)

#Tabelas de Frequência

freq_bedrooms = df_delhi['bedrooms'].value_counts().sort_index()
freq_bathrooms = df_delhi['bathrooms'].value_counts().sort_index()
freq_car_garage = df_delhi['car_garage'].value_counts().sort_index()
tabela_frequencia = pd.DataFrame({
    'Bedrooms': freq_bedrooms,
    'Bathrooms': freq_bathrooms,
    'Car Garage': freq_car_garage
})
tabela_frequencia = tabela_frequencia.fillna(0)
print(tabela_frequencia)





