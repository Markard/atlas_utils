from get_space_keys.entities.space import Space


class Result:
    spaces: list[Space] = []
    has_more: bool

    def __init__(self, has_more: bool):
        self.has_more = has_more

    def add(self, space: Space):
        self.spaces.append(space)
