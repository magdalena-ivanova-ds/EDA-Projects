import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL.ImageColor import colormap

#Data Cleaning & Preprocessing
pd.set_option('display.max_columns', None)
covid19_df = pd.read_csv("country_wise_latest.csv")
#print(covid19_df.isna().sum())  #no NA values
#print(covid19_df.info())
#print(covid19_df.describe())
covid19_df["Death Rate"] = (covid19_df["Deaths"] / covid19_df["Confirmed"] * 100).round(2)
covid19_df["Recovery Rate"] = (covid19_df["Recovered"] / covid19_df["Confirmed"] * 100).round(2)
covid19_df.drop(columns=["Deaths / 100 Recovered"], inplace=True)
#print(covid19_df.head())

#Exploratory Data Analysis (EDA) & Visualizations
covid19_df_top10 = covid19_df.sort_values(by=["Confirmed", "Deaths", "Recovered"], ascending=False)
covid19_df_top10 = covid19_df_top10.reset_index(drop=True).iloc[:10,:]
print(covid19_df.head())

# Melt the data for Seaborn
melted_df = covid19_df_top10.melt(id_vars="Country/Region", value_vars=["Confirmed", "Deaths", "Recovered"],
                            var_name="Category", value_name="Count")
#print(melted_df)

##Top 10 most affected countries – Bar chart of total cases, deaths, and recoveries.
sns.set_style("darkgrid")
sns.set_palette("flare")

plt.figure(figsize=(12,6), dpi=300)
ax = sns.barplot(x="Country/Region", y="Count", data=melted_df, hue="Category")
plt.ticklabel_format(axis='y', style='plain')
plt.gca().set_yticks(plt.gca().get_yticks())  # Keeps default ticks
plt.gca().set_yticklabels([f"{int(y/1e6)} Mil" for y in plt.gca().get_yticks()])  # Convert to millions
plt.xlabel("Country/Region", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.title("Top 10 most affected countries by COVID-19", fontsize=14)
plt.legend(title="Category")
plt.show()

##Recovery vs. Death Rate – Scatter plot comparing recovery and death rates across countries.
plt.figure(figsize=(8,5), dpi=300)
sns.scatterplot(data=covid19_df, y="Death Rate", x="Recovery Rate")
plt.xlabel("Recovery Rate", fontsize=12)
plt.ylabel("Death Rate", fontsize=12)
plt.title("Recovery vs. Death Rate", fontsize=14)
plt.show()

#WHO Region Analysis