import os
import redis
from rq import Queue

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
        self.redis_connection=redis.Redis(
            host=os.getenv("REDIS_HOST", "127.0.0.1"),
            port=os.getenv("REDIS_PORT", "6379"),
        )
        self.redis_queue = Queue(connection=redis_connection)

    def create(self):
        self.workers.append(Worker())
        
    def delete(self, id):
        for w in self.workers:
            if w.id==id:
                self.workers.remove(w)

    def submit_task_queue(self, url):
        result=self.redis_queue.enqueue(url_task,url)

                
    
