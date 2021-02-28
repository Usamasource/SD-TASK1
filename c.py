import xmlrpc.client
import requests
import sys
import click

s = xmlrpc.client.ServerProxy('http://localhost:9000')

@click.command()
@click.argument('worker', required=False)
@click.option('--create', type=click.INT)
@click.option('--delete', type=click.INT)
def worker(worker, create, delete):
    if worker is not None:
        if create is not None:
            s.create_w(create)
        if delete is not None:
            s.delete_w(create)

@click.command()
@click.argument('job')
@click.option('--run')
@click.option('--wordcount')
@click.option('--countwords')
def job(job, run, wordcount, countwords):
    if job is not None:
        if run is not None:
            if wordcount is not None:
                s.send_url(wordcount)
                server.master.tasks[wordcount]

worker()
s.send_url("http://localhost:8000/hola.txt")
