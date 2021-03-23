#!/usr/bin/python

import os
import redis
import json
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import requests
import multiprocessing
from flask import Flask
import time

app = Flask(__name__)

class Master():

    def __init__(self,ip,port):
        self.redis_connection=redis.Redis(
            host=os.getenv("REDIS_HOST", ip),
            port=os.getenv("REDIS_PORT", port),
        )
        self.TASKS={}
        self.TASK_ID=0
        self.WORKERS ={}
        self.WORKER_ID = 0
        self.RESULTS = multiprocessing.Manager().dict()
        self.RESULTS_CONT = 0

 

   
    
    @app.route('/start_worker')
    def start_worker(self):
        while True:
            task=self.redis_connection.rpop('queue:tasks')
            if task:
                task=json.loads(task)
                print("tarea desencolada: "+ task[0])
                if task:
                    if task[0] == 'wordcount':
                        result=self.word_count(requests.get(task[1]).text)
                    if task[0] == 'countwords':
                        result=self.counting_words(requests.get(task[1]).text)
                        print("resultado ejecucion: "+str(result))
                    self.TASKS[task[2]]=result
                    self.return_result(result, task[2])

    def return_result(self, result, id):
        self.redis_connection.rpush('queue:results', json.dumps([result, id]))

    def read_redis_results(self):
        print("helloworlds")
        while True:
            time.sleep(1.0)
            result=self.redis_connection.rpop('queue:results')
            if result:
                task=json.loads(result)
                self.RESULTS[task[1]]=task[0]
                self.RESULTS_CONT=+1

    @app.route('/create')
    def create_worker(self):
        proc=multiprocessing.Process(target=self.start_worker)
        proc.start()

        self.WORKERS[self.WORKER_ID]=proc
        self.WORKER_ID=+1

    @app.route('/delete')
    def delete_worker(self):
        if self.WORKERS[self.WORKER_ID].is_alive():
            self.WORKERS[self.WORKER_ID].terminate()
        self.WORKERS[self.WORKER_ID]=None
        self.WORKERS_ID=-1

    def list_workers(self):
        for worker in self.WORKERS:
            print(worker.getpid())
            print(self.WORKERS[worker])
        
    def send_url(self, urls, task):
        ids=[]
        for url in urls:
            print("url enviada: "+url)
            job=self.redis_connection.rpush('queue:tasks', json.dumps([task, url, self.TASK_ID]))
            ids.append(self.TASK_ID)
            print("id de la url enviada: "+str(self.TASK_ID))
            self.TASK_ID+=1
        return ids

    def counting_words(self, text):
        return len(text.split())

    def word_count(self, text):
        word_frequencies={}
        words_list=text.split()
        for word in words_list:
            word_frequencies[word]=words_list.count(word)
        return word_frequencies
     
    def getResults(self):
        return str(self.RESULTS)




#@Fuera de la clase

master=Master("localhost","6379")

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/','/RPC2')

def create_w(n_workers):
    print("Creating "+str(n_workers)+" workers...")
    for i in range(n_workers):
        master.create_worker()

def delete_w(n_workers):
    print("Removing "+str(n_workers)+" workers...")
    for i in range(n_workers):
        master.delete_worker()



def get_result(ids):
    return master.getResults()


# Ceate server
server=SimpleXMLRPCServer(('localhost', 9000),
    requestHandler=RequestHandler,
    logRequests=True,
    allow_none=True)


results_process=multiprocessing.Process(target=master.read_redis_results)
results_process.start()

server.register_multicall_functions()
server.register_introspection_functions
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


  