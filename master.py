   
import redis
import multiprocessing
class Master:
    WORKERS = {}
    WORKER_ID = 0

    def __init__(self,ip,port):
        self.redis_connection=redis.Redis(
            host=os.getenv("REDIS_HOST", ip),
            port=os.getenv("REDIS_PORT", port),
        )
        self.redis_queue = Queue(connection=self.redis_connection)

   

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
        
    