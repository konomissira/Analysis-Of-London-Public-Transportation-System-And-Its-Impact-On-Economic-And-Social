import pandas as pd

# Load the excel file into a pandas DataFrame
df = pd.read_excel('../../data/raw/travel.xlsx')
# Drop unnecessary rows
df_travel = df.iloc[7:].reset_index(drop=True)

# Assign column names
df_travel.columns = df.iloc[6]

# Drop any NaN columns (as it seems there's a NaN column from the output)
df_travel = df_travel.dropna(axis=1, how='all')

# Display the cleaned data
print(df_travel.head())


df_travel.to_excel('../../data/cleaned/travel.xlsx', index=False)