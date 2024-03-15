from app.shared import state


class Player:
    def __init__(self, id, full_name, position):
        self.id = id
        self.full_name = full_name
        self.position = position
        self.headers = state['headers']

    def details(self):
        details_list = []
        labels = self.headers.labels()

        # for index, value in enumerate(stats, start=0):
        #     details_list.append({'label': labels[index], 'value': value})

        return details_list
