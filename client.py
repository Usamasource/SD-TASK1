import xmlrpc.client
from concurrent.futures import ThreadPoolExecutor, as_completed

def call_counting_words():
   server = xmlrpc.client.ServerProxy("http://localhost:9000/", allow_none=True)
   return server.counting_words()

def call_word_count():
       server = xmlrpc.client.ServerProxy("http://localhost:9000/", allow_none=True)
   return server.word_count()

with ThreadPoolExecutor() as executor:
    count_w = {executor.submit(counting_words) for _ in range(4)}
    w_count = {executor.submit(counting_words) for _ in range(4)}
    for future in as_completed(sleeps):
        sleep_time = future.result()
        print(sleep_time)