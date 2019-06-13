# -*- coding: utf-8 -*-

"""Console script for mach_o_peek."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for mach_o_peek."""
    click.echo("Replace this message by putting your code into "
               "mach_o_peek.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
