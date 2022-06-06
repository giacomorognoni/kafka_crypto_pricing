from kafka import KafkaConsumer, KafkaProducer
from .config import SERVER, TOPIC, API_KEY, API_SECRET, CURRENCY_CODE, PRICE_CALL_DELAY_SECONDS
from coinbase.wallet.client import Client
import time

class CoinbaseClient:
    def __init__(self):
        self.server = SERVER
        self.topic = TOPIC
        self.consumer = KafkaConsumer(self.topic, bootstrap_servers=self.server)
        self.producer = KafkaProducer(bootstrap_servers=self.server)
        self.previous_bitcoin_value = 0.0
        self.currency_code = CURRENCY_CODE
        self.delay = PRICE_CALL_DELAY_SECONDS

    def produce(self) -> None:
        while True:
            client = Client(API_KEY, API_SECRET, api_version='YYYY-MM-DD')
            price = client.get_spot_price(currency=self.currency_code)
            message = self.producer.send(self.topic, f"{price.amount}".encode('utf-8'))
            result = message.get(timeout=60)
            time.sleep(self.delay)

    def live_consume(self) -> None:
        while True:
            for message in self.consumer:
                message = message.value.decode('UTF-8')
                if self.previous_bitcoin_value == 0.0:
                    print(f"The current Bitcoin price is {self.currency_code} {message}")
                    self.previous_bitcoin_value = float(message)
                else:
                    print(f"The previous Bitcoin price was {self.currency_code} {self.previous_bitcoin_value}, "
                    f"the new price is {self.currency_code} {message} there has been a change of "
                    f"{self.currency_code} {'%.2f' % (self.previous_bitcoin_value - float(message))} "
                    f"({'%.2f' % (100*(self.previous_bitcoin_value - float(message))/self.previous_bitcoin_value)}%)")
                    self.previous_bitcoin_value = float(message)