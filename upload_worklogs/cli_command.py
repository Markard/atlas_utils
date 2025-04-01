import os
from datetime import datetime
from zoneinfo import ZoneInfo

import click

from upload_worklogs.use_case.upload_worklogs import Uploader


@click.command()
@click.option('-d', '--day',
              type=click.DateTime(formats=['%Y-%m-%d']),
              required=True,
              help='Date in %Y-%m-%d format (required)')
@click.option('-f', '--flush',
              type=bool,
              default=False,
              help='If True, uploads worklogs to Jira. If False, only displays the logs (default: False)')
def upload_worklog(day: datetime, flush: bool) -> None:
    day = day.replace(tzinfo=ZoneInfo(os.getenv('TZ')))
    logs_for_day = Uploader().upload(day, flush)

    success_msg = f'Successfully transferred' if flush else f'Load locally'
    click.secho(success_msg, fg='green', underline=True, bold=True)
    for log in logs_for_day:
        click.secho(f'ID: {log.id if log.id else 'None':<6}' + log.get_report())
