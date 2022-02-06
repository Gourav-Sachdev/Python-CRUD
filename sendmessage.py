import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello RabbitMQ!')
print(" [x] Sent 'Hello RabbitMQ!")

connection.close()