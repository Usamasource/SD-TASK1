#!/usr/bin/python

import os
import redis
import json
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import requests
from multiprocessing import Process
from flask import Flask

app = Flask(__name__)

class Master():
    WORKERS = {}
    WORKER_ID = 0
    tasks={}

    def __init__(self,ip,port):
        self.redis_connection=redis.Redis(
            host=os.getenv("REDIS_HOST", ip),
            port=os.getenv("REDIS_PORT", port),
        )

    @app.route('/start_worker')
    def start_worker(self):
        while(self.redis_connection.llen('queue:tasks')!=0):
            task=json.loads(self.redis_connection.rpop('queue:tasks'))
            if task:
                if task[0] == 'wordcount':
                    result=self.word_count(task[1])
                    print(result)
                if task[0] == 'countwords':
                    result=self.counting_words(task[1])
                    print(result)
                

    @app.route('/create')
    def create_worker(self):
        proc = Process(target=master.start_worker)
        proc.start()

        master.WORKERS[master.WORKER_ID]=proc
        master.WORKER_ID=+1

    @app.route('/delete')
    def delete_worker(self):
        if master.WORKERS[master.WORKER_ID].is_alive():
            master.WORKERS[master.WORKER_ID].terminate()
        master.WORKERS[master.WORKER_ID]=None
        master.WORKERS_ID=-1
    
    def list_workers(self):
        for worker in self.WORKERS:
            print(worker.getpid())
            print(WORKERS.index(worker))

    def send_url(self, urls, task):
        for url in urls:
            job=self.redis_connection.rpush('queue:tasks', json.dumps([task, url]))

    def counting_words(self, text):
        return len(text.split())

    def word_count(self, text):
        word_frequencies=[]
        words_list=text.split()
        for word in words_list:
            word_frequencies.append(words_list.count(word))
        return word_frequencies

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/','/RPC2')

def create_w(n_workers):
    print("Creating "+str(n_workers)+"...")
    for i in range(n_workers):
        master.create_worker()

def delete_w(n_workers):
    print("Removing "+str(n_workers)+"...")
    for i in range(n_workers):
        master.delete_worker()

# Ceate server
server=SimpleXMLRPCServer(('localhost', 9000),
    requestHandler=RequestHandler,
    logRequests=True,
    allow_none=True)

master=Master("localhost","6379")

server.register_introspection_functions
server.register_multicall_functions()
server.register_instance(master)
server.register_function(create_w, 'create_w')
server.register_function(delete_w, 'delete_w')

# Run the server's main loop
try:
    print('Use Control-C to exit')
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting')


  