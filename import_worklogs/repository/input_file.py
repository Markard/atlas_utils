import os
from datetime import datetime
from enum import Enum


class Format(Enum):
    JSON: str = 'json'
    YML: str = 'yml'


class InputFile:
    def __init__(self, format: Format):
        self.__format = format.value
        self.__log_folder_entry = os.getenv('LOG_FOLDER_ENTRY')
        if not os.path.exists(self.__log_folder_entry):
            raise NotADirectoryError(f'{self.__log_folder_entry} - check variable LOG_FOLDER_ENTRY in .env.')

    def get_filepath(self, date: datetime):
        filepath = os.path.join(
            self.__log_folder_entry,
            str(date.year),
            str(date.month),
            f'{date.day}.{self.__format}'
        )
        if not os.path.exists(filepath):
            raise FileNotFoundError(filepath)

        return filepath
