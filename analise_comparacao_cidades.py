import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from scipy.stats import skew

# importar datasets
data_delhi = "datasetfiles/delhi_housing.csv"
df_delhi = pd.read_csv(data_delhi)

data_melbourne = "datasetfiles/melbourne_housing.csv"
df_melbourne = pd.read_csv(data_melbourne)

data_perth = "datasetfiles/perth_housing.csv"
df_perth = pd.read_csv(data_perth)


data_total= "datasetfiles\concatenated_housing.csv"
df_analise = pd.read_csv(data_total)

# # mediana dos metros quarados disponiveis
# median_sqft = df_analise['sqft_living'].median()
# print("Mediana de metros quadrados disponíveis: ", median_sqft)
#
# # mediana dos preços
# median_price = df_analise['price'].median()
# print("Mediana dos preços: ", median_price)
#
# #média dos preços
# mean_price = df_analise['price'].mean()
# print("Média dos preços: ", mean_price)
#
# #média dos quartos disponíveis arredondada
# mean_bedrooms = round(df_analise['bedrooms'].mean())
# print("Média dos quartos disponíveis: ", mean_bedrooms)

#gráfico três dimensões latitude, longitude e preço
def price_latitude_longitude(df_analise):

    plt.figure(figsize=(10, 6))
    plt.scatter(df_analise['longitude'], df_analise['latitude'], c=df_analise['price'], cmap='viridis', s=35, alpha=0.7)
    plt.clim(df_analise['price'].min(), df_analise['price'].max() * 0.15)
    plt.colorbar(label='Price')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Preço por região do mapa ')
    Caption= "Os pontos no canto superior esquerdo correspondem às casas em Deli, os que estão mais próximos do meio a Perth e os restantes a Melbourne."
    plt.text(0.5,-0.12, Caption,ha='center',va='center', transform=plt.gca().transAxes, fontsize= 7)
    plt.grid(True)
    plt.show()

#tabela com o ano de construção e o número de casas construídas nesse ano
def year_built(df_analise):
    df_year_built = df_analise.groupby('year_built').size().reset_index(name='Number of houses')
    pd.set_option('display.max_rows', None)
    print(df_year_built)


#year_built(df_analise)


# gráfico que relaciona ano de construção da casa com número de quartos e casas de banho
def yrbuilt_bathrooms_bedrooms(df_analise):
    x = df_analise['bathrooms']
    y = df_analise['bedrooms']
    z = df_analise['year_built']

    fig, ax = plt.subplots(figsize=(9, 6))

    hexbin = ax.hexbin(x=x, y=y, C=z, gridsize=20,
                       cmap='Greens'
                       )

    ax.set_xlabel('Casas de Banho')
    ax.set_ylabel('Quartos')
    cb = fig.colorbar(hexbin, ax=ax, label='Ano de Construção')

    ax.set_title('Casas de Banho e Quartos em função do ano de construção, 1930 em diante', size=14)

    plt.show()


def sqft_latitude_longitude(df_analise):

    grouped = df_analise.groupby('latitude')

    data = []
    for name, group in grouped:
        data.extend(zip(group['latitude'], group['longitude'], group['sqft_living']))

    df_table = pd.DataFrame(data, columns=['Latitude', 'Longitude', 'Square Footage of Living Space'])
    df_table = df_table.sort_values(by='Latitude')
    df_table.reset_index(drop=True, inplace=True)

    # Display the DataFrame
    print(df_table)


# Assuming df_analise is your DataFrame
sqft_latitude_longitude(df_analise)
