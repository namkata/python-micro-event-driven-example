import pika
import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from products.models import Product  # noqa
from django.conf import settings  # noqa

print("Hello the gioi", settings.RABBITMQ_URI)
params = pika.URLParameters(settings.RABBITMQ_URI)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="admin")


def callback(ch, method, properties, body):
    # sourcery skip: avoid-builtin-shadow
    try:
        id = json.loads(body)
        print(f"[<<<<] ................ Received ID: {id}")
        product = Product.objects.get(id=id)
        product.likes = product.likes + 1
        product.save()
        print("Product likes increased!")
    except Product.DoesNotExist:
        print(f"Product with ID {id} does not exist.")


channel.basic_consume(queue="admin", on_message_callback=callback, auto_ack=True)

print("Started Consuming")

channel.start_consuming()

channel.close()
