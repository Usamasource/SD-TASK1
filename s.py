from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import os
import json
import requests
import urllib.request 



# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/','/RPC2')

# Create server
with SimpleXMLRPCServer(('localhost', 9000),
    requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    
    # Register a function under a different name
    def show_act_dir():
        return os.getcwd()
    
    server.register_function(show_act_dir, 'dir')


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