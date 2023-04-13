#!/usr/bin/env python
# coding: utf-8

# # Zomato dataset Exploratory data analysis

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


df = pd.read_csv(r'C:\Users\hp\Downloads\Zomatodataset\zomato.csv', encoding='latin-1')
df.head()


df.columns


df.info()
df.describe()


# depends on only integer variables no categorical variable

# # Things we'll do in Data Analysis
# 1. Missing values
# 2. Explore about the Numerical variables
# 3. Explore about Categorical variables
# 4. Finding relationship b/w features

# # 1. Missing values

df.isnull().sum()

# --> Let's try with List comprehension


[features for features in df.columns if df[features].isnull().sum()>0]


# --> Let's try with heatmap

df.shape


sns.heatmap(df.isnull(), cmap='viridis')

plt.figure(figsize=(14,12))
sns.heatmap(df.isna().sum().to_frame(), annot=True, cmap='vlag',fmt='d')


# # All the above methods can be used to find the missing values

get_ipython().run_line_magic('pip', 'install openpyxl')


# ---> We use openpyxl to read 'xlsx' excel file in jupyter notebook

df_country= pd.read_excel(r'C:\Users\hp\Downloads\Zomatodataset\Country-code.xlsx')
df_country.head()

df.columns


# --> Both the dataset has 'Country code' in common so let's merge the two

final_df = pd.merge(df, df_country, on='Country Code', how='left')
final_df.shape

final_df.columns


country_names = final_df.Country.value_counts().index

country_val = final_df.Country.value_counts().values

#pie chart for top 3 countries
plt.pie(country_val[:3], labels=country_names[:3], autopct='%1.2f%%')


final_df.columns


ratings = final_df.groupby(['Aggregate rating', 'Rating color', 'Rating text']).size().reset_index().rename(columns={0:'Rating Count'})


ratings.head()


import matplotlib
matplotlib.rcParams['figure.figsize'] = (12,6)
sns.barplot(x='Aggregate rating', y='Rating Count', data=ratings)


# --> We can also map the colors given in dataframe


sns.barplot(x='Aggregate rating', y='Rating Count', data=ratings, hue='Rating color', palette=['lightgrey','red','orange','yellow','lightgreen','green'])


# # country names that has given 0 rating

final_df.groupby(['Aggregate rating', 'Country']).size().reset_index().head()

# # Finding which currency is used by which currency?

final_df.groupby(['Country', 'Currency']).size().reset_index()


# # Which country has online delivery

final_df.columns


final_df[final_df['Has Online delivery'] == "Yes"].Country.values


