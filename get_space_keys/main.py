import argparse
import os

import dotenv
from atlassian import Confluence

from get_space_keys.entities.result import Result
from get_space_keys.entities.result import Space


def main(start: int, limit: int) -> Result:
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

    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='Get space keys',
        description='Returns list of space name and keys'
    )
    parser.add_argument(
        '-s', '--start',
        type=int,
        default=0,
        help='Start index'
    )
    parser.add_argument(
        '-l', '--limit',
        type=int,
        default=500,
        help='Limit output'
    )
    args = parser.parse_args()

    result = main(args.start, args.limit)

    print(f'Start: {args.start}\tLimit: {args.limit}\tHas more: {result.has_more}\n')
    print(f'-' * 10)
    for space in result.spaces:
        print(space.output())
