#!/usr/bin/python

import os
import redis
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import requests
from multiprocessing import Process
from flask import Flask

app = Flask(__name__)

class Master():
    WORKERS = {}
    WORKER_ID = 0

    def __init__(self,ip,port, server):
        self.redis_connection=redis.Redis(
            host=os.getenv("REDIS_HOST", ip),
            port=os.getenv("REDIS_PORT", port),
            )
        self.server=server

    @app.route('/start_worker')
    def start_worker(self, funct1, funct2):
        while(1):
            task=self.redis_connection.blpop('queue:tasks', 0)
            if task:
                data=requests.get(url)
                n_words=funct1(data)
                words_frequency=funct2(data)

    @app.route('/create')
    def create_worker(self, funct1, funct2):
        global WORKERS
        global WORKER_ID

        proc = Process(target=master.start_worker, args=(funct1, funct2))
        proc.start()

        master.WORKERS[master.WORKER_ID]=proc
        WORKER_ID=+1

    @app.route('/delete')
    def delete_worker(self):
        global WORKERS
        global WORKER_ID

        WORKERS.remove(WORKER_ID)
        WORKERS_ID=-1

    def send_url(self, url_task):
        job=self.redis_connection.rpush('queue:tasks', json.dumps(url_task))

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/','/RPC2')

def counting_words(text):
        return len(text.split(" "))

def word_count(text):
    word_frequencies=[]
    words_list=text.split()
    for word in words_list:
        word_frequencies.append(words_list.count(word))
    return word_frequencies

# Create server
with SimpleXMLRPCServer(('localhost', 9000),
    requestHandler=RequestHandler) as server:
    server.register_introspection_functions()
    master=Master("localhost","6379", server)
    
    for i in range(10):
        master.create_worker(counting_words, word_count)

server.register_function(counting_words, 'count')
server.register_function(word_count, 'wcount')
# Run the server's main loop
server.serve_forever()


  