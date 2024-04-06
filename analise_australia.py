import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, spearmanr, pearsonr
import plotly.express as px

data_australia = "datasetfiles/australian_housing.csv"
df_australia = pd.read_csv(data_australia)

#Média e Mediana dos preços, quartos, casas de banho e carros na garagem na Austrália

def avg_median(df_australia):
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

def map_plot_price(df_australia):
    fig = px.scatter_mapbox(df_australia,
                            lat="latitude",
                            lon="longitude",
                            color="price",
                            center=dict(lat=-32.09, lon=133.25),
                            zoom=4,
                            color_continuous_scale=px.colors.cyclical.IceFire,
                            range_color=(df_australia['price'].min(), df_australia['price'].max()),
                            custom_data=[df_australia['bathrooms'], df_australia['bedrooms'],
                                         df_australia['sqft_living'], df_australia['price']])

    fig.update_traces(hovertemplate="<b>Latitude:</b> %{lat}<br>" +
                                    "<b>Longitude:</b> %{lon}<br>" +
                                    "<b>Preço:</b> %{marker.color} €<br>" +
                                    "<b>Casas de Banho:</b> %{customdata[0]} <br>" +
                                    "<b>Quartos:</b> %{customdata[1]}<br>" +
                                    "<b>Metros Quadrados:</b> %{customdata[2]} m²<extra></extra>")

    fig.update_layout(mapbox_style="open-street-map")
    fig.show()


#year_built(df_australia)
#skewness_price(df_australia)
#pearson_correlation_price_sqft(df_australia)
#avg_median(df_australia)
#map_plot_price(df_australia)
