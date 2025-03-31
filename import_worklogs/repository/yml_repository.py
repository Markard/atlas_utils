from yaml import load, dump
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
        logs_for_day = []
        filepath = self.__input_file.get_filepath(day)
        with open(filepath) as file:
            raw_data = load(file, Loader)
            for raw_log in raw_data:
                log = create_from_raw_data(raw_log, day)
                logs_for_day.append(log)

        return logs_for_day



