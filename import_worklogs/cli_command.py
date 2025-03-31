import os
from datetime import datetime
from zoneinfo import ZoneInfo

import click


@click.command()
@click.option('-d', '--date', type=click.DateTime(), required=True, help='Date')
def issue_worklog(date: datetime) -> None:
    date = date.replace(tzinfo=ZoneInfo(os.getenv('TZ')))
    click.secho(f'Success')
