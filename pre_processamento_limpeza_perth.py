import pandas as pd


data_perth = "datasetfiles/perth_housing.csv"
df_perth = pd.read_csv(data_perth)

missing_values = df_perth.isnull().sum()
print(missing_values)

#colunas_em_falta = ["car_garage", "year_built "]

#for col in df_perth.columns:
    #if df_perth[col].dtype != 'object':
        #median = df_perth[col].median()
        #df_perth[col].fillna(median, inplace=True)

#df_perth.to_csv('datasetfiles/perth_housing.csv', index=False)