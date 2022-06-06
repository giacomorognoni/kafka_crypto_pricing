from kafka import KafkaConsumer, KafkaProducer


class CoinbaseClient:
    def __init__(self):
        self.server = "localhost:1234"
        self.topic = "coinbase_price_data"
        self.consumer = KafkaConsumer(self.topic, bootstrap_servers=self.server)
        self.producer = KafkaProducer(bootstrap_servers=self.server)

    def produce(self, data: str) -> None:
        message = self.producer.send(self.topic, '{"data":data}')
        result = message.get(timeout=60)
        return None

    def live_consume(self) -> str:
        for message in self.consumer:
            print(message)
            return message
