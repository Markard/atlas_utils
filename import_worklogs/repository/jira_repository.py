import os

from atlassian import Jira

from import_worklogs.entity.log import Log


class JiraRepository:
    def __init__(self):
        self.__jira = Jira(
            url=os.getenv('ATLASSIAN_URL'),
            username=os.getenv('ATLASSIAN_USERNAME'),
            password=os.getenv('ATLASSIAN_TOKEN'),
            api_version='latest',
            cloud=os.getenv('IS_IN_CLOUD')
        )

    def issue_worklog(self, log: Log) -> int:
        result = self.__jira.issue_worklog(log.issue_key, log.get_started_at(), log.get_time_sec(), log.comment)
        return result['id']
