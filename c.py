import xmlrpc.client
import requests

s = xmlrpc.client.ServerProxy('http://localhost:9000')
print(s.dir()) 
print(s.count(requests.get("http://localhost:8000/"+"ml/hola1.txt").text))
print(s.wcount(requests.get("http://localhost:8000/"+"ml/hola1.txt").text))





