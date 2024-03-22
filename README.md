# Real-time-Weather-Data-Processing

Real-time weather data processing is crucial for various applications ranging from agriculture to transportation. This project provides a scalable solution to fetch weather data based on location using RapidAPI, process it in real-time using Kafka, store it in Snowflake for analytics, and perform SQL queries to extract temperature details.

## Architecture Overview

The architecture consists of the following components:

* RapidAPI: Provides weather data based on location.
* Docker: Containerizes the application components for easy deployment.
* Snowflake: Cloud-based data warehousing solution for storing and analyzing data.
* Kafka: Distributed streaming platform for handling real-time data streams.
* SQL: Query language for extracting temperature details and performing analytics.

## Components
### RapidAPI
RapidAPI provides access to real-time weather data. This project utilizes RapidAPI to fetch weather information based on the specified location.

### Docker
Docker is used for containerization, allowing the application components to be packaged into containers for easy deployment and scalability.

### Snowflake
Snowflake is a cloud-based data warehousing platform that provides scalable storage and analytics capabilities. Weather data processed in real-time is stored in Snowflake for further analysis.

### Kafka
Kafka is a distributed streaming platform that enables the handling of real-time data streams. In this project, Kafka is used to ingest and process real-time weather data streams.

### SQL
SQL (Structured Query Language) is utilized for querying and manipulating data stored in Snowflake. It is used to extract temperature details and perform various analytics tasks on the weather data.

## Setup
* Clone the repository: git clone
* Install Docker and Docker Compose if not already installed.
* Set up Snowflake account and obtain necessary credentials.
* Configure RapidAPI access by obtaining an API key.
* Update the configuration files with appropriate credentials and configurations.
* Run automation.py to get automated weaather report of the day upto that point.

## Usage
* Build and run the Docker containers.
* Configure Kafka topics for weather data streams by changing the prefered location name(ideally state or country)
* Ingest weather data from RapidAPI into Kafka topics.
* Process the data in real-time using Kafka consumers.
* Store processed data in Snowflake for analytics.
* Perform SQL queries to extract temperature details and analyze weather data.

## Contributing
Contributions to improve the project are welcome! Please fork the repository, make changes, and submit a pull request.
* You can parse more data from the API response and get other weather parameters as per requirement.
* You can perform more advanced calculations on historical data by changing the api.

Feel free to expand on each component's setup and usage instructions as needed. This documentation provides a high-level overview to get users started with the project.


