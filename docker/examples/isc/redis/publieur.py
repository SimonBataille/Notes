import redis
import time

red = redis.Redis(host='localhost', port=6379, db=0)

for i in range(100):
    message = f'Message {i}'
    red.publish('chat', message=message)
    print(f"J'ai envoye {message}")
    time.sleep(1)