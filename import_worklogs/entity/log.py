from datetime import datetime

WORK: str = 'work'


class Log:
    def __init__(
            self,
            started_at: datetime,
            ended_at: datetime,
            comment: str,
            issue_key: str | None,
            tags: list[str]
    ):
        self.started_at = started_at
        self.ended_at = ended_at
        self.comment = comment
        self.issue_key = issue_key
        self.tags = tags
        self.id = None

    def get_started_at(self) -> str:
        return self.started_at.strftime('%Y-%m-%dT%H:%M:%S.000%z')

    def get_time_sec(self) -> int:
        return int((self.ended_at - self.started_at).total_seconds())

    def is_worklog(self) -> bool:
        return WORK in self.tags

    def get_report(self) -> str:
        return '{0:{time_f}} - {1:{time_f}} ({2:<6}) | {3:<45} | {4:<5} | [{5}]'.format(
            self.started_at,
            self.ended_at,
            self.get_time_sec(),
            (self.comment[:40] + '...') if len(self.comment) > 40 else self.comment,
            self.issue_key if self.issue_key else 'None',
            ', '.join(self.tags),
            time_f='%H:%M'
        )

    def set_id(self, id: int):
        self.id = id


def create_from_raw_data(raw_data: list[dict], day: datetime) -> list[Log]:
    logs_for_day = []
    for raw_log in raw_data:
        s_time = datetime.strptime(raw_log['started_at'], '%H:%M')
        e_time = datetime.strptime(raw_log['ended_at'], '%H:%M')

        log = Log(
            day.replace(hour=s_time.hour, minute=s_time.minute),
            day.replace(hour=e_time.hour, minute=e_time.minute),
            raw_log['comment'],
            raw_log['issue_key'] if 'issue_key' in raw_log else None,
            raw_log['tags'] if 'tags' in raw_log else []
        )
        logs_for_day.append(log)

    return logs_for_day
