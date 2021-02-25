from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import requests
import multiprocessing
import master as m
import flask as Flask





# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/','/RPC2')

# Create server
with SimpleXMLRPCServer(('localhost', 9000),
    requestHandler=RequestHandler) as server:
    server.register_introspection_functions()
    
    master=m.Master("localhost","6379")

    def counting_words(text):
        return len(text.split(" "))
    
    server.register_function(counting_words, 'count')

    def word_count(text):
        word_frequencies=[]
        words_list=text.split()
        for word in words_list:
            word_frequencies.append(words_list.count(word))
        return word_frequencies

    server.register_function(word_count, 'wcount')

    

    # Run the server's main loop
    server.serve_forever()

    def recive_url(url_task):
        master.recive_url(url_task)
    

  