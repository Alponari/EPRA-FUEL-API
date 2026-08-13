from flask import Flask
from database import get_fuel_prices

app = Flask(__name__)

@app.route("/")
def home():
	return {"message": "EPRA API is running"}

@app.route("/fuel-prices")
def fuel_price():
	rows = get_fuel_prices()

	prices = []

	for row in rows:
		fuel = {
			"id": row[0],
			"from_date": str(row[1]),
			"to_date": str(row[2]),
			"town": row[3],
			"super": float(row[4]),
			"diesel": float(row[5]),
			"kerosene": float(row[6])
		}

		prices.append(fuel)

	return prices


if __name__ == "__main__":
	app.run(debug=True)
