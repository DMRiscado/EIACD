import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, spearmanr, pearsonr
import plotly.express as px


data_australia = "datasetfiles/australian_housing.csv"
df_australia = pd.read_csv(data_australia)


#Média e Mediana dos preços

def avg_median_price(df_australia):
    media_preco = df_australia['price'].mean()
    mediana_preco = df_australia['price'].median()
    print(f"Média dos preços na Austrália: {media_preco:.2f} €")
    print(f"Mediana dos preços na Austrália: {mediana_preco:.2f} €\n")

#Correlação de Pearson entre preço e área em metros quadrados

def pearson_correlation_price_sqft(df_australia):
    corr, _ = pearsonr(df_australia['sqft_living'], df_australia['price'])
    print('Correlação de Pearson para os metros quadrados úteis da casa e preço: %.3f' % corr)

# Skewness do preço australiano

def skewness_price(df_australia):
    skewness = skew(df_australia['price'])
    print("Skewness: ", skewness)

#Ano de construção das casas na Austrália

def year_built(df_australia):
    df_year_built = df_australia.groupby('year_built').size().reset_index(name='Number of houses')
    pd.set_option('display.max_rows', None)
    print(df_year_built)

#Mapa de preços (HTML)

def map_plot_price(df_australia, filename="map_australia.html"):
    # Assuming 'price' is in AUD, converting it to Euros
    df_australia['price_eur'] = df_australia['price'] * 0.62  # Conversion rate: 1 AUD = 0.62 EUR

    fig = px.scatter_mapbox(df_australia,
                            lat="latitude",
                            lon="longitude",
                            color="price_eur",
                            center=dict(lat=-32.09, lon=133.25),
                            zoom=4,
                            color_continuous_scale=px.colors.cyclical.IceFire,
                            range_color=(df_australia['price_eur'].min(), df_australia['price_eur'].max()),
                            custom_data=[df_australia['bathrooms'], df_australia['bedrooms'],
                                         df_australia['sqft_living'], df_australia['price']])

    fig.update_traces(hovertemplate="<b>Latitude:</b> %{lat}<br>" +
                                    "<b>Longitude:</b> %{lon}<br>" +
                                    "<b>Price:</b> %{marker.color:.2f} €<br>" +
                                    "<b>Bathrooms:</b> %{customdata[0]} <br>" +
                                    "<b>Bedrooms:</b> %{customdata[1]}<br>" +
                                    "<b>Sqft Living:</b> %{customdata[2]} m²<extra></extra>")

    fig.update_layout(mapbox_style="open-street-map")
    fig.write_html(filename)

#Média e Mediana de quartos, casas de banho e garagem

def avg_median_bedrooms(df_australia):
    media_quartos = df_australia["bedrooms"].mean()
    mediana_quartos = round(media_quartos)
    print(f"Média de quartos em Austrália: {int(media_quartos)}")
    print(f"Mediana de quartos em Austrália: {mediana_quartos}\n")

def avg_median_bathrooms(df_australia):
    media_wc = df_australia["bathrooms"].mean()
    mediana_wc = df_australia["bathrooms"].median()
    print(f"Média de casas de banho em Austrália: {int(media_wc)}")
    print(f"Mediana de casas de banho em Austrália: {mediana_wc}\n")

def avg_median_garage(df_australia):
    media_carros = df_australia["car_garage"].mean()
    mediana_carros = df_australia["car_garage"].median()
    print(f"Média de carros na garagem em Austrália: {int(media_carros)}")
    print(f"Mediana de carros na garagem em Austrália: {mediana_carros}\n")


#Execução das funções

year_built(df_australia)
skewness_price(df_australia)
pearson_correlation_price_sqft(df_australia)
avg_median_price(df_australia)
map_plot_price(df_australia)
avg_median_bedrooms(df_australia)
avg_median_bathrooms(df_australia)
avg_median_garage(df_australia)
