import requests
from datetime import datetime
from bs4 import BeautifulSoup
from database import save_fuel_price

url = "https://www.epra.go.ke/pump-prices"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table")

fuel_prices = []

if table:
    rows = table.find_all("tr")
    headers = [th.get_text(strip=True) for th in rows[0].find_all(["th", "td"])]
    print(headers)


    for row in rows[1:]:
        columns = [td.get_text(strip=True) for td in row.find_all("td")]

        if columns:
            fuel = {
       		"from_date" : datetime.strptime(columns[0],
		"%d-%m-%Y").date(),
        	"to_date" : datetime.strptime(columns[1],
		"%d-%m-%Y").date(),
        	"town" : columns[2],
        	"super" : float(columns[3]),
        	"diesel" :float(columns[4]),
        	"kerosene" : float(columns[5])
            }

            fuel_prices.append(fuel)
            save_fuel_price(fuel)
        print(fuel_prices)


else:
    print("No table found.")




