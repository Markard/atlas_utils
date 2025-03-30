import click
import dotenv

from export_pdf.cli_command import export_pdf
from get_space_keys.cli_command import get_space_keys


@click.group()
def entry_point():
    pass


entry_point.add_command(export_pdf)
entry_point.add_command(get_space_keys)

if __name__ == '__main__':
    dotenv.load_dotenv()
    entry_point()
