import pandas as pd

data_melbourne = "datasetfiles/melbourne_housing.csv"
df_melbourne = pd.read_csv(data_melbourne)

missing_values = df_melbourne.isnull().sum()
print(missing_values)


#def remover_linhas(df_melbourne, arquivo_csv):
    #valores_falta = df_melbourne.isnull().sum(axis=1)
    #indices_remover = valores_falta[valores_falta == 7].index
    #df = df_melbourne.drop(indices_remover)
    #df.to_csv(arquivo_csv, index=False)

#remover_linhas(df_melbourne, 'datasetfiles/melbourne_housing.csv')


#colunas_em_falta = ["bedrooms", "bathrooms", "car_garage", "sqft_living", "year_built", "latitude", "longitude"]

#for col in df_melbourne.columns:
    #if df_melbourne[col].dtype != 'object':
        #median = df_melbourne[col].median()
        #df_melbourne[col].fillna(median, inplace=True)

#df_melbourne.to_csv('datasetfiles/melbourne_housing.csv', index=False)