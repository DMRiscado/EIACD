import pandas as pd


data_perth = "datasetfiles/perth_housing.csv"
df_perth = pd.read_csv(data_perth)

missing_values = df_perth.isnull().sum()
#print(missing_values)

#Remoção de linhas com valores nulos

#colunas_em_falta = ["car_garage", "year_built "]

#for col in df_perth.columns:
#    if df_perth[col].dtype != 'object':
#        median = df_perth[col].median()
#        df_perth[col].fillna(median, inplace=True)

#df_perth.to_csv('datasetfiles/perth_housing.csv', index=False)

#Remoção de outliers usando a técnica IQR 5/95

#Q1 = df_perth['year_built'].quantile(0.05)
#Q3 = df_perth['year_built'].quantile(0.95)
#IQR = Q3 - Q1
#outliers = df_perth[(df_perth['year_built'] >= Q1 - 1.5 * IQR) & (df_perth['year_built'] <= Q3 + 1.5 * IQR)]
#outliers.to_csv('datasetfiles/perth_housing.csv', index=False)

#Q1 = df_perth['sqft_living'].quantile(0.05)
#Q3 = df_perth['sqft_living'].quantile(0.95)
#IQR = Q3 - Q1
#outliers = df_perth[(df_perth['sqft_living'] >= Q1 - 1.5 * IQR) & (df_perth['sqft_living'] <= Q3 + 1.5 * IQR)]
#outliers.to_csv('datasetfiles/melbourne_housing.csv', index=False)

#Q1 = df_perth['sqft_lot'].quantile(0.05)
#Q3 = df_perth['sqft_lot'].quantile(0.95)
#IQR = Q3 - Q1
#outliers = df_perth[(df_perth['sqft_lot'] >= Q1 - 1.5 * IQR) & (df_perth['sqft_lot'] <= Q3 + 1.5 * IQR)]
#outliers.to_csv('datasetfiles/perth_housing.csv', index=False)

#Q1 = df_perth['bedrooms'].quantile(0.05)
#Q3 = df_perth['bedrooms'].quantile(0.95)
#IQR = Q3 - Q1
#outliers = df_perth[(df_perth['bedrooms'] >= Q1 - 1.5 * IQR) & (df_perth['bedrooms'] <= Q3 + 1.5 * IQR)]
#outliers.to_csv('datasetfiles/perth_housing.csv', index=False)

#Q1 = df_perth['bathrooms'].quantile(0.05)
#Q3 = df_perth['bathrooms'].quantile(0.95)
#IQR = Q3 - Q1
#outliers = df_perth[(df_perth['bathrooms'] >= Q1 - 1.5 * IQR) & (df_perth['bathrooms'] <= Q3 + 1.5 * IQR)]
#outliers.to_csv('datasetfiles/perth_housing.csv', index=False)

#Q1 = df_perth['car_garage'].quantile(0.05)
#Q3 = df_perth['car_garage'].quantile(0.95)
#IQR = Q3 - Q1
#outliers = df_perth[(df_perth['car_garage'] >= Q1 - 1.5 * IQR) & (df_perth['car_garage'] <= Q3 + 1.5 * IQR)]
#outliers.to_csv('datasetfiles/perth_housing.csv', index=False)

#Q1 = df_perth['price'].quantile(0.05)
#Q3 = df_perth['price'].quantile(0.95)
#IQR = Q3 - Q1
#outliers = df_perth[(df_perth['price'] >= Q1 - 1.5 * IQR) & (df_perth['price'] <= Q3 + 1.5 * IQR)]
#outliers.to_csv('datasetfiles/perth_housing.csv', index=False)

#Q1 = df_perth['zipcode'].quantile(0.05)
#Q3 = df_perth['zipcode'].quantile(0.95)
#IQR = Q3 - Q1
#outliers = df_perth[(df_perth['zipcode'] >= Q1 - 1.5 * IQR) & (df_perth['zipcode'] <= Q3 + 1.5 * IQR)]
#outliers.to_csv('datasetfiles/perth_housing.csv', index=False)