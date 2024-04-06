import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from scipy.stats import skew, spearmanr, pearsonr


# importar datasets
data_delhi = "datasetfiles/delhi_housing.csv"
df_delhi = pd.read_csv(data_delhi)

data_melbourne = "datasetfiles/melbourne_housing.csv"
df_melbourne = pd.read_csv(data_melbourne)

data_perth = "datasetfiles/perth_housing.csv"
df_perth = pd.read_csv(data_perth)


data_total= "datasetfiles\concatenated_housing.csv"
df_analise = pd.read_csv(data_total)

# mediana dos metros quarados disponiveis

def median_sqft(df_analise):
    median_sqft = df_analise['sqft_living'].median()
    print("Mediana de metros quadrados disponíveis: ", median_sqft)

# mediana dos preços

def median_price(df_analise):
    median_price = df_analise['price'].median()
    print("Mediana dos preços: ", median_price)

#média dos preços

def mean_price(df_analise):
    mean_price = df_analise['price'].mean()
    print("Média dos preços: ", mean_price)

#média dos quartos disponíveis arredondada

def mean_bedrooms(df_analise):
    mean_bedrooms = round(df_analise['bedrooms'].mean())
    print("Média dos quartos disponíveis: ", mean_bedrooms)

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

#Tabela com a latitude, longitude e metros quadrados de cada casa

def sqft_latitude_longitude(df_analise):

    grouped = df_analise.groupby('latitude')

    data = []
    for name, group in grouped:
        data.extend(zip(group['latitude'], group['longitude'], group['sqft_living']))
    df_table = pd.DataFrame(data, columns=['Latitude', 'Longitude', 'Square Footage of Living Space'])
    df_table = df_table.sort_values(by='Latitude')
    df_table.reset_index(drop=True, inplace=True)

    print(df_table)

# tabela de frequência do tipo de casa na Índia

def type_house_delhi(df_analise):
    df_analise['type_of_building'] = df_analise['type_of_building'].str.replace(' ', '')
    df_type_house = df_analise['type_of_building'].value_counts().reset_index(name='Número de casas')
    print(df_type_house)

# tabela de frequência do tipo de casa em Melbourne

def type_house_melbourne(df_analise):
    df_analise['type'] = df_analise['type'].str.replace(' ', '')
    df_type_house = df_analise['type'].value_counts().reset_index(name='Número de casas')
    print("As letras respeitam a seguinte tipologia: h-house | u-unit (apartamento ou unidade) | t-townhouse \n")
    print(df_type_house)

# skewness do preço

def skewness_price(df_analise):
    skewness = skew(df_analise['price'])
    print("Skewness: ", skewness)


#correlação de spearman sobre o preço e os metros quadrados

def spearman_correlation_price_sqft(df_analise):
    df_cleaned = df_analise.dropna(subset=['sqft_living', 'price'])
    spearman_corr, p_value = spearmanr(df_cleaned['price'], df_cleaned['sqft_living'])

    print("Correlação de Spearman para preço e metros quadrados:", spearman_corr)
    print("p-value:", p_value)


#correlação de pearson sobre o preço e os metros quadrados

def pearson_correlation_price_sqft(df_analise):
    df_cleaned= df_analise.dropna(subset=['sqft_living','price'])
    corr, _ = pearsonr(df_cleaned['price'], df_cleaned['sqft_living'])
    print('Correlação de Pearson para preço e metros quadrados: %.3f' % corr)

# correlação de spearman entre casas de banho e quartos

def spearman_correlation_bathroom_bedroom(df_analise):
    df_cleaned = df_analise.dropna(subset=['bathrooms', 'bedrooms'])
    spearman_corr, p_value = spearmanr(df_cleaned['bathrooms'], df_cleaned['bedrooms'])

    print("Spearman correlation coefficient:", spearman_corr)
    print("p-value:", p_value)

#correlação de pearson entre casas de banho e quartos

