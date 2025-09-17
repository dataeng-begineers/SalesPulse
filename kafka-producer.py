from confluent_kafka import Producer
from feature.datagenerator import generate_sale_event
import json
import time

producer_conf = {'bootstrap.servers': 'localhost:9092'}
producer = Producer(producer_conf)
topic = "supermarket_sales"

print("Starting Kafka producer...")

try:
    while True:
        event = generate_sale_event()
        producer.produce(topic, value=json.dumps(event))
        producer.flush()
        print("Produced event:", event)
        time.sleep(1)

except KeyboardInterrupt:
    print("Producer stopped.")
