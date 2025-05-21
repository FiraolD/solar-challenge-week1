import pandas as pd

ef load_data():
    return {
        'Benin': pd.read_csv("C:/Users/firao/Desktop/PYTHON PROJECTS/KIAM PROJECTS/solar-challenge-week/data/benin_clean.csv"),
        'Sierra Leone': pd.read_csv("C:/Users/firao/Desktop/PYTHON PROJECTS/KIAM PROJECTS/solar-challenge-week/data/sierraleone_clean.csv"),
        'Togo': pd.read_csv("C:/Users/firao/Desktop/PYTHON PROJECTS/KIAM PROJECTS/solar-challenge-week/data/togo_clean.csv")
    }

