import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

#Daraframe de Melbourne

data_melbourne = "datasetfiles/melbourne_housing.csv"
df_melbourne = pd.read_csv(data_melbourne)


#Média e Mediana dos preços, quartos, casas de banho e carros na garagem em Melbourne

def avg_median_price(df_melbourne):
    media_preco = df_melbourne['price'].mean()
    mediana_preco = df_melbourne['price'].median()
    print(f"Média dos preços em Melbourne: {media_preco:.2f} €")
    print(f"Mediana dos preços em Melbourne: {mediana_preco:.2f} €\n")

def avg_median_bedrooms(df_melbourne):
    media_quartos = df_melbourne["bedrooms"].mean()
    mediana_quartos = df_melbourne["bedrooms"].median()
    print(f"Média de quartos em Melbourne: {int(media_quartos)}")
    print(f"Mediana de quartos em Melbourne: {mediana_quartos}\n")

def avg_median_bathrooms(df_melbourne):
    media_wc = df_melbourne["bathrooms"].mean()
    mediana_wc = df_melbourne["bathrooms"].median()
    print(f"Média de casas de banho em Melbourne: {int(media_wc)}")
    print(f"Mediana de casas de banho em Melbourne: {mediana_wc}\n")

def avg_median_garages(df_melbourne):
    media_carros = df_melbourne["car_garage"].mean()
    mediana_carros = df_melbourne["car_garage"].median()
    print(f"Média de carros na garagem em Melbourne: {int(media_carros)}")
    print(f"Mediana de carros na garagem em Melbourne: {mediana_carros}\n")

#Funções de Análise

#Preço Médio por Subúrbio

def price_suburb(df_melbourne):
    preco_por_suburb = df_melbourne.groupby('suburb')['price'].mean().reset_index()
    preco_por_suburb.columns = ['Subúrbio', 'Preço Médio (em €)']
    preco_por_suburb['Preço Médio (em €)'] = preco_por_suburb['Preço Médio (em €)'].round(2)
    preco_por_suburb_sorted = preco_por_suburb.sort_values(by='Preço Médio (em €)', ascending=True)
    print(preco_por_suburb_sorted)

#Preço em relação a Quartos e Casas de Banho

def price_bedrooms_bathrooms(df_melbourne):
    plt.figure(figsize=(10, 6))
    plt.scatter(df_melbourne['bedrooms'], df_melbourne['bathrooms'], c=df_melbourne['price'], cmap='viridis', s=50, alpha=1)
    plt.clim(df_melbourne['price'].min(), df_melbourne['price'].max() * 1)
    plt.xticks(ticks=range(0, int(df_melbourne['bedrooms'].max()) + 2, 2))
    plt.title('Preço em relação a Quartos e Casas de Banho')
    plt.xlabel('Quartos')
    plt.ylabel('Casas de Banho')
    plt.colorbar(label='Preço (em €)')
    plt.grid(True)
    plt.show()

#Distribuição Percentual dos Tipos de Casas

def type(df_melbourne):
    plt.figure(figsize=(9, 8))
    type_counts = df_melbourne['type'].value_counts(normalize=True) * 100
    plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('Distribuição Percentual dos Tipos de Casas')
    plt.axis('equal')
    plt.text(-1.5, -1.3,
             'h: House,Cottage,Villa, Semi,Terrace\nu:  Unit, Duplex\nt: Townhouse',
             fontsize=12,
             bbox=dict(facecolor='lightgrey', alpha=0.5))
    plt.show()

#Preço Médio por Tipo de Casa

def price_type(df_melbourne):
    plt.figure(figsize=(10, 6))
    price_mean_by_type = df_melbourne.groupby('type')['price'].mean()
    price_mean_by_type.plot(kind='bar', color='skyblue')
    plt.title('Preço médio em relação ao Tipo de Casa')
    plt.xlabel('Tipo de Casa')
    plt.ylabel('Preço Médio (em €)')
    plt.xticks(rotation=0)
    plt.text(1.2, 650000,
             'h: House,Cottage,Villa, Semi,Terrace\nu:  Unit, Duplex\nt: Townhouse',
             fontsize=12,
             bbox=dict(facecolor='lightgrey', alpha=0.5))
    plt.show()

#Preço em relação à Área Construída

def sqft_price(df_melbourne):
    plt.figure(figsize=(10, 6))
    plt.scatter("sqft_living", "price", data=df_melbourne, color='blue', alpha=0.5)
    plt.title('Preço em relação à Área Construída')
    plt.xlabel('Área Construída (em m²)')
    plt.ylabel('Preço (em €)')
    plt.grid(True)
    plt.ticklabel_format(style='plain', axis='y')
    plt.show()

