import pika
import json
from config import Config
# Tạo kết nối đến RabbitMQ sử dụng tham số được cấu hình từ Config.RABBITMQ_URI
params = pika.URLParameters(Config.RABBITMQ_URI)

connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish(method, body):
    """
    Hàm này được sử dụng để gửi tin nhắn tới hàng đợi "admin" trên RabbitMQ.
    - `method`: Phương thức của tin nhắn.
    - `body`: Nội dung tin nhắn, được chuyển đổi sang định dạng JSON.
    """
    # Tạo các thuộc tính cơ bản cho tin nhắn
    properties = pika.BasicProperties(method)
    
    # Gửi tin nhắn tới hàng đợi "admin" với các thuộc tính và nội dung cụ thể
    print("Pushing for admin: \n")
    channel.basic_publish(
        exchange="", routing_key="admin", body=json.dumps(body), properties=properties
    )
    print("Content: \n", json.dumps(body, indent=4))
    print("Requesting ................ [>>>>]")