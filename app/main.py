import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from local address
@st.cache_data
def load_data():
    benin = pd.read_csv("C:/Users/firao/Desktop/PYTHON PROJECTS/KIAM PROJECTS/solar-challenge-week/data/benin_clean.csv")
    sierra_leone = pd.read_csv("C:/Users/firao/Desktop/PYTHON PROJECTS/KIAM PROJECTS/solar-challenge-week/data/sierraleone_clean.csv")
    togo = pd.read_csv("C:/Users/firao/Desktop/PYTHON PROJECTS/KIAM PROJECTS/solar-challenge-week/data/togo_clean.csv")

    benin["Country"] = "Benin"
    sierra_leone["Country"] = "Sierra Leone"
    togo["Country"] = "Togo"

    combined = pd.concat([benin, sierra_leone, togo], ignore_index=True)
    return {
        'Benin': benin,
        'Sierra Leone': sierra_leone,
        'Togo': togo,
        'All': combined
    }

def plot_boxplot(data, metric):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(data=data, x="Country", y=metric, ax=ax)
    ax.set_title(f'{metric} Distribution by Country')
    ax.set_xlabel("Country")
    ax.set_ylabel(f"{metric} (W/m²)")
    plt.xticks(rotation=45)
    st.pyplot(fig)

def generate_summary(df_dict, metric):
    return pd.DataFrame({
        'Mean': {country: df[metric].mean() for country, df in df_dict.items() if country != 'All'},
        'Median': {country: df[metric].median() for country, df in df_dict.items() if country != 'All'},
        'Std Dev': {country: df[metric].std() for country, df in df_dict.items() if country != 'All'}
    })

# STREAMLIT UI 
st.title("🌍 Solar Energy Dashboard")
data_dict = load_data()

# Country-Specific GHI Time Series
country = st.selectbox("Select Country", ["Benin", "Sierra Leone", "Togo"])
data = data_dict[country]

st.subheader(f"{country} - GHI Over Time")
st.line_chart(data.set_index('Timestamp')['GHI'])

if st.checkbox("Show Top Regions by Average GHI"):
    summary = {k: v['GHI'].mean() for k, v in data_dict.items() if k != 'All'}
    summary_df = pd.DataFrame(summary.items(), columns=['Country', 'Avg GHI']).sort_values(by='Avg GHI', ascending=False)
    st.table(summary_df)

# Metric Distribution Comparison
st.subheader("📊 Compare Solar Irradiance Metrics")
selected_metric = st.selectbox("Select Irradiance Metric", ['GHI', 'DNI', 'DHI'])
plot_boxplot(data_dict['All'], selected_metric)

# Show Summary Table
st.subheader(f"📈 Summary Statistics for {selected_metric}")
summary_table = generate_summary(data_dict, selected_metric)
st.dataframe(summary_table)

# Generate automated observations and recommendations
st.subheader("📊 Observations & 🔧 Recommendations")

# Calculate average GHI for ranking
summary_ghi = {k: v['GHI'].mean() for k, v in data_dict.items()}
ranked = sorted(summary_ghi.items(), key=lambda x: x[1], reverse=True)
top_country = ranked[0][0]
bottom_country = ranked[-1][0]

# Observations
st.markdown("### Key Observations:")
st.markdown(f"- 🌞 **{top_country}** has the highest average Global Horizontal Irradiance (GHI): **{ranked[0][1]:.2f} W/m²**")
st.markdown(f"- ☁️ **{bottom_country}** has the lowest average GHI: **{ranked[-1][1]:.2f} W/m²**")
st.markdown(f"- 📉 {country} shows a **standard deviation of {data['GHI'].std():.2f}**, indicating {'high' if data['GHI'].std() > 100 else 'moderate to low'} variability in solar radiation.")

# Recommendations
st.markdown("### Strategic Recommendations:")
if top_country == country:
    st.success(f"✅ Consider prioritizing solar installations in **{country}** — it shows the best solar potential based on GHI.")
else:
    st.info(f"📌 While **{country}** is not the top-ranked in GHI, further investigation into seasonal trends or combining solar with storage could enhance feasibility.")

if data['GHI'].std() > 100:
    st.warning("⚠️ High variability in GHI suggests a need for **solar energy storage** or **hybrid systems** to ensure consistent energy supply.")
else:
    st.success("✅ Stable GHI levels in this region support **efficient solar panel performance with minimal intermittency**.")




