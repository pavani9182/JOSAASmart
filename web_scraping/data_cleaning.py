import pandas as pd

# Finally data stored is cleaned using this code
  
# Load the Excel file
excel_file = "C:/Users/pavan/OneDrive/Desktop/data_final3.xlsx"  # Update this path

# Read the first sheet of the Excel file
data = pd.read_excel(excel_file) 
data['Institute'] = data['Institute'].str.replace(r'\s+', ' ', regex=True).str.strip()
con1=data['Institute'].str.contains('Indian Institute of Technology', na=False)
con3=data['Opening Rank'].str.contains('P', na=False)
con4=data['Closing Rank'].str.contains('P', na=False)
data_clean=data[con1 & ~con3 & ~con4]
data_clean['Opening Rank'] = data_clean['Opening Rank'].astype(float).astype(int)
data_clean['Closing Rank']=data_clean['Closing Rank'].astype(float).astype(int)
data_clean['Gender'] = data_clean['Gender'].fillna('Gender-Neutral')

# Save the data to a CSV file
csv_file = "C:/Users/pavan/OneDrive/Desktop/data_final4.xlsx"  # Update this path
data_clean.to_excel(csv_file, index=False)

print(f"Excel file {excel_file} has been converted to {csv_file}")