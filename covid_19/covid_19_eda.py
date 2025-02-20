import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Data Cleaning & Preprocessing
pd.set_option('display.max_columns', None)
covid19_df = pd.read_csv("country_wise_latest.csv")
#print(covid19_df.isna().sum())  #no NA values
#print(covid19_df.info())
#print(covid19_df.describe())
covid19_df["Death Rate"] = (covid19_df["Deaths"] / covid19_df["Confirmed"] * 100).round(2)
covid19_df["Recovery Rate"] = (covid19_df["Recovered"] / covid19_df["Confirmed"] * 100).round(2)
covid19_df.drop(columns=["Deaths / 100 Recovered"], inplace=True)
covid19_df.rename(columns={"Country/Region": "Country", "WHO Region":"Region"}, inplace=True)
#print(covid19_df.head())

#Exploratory Data Analysis (EDA) & Visualizations
covid19_df_top10 = covid19_df.sort_values(by=["Confirmed", "Deaths", "Recovered"], ascending=False)
covid19_df_top10 = covid19_df_top10.reset_index(drop=True).iloc[:10,:]
print(covid19_df.head())

# Melt the data for Seaborn
melted_df = covid19_df_top10.melt(id_vars="Country", value_vars=["Confirmed", "Deaths", "Recovered"],
                            var_name="Category", value_name="Count")
#print(melted_df)

##Top 10 most affected countries – Bar chart of total cases, deaths, and recoveries.
sns.set_style("darkgrid")
sns.set_palette("flare")

plt.figure(figsize=(12,6), dpi=300)
ax = sns.barplot(x="Country", y="Count", data=melted_df, hue="Category")
plt.xlabel("Country", fontsize=12)
plt.ylabel("Count (in millions)", fontsize=12)
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

#Region Analysis
confirmed_cases_per_region = covid19_df.groupby("Region")["Confirmed"].sum()
pie_values = confirmed_cases_per_region.values.tolist()
pie_labels = confirmed_cases_per_region.index.values.tolist()
explode = (0.1,0.1,0,0,0,0.2)
sns.set_palette("deep")

plt.figure(figsize=(8,4), dpi=300)
plt.pie(pie_values, labels=pie_labels, autopct="%1.1f %%", pctdistance=0.8, startangle=140,
        explode=explode, shadow=True, textprops={'fontsize': 12})
plt.title("Confirmed cases per region", fontsize=14, bbox={'facecolor':'0.8', 'pad':5,'edgecolor': 'black', 'linewidth': 1})
plt.show()

#1 week % increase
plt.figure(figsize=(8,4), dpi=300)
sns.histplot(covid19_df["1 week % increase"], bins=10, kde=True, stat="count")
plt.xlim(0,60)
plt.xlabel("Increase in cases per week (in %)")
plt.title("")
plt.show()

##Correlation
df_no_countries = covid19_df.drop(columns=["Country", "Region"])
plt.figure(figsize=(8,4), dpi=300)
sns.heatmap(df_no_countries.corr(), annot=True, vmin=0, vmax=1, cmap='YlGnBu')
plt.show()

##Trend analysis
grouped_region_df = covid19_df.groupby("Region", as_index=False)[["Confirmed", "Deaths", "Recovered"]].sum().sort_values(by="Confirmed")
plt.figure(figsize=(12, 6))
sns.lineplot(data=grouped_region_df, x="Region", y="Confirmed", marker="o", label="Total Cases")
sns.lineplot(data=grouped_region_df, x="Region", y="Deaths", marker="o", label="Total Deaths", color="red")
sns.lineplot(data=grouped_region_df, x="Region", y="Recovered", marker="o", label="Total Recovered", color="green")

plt.ylabel("Count (in millions)")
plt.title("COVID-19 Case Comparison Across Regions")
plt.legend()
plt.show()