from datetime import datetime

import click


@click.command()
@click.option('-d', '--date', type=click.DateTime(), required=True, help='Date')
def issue_worklog(date: datetime) -> None:
    click.secho(f'Success')
