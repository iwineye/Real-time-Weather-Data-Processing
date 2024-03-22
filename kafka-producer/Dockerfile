# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the Python scripts and configuration files into the container
COPY kafka-producer/ /usr/src/app/kafka-producer/
COPY config.py /usr/src/app/
COPY requirements.txt /usr/src/app/

# Install any dependencies required by the Python scripts
RUN pip install --no-cache-dir -r requirements.txt

# Define the command to run your Python script
CMD ["python", "./kafka-producer/producer.py"]
