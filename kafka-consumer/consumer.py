from kafka import KafkaConsumer
import snowflake.connector
from config import KAFKA_SERVER, KAFKA_TOPIC, SNOWFLAKE_CONFIG

# Connect to Snowflake
conn = snowflake.connector.connect(**SNOWFLAKE_CONFIG)

# Create Kafka consumer
consumer = KafkaConsumer(KAFKA_TOPIC,
                         bootstrap_servers=[KAFKA_SERVER],
                         auto_offset_reset='earliest',
                         enable_auto_commit=True,
                         group_id='weather_group')

# Consume messages from Kafka topic and insert temperature data into Snowflake
for message in consumer:
    temperature_info = json.loads(message.value)
    temp = temperature_info['temp']
    feels_like = temperature_info['feels_like']
    temp_min = temperature_info['temp_min']
    temp_max = temperature_info['temp_max']
    humidity = temperature_info['humidity']
    
    cursor = conn.cursor()
    cursor.execute("INSERT INTO temperature_data (temp, feels_like, temp_min, temp_max, humidity) VALUES (%s, %s, %s, %s, %s)", (temp, feels_like, temp_min, temp_max, humidity))
    cursor.close()
    conn.commit()
