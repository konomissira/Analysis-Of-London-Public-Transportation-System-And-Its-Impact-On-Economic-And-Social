import pandas as pd

# Load the CSV into a pandas DataFrame
df = pd.read_csv('../data/raw/workforce-jobs-by-sector.csv')

# Inspect the first few rows of the dataframe to understand its structure
print(df.head())

# Check for any missing values in the dataframe
print(df.isnull().sum())

# Additional cleaning, transformation, or validation can be done here. 
# For now, we'll assume the data matches the table structure and data types.

# Save the cleaned data to a new CSV file
df.to_csv('../data/raw/cleaned_workforce_jobs.csv', index=False)
