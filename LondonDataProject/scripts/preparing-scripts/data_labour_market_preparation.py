import pandas as pd

# Load the Excel file into a pandas DataFrame
# Load the Excel file while skipping the first few rows
df_labour_market = pd.read_excel('../../data/raw/labour-market.xlsx', skiprows=5)

# Drop the first row which seems like a sub-header
df_labour_market = df_labour_market.drop(0)

# Rename columns for clarity
df_labour_market.columns = ['Quarter', 'London_Unemployment', 'UK_Unemployment', 'Unused']

# Drop the 'Unused' column as it contains NaN values
df_labour_market = df_labour_market.drop(columns=['Unused'])

# Reset the index for good measure
df_labour_market.reset_index(drop=True, inplace=True)

df_labour_market.to_excel('../../data/cleaned/labour-market.xlsx', index=False)

# Display the cleaned data
print(df_labour_market.head())

