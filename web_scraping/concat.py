import pandas as pd
import os

#this helps to concat multiple files by iterating

# Define the path to the directory containing the Excel files
directory_path = "C:/Users/pavan/Downloads/all_data"

# Initialize an empty list to hold the DataFrames
dataframes = []

# Loop through the files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".xlsx"):
        # Read each Excel file and append the DataFrame to the list
        file_path = os.path.join(directory_path, filename)
        df = pd.read_excel(file_path)
        dataframes.append(df)

# Concatenate all DataFrames in the list into a single DataFrame
combined_df = pd.concat(dataframes, ignore_index=True)

# Save the combined DataFrame to a new Excel file
output_file_path = "C:/Users/pavan/OneDrive/Desktop/2016-2023_data.xlsx"
combined_df.to_excel(output_file_path, index=False)

print("Excel files concatenated and saved successfully.")
