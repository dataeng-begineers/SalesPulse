import requests
from kafka import KafkaProducer
import json
import time

# Kafka setup
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',  # Use service name from docker-compose
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    try:
        # Fetch latest data from FastAPI service
        response = requests.get("http://fastapi-service:8000/latest")
        data = response.json()
        
        # Send each record to Kafka
        for record in data:
            producer.send('sales_topic', record)
            print(f"Sent: {record}")

        time.sleep(1)  # Fetch data every second

    except Exception as e:
        print(f"Error fetching/sending data: {e}")
        time.sleep(5)


