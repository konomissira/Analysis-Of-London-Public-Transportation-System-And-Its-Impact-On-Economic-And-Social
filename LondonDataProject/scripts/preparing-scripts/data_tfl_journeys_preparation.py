import pandas as pd

df = pd.read_csv('../../data/raw/tfl-journeys-type.csv')
#print(df.head())
print(df.isnull().sum())
