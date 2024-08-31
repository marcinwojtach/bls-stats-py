from app.services import SoupProvider, ScrapingHelper, HttpService


league_id_1 = 142
league_id_2 = 143


class LeagueRepository:
    @staticmethod
    def url():
        return 'https://blssiatkowka.ligspace.pl/index.php?mod=Teams&ac=Browse'

    def __init__(self):
        self.http = HttpService()

    def get_teams_for_league(self, league_no):
        """
        Returns collection of teams in league
        Args:
            league_no (int): 1 | 2
        """

        soup = SoupProvider.html_parser(self.__get_teams_html((league_id_2, league_id_1)[int(league_no) == 1]))
        table = soup.find('table', class_='t2 teams')
        teams = []

        for tr in table.find_all('tr'):
            tds = tr.find_all('td')
            if tds:
                href = tds[0].find('a').get('href')
                teams.append({'name': tds[0].text.strip(), 'id': ScrapingHelper.get_href_id(href, 't_id')})

        return teams

    def __get_teams_html(self, league_id):
        return self.http.post(LeagueRepository.url(), {
            'league': league_id,
            'season': 70,
            'selectSchedule': 'Zmień',
        })
