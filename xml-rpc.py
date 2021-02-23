from socketserver import ThreadingMixIn
from xmlrpc.server import SimpleXMLRPCServer
import logging
import multiprocessing
import time
import random

class SimpleThreadedXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass

logging.basicConfig(level=logging.INFO)
server=SimpleXMLRPCServer(
    ('localhost', 9000),
    logRequests=True,
)

def counting_words(text):
    return len(text.split())

def word_count(text):
    word_frequencies=[]
    words_list=text.split()
    for word in words_list:
        word_frequencies.append(words_list.count(word))
    return word_frequencies

def run_server(host="localhost", port=8000):
    server_addr = (host, port)
    server = SimpleThreadedXMLRPCServer(server_addr)
    server.register_function(counting_words, 'counting_words')
    server.register_function(word_count, 'word_count')
    print("Server thread started. Testing server ...")
    print('listening on {} port {}'.format(host, port))

    server.serve_forever()

if __name__ == '__main__':
    run_server()