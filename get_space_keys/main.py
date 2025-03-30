import os

import dotenv
from atlassian import Confluence


def main():
    dotenv.load_dotenv()

    confluence = Confluence(
        url=os.getenv('ATLASSIAN_URL'),
        username=os.getenv('ATLASSIAN_USERNAME'),
        password=os.getenv('ATLASSIAN_TOKEN'),
        api_version='cloud' if os.getenv('IS_IN_CLOUD') else 'latest',
        cloud=os.getenv('IS_IN_CLOUD')
    )

    result = []
    for space in confluence.get_all_spaces()['results']:
        result.append({'name': space['name'], 'key': space['key']})

    return result


if __name__ == '__main__':
    spaces = main()
    for space in spaces:
        print(f'Name: {space['name']}')
        print(f'Key: {space['key']}')
        print(f'-' * 10)
