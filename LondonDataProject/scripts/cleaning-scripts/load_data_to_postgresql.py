import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Load your cleaned data
df = pd.read_csv('../../data/cleaned/cleaned_workforce_jobs.csv')

# Establish a connection to the PostgreSQL database
DATABASE_URL = "postgresql+psycopg2://mahamadoucamara@localhost:5432/londondata"
engine = create_engine(DATABASE_URL)

# Load data into PostgreSQL
df.to_sql('workforce_jobs_by_sector', engine, if_exists='replace', index=False)
