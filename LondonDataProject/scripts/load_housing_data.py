import pandas as pd
from sqlalchemy import create_engine

# Database connection details
DATABASE_URL = 'postgresql://mahamadoucamara@localhost:5432/londondata'

# Connect to the database
engine = create_engine(DATABASE_URL)

# Load cleaned data into a dataframe
df = pd.read_excel('../data/cleaned/housing-price-index-UK-London_cleaned.xlsx')

# Load dataframe into the database
df.to_sql('housing_price_index', engine, if_exists='replace', index=False)
