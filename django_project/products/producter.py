import pika
import json
from django.conf import settings

params = pika.URLParameters(
   settings.RABBITMQ_URI
)

connect = pika.BlockingConnection(params)

channel = connect.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(
        exchange="", routing_key="main", body=json.dumps(body), properties=properties
    )
