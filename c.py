import xmlrpc.client
import requests
import sys
import click
from logging import ERROR

s = xmlrpc.client.ServerProxy('http://localhost:9000')

@click.group()
def cli():
    None

@cli.command()
@click.argument('worker')
@click.option('--create', type=click.INT)
@click.option('--delete', type=click.INT)
def worker(worker, create, delete):
    if worker != None:
        if create != None:
            s.create_w(create)
        if delete != None:
            s.delete_w(delete)


@cli.command()
@click.argument('job_run')
@click.option('--wordcount', multiple=True)
@click.option('--countwords', multiple=True)
def job(job_run, wordcount, countwords):
    ids=[]
    if job != None:
        if wordcount != "()":
            for i in s.send_url(wordcount, 'wordcount'):
                ids.append(i)
        if countwords != "()":
            for i in s.send_url(countwords, 'countwords'):
                ids.append(i)
        print(ids)
        print(s.get_result(ids))


cli()