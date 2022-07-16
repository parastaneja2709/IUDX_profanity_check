import pika, sys, os,json
from verification import profanity_check

def RabbitMq(es_index_name,queue_name):
    print('Making a connection to rmq ...')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    # credentials = pika.PlainCredentials('admin', '9pFo6bvZ69tpeKmdUejb')
    # connection = pika.BlockingConnection(pika.ConnectionParameters('databroker.iudx.io',29042,'IUDX-INTERNAL',credentials))
    channel = connection.channel()
    print('connection established to rmq')

    def callback(ch, method, properties, body):
        #print(" [x] %r " % body)
        payload = json.loads(body)
        Comment = payload.get('comment')
        Id = payload.get('id')
        print(Id)
        print(Comment)
        profanity_check(es_index_name,Id,Comment)

    status=channel.queue_declare(queue_name,passive=True)
    if status.method.message_count == 0:
        print("empty queue")
        #print(' [*] Waiting for logs. To exit press CTRL+C')
    else:
        channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
        channel.start_consuming()
    print('To exit press CTRL+C')
    connection.close()

# queue_name = "catalogue-rating"
# print('Making a connection to rmq ...') 
# credentials = pika.PlainCredentials('admin', '9pFo6bvZ69tpeKmdUejb')
# connection = pika.BlockingConnection(pika.ConnectionParameters('databroker.iudx.io',29042,'IUDX-INTERNAL',credentials))
# channel = connection.channel()
# print('connection established to rmq')

