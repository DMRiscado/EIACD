import pandas as pd
import os
import numpy as np

data_delhi = "datasetfiles/delhi_housing.csv"
data_melbourne = "datasetfiles/melbourne_housing.csv"
data_perth = "datasetfiles/perth_housing.csv"

# Carregar os DataFrames

df_delhi = pd.read_csv(data_delhi)
df_melbourne = pd.read_csv(data_melbourne)
df_perth = pd.read_csv(data_perth)

# Eliminação de colunas desnecessárias se as colunas existirem no DataFrame, COMENTADO PARA NÃO ACUSAR ERRO

#delhi_drop = ["Status", "neworold", "Furnished_status", "Lift", "Landmarks", "desc", "Unnamed: 0"]
#df_delhi.drop(columns=delhi_drop, inplace=True)

#melbourne_drop = ["Rooms", "Method", "SellerG", "Distance", "BuildingArea", "CouncilArea", "Regionname", "Propertycount", "Unnamed: 0"]
#df_melbourne.drop(columns=melbourne_drop, inplace=True)

#perth_drop = ["CBD_DIST", "NEAREST_STN","NEAREST_STN_DIST", "NEAREST_SCH", "NEAREST_SCH_DIST", "NEAREST_SCH_RANK"]
#df_perth.drop(columns=perth_drop, inplace=True)



# Renomear colunas Delhi
df_delhi.rename(columns = {'price':'price'}, inplace = True)
df_delhi.rename(columns = {'Address':'address'}, inplace = True)
df_delhi.rename(columns = {'area':'sqft_living'}, inplace = True)
df_delhi.rename(columns = {'latitude':'latitude'}, inplace = True)
df_delhi.rename(columns = {'longitude':'longitude'}, inplace = True)
df_delhi.rename(columns = {'Bedrooms':'bedrooms'}, inplace = True)
df_delhi.rename(columns = {'Bathrooms':'bathrooms'}, inplace = True)
df_delhi.rename(columns = {'Balcony':'balcony'}, inplace = True)
df_delhi.rename(columns = {'parking':'car_garage'}, inplace = True)
df_delhi.rename(columns = {'type_of_building':'type_of_building'}, inplace = True)
df_delhi.rename(columns = {'Price_sqft':'price_sqft'}, inplace = True)

# Renomear colunas Melbourne
df_melbourne.rename(columns = {'Suburb':'suburb'}, inplace = True)
df_melbourne.rename(columns = {'Landsize':'sqft_living'}, inplace = True)
df_melbourne.rename(columns = {'Address':'address'}, inplace = True)
df_melbourne.rename(columns = {'Type':'type'}, inplace = True)
df_melbourne.rename(columns = {'Price':'price'}, inplace = True)
df_melbourne.rename(columns = {'Date':'date_sold'}, inplace = True)
df_melbourne.rename(columns = {'Postcode':'zipcode'}, inplace = True)
df_melbourne.rename(columns = {'Bedroom2':'bedrooms'}, inplace = True)
df_melbourne.rename(columns = {'Bathroom':'bathrooms'}, inplace = True)
df_melbourne.rename(columns = {'Car':'car_garage'}, inplace = True)
df_melbourne.rename(columns = {'YearBuilt':'year_built'}, inplace = True)
df_melbourne.rename(columns = {'Lattitude':'latitude'}, inplace = True)
df_melbourne.rename(columns = {'Longtitude':'longitude'}, inplace = True)

# Renomear colunas Perth
df_perth.rename(columns = {'ADDRESS':'address'}, inplace = True)
df_perth.rename(columns = {'SUBURB':'suburb'}, inplace = True)
df_perth.rename(columns = {'PRICE':'price'}, inplace = True)
df_perth.rename(columns = {'BEDROOMS':'bedrooms'}, inplace = True)
df_perth.rename(columns = {'BATHROOMS':'bathrooms'}, inplace = True)
df_perth.rename(columns = {'GARAGE':'car_garage'}, inplace = True)
df_perth.rename(columns = {'LAND_AREA':'sqft_lot'}, inplace = True)
df_perth.rename(columns = {'FLOOR_AREA':'sqft_living'}, inplace = True)
df_perth.rename(columns = {'BUILD_YEAR':'year_built'}, inplace = True)
df_perth.rename(columns = {'DATE_SOLD':'date_sold'}, inplace = True)
df_perth.rename(columns = {'POSTCODE':'zipcode'}, inplace = True)
df_perth.rename(columns = {'LATITUDE':'latitude'}, inplace = True)
df_perth.rename(columns = {'LONGITUDE':'longitude'}, inplace = True)

#Conversão de dados em inteiros

# Lista das colunas a serem convertidas para inteiros em cada DataFrame
# cols_to_convert_delhi = ['price', 'sqft_living', 'bedrooms', 'bathrooms','balcony', 'car_garage', 'price_sqft']
# cols_to_convert_perth = ['car_garage', 'year_built']
# cols_to_convert_melbourne = ['zipcode', 'bedrooms', 'bathrooms', 'car_garage', 'year_built', 'sqft_living']
#
# for col in cols_to_convert_delhi:
#     df_delhi[col] = pd.to_numeric(df_delhi[col], errors='coerce').astype('Int64')
#
# for col in cols_to_convert_perth:
#     df_perth[col] = pd.to_numeric(df_perth[col], errors='coerce').astype('Int64')
#
# for col in cols_to_convert_melbourne:
#     df_melbourne[col] = pd.to_numeric(df_melbourne[col], errors='coerce').astype('Int64')

#Conversão de datas; COMENTADO PARA NÃO ACUSAR ERRO
# df_perth['date_sold'] = pd.to_datetime(df_perth['date_sold'], format= "%m/%Y")
# df_perth['date_sold'] = df_perth['date_sold'].dt.strftime("%m/%Y")

#df_melbourne['date_sold'] = pd.to_datetime(df_melbourne['date_sold'], format= "%d/%m/%Y")
#df_melbourne['date_sold'] = df_melbourne['date_sold'].dt.strftime("%m/%Y")

#Conversão de preços para euros

#taxa_delhi = 0.011
#df_delhi['price'] *= taxa_delhi

# taxa_australia= 0.60
# df_melbourne['price'] *= taxa_australia
# df_perth['price'] *= taxa_australia


# Reescrever os arquivos originais com os DataFrames modificados
df_delhi.to_csv(data_delhi, index=False)
df_melbourne.to_csv(data_melbourne, index=False)
df_perth.to_csv(data_perth, index=False)


#print(df_delhi.dtypes)
#print(df_melbourne.dtypes)
#print(df_perth.dtypes)

#Concatenar os datasets depois de apurados e gravá-los numa novo CSV

concatenated_df = pd.concat([df_delhi, df_melbourne, df_perth], ignore_index=True)

concatenated_df.to_csv("datasetfiles/concatenated_housing.csv", index=False)



