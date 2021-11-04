import click
from . import __version__


@click.command()
@click.version_option(version=__version__)
def main():
    """s3-sample: a tool designed to sample large files directly from AWS S3"""
    click.echo("Hello, world!")