import requests
from bs4 import BeautifulSoup


url = "https://www.epra.go.ke/pump-prices"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
links = soup.find_all("a")

for link in links:
	text = link.get_text(strip=True)
	href = link.get("href")
	
	print(f"Text: {text}")
	print(f"Link: {href}")
	print("_________")

