import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from scipy.stats import zscore

plt.style.use('ggplot')

# Load data
df = pd.read_csv("C:/Users/firao/Desktop/PYTHON PROJECTS/KIAM PROJECTS/solar-challenge-week/data/togo.csv", parse_dates=['Timestamp'])

# Basic info
print("Dataset shape:", df.shape)
print(df.info())
print(df.describe())

# Data cleaning
# Drop Comments (all null)
df = df.drop(columns=['Comments'])

# Handle negative GHI, DNI, DHI (set to 0 as they are physically invalid)
for col in ['GHI', 'DNI', 'DHI']:
    df[col] = df[col].clip(lower=0)
    print(f"Negative {col} values set to 0:", (df[col] < 0).sum())

# Missing values
print("Missing values:\n", df.isnull().sum())

# Outlier detection
z_scores = df[['GHI', 'DNI', 'DHI']].apply(zscore)
outliers = (z_scores.abs() > 3).sum()
print("Outliers (z-score > 3):\n", outliers)

# Time series plot
plt.figure(figsize=(12, 6))
df.set_index('Timestamp')['GHI'].plot()
plt.title('GHI Over Time')
plt.xlabel('Timestamp')
plt.ylabel('GHI (W/m²)')
plt.tight_layout()
plt.show()

# Monthly GHI
df['Month'] = df['Timestamp'].dt.month
monthly_ghi = df.groupby('Month')['GHI'].mean()
plt.figure(figsize=(8, 5))
monthly_ghi.plot(kind='bar')
plt.title('Average GHI by Month')
plt.xlabel('Month')
plt.ylabel('GHI (W/m²)')
plt.tight_layout()
plt.show()

# Cleaning impact
cleaning_effect = df.groupby('Cleaning')[['ModA', 'ModB']].mean()
print("Cleaning impact (mean ModA/ModB):\n", cleaning_effect)

# Correlation matrix
corr = df[['GHI', 'DNI', 'DHI', 'Tamb', 'RH', 'WS']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.tight_layout()
plt.show()

# Wind rose (simplified)
wd_bins = pd.cut(df['WD'], bins=16, right=False)
ws_mean = df.groupby(wd_bins)['WS'].mean()
plt.figure(figsize=(8, 8))
ws_mean.plot(kind='bar')
plt.title('Average Wind Speed by Direction')
plt.xlabel('Wind Direction (degrees)')
plt.ylabel('Wind Speed (m/s)')
plt.tight_layout()
plt.show()

# Temperature analysis
plt.figure(figsize=(10, 6))
df[['Tamb', 'TModA', 'TModB']].plot.hist(alpha=0.5, bins=50)
plt.title('Distribution of Temperatures')
plt.xlabel('Temperature (°C)')
plt.tight_layout()
plt.show()

# Bubble chart: GHI vs. Tamb, sized by WS
fig = px.scatter(df[df['GHI'] > 0].sample(1000), x='Tamb', y='GHI', size='WS', 
color='RH', title='GHI vs. Temperature (Bubble Size: Wind Speed)')
fig.show()

# Save cleaned data
df.to_csv("C:/Users/firao/Desktop/PYTHON PROJECTS/KIAM PROJECTS/solar-challenge-week/data/togo_clean.csv", index=False)
print("Cleaned data saved to data/benin_clean.csv")

