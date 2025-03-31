from datetime import datetime

from upload_worklogs.entity.log import Log
from upload_worklogs.repository.jira_repository import JiraRepository
from upload_worklogs.repository.yml_repository import YmlRepository


class Uploader:
    def __init__(self):
        self.__loader_from_file = YmlRepository()
        self.__provider = JiraRepository()

    def upload(self, day: datetime, flush: bool) -> list[Log]:
        logs_for_day = self.__loader_from_file.load(day)
        if not flush:
            return logs_for_day

        for log in logs_for_day:
            if log.is_worklog():
                id = self.__provider.issue_worklog(log)
                log.set_id(id)

        return logs_for_day
