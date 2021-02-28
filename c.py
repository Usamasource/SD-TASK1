import xmlrpc.client
import requests
import sys


s = xmlrpc.client.ServerProxy('http://localhost:9000')
arguments = sys.argv

s.send_url("http://localhost:8000/hola.txt")



"""if(len(arguments)<= 2):
    print("!Error!: Has d'introduir més parametres. Format: client.py <workers> <create-delete> || client.py run ")
else:
    if(arguments[1] == 'run'):
        print("Running...")
    if(arguments[1] == 'worker'):
        if(arguments[1] == 'create'):
            print("Creant...")
        if(arguments[1] == 'delete'):
            print("Eliminant...")"""
