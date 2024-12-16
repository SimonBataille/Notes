import time
import redis

# Connexion à Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

def emetteur():
    """
    Envoie des messages dans une liste Redis.
    """
    for i in range(5):
        message = f'Message {i}'
        print('J\'envoie :', message)
        redis_client.rpush('message_queue', message)  # Ajouter à la file d'attente Redis
        time.sleep(1)
    redis_client.rpush('message_queue', 'FIN')  # Indiquer la fin des messages

if __name__ == '__main__':
    emetteur()
