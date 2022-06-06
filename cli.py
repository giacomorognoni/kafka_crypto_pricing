import click
from model.kafka import CoinbaseClient


@click.group()
def main() -> None:
    pass


@main.command(help="Retrieve the Bitcoin price for the Coinbase API and pubblish to kafka topic")
def produce() -> None:
    kafka_client.produce()
    return None


@main.command(help="Activate Kafka consumer")
def activate_consumer() -> str:
    message = kafka_client.live_consume()
    return message


if __name__ == "__main__":
    kafka_client = CoinbaseClient()
    main()
