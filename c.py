import xmlrpc.client
import requests
import sys
import click

s = xmlrpc.client.ServerProxy('http://localhost:9000')

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
            s.delete_w(create)


@cli.command()
@click.argument('job_run')
@click.option('--wordcount')
@click.option('--countwords')
def job(job_run, wordcount, countwords):
    if job is not None:
        print(wordcount)
        if wordcount is not None:
            s.send_url(wordcount)
            print(s.get_result())

cli()