#Preço Médio por Número de Vagas na Garagem

def price_car_garage(df_melbourne):
    plt.figure(figsize=(10, 6))
    df_melbourne.groupby('car_garage')['price'].mean().plot(kind='bar')
    plt.title('Preço Médio por Número de Vagas na Garagem')
    plt.xlabel('Número de Vagas de Garagem')
    plt.ylabel('Preço (em €)')
    plt.xticks(rotation=0)
    plt.ticklabel_format(axis='y', style='plain')
    plt.show()

#Preço em relação à Localização Geográfica

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

#Preço em relação à Data de Venda

def price_date_sold(df_melbourne):
    plt.figure(figsize=(10, 6))
    df_melbourne['date_sold'] = pd.to_datetime(df_melbourne['date_sold'], format='%m/%Y')
    df_melbourne.groupby(df_melbourne['date_sold'].dt.strftime('%Y-%m'))['price'].mean().plot(kind='line', marker='o')
    plt.title('Preço em relação à Data de Venda')
    plt.xlabel('Data de Venda')
    plt.ylabel('Preço (em €)')
    plt.xticks(rotation=0)
    plt.show()

#Preço em relação ao Ano de Construção

def price_year_built(df_melbourne):
    plt.figure(figsize=(10, 6))
    df_melbourne.groupby('year_built')['price'].mean().plot(kind='line', marker='o')
    plt.title('Preço em relação ao Ano de Construção')
    plt.xlabel('Ano de Construção')
    plt.ylabel('Preço (em €)')
    plt.xticks(rotation=1)
    plt.show()

#Preço em relação ao Código Postal

def price_zipcode(df_melbourne):
    preco_por_zipcode = df_melbourne.groupby('zipcode')['price'].mean().reset_index()
    preco_por_zipcode.columns = ['Código Postal', 'Preço Médio (em €)']
    preco_por_zipcode['Preço Médio (em €)'] = preco_por_zipcode['Preço Médio (em €)'].round(2)
    preco_por_suburb_sorted = preco_por_zipcode.sort_values(by='Preço Médio (em €)', ascending=True)
    print(preco_por_suburb_sorted)

#Área Construída em relação ao Ano de Construção

def sqft_living_year_built(df_melbourne):
    plt.figure(figsize=(10, 6))
    plt.scatter("year_built", "sqft_living", data=df_melbourne, color='blue', alpha=0.5)
    plt.title('Comparação entre Ano de Construção e Área Construída')
    plt.xlabel('Ano de Construção')
    plt.ylabel('Área Construída (em m²)')
    plt.grid(True)
    plt.show()

#Ano de Construção por Subúrbio

def suburb_year_built(df_melbourne):
    preco_por_zipcode = df_melbourne.groupby('suburb')['year_built'].mean().reset_index()
    preco_por_zipcode.columns = ['Subúrbio', 'Ano de Construção']
    preco_por_zipcode['Ano de Construção'] = preco_por_zipcode['Ano de Construção'].round(0)
    preco_por_suburb_sorted = preco_por_zipcode.sort_values(by='Ano de Construção', ascending=True)
    print(preco_por_suburb_sorted)

#Número de casas construídas por ano

def year_built(df_melbourne):
    df_melbourne['year_built'] = df_melbourne['year_built'].fillna(0).astype(int)
    df = df_melbourne[df_melbourne['year_built'] != 0]
    casas_por_ano = df.groupby('year_built').size()
    casas_por_ano_ordenado = casas_por_ano.sort_values(ascending=False)
    print("Número de casas construídas por ano:")
    print(casas_por_ano_ordenado)


#Tabelas de Frequência, quartos, casas de banho e carros na garagem em Melbourne

def tabelas_frequencia(df_melbourne):
    print("Tabela de Frequência de Quartos, Casas de Banho e Carros na Garagem em Melbourne:\n")
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
    print("__________________________________________________________\n")





# Execução das funções


# avg_median_price(df_melbourne)
# avg_median_bedrooms(df_melbourne)
# avg_median_bathrooms(df_melbourne)
# avg_median_garages(df_melbourne)
# price_suburb(df_melbourne)
# price_bedrooms_bathrooms(df_melbourne)
# type(df_melbourne)
# price_type(df_melbourne)
# sqft_price(df_melbourne)
# price_car_garage(df_melbourne)
# price_latitude_longitude(df_melbourne)
# price_date_sold(df_melbourne)
# price_year_built(df_melbourne)
# price_zipcode(df_melbourne)
# sqft_living_year_built(df_melbourne)
# suburb_year_built(df_melbourne)
# year_built(df_melbourne)
# tabelas_frequencia(df_melbourne)
