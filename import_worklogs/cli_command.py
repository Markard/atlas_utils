import os
from datetime import datetime
from zoneinfo import ZoneInfo

import click

from import_worklogs.use_case.transfer_worklog import Transfer


@click.command()
@click.option('-d', '--day',
              type=click.DateTime(formats=['%Y-%m-%d']),
              required=True,
              help='Current date, for example:2025-03-31')
@click.option('-f', '--flush', type=bool, default=False, help='Ready to upload to logs?')
def issue_worklog(day: datetime, flush: bool) -> None:
    day = day.replace(tzinfo=ZoneInfo(os.getenv('TZ')))
    logs_for_day = Transfer().transfer(day, flush)

    success_msg = f'Successfully transferred' if flush else f'Load locally'
    click.secho(success_msg, fg='green', underline=True, bold=True)
    for log in logs_for_day:
        click.secho(f'ID: {log.id if log.id else 'None':<6}' + log.get_report())
