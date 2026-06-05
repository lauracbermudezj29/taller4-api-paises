from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

print("Conexión exitosa")

import requests
from pymongo import MongoClient

# Conexión MongoDB
client = MongoClient("mongodb://localhost:27017/")

db = client["taller4_db"]
collection = db["raw_data"]

# API
url = "https://restcountries.com/v3.1/all?fields=name,capital,population,region,subregion,area,flags"
response = requests.get(url)

print("Status:", response.status_code)

if response.status_code == 200:
    data = response.json()

    collection.delete_many({})

    collection.insert_many(data)

    print(f"Se insertaron {len(data)} registros")

else:
    print("Error al consultar la API")
    print(response.text)