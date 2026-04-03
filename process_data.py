import pandas as pd
import glob
import os

# Define the data directory and output file
data_dir = 'data'
output_file = 'formatted_data.csv'

# Find all CSV files in the data directory
csv_files = glob.glob(os.path.join(data_dir, 'daily_sales_data_*.csv'))

# List to store processed DataFrames
dataframes = []

for file in csv_files:
    # Read the CSV file
    df = pd.read_csv(file)
    
    # Filter for "pink morsel" (case-insensitive)
    df = df[df['product'].str.lower() == 'pink morsel']
    
    # Clean the price column (remove "$" and convert to float)
    df['price'] = df['price'].str.replace('$', '', regex=False).astype(float)
    
    # Calculate sales
    df['sales'] = df['price'] * df['quantity']
    
    # Keep only Sales, Date, and Region
    df = df[['sales', 'date', 'region']]
    
    # Rename columns to match the requirement (Capitalized)
    # The requirement says "Sales, Date, Region" in the final visualization,
    # but also says "Your output file should contain three fields: Sales, Date, Region".
    # I'll use capitalized column names for the output.
    df.columns = ['Sales', 'Date', 'Region']
    
    dataframes.append(df)

# Concatenate all DataFrames
final_df = pd.concat(dataframes, ignore_index=True)

# Save to CSV
final_df.to_csv(output_file, index=False)

print(f"Processed data saved to {output_file}")
