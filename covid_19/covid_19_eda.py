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
covid19_df["Active Case Rate"] = (covid19_df["Active"] / covid19_df["Confirmed"] * 100).round(2)
covid19_df.drop(columns=["Deaths / 100 Recovered"], inplace=True)
print(covid19_df.head())

#Exploratory Data Analysis (EDA) & Visualizations
