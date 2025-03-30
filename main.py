import click
import dotenv

from export_pdf.cli_command import export_pdf


@click.group()
def entry_point():
    pass


entry_point.add_command(export_pdf)

if __name__ == '__main__':
    dotenv.load_dotenv()
    entry_point()
