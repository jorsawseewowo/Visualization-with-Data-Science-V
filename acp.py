import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Penguins Data.csv")

plt.scatter(df["Culmen Length (mm)"], df["Body Mass (g)"])
plt.xlabel("Culmen Length (mm)")
plt.ylabel("Body Mass (g)")
plt.title("Scatter Plot: Culmen Length vs Body Mass")
plt.show()

plt.scatter(df["Culmen Depth (mm)"], df["Body Mass (g)"])
plt.xlabel("Culmen Depth (mm)")
plt.ylabel("Body Mass (g)")
plt.title("Scatter Plot: Culmen Depth vs Body Mass")
plt.show()

sns.pairplot(df)
plt.show()

plt.fill_between(df["Culmen Length (mm)"], df["Body Mass (g)"])
plt.xlabel("Culmen Length (mm)")
plt.ylabel("Body Mass (g)")
plt.title("Area Graph: Culmen Length vs Body Mass")
plt.show()