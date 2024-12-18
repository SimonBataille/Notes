import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='File1')

for i in range(100):
    channel.basic_publish(exchange='', routing_key='File1', body=f"Message {i}")
    print(f'Send message {i}')
    time.sleep(1)

connection.close()