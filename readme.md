# Bitcoin "live" pricing with Kafka-Python and Coinbase API

## Overview
This simple project provides an initial testing environment for Kafka-Python. The aim of the project is that of pulling pricing data from the Coinbase API and calculating the change in price of the cryptocurrency using "real time" streaming.

## Requirements
In order for the code to run successfully, the following are required:
  1. Python v3.10 
  2. Kafka-Python v2.0.2
  3. Kafka v3.2.0 (with relevant server and brokers setup accordingly, for further information on this visit https://kafka.apache.org/quickstart)

## Quick start
1. cd into the downloaded kafka installation folder and build the project
```
./gradlew jar -PscalaVersion=2.13.6
```
2. Startup the bootstrap server
```
bin/zookeeper-server-start.sh config/zookeeper.properties
```
3. Start the kafka server
```
bin/kafka-server-start.sh config/server.properties
```
4. Proceed to create the relevant kafka topic to which the bitcoin prices will be sent on the kafka server
```
bin/kafka-topics.sh --create --bootstrap-server localhost:<localhost port> --replication-factor 1 --partitions 1 --topic <topic name>
```
5. Verify topic creation
- list topics
```
bin/kafka-topics.sh --list --bootstrap-server localhost:<localhost port>
```
- describe topics
```
bin/kafka-topics.sh --describe --bootstrap-server localhost:<localhost port> --topic <topic name>
```
6. Make a copy of the .env.sample file and save as .env in the same location
7. Source the .env file within the project
8. Edit model/config.py according to the user requirements
9. Startup Kafka consumer from CLI
```
python cli.py activate-consumer   
```
10. Startup Kafka producer from CLI
```
python cli.py produce
```
11. The Bitcoin prices will be printed to the CLI (by default every 30 seconds)



