from kafka import KafkaConsumer
consumer = KafkaConsumer('sample', api_version=(2,0,2))
for message in consumer:
    print (message)
