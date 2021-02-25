import os
import redis
from rq import Queue
import multiprocessing


"""
WORKERS = {}
WORKER_ID = 0

def start_worker(worker_id,url):
    
    
    

def create_worker():
    global WORKERS
    global WORKER_ID
    proc = Process(target=start_worker, args=(WORKER_ID,url))
    proc.start()
    WORKERS[WORKER_ID]=proc
    WORKER_ID=+1

def delete_worker():
    global WORKERS
    global WORKER_ID
    WORKERS.remove(WORKER_ID)
    WORKERS_ID=-1
"""


class Worker:
    def __init__(self):
        self.id=id("tap")

    def counting_words(self, text):
        return len(text.split())

    def word_count(self, text):
        word_frequencies=[]
        words_list=text.split()
        for word in words_list:
           word_frequencies.append(words_list.count(word))
        return word_frequencies

class Master:
    def __init__(self):
        self.workers=[]
        worker_id
        self.redis_connection=redis.Redis(
            host=os.getenv("REDIS_HOST", "127.0.0.1"),
            port=os.getenv("REDIS_PORT", "6379"),
        )
        self.redis_queue = Queue(connection=redis_connection)

    def start_worker(url):
        word_count(url) 

    def create_worker():
        proc = Process(target=start_worker, args=(url,op))
        proc.start()
        self.workers.append(proc)
        
    def delete(id):
        for w in self.workers:
            if w.id==id:
                self.workers.remove(w)

    def submit_task_queue(self, url):
        result=self.redis_queue.enqueue(url_task,url)

                
    
