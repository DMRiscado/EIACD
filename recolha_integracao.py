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


if set(["SellerG", "Unnamed: 0"]).issubset(df_melbourne.columns):
    df_melbourne.drop(["SellerG", "Unnamed: 0"], axis=1, inplace=True)

if set(['nearest_sch_rank','nearest_sch_dist','nearest_sch','nearest_stn_dist','nearest_stn', 'cbd_dist'  , "Unnamed: 0"]).issubset(df_perth.columns):
    df_perth.drop(["nearest_sch_rank", 'nearest_sch_rank', 'nearest_sch', 'nearest_stn_dist', 'nearest_stn', 'cbd_dist', "Unnamed: 0"], axis=1, inplace=True)


# Renomear colunas Delhi


# Renomear colunas Melbourne
df_melbourne.rename(columns = {'Suburb':'suburb'}, inplace = True)
df_melbourne.rename(columns = {'Address':'address'}, inplace = True)
df_melbourne.rename(columns = {'Rooms':'rooms'}, inplace = True)
df_melbourne.rename(columns = {'Type':'type'}, inplace = True)
df_melbourne.rename(columns = {'Price':'price'}, inplace = True)
df_melbourne.rename(columns = {'Method':'method_sale'}, inplace = True)
df_melbourne.rename(columns = {'Date':'date_sold'}, inplace = True)
df_melbourne.rename(columns = {'Distance':'cbd_dist'}, inplace = True)
df_melbourne.rename(columns = {'Postcode':'zipcode'}, inplace = True)
df_melbourne.rename(columns = {'Bedroom2':'bedrooms'}, inplace = True)
df_melbourne.rename(columns = {'Bathroom':'bathrooms'}, inplace = True)
df_melbourne.rename(columns = {'Car':'car_garage'}, inplace = True)
df_melbourne.rename(columns = {'Landsize':'sqft_terrain'}, inplace = True)
df_melbourne.rename(columns = {'BuildingArea':'sqft_contructionarea'}, inplace = True)
df_melbourne.rename(columns = {'YearBuilt':'yr_built'}, inplace = True)
df_melbourne.rename(columns = {'CouncilArea':'councilarea'}, inplace = True)
df_melbourne.rename(columns = {'Latitude':'latitude'}, inplace = True)
df_melbourne.rename(columns = {'Longtitude':'longitude'}, inplace = True)
df_melbourne.rename(columns = {'Regionname':'regionname'}, inplace = True)
df_melbourne.rename(columns = {'Propertycount':'propertycount'}, inplace = True)

# Renomear colunas Perth
df_perth.rename(columns = {'ADDRESS':'address'}, inplace = True)
df_perth.rename(columns = {'SUBURB':'suburb'}, inplace = True)
df_perth.rename(columns = {'PRICE':'price'}, inplace = True)
df_perth.rename(columns = {'BEDROOMS':'bedrooms'}, inplace = True)
df_perth.rename(columns = {'BATHROOMS':'bathrooms'}, inplace = True)
df_perth.rename(columns = {'GARAGE':'car_garage'}, inplace = True)
df_perth.rename(columns = {'LAND_AREA':'sqft_lot'}, inplace = True)
df_perth.rename(columns = {'FLOOR_AREA':'sqft_living'}, inplace = True)
df_perth.rename(columns = {'BUILD_YEAR':'yr_built'}, inplace = True)
df_perth.rename(columns = {'CBD_DIST':'cbd_dist'}, inplace = True)
df_perth.rename(columns = {'NEAREST_STN':'nearest_stn'}, inplace = True)
df_perth.rename(columns = {'NEAREST_STN_DIST':'nearest_stn_dist'}, inplace = True)
df_perth.rename(columns = {'DATE_SOLD':'date_sold'}, inplace = True)
df_perth.rename(columns = {'POSTCODE':'zipcode'}, inplace = True)
df_perth.rename(columns = {'LATITUDE':'latitude'}, inplace = True)
df_perth.rename(columns = {'LONGITUDE':'longitude'}, inplace = True)
df_perth.rename(columns = {'NEAREST_SCH':'nearest_sch'}, inplace = True)
df_perth.rename(columns = {'NEAREST_SCH_DIST':'nearest_sch_dist'}, inplace = True)
df_perth.rename(columns = {'NEAREST_SCH_RANK':'nearest_sch_rank'}, inplace = True)


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

