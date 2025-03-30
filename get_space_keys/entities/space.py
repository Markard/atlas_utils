class Space:
    name: str
    key: str

    def __init__(self, name: str, key: str):
        self.name = name
        self.key = key

    def output(self):
        return f'Name: {self.name}\nKey: {self.key}\n' + '-' * 10
