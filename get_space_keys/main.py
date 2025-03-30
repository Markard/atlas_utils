import argparse
import os

import dotenv
from atlassian import Confluence


def main(start: int, limit: int):
    dotenv.load_dotenv()

    confluence = Confluence(
        url=os.getenv('ATLASSIAN_URL'),
        username=os.getenv('ATLASSIAN_USERNAME'),
        password=os.getenv('ATLASSIAN_TOKEN'),
        api_version='cloud' if os.getenv('IS_IN_CLOUD') else 'latest',
        cloud=os.getenv('IS_IN_CLOUD')
    )

    result = []
    spaces = confluence.get_all_spaces(start, limit)
    for space in spaces['results']:
        result.append({'name': space['name'], 'key': space['key']})

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

    spaces = main(args.start, args.limit)

    print(f'Start: {args.start}\tLimit: {args.limit}\n')
    print(f'-' * 10)
    for space in spaces:
        print(f'Name: {space['name']}')
        print(f'Key: {space['key']}')
        print(f'-' * 10)
