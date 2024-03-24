import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium
# importar dataset
data_total= "datasetfiles\concatenated_housing.csv"
df_analise = pd.read_csv(data_total)

# mediana dos metros quarados disponiveis
median_sqft = df_analise['sqft_living'].median()
print("Mediana de metros quadrados disponíveis: ", median_sqft)

# mediana dos preços
median_price = df_analise['price'].median()
print("Mediana dos preços: ", median_price)

#média dos preços
mean_price = df_analise['price'].mean()
print("Média dos preços: ", mean_price)

#média dos quartos disponíveis arredondada
mean_bedrooms = round(df_analise['bedrooms'].mean())
print("Média dos quartos disponíveis: ", mean_bedrooms)

#gráfico três dimensões latitude, longitude e preço

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

#gráfico três dimensões com ano de construção, metros quadrados úteis e preço