import pika
import time
import random
#create connection locally running rabbitmq
connection_parametre = pika.ConnectionParameters('localhost')

#create connection to rabbitmq broker
connection = pika.BlockingConnection(connection_parametre)

#create channel 
channel = connection.channel()

channel.queue_declare(queue='LettreBox')

messageId =1

#using the infinte loop to publish a msg every couple seconds
while(True):
    message = f'sending messageId: {messageId}'

    channel.basic_publish(exchange='',routing_key='LettreBox')

    print(f'sent message: {message}')

    time.sleep(random.randint(1,4))

    #close the connection 
    # connection.close()

    messageId += 1