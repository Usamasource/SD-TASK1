import xmlrpc.client
import requests

s = xmlrpc.client.ServerProxy('http://localhost:9000')

recive_url("localhost:8000/hola.txt")





"""print(s.count(requests.get("http://localhost:8000/"+"ml/hola1.txt").text))
print(s.wcount(requests.get("http://localhost:8000/"+"ml/hola1.txt").text))"""





