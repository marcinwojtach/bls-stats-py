from app.repositories import LeagueRepository


class HomeController:
    def __init__(self):
        self.league_repository = LeagueRepository()

    def index(self):
        return {
            'league_teams_1': self.league_repository.get_teams_for_league(1),
            'league_teams_2': self.league_repository.get_teams_for_league(2),
        }
