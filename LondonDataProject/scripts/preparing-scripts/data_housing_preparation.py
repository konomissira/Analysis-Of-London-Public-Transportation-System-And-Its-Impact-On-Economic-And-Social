import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt

# Read the Excel file with a multi-index header
df = pd.read_excel('../../data/raw/housing-price-index-UK-London.xlsx', dtype={'London_Value': str, 'UK_Value': str})

# Renaming the columns
df.columns = ['Month', 'London_Value', 'London_Annual_Growth', 'UK_Value', 'UK_Annual_Growth']

df['London_Annual_Growth'] = pd.to_numeric(df['London_Annual_Growth'], errors='coerce')
df['UK_Annual_Growth'] = pd.to_numeric(df['UK_Annual_Growth'], errors='coerce')
# Remove the '£' symbol from the UK_Value column
#df['UK_Value'] = df['UK_Value'].str.replace('£', '', regex=False)
# Convert the column to numeric
df['UK_Value'] = pd.to_numeric(df['UK_Value'], errors='coerce')



# Now, fill in the missing values
df['London_Annual_Growth'].fillna(value=df['London_Annual_Growth'].mean(), inplace=True)
df['UK_Value'].fillna(value=df['UK_Value'].mean(), inplace=True)
df['UK_Annual_Growth'].fillna(value=df['UK_Annual_Growth'].mean(), inplace=True)

# Since the first row seems to contain repetitive information, drop it
df = df.drop(0)

# Convert the 'Month' column to a datetime format for better handling in future operations
# Try converting the 'Month' column to datetime format using the format "Month-Year"
df['Month'] = pd.to_datetime(df['Month'], errors='coerce')

# Drop rows where 'Month' is NaT (i.e., not a timestamp)
df = df.dropna(subset=['Month'])

# Reset the index after dropping rows
df = df.reset_index(drop=True)

# Display the cleaned-up head of the dataframe
#print(df.head())

#for debugging code
#msno.matrix(df)
#plt.show()


print(df.head())

df.to_excel('../../data/cleaned/housing-price-index-UK-London_cleaned.xlsx', index=False)