import pika
import time 
import random


'''This function is a callback function that will be called 
 whenever a message is received by the consumer
 ch: is the channel object in use.
 method: is the method object that describes the received message.
 properties: is the message properties.
 body: is the message body.'''
def on_message_received(ch,method,properties,body):
    #genetrates a random int between 1 & 6 which simulates the time it takes
    #to process the message 
    processing_time = random.randint(1,6)
    print(f'recieved: {body} , will take {processing_time} to process ')
    #sleep for the amount of time generated in the prev step
    time.sleep(processing_time)
    """
    acknowledges to the RabbitMQ server that the message has been received and processed successfully. 
    This tells RabbitMQ to remove the message from the queue
    """
    ch.basic_ack(delivery_tag = method.delivery_tag)
    print('Finish processing the message')

#create connection locally running rabbitmq
connection_parametre = pika.ConnectionParameters('localhost')

#create connection to rabbitmq broker
connection = pika.BlockingConnection(connection_parametre)

#create channel 
channel = connection.channel()

channel.queue_declare(queue='LettreBox')

"""
 parameter specifies the maximum number of messages that the server will 
 deliver to the consumer before waiting for acknowledgments. 
 In this case, the value of 1 means that the server will only send one message at a time to this consumer
"""

channel.basic_qos(prefetch_count=1)

#remove ack 
channel.basic_consume(queue='LettreBox',on_message_callback=on_message_received)

print('Starting Consuming')

channel.start_consuming()

