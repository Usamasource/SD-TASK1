from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import requests
from multiprocessing import Process
import redis
from funcions import counting_words,word_count

WORKERS = {}
WORKER_ID = 0




conn = redis.Redis('localhost')
# Restrict to a particular path.
server = SimpleXMLRPCServer(
    ('localhost', 9000),
    logRequests=True,
)
      


def delete_worker():
    global WORKER_ID
    WORKERS_ID=-1
    return 'Worker deleted with PID:' + str(WORKER_ID+1)


server.register_function(delete_worker, 'delete')

def create_worker():
    global WORKER_ID
    WORKER_ID= WORKER_ID +1
    return 'Worker created with PID:' + str(WORKER_ID)


server.register_function(create_worker, 'create')

def start_worker(tipus):
    global WORKER_ID
    url = conn.rpop("queue:urls")
    proc = Process(target=counting_words, args=(requests.get(url).text,))
    proc.start()
    proc.join()
    print(proc.get())
server.register_function(start_worker, 'start')

try:
    print('Use Control-C to exit')
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting')


