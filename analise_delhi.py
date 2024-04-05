import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

#Dataframe de Delhi

data_delhi = "datasetfiles/delhi_housing.csv"
df_delhi = pd.read_csv(data_delhi)

#Média e Mediana dos preços, quartos, casas de banho e carros na garagem em Delhi

media_preco = df_delhi['price'].mean()
mediana_preco = df_delhi['price'].median()
print(f"Média dos preços em Delhi: {media_preco:.2f} €")
print(f"Mediana dos preços em Delhi: {mediana_preco:.2f} €\n")


media_quartos = df_delhi["bedrooms"].mean()
mediana_quartos = round(media_quartos)
print(f"Média de quartos em Delhi: {int(media_quartos)}")
print(f"Mediana de quartos em Delhi: {mediana_quartos}\n")

media_wc = df_delhi["bathrooms"].mean()
mediana_wc = df_delhi["bathrooms"].median()
print(f"Média de casas de banho em Delhi: {int(media_wc)}")
print(f"Mediana de casas de banho em Delhi: {mediana_wc}\n")

media_carros = df_delhi["car_garage"].mean()
mediana_carros = df_delhi["car_garage"].median()
print(f"Média de carros na garagem em Delhi: {int(media_carros)}")
print(f"Mediana de carros na garagem em Delhi: {mediana_carros}\n")
print("__________________________________________________________\n")

#Funções de Análise

def price_sqft_living(df_delhi): #Preço em relação à Área Construída
    plt.figure(figsize=(10, 6))
    plt.scatter("sqft_living", "price", data=df_delhi, color='blue', alpha=0.5)
    plt.title('Preço em relação à Área Construída')
    plt.xlabel('Área Construída (em m²)')
    plt.ylabel('Preço (em €)')
    plt.grid(True)
    plt.yticks(ticks=range(0, int(df_delhi['price'].max()) + 100000, 100000))
    plt.ticklabel_format(style='plain', axis='y')
    plt.show()


def price_type_of_building(df_delhi): #Preço Médio por Tipo de Construção
    plt.figure(figsize=(10, 6))
    preco_por_tipo = df_delhi.groupby('type_of_building')['price'].mean()
    preco_por_tipo.plot(kind='bar', color='blue')
    plt.title('Preço Médio por Tipo de Construção')
    plt.xlabel('Tipo de Construção')
    plt.ylabel('Preço Médio (em €)')
    plt.xticks(rotation=1)
    plt.grid(axis='y')
    plt.show()


def price_balcony(df_delhi): #Preço Médio por Varanda
    plt.figure(figsize=(10, 6))
    preco_por_varanda = df_delhi.groupby('balcony')['price'].mean()
    preco_por_varanda.plot(kind='bar', color='blue')
    plt.title('Preço Médio por Número de Varandas')
    plt.xlabel('Varandas')
    plt.ylabel('Preço Médio (em €)')
    plt.xticks(rotation=1)
    plt.grid(axis='y')
    plt.show()


def price_latitude_longitude(df_delhi): #Preço em relação à Localização Geográfica
    plt.figure(figsize=(10, 6))
    plt.scatter(df_delhi['longitude'], df_delhi['latitude'], c=df_delhi['price'], cmap='viridis', s=50, alpha=0.5)
    plt.clim(df_delhi['price'].min(), df_delhi['price'].max()*1)
    plt.title('Preço em relação à Localização Geográfica')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.colorbar(label='Preço (em €)')
    plt.grid(True)
    plt.show()


def price_bedrooms_bathrooms(df_delhi): #Preço em relação a Quartos e Casas de Banho
    plt.figure(figsize=(10, 6))
    plt.scatter(df_delhi['bedrooms'], df_delhi['bathrooms'], c=df_delhi['price'], cmap='viridis', s=50, alpha=0.5)
    plt.clim(df_delhi['price'].min(), df_delhi['price'].max() * 1)
    plt.title('Preço em relação a Quartos e Casas de Banho')
    plt.xlabel('Quartos')
    plt.ylabel('Casas de Banho')
    plt.colorbar(label='Preço (em €)')
    plt.grid(True)
    plt.show()
# Perceber a distribuição (Gaussiana?)

def price_car_garage(df_delhi): #Preço Médio por Número de Vagas na Garagem
    plt.figure(figsize=(10, 6))
    plt.scatter(df_delhi['car_garage'], df_delhi['price'], color='blue', alpha=0.5)
    plt.title('Preço em relação a Número de Vagas de Garagem')
    plt.xlabel('Número de Vagas de Garagem')
    plt.ylabel('Preço (em €)')
    plt.grid(True)
    plt.show()


def type_of_building_latitude_longitude(df_delhi): #Localização por Tipo de Construção
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


def price_sqft_latitude_longitude(df_delhi): #Preço por metro quadrado em relação à Localização Geográfica
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='longitude', y='latitude', hue='price_sqft', palette='viridis', data=df_delhi)
    plt.title('Preço por metro quadrado em relação à Localização Geográfica')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    scatter = plt.scatter([], [], c=[], cmap='viridis')
    plt.grid(True)
    plt.show()

def pearson_correlation_price_sqft(df_delhi):
    corr, _ = pearsonr(df_delhi['sqft_living'], df_delhi['price'])
    print('Correlação de Pearson para os metros quadrados úteis da casa e preço: %.3f' % corr)

#Tabelas de Frequência, quartos, casas de banho e carros na garagem em Delhi

def freq_table(df_delhi):
    print("Tabela de Frequência de Quartos, Casas de Banho e Carros na Garagem em Delhi:")
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
    print("__________________________________________________________\n")

#Funções de Análise, Para serem executadas é retirar o "#" da frente de cada função

# price_sqft_living(df_delhi)
# price_type_of_building(df_delhi)
# price_balcony(df_delhi)
# price_latitude_longitude(df_delhi)
# price_bedrooms_bathrooms(df_delhi)
# price_car_garage(df_delhi)
# type_of_building_latitude_longitude(df_delhi)
# price_sqft_latitude_longitude(df_delhi)
# pearson_correlation_price_sqft(df_delhi)
# freq_table(df_delhi)
