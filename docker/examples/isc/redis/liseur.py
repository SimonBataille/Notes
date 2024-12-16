import redis

red = redis.Redis(host='localhost', port=6379, db=0)

pubsub = red.pubsub()
pubsub.subscribe('chat')

print('En attente...')

for message in pubsub.listen():
    if message['type'] == 'message':
        print(f"J'ai recu {message['data']}")