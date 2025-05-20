import pandas as pd

def load_data():
    return {
        'Benin': pd.read_csv("C:/Users/firao/Desktop/PYTHON PROJECTS/solar-challenge-week1/data/benin_clean.csv"),
        'Sierra Leone': pd.read_csv("C:/Users/firao/Desktop/PYTHON PROJECTS/solar-challenge-week1/data/sierraleone_clean.csv"),
        'Togo': pd.read_csv("C:/Users/firao/Desktop/PYTHON PROJECTS/solar-challenge-week1/data/togo_clean.csv")
    }
