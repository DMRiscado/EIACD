import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, spearmanr, pearsonr

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


#year_built(df_australia)
#skewness_price(df_australia)
#pearson_correlation_price_sqft(df_australia)
#avg_median(df_australia)


