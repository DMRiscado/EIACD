import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data_melbourne = "datasetfiles/melbourne_housing.csv"

df_melbourne = pd.read_csv(data_melbourne)

media_preco = df_melbourne['price'].mean()
mediana_preco = df_melbourne['price'].median()
print(f"Média dos preços em Melbourne: {media_preco:.2f} €")
print(f"Mediana dos preços em Melbourne: {mediana_preco:.2f} €\n")


media_quartos = df_melbourne["bedrooms"].mean()
mediana_quartos = df_melbourne["bedrooms"].median()
print(f"Média de quartos em Melbourne: {int(media_quartos)}")
print(f"Mediana de quartos em Melbourne: {mediana_quartos}\n")

media_wc = df_melbourne["bathrooms"].mean()
mediana_wc = df_melbourne["bathrooms"].median()
print(f"Média de casas de banho em Melbourne: {int(media_wc)}")
print(f"Mediana de casas de banho em Melbourne: {mediana_wc}\n")

media_carros = df_melbourne["car_garage"].mean()
mediana_carros = df_melbourne["car_garage"].median()
print(f"Média de carros na garagem em Melbourne: {int(media_carros)}")
print(f"Mediana de carros na garagem em Melbourne: {mediana_carros}\n")


def price_suburb(df_melbourne):
    preco_por_suburb = df_melbourne.groupby('suburb')['price'].mean().reset_index()
    preco_por_suburb.columns = ['Subúrbio', 'Preço Médio (em €)']
    preco_por_suburb['Preço Médio (em €)'] = preco_por_suburb['Preço Médio (em €)'].round(2)
    preco_por_suburb_sorted = preco_por_suburb.sort_values(by='Preço Médio (em €)', ascending=True)
    print(preco_por_suburb_sorted)

def price_bedrooms_bathrooms(df_melbourne):
    plt.figure(figsize=(10, 6))
    df_melbourne.groupby(['bedrooms', 'bathrooms'])['price'].mean().unstack().plot(kind='bar', stacked=True,)
    plt.title('Preço em relação aos Quartos e Casas de Banho')
    plt.xlabel('Quartos')
    plt.ylabel('Preço (em €)')
    plt.xticks(rotation=0)
    plt.legend(title='Banheiros')
    plt.show()
def type(df_melbourne):
    type_counts = df_melbourne['type'].value_counts(normalize=True) * 100
    plt.figure(figsize=(9, 8))
    plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('Distribuição Percentual dos Tipos de Casas')
    plt.axis('equal')
    plt.text(-1.5, -1.3,
             'h: House,Cottage,Villa, Semi,Terrace\nu:  Unit, Duplex\nt: Townhouse',
             fontsize=12,
             bbox=dict(facecolor='lightgrey', alpha=0.5))
    plt.show()

def price_type(df_melbourne):
    price_mean_by_type = df_melbourne.groupby('type')['price'].mean()
    plt.figure(figsize=(10, 6))
    price_mean_by_type.plot(kind='bar', color='skyblue')
    plt.title('Preço médio em relação ao Tipo de Casa')
    plt.xlabel('Tipo de Casa')
    plt.ylabel('Preço (em €)')
    plt.xticks(rotation=0)
    plt.text(1.2, 650000,
             'h: House,Cottage,Villa, Semi,Terrace\nu:  Unit, Duplex\nt: Townhouse',
             fontsize=12,
             bbox=dict(facecolor='lightgrey', alpha=0.5))
    plt.show()


def price_sqft_living(df_melbourne):
    plt.figure(figsize=(10, 6))
    plt.scatter("sqft_living", "price", data=df_melbourne, color='blue', alpha=0.5)
    plt.title('Comparação entre Área Construída e Preço')
    plt.xlabel('Área Construída (em m²)')
    plt.ylabel('Preço (em €)')
    plt.grid(True)
    plt.ticklabel_format(style='plain', axis='y')
    plt.show()

