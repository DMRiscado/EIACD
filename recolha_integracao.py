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

# Eliminação de colunas desnecessárias se as colunas existirem no DataFrame
if set(["Status", "newoorold", "Furnished_status", "Lift", "Landmarks", "desc", "Unnamed: 0"]).issubset(df_delhi.columns):
    df_delhi.drop(["Status", "newoorold", "Furnished_status", "Lift", "Landmarks", "desc", "Unnamed: 0"], axis=1, inplace=True)

if set(["Rooms", "Method", "SallerG", "Distance", "LandSize", "BuildingArea", "CouncilArea", "Regionname", "Propertycount", "Unnamed: 0"]).issubset(df_melbourne.columns):
    df_melbourne.drop(["Rooms", "Method", "SallerG", "Distance", "LandSize", "BuildingArea", "CouncilArea", "Regionname", "Propertycount", "Unnamed: 0"], axis=1, inplace=True)

if set(["CBD_DIST", "NEAREST_STN","NEAREST_STN_DIST", "NEAREST_SCH", "NEAREST_SCH_DIST", "NEAREST_SCH_RANK", "Unnamed: 0"]).issubset(df_perth.columns):
    df_perth.drop(["CBD_DIST", "NEAREST_STN","NEAREST_STN_DIST", "NEAREST_SCH", "NEAREST_SCH_DIST", "NEAREST_SCH_RANK", "Unnamed: 0"], axis=1, inplace=True)


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


#Conversão de inteiros





#Conversão de datas
df_perth['date_sold'] = pd.to_datetime(df_perth['date_sold'])
df_perth['date_sold'] = df_perth['date_sold'].dt.strftime("%m/%Y")




# Reescrever os arquivos originais com os DataFrames modificados
df_delhi.to_csv(data_delhi, index=False)
df_melbourne.to_csv(data_melbourne, index=False)
df_perth.to_csv(data_perth, index=False)

# print(df_kansas.dtypes)
# print(df_melbourne.dtypes)
# print(df_perth.dtypes)

# full join dos 3 dataframes

df_full = pd.concat([df_delhi, df_melbourne, df_perth], ignore_index=True)
df_full.to_csv("datasetfiles/full_housing.csv", index=False)

