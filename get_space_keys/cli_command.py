import os

import click
import dotenv
from atlassian import Confluence

from get_space_keys.entity.result import Result
from get_space_keys.entity.result import Space


@click.command()
@click.option('-s', '--start', type=int, default=0, help='Start')
@click.option('-l', '--limit', type=int, default=500, help='Limit spaces in response')
def get_space_keys(start: int, limit: int) -> None:
    dotenv.load_dotenv()

    confluence = Confluence(
        url=os.getenv('ATLASSIAN_URL'),
        username=os.getenv('ATLASSIAN_USERNAME'),
        password=os.getenv('ATLASSIAN_TOKEN'),
        api_version='cloud' if os.getenv('IS_IN_CLOUD') else 'latest',
        cloud=os.getenv('IS_IN_CLOUD')
    )

    spaces = confluence.get_all_spaces(start, limit)
    has_more = next in spaces['_links']
    result = Result(has_more)
    for space in spaces['results']:
        result.add(Space(space['name'], space['key']))

    click.secho(f'Start: {start}\tLimit: {limit}\tHas more: {result.has_more}', fg='green')
    for space in result.spaces:
        click.secho(space.output())
