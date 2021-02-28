import xmlrpc.client
import requests
import sys
import redis
import json
from master import start_worker

conn = redis.Redis('localhost')
s = xmlrpc.client.ServerProxy('http://localhost:9000')
arguments = sys.argv

"""print(s.count(requests.get("http://localhost:8000/"+"ml/hola1.txt").text))
print(s.wcount(requests.get("http://localhost:8000/"+"ml/hola1.txt").text))"""


if(len(arguments)<= 2):
    print("!Error!: Has d'introduir més parametres. Format: client.py <workers> <create-delete> || client.py run ")
else:
    if(arguments[1].split("-")[0] == 'run'):
       
        for url in arguments[2].split(" "):
            conn.rpush('queue:urls',url)
        print("The elements were correctly added to the queue")
        print("STARTING WORKERS...")
        
        print(s.start(str(arguments[1].split("-")[1])))
            
    if(arguments[1] == 'worker'):
        if(arguments[2] == 'create'):
            print("Creant...")
            s.create()
            """print(requests.get("http://localhost:5000/create").text)"""
        if(arguments[2] == 'delete'):
            print("Eliminant...")
            s.delete()
            print(requests.get("http://localhost:5000/delete").text)