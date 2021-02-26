   
import redis
from multiprocessing import Process
from flask import Flask

app = Flask(__name__)

WORKERS = {}
WORKER_ID = 0


@app.route('/create')
def create_worker():
    global WORKERS
    global WORKER_ID
    proc = Process(target=start_worker, args=(url))
    proc.start()
    WORKERS[WORKER_ID]=proc
    WORKER_ID=+1

@app.route('/delete')
def delete_worker():
    global WORKERS
    global WORKER_ID
    WORKERS.remove(WORKER_ID)
    WORKERS_ID=-1

def start_worker():
    

if __name__ == '__main__':
    app.run()