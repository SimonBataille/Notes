import pika

# Configuration et connexion au serveur RabbitMQ
try:
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Déclaration de la file (assure qu'elle existe)
    channel.queue_declare(queue='File1', durable=True)

    # Fonction de rappel pour traiter les messages reçus
    def callback(ch, method, properties, body):
        print(f"RECEIVED: {body.decode('utf-8')}")  # Assurez-vous de décoder le message en UTF-8

    # Configurer la consommation de messages
    channel.basic_consume(queue='File1', on_message_callback=callback, auto_ack=True)

    print('En attente de messages. Appuyez sur CTRL+C pour quitter.')
    
    # Démarrer la consommation des messages
    channel.start_consuming()

except pika.exceptions.AMQPConnectionError as e:
    print("Erreur de connexion à RabbitMQ :", e)
except KeyboardInterrupt:
    print("\nArrêt manuel de la consommation des messages.")
finally:
    if 'connection' in locals() and connection.is_open:
        connection.close()
