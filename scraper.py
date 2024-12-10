import requests
from bs4 import BeautifulSoup
import pandas as pd
from fake_useragent import UserAgent

# Send request to the page
url = "https://www.scrapethissite.com/pages/forms/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Create a fake user agent
ua = UserAgent()

# Find the table in the page
table = soup.find('table')
rows = table.find_all('tr')

# Initialize a list to store row data
data = []

# Loop through all rows, excluding the header
for row in rows[1:]:
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    data.append(cols)

# Define column names
columns = ["Team Name", "Year", "Wins", "Losses", "OT Losses", "Win %", 
           "Goals For (GF)", "Goals Against (GA)", "+ / -"]

# Create a DataFrame
df = pd.DataFrame(data, columns=columns)

# Save the data to a CSV file
df.to_csv('scraped_data.csv', index=False)
print("Data saved to 'scraped_data.csv'")
