# Use a lightweight Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy producer code into the container
COPY kafka-producer.py .

# Install required Python packages
RUN pip install --no-cache-dir kafka-python requests

# Command to run the producer
CMD ["python", "kafka-producer.py"]


