import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Step 1: Read the Excel file
file_path = "../../data/cleaned/travel.xlsx"
df = pd.read_excel(file_path, engine='openpyxl', skiprows=6)

# Step 2: Process the data
df.columns = ["Period", "London_Underground", "Bus", "Total", "London_Underground_Avg", "Bus_Avg", "Total_Avg"]

# Drop the 'Total' and 'Total_Avg' columns
df.drop(["Total", "Total_Avg"], axis=1, inplace=True)

# Convert 'Period' to DATE format
def convert_period_to_date(period_str):
    year, month = period_str.split('-')
    start_year = year.split('/')[0]
    # Assuming the split is monthly
    return f"{start_year}-{month}-01"


# Split dataframe into two: Journeys and Moving Average
travel_jouneys = df[["Period", "London_Underground", "Bus"]]
travel_moving_avg = df[["Period", "London_Underground_Avg", "Bus_Avg"]]

# Step 3: Set up the PostgreSQL connection
DATABASE_URL = "postgresql://mahamadoucamara@localhost:5432/londondata"
engine = create_engine(DATABASE_URL)

# Step 4: Create tables if they don't exist and Insert data
travel_jouneys.to_sql('travel_journeys', engine, if_exists='replace', index=False, method='multi')
travel_moving_avg.to_sql('travel_moving_avg', engine, if_exists='replace', index=False, method='multi')

print("Data successfully loaded into PostgreSQL!")
