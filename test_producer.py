from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092', api_version=(2,0,2))
producer.send('sample', b'Hello, World!')
producer.send('sample', key=b'message-two', value=b'This is Kafka-Python')
