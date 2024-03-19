import pandas as pd

data_kansas = "datasetfiles/kansas_housing.csv"
data_melbourne = "datasetfiles/melbourne_housing.csv"
data_perth = "datasetfiles/perth_housing.csv"

df_kansas = pd.read_csv(data_kansas)
df_melbourne = pd.read_csv(data_melbourne)
df_perth = pd.read_csv(data_perth)


df_full = pd.concat([df_kansas, df_melbourne, df_perth], ignore_index=True)

df_full.to_csv('datasetfiles/housingsfull.csv', index=False)


