import time

import pika
from dotenv import load_dotenv
import os

load_dotenv()

AMQP_USER = os.getenv("AMQP_USER")
AMQP_PASSWORD = os.getenv("AMQP_PASSWORD")
AMQP_ADDRESS = os.getenv("AMQP_ADDRESS")
AMQP_VHOST = os.getenv("AMQP_VHOST")
AMQP_PORT = os.getenv("AMQP_PORT")


def wait_for_rabbitmq():
    max_retries = 10
    retry_delay = 5

    for _ in range(max_retries):
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                    host=AMQP_ADDRESS,
                    port=int(AMQP_PORT),
                    virtual_host=AMQP_VHOST,
                    credentials=pika.PlainCredentials(AMQP_USER, AMQP_PASSWORD),
                )
            )
            connection.close()
            print("RabbitMQ is up and running.")
            return True
        except Exception as e:
            print(f"Connection to RabbitMQ failed: {e}")
            print("Connection to RabbitMQ failed. Retrying...")
            time.sleep(retry_delay)

    print("Failed to connect to RabbitMQ after multiple retries.")
    return False


def get_connection(local: bool = False) -> pika.BlockingConnection:
    if local:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="localhost")
        )
    else:
        if not wait_for_rabbitmq():
            raise SystemExit("Unable to connect to RabbitMQ. Exiting...")

        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=AMQP_ADDRESS,
                port=int(AMQP_PORT),
                virtual_host=AMQP_VHOST,
                credentials=pika.PlainCredentials(AMQP_USER, AMQP_PASSWORD),
            )
        )
    return connection

