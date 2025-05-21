import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load cleaned datasets
benin = pd.read_csv("C:/Users/firao/Desktop/PYTHON PROJECTS/solar-challenge-week1/data/benin_clean.csv")
sierra_leone = pd.read_csv("C:/Users/firao/Desktop/PYTHON PROJECTS/solar-challenge-week1/data/sierraleone_clean.csv")
togo = pd.read_csv("C:/Users/firao/Desktop/PYTHON PROJECTS/solar-challenge-week1/data/togo_clean.csv")

# Create subplots: one row, three columns for GHI, DNI, DHI
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Define metrics to plot graphs
metrics = ['GHI', 'DNI', 'DHI']

# Loop over each metric and plot boxplot
for i, metric in enumerate(metrics):
    # Prepare data for boxplot
    data = [benin[metric], sierra_leone[metric], togo[metric]]

    # Create boxplot
    sns.boxplot(data=data, ax=axes[i])

    # Set fixed tick positions (0, 1, 2) for Benin, Sierra Leone, Togo
    axes[i].set_xticks([0, 1, 2])

    # Set custom tick labels
    axes[i].set_xticklabels(['Benin', 'Sierra Leone', 'Togo'])

    # Add title
    axes[i].set_title(f'{metric} Distribution')

    # Optional: Rotate x-labels for better readability
    axes[i].tick_params(axis='x', rotation=45)

# Adjust layout to prevent overlap
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
    print(f"\n Summary Statistics for {metric}:")
    summary = generate_summary(country_data, metric)
    print(summary)
