import argparse
import os

import dotenv
from atlassian import Confluence

from export_pdf.exporter import PdfExporter


def main(space_key: str):
    dotenv.load_dotenv()

    confluence = Confluence(
        url=os.getenv('ATLASSIAN_URL'),
        username=os.getenv('ATLASSIAN_USERNAME'),
        password=os.getenv('ATLASSIAN_TOKEN'),
        api_version='cloud' if os.getenv('IS_IN_CLOUD') else 'latest',
        cloud=os.getenv('IS_IN_CLOUD')
    )

    PdfExporter(confluence).export(space_key, os.getenv('CONF_EXPORT_DIR'))


def validate_space_key(space_key: str):
    if not isinstance(space_key, str):
        raise ValueError("The space_key parameter must be a string")
    if not space_key.strip():
        raise ValueError("The space_key parameter cannot be empty")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'space_key',
        type=str,
        help='Confluence space key (should be string)'
    )
    args = parser.parse_args()

    try:
        validate_space_key(args.space_key)
    except ValueError as e:
        print(f"Value error: {e}")
        parser.print_help()

    main(args.space_key)
