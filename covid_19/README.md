# COVID-19 Data Analysis & Visualization

## Overview
This project analyzes global COVID-19 data, focusing on key metrics such as confirmed cases, deaths, recoveries, and weekly growth rates. The goal is to extract meaningful insights and visualize trends using Python libraries like Pandas, Seaborn, and Matplotlib.

## Dataset
The dataset used is 
[country_wise_latest.csv](https://github.com/magdalena-ivanova-ds/EDA-Projects/blob/main/covid_19/country_wise_latest.csv), containing country-level COVID-19 statistics such as:

- Confirmed cases
- Deaths
- Recoveries
- Weekly percentage increase
- Regional classification

## Key Features
- Data Cleaning & Preprocessing: Handling missing values, renaming columns, and creating new metrics like Death Rate and Recovery Rate.
- Exploratory Data Analysis (EDA): Understanding the dataset through descriptive statistics.
- Visualizations:
     - Bar chart of top 10 most affected countries
     - Scatter plot comparing recovery and death rates
     - Pie chart showing confirmed cases per region
     - Histogram of weekly case increases
     - Correlation heatmap of selected metrics
     - Line plot showing COVID-19 trends across regions

## Requirements
To run this analysis, install the required Python libraries. Use the package manager [pip](https://pip.pypa.io/en/stable/).

```bash
pip install pandas numpy matplotlib seaborn
```

## Running the Project
Simply run the Jupyter Notebook containing the code to generate visualizations and insights.

## Author
Magdalena Ivanova

## License
This project is open-source and available under the MIT License.