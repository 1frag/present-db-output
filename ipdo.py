import os
import sys
import json
import click


@click.command()
@click.option("-i", type=click.Choice(["clipboard", "type"], case_sensitive=False), default="clipboard")
@click.option("-o", default="stdout")
@click.option("-f", help="format output", type=click.Choice(["json"], case_sensitive=False), default="json")
def cli(i, o, f):
    present(i, o, f)


def present(read_from, write_to, format):
    if read_from.lower() == "clipboard":
        source = os.popen("xsel -o")
    else:
        source = sys.stdin
    table = source.read().split("\n")
    headers, _, *rows, _ = [[*map(str.strip, row.split("|"))] for row in table]
    rows = [dict(zip(headers, row)) for row in rows]

    if write_to == "stdout":
        target = sys.stdout
    else:
        target = open(write_to, "w")

    if format.lower() == "json":
        json.dump(rows, target, indent=2)
    else:
        raise NotImplementedError("format", format)
