import pika


#This function is a callback function that will be called 
# whenever a message is received by the consumer
# ch: is the channel object in use.
# method: is the method object that describes the received message.
# properties: is the message properties.
# body: is the message body.
def on_message_received(ch,method,properties,body):
    print(f'recieved new message: {body}')

#create connection locally running rabbitmq
connection_parametre = pika.ConnectionParameters('localhost')

#create connection to rabbitmq broker
connection = pika.BlockingConnection(connection_parametre)

#create channel 
channel = connection.channel()

channel.queue_declare(queue='LettreBox')


channel.basic_consume(queue='LettreBox',auto_ack=True,on_message_callback=on_message_received)

print('Starting Consuming')

channel.start_consuming()

