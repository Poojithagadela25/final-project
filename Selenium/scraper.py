from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()

url = "https://www.scrapethissite.com/pages/forms/"
driver.get(url)

time.sleep(3)

rows = driver.find_elements(By.CSS_SELECTOR, 'table tbody tr')

data = []

for row in rows:
    cols = row.find_elements(By.TAG_NAME, 'td')
    cols_text = [col.text.strip() for col in cols]
    data.append(cols_text)

columns = ["Team Name", "Year", "Wins", "Losses", "OT Losses", "Win %", "Goals For (GF)", "Goals Against (GA)", "+ / -"]

df = pd.DataFrame(data, columns=columns)
df.to_csv('scraped_data.csv', index=False)

driver.quit()

print("Data saved to 'scraped_data.csv'")
