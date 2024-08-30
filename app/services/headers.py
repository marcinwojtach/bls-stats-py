from app.services.json_provider import JsonProvider


class Headers:
    def __init__(self):
        self.columns = JsonProvider('app/data/columns.json').as_dict()

    def all(self):
        return self.columns

    def labels(self):
        labels = []
        for value in self.columns.values():
            labels.append(value['label'])
        return labels

    def keys(self):
        return self.columns.keys()
