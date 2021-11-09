import click
from . import __version__
from s3_sample.csv import sample_csv_head
from s3_sample.utils import generate_outpath


@click.command()
@click.version_option(version=__version__)
@click.option("--infile", help="infile for data")
@click.option("--outfile", default=None, help="oufile path: e.g. path/to/output/sample.csv")
@click.option("--nlines", default=10, help = "Number of lines to take from head")

## main is sample head for now. Will expand as other options are desired
def main(infile, outfile, nlines):
    """s3-sample: a tool designed to sample large files directly from AWS S3"""
    out_path = generate_outpath(in_path=infile,out_path=outfile)
    sample_csv_head(in_path=infile, out_path=out_path,n=nlines)

    click.echo(f"Sampled {nlines} lines\nData sampled from {infile}\nData written to {out_path}")