import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

HouseDF = pd.read_csv('USA_Housing.csv')

corr = HouseDF.select_dtypes(include="number").corr()

HouseDF.head()

HouseDF.info()

HouseDF.columns

sns.pairplot(HouseDF)
plt.figure(figsize=(10,8))

sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()