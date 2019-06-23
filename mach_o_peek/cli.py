#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from pprint import pprint
import click
from .header import Header


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
    print(f"File Name:\t{header.file}")
    print(f"MagicType:\t{header.magic}")
    print(f"File Type:\t{header.filetype}")
    print(f"CPU Type:\t{header.cputype}")
    print(f"Number of Cmds:\t{header.ncmds}")
    print(f"Size of Cmds:\t{header.sizeofcmds}")


cli.add_command(header)
