import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
import plotly.express as px

#Dataframe de Delhi

data_delhi = "datasetfiles/delhi_housing.csv"
df_delhi = pd.read_csv(data_delhi)

#Média e Mediana dos preços, quartos, casas de banho e carros na garagem em Delhi

def avg_median_price(df_delhi):
    media_preco = df_delhi['price'].mean()
    mediana_preco = df_delhi['price'].median()
    print(f"Média dos preços em Delhi: {media_preco:.2f} €")
    print(f"Mediana dos preços em Delhi: {mediana_preco:.2f} €\n")

def avg_median_bedrooms(df_delhi):
    media_quartos = df_delhi["bedrooms"].mean()
    mediana_quartos = round(media_quartos)
    print(f"Média de quartos em Delhi: {int(media_quartos)}")
    print(f"Mediana de quartos em Delhi: {mediana_quartos}\n")

def avg_median_bathrooms(df_delhi):
    media_wc = df_delhi["bathrooms"].mean()
    mediana_wc = df_delhi["bathrooms"].median()
    print(f"Média de casas de banho em Delhi: {int(media_wc)}")
    print(f"Mediana de casas de banho em Delhi: {mediana_wc}\n")

def avg_median_garage(df_delhi):
    media_carros = df_delhi["car_garage"].mean()
    mediana_carros = df_delhi["car_garage"].median()
    print(f"Média de carros na garagem em Delhi: {int(media_carros)}")
    print(f"Mediana de carros na garagem em Delhi: {mediana_carros}\n")


#Funções de Análise

#Preço em relação à Área Construída

def price_sqft_living(df_delhi):
    plt.figure(figsize=(10, 6))
    plt.scatter("sqft_living", "price", data=df_delhi, color='blue', alpha=0.5)
    plt.title('Preço em relação à Área Construída')
    plt.xlabel('Área Construída (em m²)')
    plt.ylabel('Preço (em €)')
    plt.grid(True)
    plt.yticks(ticks=range(0, int(df_delhi['price'].max()) + 100000, 100000))
    plt.ticklabel_format(style='plain', axis='y')
    plt.show()

#Preço Médio por Tipo de Construção

def price_type_of_building(df_delhi):
    plt.figure(figsize=(10, 6))
    preco_por_tipo = df_delhi.groupby('type_of_building')['price'].mean()
    preco_por_tipo.plot(kind='bar', color='blue')
    plt.title('Preço Médio por Tipo de Construção')
    plt.xlabel('Tipo de Construção')
    plt.ylabel('Preço Médio (em €)')
    plt.xticks(rotation=1)
    plt.grid(axis='y')
    plt.show()

#Preço Médio por Varanda

def price_balcony(df_delhi):
    plt.figure(figsize=(10, 6))
    preco_por_varanda = df_delhi.groupby('balcony')['price'].mean()
    preco_por_varanda.plot(kind='bar', color='blue')
    plt.title('Preço Médio por Número de Varandas')
    plt.xlabel('Varandas')
    plt.ylabel('Preço Médio (em €)')
    plt.xticks(rotation=1)
    plt.grid(axis='y')
    plt.show()

#Preço em relação à Localização Geográfica

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

#Preço em relação a Quartos e Casas de Banho

def price_bedrooms_bathrooms(df_delhi):
    plt.figure(figsize=(10, 6))
    plt.scatter(df_delhi['bedrooms'], df_delhi['bathrooms'], c=df_delhi['price'], cmap='viridis', s=50, alpha=0.5)
    plt.clim(df_delhi['price'].min(), df_delhi['price'].max() * 1)
    plt.title('Preço em relação a Quartos e Casas de Banho')
    plt.xlabel('Quartos')
    plt.ylabel('Casas de Banho')
    plt.colorbar(label='Preço (em €)')
    plt.grid(True)
    plt.show()


#Preço Médio por Número de Vagas na Garagem

def price_car_garage(df_delhi):
    plt.figure(figsize=(10, 6))
    plt.scatter(df_delhi['car_garage'], df_delhi['price'], color='blue', alpha=0.5)
    plt.title('Preço em relação a Número de Vagas de Garagem')
    plt.xlabel('Número de Vagas de Garagem')
    plt.ylabel('Preço (em €)')
    plt.grid(True)
    plt.show()

#Localização por Tipo de Construção

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

#Preço por metro quadrado em relação à Localização Geográfica

def price_sqft_latitude_longitude(df_delhi):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='longitude', y='latitude', hue='price_sqft', palette='viridis', data=df_delhi)
    plt.title('Preço por metro quadrado em relação à Localização Geográfica')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    scatter = plt.scatter([], [], c=[], cmap='viridis')
    plt.grid(True)
    plt.show()
    # Perceber a distribuição (Gaussiana?)

# Correlação de Pearson entre preço e metros quadrados

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

def map_plot_price(df_delhi):
    fig = px.scatter_mapbox(df_delhi,
                            lat="latitude",
                            lon="longitude",
                            color="price",
                            center=dict(lat=28.70, lon=77.10),
                            zoom=8,
                            color_continuous_scale=px.colors.cyclical.IceFire,
                            range_color=(df_delhi['price'].min(), df_delhi['price'].max()),
                            custom_data=[df_delhi['bathrooms'], df_delhi['bedrooms'], df_delhi['sqft_living'], df_delhi['price']])

    fig.update_traces(hovertemplate="<b>Latitude:</b> %{lat}<br>" +
                                    "<b>Longitude:</b> %{lon}<br>" +
                                    "<b>Preço:</b> %{marker.color} €<br>" +
                                    "<b>Casas de Banho:</b> %{customdata[0]}<br>" +
                                    "<b>Quartos:</b> %{customdata[1]}<br>" +
                                    "<b>Metros Quadrados:</b> %{customdata[2]} m²<extra></extra>")

    fig.update_layout(mapbox_style="open-street-map")
    fig.show()



# Execução das funções

#avg_median_price(df_delhi)
#avg_median_bedrooms(df_delhi)
#avg_median_bathrooms(df_delhi)
#avg_median_garage(df_delhi)
#price_sqft_living(df_delhi)
#price_type_of_building(df_delhi)
#price_balcony(df_delhi)
#price_latitude_longitude(df_delhi)
#price_bedrooms_bathrooms(df_delhi)
#price_car_garage(df_delhi)
#type_of_building_latitude_longitude(df_delhi)
#price_sqft_latitude_longitude(df_delhi)
#pearson_correlation_price_sqft(df_delhi)
#freq_table(df_delhi)
#map_plot_price(df_delhi)