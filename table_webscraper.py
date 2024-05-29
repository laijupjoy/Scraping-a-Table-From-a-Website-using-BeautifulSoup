import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://ticker.finology.in/"
r = requests.get(url)
print(r.status_code)

soup = BeautifulSoup(r.text,"lxml")

table = soup.find("table",class_ = "table table-sm table-hover screenertable")

headers = soup.find_all("th")      #table header

titles = []
for i in headers:
    title = i.text
    titles.append(title)

print(titles)  
# output is ['Company', 'PriceRs.', 'Day HighRs.', 'Company', 'PriceRs.', 'Day LowRs.', 'Company', 'priceRs.', 'Change%', 'Company', 'priceRs.', 'Change%']
# we required only first 3 columns, so filter it in next step

titles_modified = titles[:3]

print(titles_modified)

df = pd.DataFrame(columns=titles_modified)
print(df)

rows = table.find_all("tr")      #table rows

# print(rows)

for i in rows[1:]:
    # print(i.text)
    data = i.find_all("td")
    # print(data)
    row = [td.text.strip() for td in data]
    # print(row)
    l = len(df)
    df.loc[l] = row

print(df)

df.to_csv("product_table.csv")



