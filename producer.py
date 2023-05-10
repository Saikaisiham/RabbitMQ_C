import pika

#create connection locally running rabbitmq
connection_parametre = pika.ConnectionParameters('localhost')

#create connection to rabbitmq broker
connection = pika.BlockingConnection(connection_parametre)

#create channel 
channel = connection.channel()

channel.queue_declare(queue='LettreBox')

message = 'Hello , first RabbitMQ'

channel.basic_publish(exchange='',routing_key='LettreBox')

print(f'sent message: {message}')

#close the connection 
connection.close()