import os

import click
from atlassian import Confluence

from export_pdf.exporter import PdfExporter


def validate_space_key(ctx, param, value) -> str:
    if not isinstance(value, str):
        raise ValueError("The space_key parameter must be a string")
    if not value.strip():
        raise ValueError("The space_key parameter cannot be empty")

    return value


@click.command()
@click.option('-sk', '--space_key', callback=validate_space_key, type=str, required=True, help='Confluence space key')
def export_pdf(space_key):
    confluence = Confluence(
        url=os.getenv('ATLASSIAN_URL'),
        username=os.getenv('ATLASSIAN_USERNAME'),
        password=os.getenv('ATLASSIAN_TOKEN'),
        api_version='cloud' if os.getenv('IS_IN_CLOUD') else 'latest',
        cloud=os.getenv('IS_IN_CLOUD')
    )

    PdfExporter(confluence).export(space_key, os.getenv('CONF_EXPORT_DIR'))

    click.echo(click.style(f'Successfully exported', fg='green'))
