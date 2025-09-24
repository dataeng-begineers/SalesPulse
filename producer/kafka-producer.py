from confluent_kafka import Producer
import json
import time
import requests

# Connect to the Kafka service by its name in docker-compose
producer_conf = {'bootstrap.servers': 'kafka:9092'}
producer = Producer(producer_conf)
topic = "supermarket_sales"

print("Starting Kafka producer...")

try:
    while True:
        event = requests.get("http://fastapi_service:8000/latest")
        producer.produce(topic, value=json.dumps(event))
        producer.flush()
        print("Produced event:", event)
        time.sleep(1)

except KeyboardInterrupt:
    print("Producer stopped.")
