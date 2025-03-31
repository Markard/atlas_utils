import json
from datetime import datetime

from upload_worklogs.entity.log import create_from_raw_data
from upload_worklogs.repository.input_file import InputFile, Format


class JsonRepository:
    def __init__(self):
        self.__input_file = InputFile(Format.JSON)

    def load(self, day: datetime):
        filepath = self.__input_file.get_filepath(day)
        with open(filepath) as file:
            raw_data = json.load(file)
            return create_from_raw_data(raw_data, day)
