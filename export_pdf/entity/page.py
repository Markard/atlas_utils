import os
import re

from typing import Optional


def sanitize_filename(name: str) -> str:
    return re.sub(r'[\\/*?:"<>|]', '_', name).strip()


class Page:
    id: str
    title: str
    path: str = ''

    def __init__(self, id: str, title: str, ancestors: Optional[list[str]] = None):
        self.id = id
        self.title = sanitize_filename(title)
        if ancestors:
            self.path = os.path.join('', *[sanitize_filename(a) for a in ancestors])
