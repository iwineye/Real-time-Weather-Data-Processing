import requests
from time import sleep
from kafka import KafkaProducer
import json
from config import API_URL, KAFKA_SERVER, KAFKA_TOPIC, RAPID_API_KEY

# Function to fetch weather data from API
def fetch_weather_data():
    url = "https://open-weather13.p.rapidapi.com/city/newdelhi"  
    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": "open-weather13.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    return response.json()

#create kafka producer
producer = KafkaProducer(bootstrap_servers=[KAFKA_SERVER], value_serializer=lambda x: json.dumps(x).encode('utf-8'))


while True:
    response = requests.get(API_URL)
    weather_data = response.json()

    
# Extract temperature information
temperature_info = {
        'temp': weather_data['main']['temp'],
        'feels_like': weather_data['main']['feels_like'],
        'temp_min': weather_data['main']['temp_min'],
        'temp_max': weather_data['main']['temp_max'],
        'humidity': weather_data['main']['humidity']
    }
    
    producer.send(KAFKA_TOPIC, value=weather_data)
    sleep(60)
# Fetches weather data every 60 seconds
