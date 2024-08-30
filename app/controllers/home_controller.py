import requests
from app.services import SoupProvider


class HomeController:
    @staticmethod
    def url(team_id):
        return requests.get(
            'https://blssiatkowka.ligspace.pl/index.php?mod=Teams&ac=ShowPlayersStats&t_id=' + str(team_id),
            stream=False
        )

    def __init__(self, team_id):
        self.html = HomeController.url(team_id).text
        self.soup = SoupProvider.html_parser(self.html)

    def index(self):
        main_table = self.soup.find('table', class_='t2')
        player_names_cells = main_table.find_all('td', class_='align-left')

        players = []
        for cell in player_names_cells:
            players.append({'name': cell.text, 'id': self._extract_player_id(cell.find('a', href=True)['href'])})

        team_name = self.soup.find('div', class_='profile-lead').find('h2').text
        season = self.soup.find('div', class_='selectcombo').find('ul').findAll('li')[1:2][0].find('label').text

        return {
            'team_name': team_name,
            'players': players,
            'season': season,
        }

    def _extract_player_id(self, text):
        return text.split('lp_id')[1].split('=')[1]
