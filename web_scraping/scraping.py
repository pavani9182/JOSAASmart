from bs4 import BeautifulSoup
import lxml
import pandas as pd

with open("C:/Users/pavan/Downloads/juice.html") as file:   #save html file of josaa table by selecting appropriate options & give the path of file here
    html_content=file.read()

soup=BeautifulSoup(html_content,'lxml')
table = soup.find('table')

data = []

# Get table headers
headers = [header.text.strip() for header in table.find_all('th')]

# Get table rows
rows = table.find_all('tr')

# Iterate through the rows and extract the cell data
for row in rows:
    cells = row.find_all(['td', 'th'])
    row_data = [cell.text.strip() for cell in cells]
    data.append(row_data)

# Optionally, you can convert this data to a more convenient format, like a list of dictionaries
table_data = [dict(zip(headers, row)) for row in data[1:]]  # Skipping the header row for data



df1=pd.DataFrame(table_data)
df1["year"]=2023
df1["round"]=6

file_path="C:/Users/pavan/OneDrive/Desktop/josaa_data/2023-6.xlsx"  #give path of a file where you would like to save the scraped data
df1.to_excel(file_path,index=False)