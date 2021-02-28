   
import redis
from multiprocessing import Process
from flask import Flask
import requests





conn = redis.Redis('localhost')
app = Flask(__name__)

WORKERS = {}
WORKER_ID = 0


@app.route('/create')
def create_worker():
    global WORKER_ID
    WORKER_ID= WORKER_ID +1
    return 'Worker created with PID:' + str(WORKER_ID)

@app.route('/delete',methods=['POST'])
def delete_worker():
    global WORKER_ID
    WORKERS_ID=-1
    return 'Worker deleted with PID:' + str(WORKER_ID+1)

def word_count(text):
        word_frequencies=[]
        words_list=text.split()
        for word in words_list:
            word_frequencies.append(words_list.count(word))
        return word_frequencies

def counting_words(text):
    return len(text.split(" "))

def start_worker(tipus):
    global WORKER_ID
    print(WORKER_ID)
 
    """
    for i in range(WORKER_ID):
        url = conn.rpop("queue:urls")
        print(str(url))
        if tipus == 'wordcount':    
            WORKERS[i] = Process(target=word_count, args=(requests.get(url).text,))
        else:
            if tipus == 'countwords':
                WORKERS[i] = Process(target=counting_words, args=(requests.get(url).text,))
        for process in WORKER_ID:
            print(WORKERS[process].start())       

    
    while(conn.llen('queue:urls') != 0):
        for process in range(WORKER_ID):
             if( not WORKERS[process].is_alive()):
                WORKERS[process] = Process(target=counting_words, args=(requests.get(conn.rpop('queue:urls')).text,))
                WORKERS[process].start()
       """ 

            




if __name__ == '__main__':
    app.run()