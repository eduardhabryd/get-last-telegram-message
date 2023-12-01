import os
import sys
import asyncio

from connection import get_connection
from bot import main as bot_main


def main():
    connection = get_connection()
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        body = str(body.decode('utf-8'))
        method, body = body.split(' ', 1)
        print(f"Method: {method}, Last Message: {body}", flush=True)
        if method == "send":
            pass

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
    print('[*] Waiting for messages. To exit press CTRL+C', flush=True)
    channel.start_consuming()


if __name__ == '__main__':
    asyncio.run(bot_main())
    main()


# if __name__ == '__main__':
#     try:
#         asyncio.run(bot_main())
#         main()
#     except KeyboardInterrupt:
#         print('Interrupted')
#         try:
#             sys.exit(0)
#         except SystemExit:
#             os._exit(0)
