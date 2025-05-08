import pandas as pd

def load_data():
    admission_data = pd.read_csv('data/HDHI Admission data.csv')
    mortality_data = pd.read_csv('data/HDHI Mortality Data.csv')
    pollution_data = pd.read_csv('data/HDHI Pollution Data.csv')
    return admission_data, mortality_data, pollution_data

def clean_data(df):
    # Exemplo de limpeza
    df.fillna(df.mean(), inplace=True)
    return df
