import json


class JsonProvider:
    def __init__(self, path):
        self.file_path = path
        self.file = open(path)

    def as_dict(self):
        data = {}

        try:
            data = json.load(self.file)
        except FileNotFoundError:
            print('Failed to load file from path: ' + self.file_path)

        return data
