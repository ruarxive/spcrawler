#!/usr/bin/env python
# -*- coding: utf8 -*-
import logging

import click

from .cmds.extractor import Project

# logging.getLogger().addHandler(logging.StreamHandler())
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)


def enableVerbose():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.DEBUG)


@click.group()
def cli1():
    pass


@cli1.command()
@click.option('--url', '-u', default=None, help='URL of the Yandex.Disk public resource')
@click.option('--verbose', '-v', is_flag=True, help='Verbose output. Print additional info')
def walk(url, verbose):
    """Print recursively resources"""
    if verbose:
        enableVerbose()
    if url is None:
        print('Public resource URL required')
        return
    acmd = Project()
    acmd.walk(url)
    pass


@click.group()
def cli2():
    pass


@cli2.command()
@click.option('--url', '-u', default=None, help='URL of the public resource to process')
@click.option('--verbose', '-v', is_flag=True, help='Verbose output. Print additional info')
def dump(url, verbose):
    """Dump all data as JSON lines files"""
    if verbose:
        enableVerbose()
    if url is None:
        print('Public resource URL required')
        return
    acmd = Project()
    acmd.dump(url)
    pass



@click.group()
def cli3():
    pass


@cli3.command()
@click.option('--url', '-u', default=None, help='URL of the public resource to process')
@click.option('--verbose', '-v', is_flag=True, help='Verbose output. Print additional info')
def ping(url, verbose):
    """Ping API endpoint"""
    if verbose:
        enableVerbose()
    if url is None:
        print('Public resource URL required')
        return
    acmd = Project()
    acmd.ping(url)
    pass

@click.group()
def cli4():
    pass


@cli4.command()
@click.option('--url', '-u', default=None, help='URL of the public resource to process')
@click.option('--verbose', '-v', is_flag=True, help='Verbose output. Print additional info')
def getfiles(url, verbose):
    """Get files"""
    if verbose:
        enableVerbose()
    if url is None:
        print('Public resource URL required')
        return
    acmd = Project()
    acmd.getfiles(url)
    pass


cli = click.CommandCollection(sources=[cli1, cli2, cli3, cli4])

# if __name__ == '__main__':
#    cli()
