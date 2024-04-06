import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Dataframe de Perth

data_perth = "datasetfiles/perth_housing.csv"
df_perth = pd.read_csv(data_perth)


#Média e Mediana dos preços, quartos, casas de banho e carros na garagem em Perth

def avg_median_price(df_perth):
    media_preco = df_perth['price'].mean()
    mediana_preco = df_perth['price'].median()
    print(f"Média dos preços em Perth: {media_preco:.2f} €")
    print(f"Mediana dos preços em Perth: {mediana_preco:.2f} €\n")

def avg_median_bedrooms(df_perth):
    media_quartos = df_perth["bedrooms"].mean()
    mediana_quartos = df_perth["bedrooms"].median()
    print(f"Média de quartos em Perth: {int(media_quartos)}")
    print(f"Mediana de quartos em Perth: {mediana_quartos}\n")

def avg_median_bathrooms(df_perth):
    media_wc = df_perth["bathrooms"].mean()
    mediana_wc = df_perth["bathrooms"].median()
    print(f"Média de casas de banho em Perth: {int(media_wc)}")
    print(f"Mediana de casas de banho em Perth: {mediana_wc}\n")

def avg_median_garage(df_perth):
    media_carros = df_perth["car_garage"].mean()
    mediana_carros = df_perth["car_garage"].median()
    print(f"Média de carros na garagem em Perth: {int(media_carros)}")
    print(f"Mediana de carros na garagem em Perth: {mediana_carros}\n")
    print("__________________________________________________________\n")

#Funções de Análise

#Preço Médio por Subúrbio

def price_suburb(df_perth):
    preco_por_suburb = df_perth.groupby('suburb')['price'].mean().reset_index()
    preco_por_suburb.columns = ['Subúrbio', 'Preço Médio (em €)']
    preco_por_suburb['Preço Médio (em €)'] = preco_por_suburb['Preço Médio (em €)'].round(2)
    preco_por_suburb_sorted = preco_por_suburb.sort_values(by='Preço Médio (em €)', ascending=True)
    print(preco_por_suburb_sorted)

#Preço em relação aos Quartos e Casas de Banho

def price_bedrooms_bathrooms(df_perth):
    plt.figure(figsize=(10, 6))
    plt.scatter(df_perth['bedrooms'], df_perth['bathrooms'], c=df_perth['price'], cmap='viridis')
    plt.colorbar(label='Preço (em €)')
    plt.xlabel('Quartos')
    plt.ylabel('Casas de Banho')
    plt.title('Preço em relação aos Quartos e Casas de Banho')
    plt.grid(True)
    plt.show()

#Preço em relação ao Ano de Venda

def price_date_sold(df_perth):
    df_perth['date_sold'] = pd.to_datetime(df_perth['date_sold'])
    df_perth['year_sold'] = df_perth['date_sold'].dt.year
    preco_por_ano = df_perth.groupby('year_sold')['price'].mean()
    plt.figure(figsize=(10, 6))
    preco_por_ano.plot(kind='line', color='blue', label='Preço Médio por Ano')
    plt.title('Preço em relação ao Ano de Venda')
    plt.xlabel('Data da Venda')
    plt.ylabel('Preço (em €)')
    plt.grid(True)
    plt.show()

#Preço Médio por Número de Vagas na Garagem

def price_car_garage(df_perth):
    plt.figure(figsize=(10, 6))
    plt.bar(df_perth['car_garage'], df_perth['price'])
    plt.xlabel('Número de Vagas na Garagem')
    plt.ylabel('Preço (em €)')
    plt.title('Preço Médio por Número de Vagas na Garagem')
    plt.show()

#Preço em relação ao Código Postal

def price_zipcode(df_perth):
    plt.figure(figsize=(10, 6))
    plt.bar(df_perth['zipcode'], df_perth['price'])
    plt.xlabel('Código Postal')
    plt.ylabel('Preço (em €)')
    plt.title('Preço em relação ao Código Postal')
    plt.xticks(rotation=45)
    plt.show()

#Preço em relação à Localização Geográfica

def price_latitude_longitude(df_perth):
    plt.figure(figsize=(10, 6))
    plt.scatter(df_perth['latitude'], df_perth['longitude'], c=df_perth['price'], cmap='coolwarm')
    plt.clim(df_perth['price'].min(), df_perth['price'].max() * 1)
    plt.colorbar(label='Preço (em €)')
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.title('Preço em relação à Localização Geográfica')
    plt.show()

#Preço em relação ao Ano de Construção

def price_year_built(df_perth):
    plt.figure(figsize=(10, 6))
    plt.bar(df_perth['year_built'], df_perth['price'])
    plt.xlabel('Ano de Construção')
    plt.ylabel('Preço (em €)')
    plt.title('Preço em relação ao Ano de Construção')
    plt.show()

#Tamanho do Lote em relação ao Tamanho da Casa

def sqft_lot_sqft_living(df_perth):
    plt.figure(figsize=(10, 6))
    plt.scatter(df_perth['sqft_lot'], df_perth['sqft_living'])
    plt.xlabel('Tamanho do Lote')
    plt.ylabel('Tamanho da Casa')
    plt.title('Tamanho do Lote em relação ao Tamanho da Casa')
    plt.show()

#Número de casas construídas por ano

def year_built(df_perth):
    df_perth['year_built'] = df_perth['year_built'].fillna(0).astype(int)
    df = df_perth[df_perth['year_built'] != 0]
    casas_por_ano = df.groupby('year_built').size()
    casas_por_ano_ordenado = casas_por_ano.sort_values(ascending=False)
    print("Número de casas construídas por ano:")
    print(casas_por_ano_ordenado)


#Tabelas de Frequência, quartos, casas de banho e carros na garagem em Perth

def tabela_frequencia(df_perth):
    print("Tabela de Frequência de Quartos, Casas de Banho e Carros na Garagem em Perth:")
    freq_bedrooms = df_perth['bedrooms'].value_counts().sort_index()
    freq_bathrooms = df_perth['bathrooms'].value_counts().sort_index()
    freq_car_garage = df_perth['car_garage'].value_counts().sort_index()
    tabela_frequencia = pd.DataFrame({
        'Bedrooms': freq_bedrooms,
        'Bathrooms': freq_bathrooms,
        'Car Garage': freq_car_garage
    })
    tabela_frequencia = tabela_frequencia.fillna(0)
    print(tabela_frequencia)
    print("__________________________________________________________\n")


# Execução das funções

#avg_median_price(df_perth)
#avg_median_bedrooms(df_perth)
#avg_median_bathrooms(df_perth)
#avg_median_garage(df_perth)
#price_suburb(df_perth)
#price_bedrooms_bathrooms(df_perth)
#price_date_sold(df_perth)
#price_car_garage(df_perth)
#price_zipcode(df_perth)
#price_latitude_longitude(df_perth)
#price_year_built(df_perth)
#sqft_lot_sqft_living(df_perth)
#year_built(df_perth)


