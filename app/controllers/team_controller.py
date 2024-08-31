from app.repositories import TeamsRepository


class TeamController:
    def __init__(self):
        self.repository = TeamsRepository()

    def index(self, team_id):
        return self.repository.index(team_id)
