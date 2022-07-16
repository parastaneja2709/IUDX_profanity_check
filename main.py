import sys,os
from subscribe import RabbitMq

queue_name = "catalogue-rating"
es_index_name="cat-rating"
try:
    RabbitMq(es_index_name,queue_name)
except KeyboardInterrupt:
    print('Interrupted')
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)
