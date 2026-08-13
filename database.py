import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def connect_db():
	connection = psycopg2.connect(
		dbname=os.getenv("DB_NAME"),
		user=os.getenv("DB_USER"),
		password=os.getenv("DB_PASSWORD"),
		host=os.getenv("DB_HOST"),
		port=os.getenv("DB_PORT")
	)

	return connection

def save_fuel_price(fuel):
	connection = connect_db()
	cursor = connection.cursor()

	cursor.execute(
		"""
		INSERT INTO fuel_prices
		(from_date, to_date, town, super, diesel, kerosene)
		VALUES (%s, %s, %s, %s, %s, %s)
		ON CONFLICT (from_date, to_date, town)
		DO NOTHING
		""",

		(
			fuel["from_date"],
			fuel["to_date"],
			fuel["town"],
			fuel["super"],
			fuel["diesel"],
			fuel["kerosene"]
		)
	)
	connection.commit()
	cursor.close()
	connection.close()

def get_fuel_prices():
	connection = connect_db()
	cursor = connection.cursor()

	cursor.execute("""
		SELECT id, from_date, to_date, town,super, diesel, kerosene
		FROM fuel_prices
		ORDER BY id
	""")
	rows = cursor.fetchall()

	cursor.close()
	connection.close()

	return rows

