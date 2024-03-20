import pandas as pd
import os
import numpy as np

data_kansas = "datasetfiles/kansas_housing.csv"
data_melbourne = "datasetfiles/melbourne_housing.csv"
data_perth = "datasetfiles/perth_housing.csv"

# Carregar os DataFrames

df_kansas = pd.read_csv(data_kansas)
df_melbourne = pd.read_csv(data_melbourne)
df_perth = pd.read_csv(data_perth)

# Eliminação de colunas desnecessárias se as colunas existirem no DataFrame
if set(["waterfront", "view", "grade", "sqft_above", "sqft_living15", "sqft_lot15", "Unnamed: 0"]).issubset(df_kansas.columns):
    df_kansas.drop(["waterfront", "view", "grade", "sqft_above", "sqft_living15", "sqft_lot15", "Unnamed: 0"], axis=1, inplace=True)

if set(["SellerG", "Unnamed: 0"]).issubset(df_melbourne.columns):
    df_melbourne.drop(["SellerG", "Unnamed: 0"], axis=1, inplace=True)



# Renomear colunas Kansas
df_kansas.rename(columns = {'id':'id'}, inplace = True)
df_kansas.rename(columns = {'date':'date_sold'}, inplace = True)
df_kansas.rename(columns = {'price':'price'}, inplace = True)
df_kansas.rename(columns = {'floors':'floors'}, inplace = True)
df_kansas.rename(columns = {'condition':'condition'}, inplace = True)
df_kansas.rename(columns = {'yr_build':'year_build'}, inplace = True)
df_kansas.rename(columns = {'yr_renovated':'year_renovated'}, inplace = True)
df_kansas.rename(columns = {'zipcode':'zipcode'}, inplace = True)
df_kansas.rename(columns = {'lat':'latitude'}, inplace = True)
df_kansas.rename(columns = {'long':'longitude'}, inplace = True)

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
df_melbourne.rename(columns = {'YearBuilt':'year_build'}, inplace = True)
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
df_perth.rename(columns = {'BUILD_YEAR':'year_build'}, inplace = True)
df_perth.rename(columns = {'CBD_DIST':'cbd_dist'}, inplace = True)
df_perth.rename(columns = {'BUILD_YEAR':'year_build'}, inplace = True)
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
conversao_kansas = ["price", "bathrooms", "floors"]
df_kansas[conversao_kansas] = df_kansas[conversao_kansas].astype(int)





#Conversão de datas
df_kansas['date_sold'] = pd.to_datetime(df_kansas['date_sold'])
df_kansas['date_sold'] = df_kansas['date_sold'].dt.strftime("%d/%m/%Y")

df_perth['date_sold'] = pd.to_datetime(df_perth['date_sold'])
df_perth['date_sold'] = df_perth['date_sold'].dt.strftime("%m/%Y")




# Reescrever os arquivos originais com os DataFrames modificados
df_kansas.to_csv(data_kansas, index=False)
df_melbourne.to_csv(data_melbourne, index=False)
df_perth.to_csv(data_perth, index=False)

# print(df_kansas.dtypes)
# print(df_melbourne.dtypes)
# print(df_perth.dtypes)

# full join dos 3 dataframes

df_full = pd.concat([df_kansas, df_melbourne, df_perth], ignore_index=True)
df_full.to_csv("datasetfiles/full_housing.csv", index=False)

#inner join dos 3 dataframes

