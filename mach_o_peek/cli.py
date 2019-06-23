import click
from pprint import pprint
import click
from .header import Header


@click.command()
@click.argument("binary")
def cli(binary):
    """Command line interface for Mach O Peek.

    Keyword arguments:

    binary -- binary to examine
    """
    header = Header(binary)
    header.read_header()
    d = header.__dict__
    pprint(d, indent=4, width=80)
