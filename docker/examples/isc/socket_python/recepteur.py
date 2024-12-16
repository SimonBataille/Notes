import redis

# Connexion à Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

def recepteur():
    """
    Reçoit et affiche les messages depuis une liste Redis.
    """
    while True:
        message = redis_client.blpop('message_queue')[1]  # Lire et supprimer le premier message
        print('Je reçois :', message)
        if message == 'FIN':  # Quitter la boucle lorsque 'FIN' est reçu
            break

if __name__ == '__main__':
    recepteur()
