from yaml import load

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from datetime import datetime

from import_worklogs.entity.log import create_from_raw_data
from import_worklogs.repository.input_file import InputFile, Format


class YmlRepository:
    def __init__(self):
        self.__input_file = InputFile(Format.YML)

    def load(self, day: datetime):
        filepath = self.__input_file.get_filepath(day)
        with open(filepath) as file:
            raw_data = load(file, Loader)
            return create_from_raw_data(raw_data, day)
