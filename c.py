import xmlrpc.client
import requests
import sys
import click
from logging import ERROR

s = xmlrpc.client.ServerProxy('http://localhost:9000')
multicall=xmlrpc.client.MultiCall(s)

@click.group()
def cli():
    None

@cli.command()
@click.argument('worker')
@click.option('--create', type=click.INT)
@click.option('--delete', type=click.INT)
def worker(worker, create, delete):
    if worker is not None:
        if create is not None:
            s.create_w(create)
        if delete is not None:
            s.delete_w(delete)


@cli.command()
@click.argument('job_run')
@click.option('--wordcount', multiple=True)
@click.option('--countwords', multiple=True)
def job(job_run, wordcount, countwords):
    if job is not None:
        if wordcount is not None:
            ids=s.send_url(wordcount, 'wordcount')
        if countwords is "()":
            ids=s.send_url(countwords, 'countwords')
        print(s.get_result(ids))

cli()