def price_car_garage(df_melbourne):
    plt.figure(figsize=(10, 6))
    df_melbourne.groupby('car_garage')['price'].mean().plot(kind='bar')
    plt.title('Preço Médio por Número de Vagas na Garagem')
    plt.xlabel('Número de Vagas de Garagem')
    plt.ylabel('Preço (em €)')
    plt.xticks(rotation=0)
    plt.show()

def price_latitude_longitude(df_melbourne):
    plt.figure(figsize=(10, 6))
    plt.scatter(df_melbourne['longitude'], df_melbourne['latitude'], c=df_melbourne['price'], cmap='viridis', s=50, alpha=0.5)
    plt.clim(df_melbourne['price'].min(), df_melbourne['price'].max()*1)
    plt.title('Preço em relação à Localização Geográfica')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.colorbar(label='Preço (em €)')
    plt.grid(True)
    plt.show()

def price_date_sold(df_melbourne):
    plt.figure(figsize=(10, 6))
    df_melbourne['date_sold'] = pd.to_datetime(df_melbourne['date_sold'], format='%m/%Y')
    df_melbourne.groupby(df_melbourne['date_sold'].dt.strftime('%Y-%m'))['price'].mean().plot(kind='line', marker='o')
    plt.title('Preço emr relação à Data de Venda')
    plt.xlabel('Data de Venda')
    plt.ylabel('Preço (em €)')
    plt.xticks(rotation=45)
    plt.show()



def price_year_built(df_melbourne):
    plt.figure(figsize=(10, 6))
    df_melbourne.groupby('year_built')['price'].mean().plot(kind='line', marker='o')
    plt.title('Preço em relação ao Ano de Construção')
    plt.xlabel('Ano de Construção')
    plt.ylabel('Preço (em €)')
    plt.xticks(rotation=1)
    plt.show()


def price_zipcode(df_melbourne):
    plt.figure(figsize=(12, 6))
    df_melbourne.groupby('zipcode')['price'].mean().sort_values().plot(kind='bar')
    plt.title('Preço Médio por Código Postal')
    plt.xlabel('Código Postal (Zipcode)')
    plt.ylabel('Preço Médio')
    plt.xticks(rotation=45)
    plt.show()


def sqft_living_year_built(df_melbourne):
    plt.figure(figsize=(10, 6))
    plt.scatter("year_built", "sqft_living", data=df_melbourne, color='blue', alpha=0.5)
    plt.title('Comparação entre Ano de Construção e Área Construída')
    plt.xlabel('Ano de Construção')
    plt.ylabel('Área Construída (em m²)')
    plt.grid(True)
    plt.show()

def suburb_year_built(df_melbourne):
    plt.figure(figsize=(10, 6))
    plt.scatter(df_melbourne['suburb'], df_melbourne['year_built'], color='blue', alpha=0.5)
    plt.title('Ano de contrução por Subúrbio')
    plt.xlabel('Subúrbio')
    plt.ylabel('Ano de Construção')
    plt.grid(True)
    plt.show()

#price_suburb(df_melbourne)
#price_bedrooms_bathrooms(df_melbourne)
#type(df_melbourne)
#price_type(df_melbourne)
#price_sqft_living(df_melbourne)
#price_car_garage(df_melbourne)
#price_latitude_longitude(df_melbourne)
#price_date_sold(df_melbourne)
#price_year_built(df_melbourne)
#price_zipcode(df_melbourne)
#sqft_living_year_built(df_melbourne)
#suburb_year_built(df_melbourne)


#Tabelas de Frequência

freq_bedrooms = df_melbourne['bedrooms'].value_counts().sort_index()
freq_bathrooms = df_melbourne['bathrooms'].value_counts().sort_index()
freq_car_garage = df_melbourne['car_garage'].value_counts().sort_index()
tabela_frequencia = pd.DataFrame({
    'Bedrooms': freq_bedrooms,
    'Bathrooms': freq_bathrooms,
    'Car Garage': freq_car_garage
})
tabela_frequencia = tabela_frequencia.fillna(0)
print(tabela_frequencia)