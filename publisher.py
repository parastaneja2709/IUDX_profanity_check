import pika, json

print('Making a connection to rmq ...')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
print('connection established to rmq')

message1 = { "rating" : 4.4, "comment" : "good resource", "resourceID" : "iisc.ac.in/89a36273d77dac4cf38114fca1bbe64392547f86/rs.iudx.io/pune-env-flood", "userID" : "b709a897-c1df-4521-86fb-60d7ba6fb888", "status" : "pending", "id" : "1a" }
message2 = { "rating" : 2, "comment" : "It sucks", "resourceID" : "iisc.ac.in/89a36273d77dac4cf38114fca1bbe64392547f86/rs.iudx.io/pune-env-flood", "userID" : "b709a897-c1df-4521-86fb-60d7ba6fb888", "status" : "pending", "id":"2b" }
message3 = { "rating" : 1.1, "comment" : "It makes no fucking sense", "resourceID" : "iisc.ac.in/89a36273d77dac4cf38114fca1bbe64392547f86/rs.iudx.io/pune-env-flood", "userID" : "c709a897-c1df-4521-86fb-60d7ba6fb888", "status" : "pending", "id":"3c" }

channel.basic_publish(exchange='test-exchange', routing_key='test', body=json.dumps(message1))
channel.basic_publish(exchange='test-exchange', routing_key='test', body=json.dumps(message2))
channel.basic_publish(exchange='test-exchange', routing_key='test', body=json.dumps(message3))
print("messages sent to queue")
connection.close()
