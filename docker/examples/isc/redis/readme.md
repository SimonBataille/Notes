# install ans launch redis container
`docker run --name redis-container -d -p 6379:6379 redis`

`docker ps`

`docker exec -it redis-container redis-cli`

```
SET cle "valeur"
GET cle
DEL cle

SUBSCRIBE chat
```

# venv python
`pip install redis`


