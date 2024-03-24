import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_delhi = "datasetfiles/delhi_housing.csv"

df_delhi = pd.read_csv(data_delhi)

media_preco = df_delhi['price'].mean()
print(f"A média dos preços em Delhi: {media_preco}")

