import requests

url = "https://www.epra.go.ke/pump-prices"

response = requests.get(url)

with open("epra_fuel_prices.pdf", "wb") as file:
	file.write(response.content)

print("Download successful")