def pearson_correlation_bathroom_bedroom(df_analise):
    df_cleaned = df_analise.dropna(subset=['bathrooms', 'bedrooms'])
    corr, _ = pearsonr(df_cleaned['bathrooms'],df_cleaned['bedrooms'])
    print('Correlação de Pearson para casas de banho e quartos: %.3f' % corr)

#correlação de spearman entre ano de construção e preço

def spearman_correlation_yrbuilt_price(df_analise):
    df_cleaned = df_analise.dropna(subset=['year_built', 'price'])
    spearman_corr, p_value = spearmanr(df_cleaned['year_built'], df_cleaned['price'])

    print("Spearman correlation coefficient:", spearman_corr)
    print("p-value:", p_value)

#correlação de pearson entre ano de construção e preço

def pearson_correlation_yrbuilt_price(df_analise):
    df_cleaned = df_analise.dropna(subset=['year_built', 'price'])
    corr, _ = pearsonr(df_cleaned['year_built'], df_cleaned['price'])
    print('Correlação de Pearson para ano de construção e preço: %.3f' % corr)

#quartis do preço

def quantile_price(df_analise):
    q1 = np.quantile(df_analise['price'], 0.25)
    q2 = np.quantile(df_analise['price'], 0.50)
    q3 = np.quantile(df_analise['price'], 0.75)

    print("Quartis do preço \n")
    print("Primeiro Quartil:", q1)
    print("Segundo Quartil:", q2)
    print("Terceiro Quartil:", q3)

#quartis dos quartos

def quantile_bedrooms(df_analise):
    df_cleaned = df_analise.dropna(subset=['bedrooms'])
    q1 = np.quantile(df_cleaned['bedrooms'], 0.25)
    q2 = np.quantile(df_cleaned['bedrooms'], 0.50)
    q3 = np.quantile(df_cleaned['bedrooms'], 0.75)

    print("Quartis dos quartos \n")
    print("Primeiro Quartil:", q1)
    print("Segundo Quartil:", q2)
    print("Terceiro Quartil:", q3)

#kurtosis do preço

def plot_price_kurtosis(df_analise):
    price_data = df_analise['price']
    kurt = price_data.kurtosis()

    plt.figure(figsize=(10, 6))
    sns.histplot(price_data, kde=True, color='blue', bins=30)

    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    y = ((1 / (np.sqrt(2 * np.pi) * price_data.std())) *
         np.exp(-0.5 * ((x - price_data.mean()) / price_data.std()) ** 2))
    plt.plot(x, y, color='red', linestyle='--', label='Normal Distribution')

    plt.title(f'Histogram of Price (Kurtosis: {kurt:.2f})')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True)
    plt.show()

#histograma do número de quartos e preço para quartos inferiores a 6

def number_bedrooms_price_under_six(df_analise):
    df = df_analise[df_analise["bedrooms"] < 6]
    g = sns.FacetGrid(df, col="bedrooms", col_wrap=4)
    g.map(sns.histplot, "price")
    g.set(xlim=(0, 2000000))
    plt.show()






#mean_price(df_analise)
#median_price(df_analise)
#median_sqft(df_analise)
#mean_bedrooms(df_analise)
#price_latitude_longitude(df_analise)
#year_built(df_analise)
#yrbuilt_bathrooms_bedrooms(df_analise)
#sqft_latitude_longitude(df_analise)
#type_house_delhi(df_analise)
#type_house_melbourne(df_analise)
#skewness_price(df_analise)
#spearman_correlation_price_sqft(df_analise)
#pearson_correlation_price_sqft(df_analise)
#spearman_correlation_bathroom_bedroom(df_analise)
#pearson_correlation_bathroom_bedroom(df_analise)
#spearman_correlation_yrbuilt_price(df_analise)
#pearson_correlation_yrbuilt_price(df_analise)
#quantile_price(df_analise)
#quantile_bedrooms(df_analise)
#plot_price_kurtosis(df_analise)
#number_bedrooms_price_under_six(df_analise)

#para determinados metros quadrados, tentar relacionar preço máximo e mínimo e perceber a inexistência de correlação
#EXPLICADO, O DOCUMENTO NÃO ESTAVA BEM CONCATENADO

