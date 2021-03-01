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
    tasks={}

    def __init__(self,ip,port):
        self.redis_connection=redis.Redis(
            host=os.getenv("REDIS_HOST", ip),
            port=os.getenv("REDIS_PORT", port),
        )

    @app.route('/start_worker')
    def start_worker(self):
            task=self.redis_connection.blpop(['queue:tasks'], 0)
            if task:
                data=task[1].split(" ")
                print(data)
                text=requests.get(task[1]).text
                if data[0] is "wordcount":
                    result=self.word_count(text)
                if data[0] is "countwords":
                    result=self.counting_words(text)
                return result

    @app.route('/create')
    def create_worker(self):
        global WORKERS
        global WORKER_ID
       
        proc = Process(target=master.start_worker)
        proc.start()

        master.WORKERS[master.WORKER_ID]=proc
        WORKER_ID=+1

    @app.route('/delete')
    def delete_worker(self):
        global WORKERS
        global WORKER_ID

        WORKERS.remove(WORKER_ID)
        
        WORKERS_ID=-1
    
    def list_workers(self):
        for worker in WORKERS:
            print(worker.getpid())
            print(WORKERS.index(worker))

    def send_url(self, url, task):
        job=self.redis_connection.rpush('queue:tasks', task+url)

    def counting_words(text):
        return len(text.split())

    def word_count(text):
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
    print("Removing "+n_workers+"...")
    for i in range(n_workers):
        master.delete_worker()


def get_result(url):
    return master.tasks[url][0]

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
server.register_function(get_result, 'get_result')

# Run the server's main loop
try:
    print('Use Control-C to exit')
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting')


  