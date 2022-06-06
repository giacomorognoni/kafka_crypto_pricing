import click
from model.kafka import CoinbaseClient


@click.group()
def main() -> None:
    kafka_client = CoinbaseClient()


@main.command()
@click.option(
    "--data",
    prompt="Please add the string to be consumed",
    help="The string to be consumed by the Kafka consumer client",
)
def produce(data: str) -> None:
    kafka_client.produce(data)
    return None


@main.command(help="Activate Kafka consumer")
def activate_consumer() -> str:
    message = kafka_client.live_consume()
    return message


if __name__ == "__main__":
    main()
