import pandas as pd


data_kansas = "datasetfiles/kc_final.csv"
data_melbourne = "datasetfiles/melbourne_housing.csv"
data_perth = "datasetfiles/perth_housing.csv"



df = pd.read_csv(data_kansas)
print(df.head())
