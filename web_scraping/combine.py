import pandas as pd
import os

#this helps to combine different dataframes saved in two different files, in this way we can concat all data into single dataframe


# Load the first sheet into a DataFrame
df1 = pd.read_excel("C:/Users/pavan/OneDrive/Desktop/josaa_data/2016/2016-1.xlsx")

# Load the second sheet into another DataFrame
df2 = pd.read_excel("C:/Users/pavan/OneDrive/Desktop/josaa_data/2017/2017-1.xlsx")

# Concatenate the DataFrames, ignoring the index to avoid duplicating index labels
combined_df = pd.concat([df1, df2], ignore_index=True)

# Write the combined DataFrame to a new Excel file
combined_df.to_excel("C:/Users/pavan/Downloads/new2016/2016-2017.xlsx", index=False)
