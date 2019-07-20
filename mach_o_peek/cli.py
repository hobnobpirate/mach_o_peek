#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pprint import pprint

import click

from mach_o_peek.header import Header


@click.group()
def cli():
    """Command line interface for Mach O Peek"""
    pass


@click.command("header")
@click.argument("binary")
def header(binary):
    """Inspect the Mach O header.

    Keyword arguments:

    binary -- binary to examine
    """
    header = Header(binary)
    header.read_header()
    header.print_header()


cli.add_command(header)
