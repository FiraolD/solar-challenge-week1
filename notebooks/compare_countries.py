import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load cleaned datasets
benin = pd.read_csv("C:/Users/firao/Desktop/PYTHON PROJECTS/KIAM PROJECTS/solar-challenge-week/data/benin_clean.csv")
sierra_leone = pd.read_csv("C:/Users/firao/Desktop/PYTHON PROJECTS/KIAM PROJECTS/solar-challenge-week/data/sierraleone_clean.csv")
togo = pd.read_csv("C:/Users/firao/Desktop/PYTHON PROJECTS/KIAM PROJECTS/solar-challenge-week/data/togo_clean.csv")

# Combine datasets with a 'Country' column for easy plotting
benin["Country"] = "Benin"
sierra_leone["Country"] = "Sierra Leone"
togo["Country"] = "Togo"

# Concatenate into a single DataFrame
df_all = pd.concat([benin, sierra_leone, togo], ignore_index=True)

# Define metrics to plot
metrics = ['GHI', 'DNI', 'DHI']

# Plot each metric separately
for metric in metrics:
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df_all, x="Country", y=metric)
    plt.title(f'{metric} Distribution by Country')
    plt.xlabel("Country")
    plt.ylabel(f'{metric} (W/m²)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Generate summary statistics for each country and metric
def generate_summary(df_dict, metric):
    return pd.DataFrame({
        'Mean': {country: df[metric].mean() for country, df in df_dict.items()},
        'Median': {country: df[metric].median() for country, df in df_dict.items()},
        'Std Dev': {country: df[metric].std() for country, df in df_dict.items()}
    })

# Dictionary of country dataframes for easy looping
country_data = {
    'Benin': benin,
    'Sierra Leone': sierra_leone,
    'Togo': togo
}

# Print summaries for all metrics
for metric in metrics:
    print(f"\nSummary Statistics for {metric}:")
    summary = generate_summary(country_data, metric)
    print(summary)
