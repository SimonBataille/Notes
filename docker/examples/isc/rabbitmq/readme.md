# Install rapidmq docker

`docker pull rabbitmq:management-alpine`

`docker run -d --name rabbitmq-container -p 5672:5672 -p 15672:15672 rabbitmq:management-alpine`

`http://localhost:15672` `guest:guest`

`docker exec -it rabbitmq-container rabbitmqctl status`

# Python env
`pip install pika`