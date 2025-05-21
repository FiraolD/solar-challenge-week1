import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from local address
@st.cache_data
def load_data():
    return {
        'Benin': pd.read_csv("C:/Users/firao/Desktop/PYTHON PROJECTS/solar-challenge-week1/data/benin_clean.csv"),
        'Sierra Leone': pd.read_csv("C:/Users/firao/Desktop/PYTHON PROJECTS/solar-challenge-week1/data/sierraleone_clean.csv"),
        'Togo': pd.read_csv("C:/Users/firao/Desktop/PYTHON PROJECTS/solar-challenge-week1/data/togo_clean.csv")
    }

st.title("🌍 Solar Energy Dashboard")

country = st.selectbox("Select Country", ["Benin", "Sierra Leone", "Togo"])
data = load_data()[country]

st.subheader(f"{country} - GHI Over Time")
st.line_chart(data.set_index('Timestamp')['GHI'])

if st.checkbox("Show Top Regions by Average GHI"):
    summary = {k: v['GHI'].mean() for k, v in load_data().items()}
    summary_df = pd.DataFrame(summary.items(), columns=['Country', 'Avg GHI']).sort_values(by='Avg GHI', ascending=False)
    st.table(summary_df)
