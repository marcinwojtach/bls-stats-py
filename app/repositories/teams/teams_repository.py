from app.services import SoupProvider, ScrapingHelper, HttpService


class TeamsRepository:
    @staticmethod
    def team_url(team_id):
        return 'https://blssiatkowka.ligspace.pl/index.php?mod=Teams&ac=ShowPlayersStats&t_id=' + str(team_id)

    def __init__(self):
        self.http = HttpService()

    def index(self, team_id):
        soup = SoupProvider.html_parser(self.__get_team_html(team_id))
        main_table = soup.find('table', class_='t2')
        player_names_cells = main_table.find_all('td', class_='align-left')
        players = []

        for cell in player_names_cells:
            players.append({'name': cell.text, 'id': ScrapingHelper.get_href_id(cell.find('a', href=True)['href'], 'lp_id')})

        team_name = soup.find('div', class_='profile-lead').find('h2').text
        season = soup.find('div', class_='selectcombo').find('ul').findAll('li')[1:2][0].find('label').text

        return {
            'team_name': team_name,
            'players': players,
            'season': season,
        }

    def __get_team_html(self, team_id):
        return self.http.get(TeamsRepository.team_url(team_id))
