import requests
from bs4 import BeautifulSoup

url = "https://www.epra.go.ke/pump-prices"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table")

if table:
    rows = table.find_all("tr")
    headers = [th.get_text(strip=True) for th in rows[0].find_all(["th", "td"])]
    print(headers)


    for row in rows[1:]:
        columns = [td.get_text(strip=True) for td in row.find_all("td")]

        if columns:
            print(columns)
else:
    print("No table found.")
