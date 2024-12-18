import pika
import time

try:
    # Connexion à RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Déclarer une file avec des messages persistants
    channel.queue_declare(queue='File1', durable=True)

    # Publier 100 messages
    for i in range(1000000):
        channel.basic_publish(
            exchange='',
            routing_key='File1',
            body=f"Message {i}",
            properties=pika.BasicProperties(delivery_mode=2)  # Messages persistants
        )
        print(f'Sent message {i}')
        # time.sleep(1)  # Facultatif
except pika.exceptions.AMQPConnectionError as e:
    print(f"Error connecting to RabbitMQ: {e}")
finally:
    # Assurez-vous de fermer la connexion proprement
    if 'connection' in locals() and connection.is_open:
        connection.close()
