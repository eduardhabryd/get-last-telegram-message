from connection import get_connection


def send_rabbit(message: str) -> None:
    # connection = get_connection()
    # channel = connection.channel()
    #
    # channel.queue_declare(queue='hello')
    #
    # channel.basic_publish(exchange='', routing_key='hello', body=message)
    # print(f" [x] Sent {message}")
    # connection.close()
    with get_connection() as connection:
        channel = connection.channel()

        channel.queue_declare(queue='hello')
        body = bytes(message, 'utf-8')
        channel.basic_publish(exchange='', routing_key='hello', body=body)
        print(f" [x] Sent {message}")


if __name__ == '__main__':
    send_rabbit("Hello Ed354uarde1")