import pika
import json
from app import db, Product
from config import Config

params = pika.URLParameters(Config.RABBITMQ_URI)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="main")


def callback(ch, method, properties, body):
    """
    Process incoming messages from RabbitMQ and perform CRUD operations on the Product table.

    Args:
        ch: The channel object.
        method: Delivery method.
        properties: Message properties.
        body: Message body containing JSON data.
    """
    # Kịch bản này xử lý việc tiếp nhận các tin nhắn từ RabbitMQ và thực hiện các hoạt động CRUD trên bảng Product.

    # Các đối số:
    #   ch: Đối tượng kênh.
    #   method: Phương thức giao hàng.
    #   properties: Các thuộc tính của tin nhắn.
    #   body: Nội dung tin nhắn chứa dữ liệu JSON.

    print("Received in main")
    data = json.loads(body)

    try:
        if properties.content_type == "product_created":
            # Handle message type: product_created
            # Xử lý loại tin nhắn: product_created
            product = Product(id=data["id"], title=data["title"], image=data["image"])
            with db.session.begin_nested():
                db.session.add(product)
            print("Product Created")

        elif properties.content_type == "product_updated":
            # Handle message type: product_updated
            # Xử lý loại tin nhắn: product_updated
            product = Product.query.get_or_404(data["id"])
            with db.session.begin_nested():
                product.title = data["title"]
                product.image = data["image"]
            print("Product Updated")

        elif properties.content_type == "product_deleted":
            # Handle message type: product_deleted
            # Xử lý loại tin nhắn: product_deleted
            product = Product.query.get_or_404(data["id"])
            with db.session.begin_nested():
                db.session.delete(product)
            print("Product Deleted")

        db.session.commit()

    except Exception as e:
        print(f"Error: {str(e)}")
        db.session.rollback()

    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue="main", on_message_callback=callback)

# Bắt đầu tiêu thụ tin nhắn từ RabbitMQ
print("Started Consuming")

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()

connection.close()
