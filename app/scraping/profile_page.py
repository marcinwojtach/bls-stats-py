from bs4 import BeautifulSoup


from app.models.player import Player
from app.services.soup_provider import SoupProvider
from app.shared import state


class ProfilePage:
    def __init__(self, profile_id: int, information_html_text: str, career_html_text: str):
        self.profile_id = profile_id
        self.information_html_text: str = information_html_text
        self.career_html_text: str = career_html_text
        self.information_soup: BeautifulSoup = SoupProvider.html_parser(information_html_text)
        self.career_soup: BeautifulSoup = SoupProvider.html_parser(career_html_text)
        self.headers = state['headers']

    def call(self):
        season_stats =  self.__get_season_stats()
        career_stats =  self.__get_career_stats()
        return {
            'player': self.__get_player(),
            'season_details': self.__get_season_details(season_stats),
            'career_details': self.__get_career_details(career_stats)
        }

    def __get_season_stats(self) -> list[float]:
        table_soup = self.information_soup.find('table', class_='t2')
        stats: list[float] = []
        tds_list = table_soup.find_all('td')

        for td in tds_list:
            stats.append(float(td.text.replace(',', '.')))

        return stats

    def __get_career_stats(self) -> list[float]:
        table_soup = self.career_soup.find('table', class_='teamsstats')
        stats: list[float] = []
        tds_rows = table_soup.find_all('tr')

        for tr in tds_rows:
            # TODO: can't access by index, wonder why..
            stat_tds = tr.find_all('td', limit=2)
            for index, stat in enumerate(stat_tds, start=0):
                if index is 1:
                    stats.append(float(stat.text.replace(',', '.')))

        return stats

    def __get_player(self) -> Player:
        profile_lead = self.information_soup.find('div', class_='profile-lead')
        profile_meta = self.information_soup.find('div', class_='aside')
        position = profile_meta.find_all('td')[3].text
        name = profile_lead.find('h2').text
        return Player(self.profile_id, name, position)

    def __get_season_details(self, stats):
        details_list = []
        labels = self.headers.labels()

        for index, value in enumerate(stats, start=0):
            details_list.append({'label': labels[index], 'value': value})

        return details_list

    def __get_career_details(self, stats):
        details_list = []
        labels = self.headers.labels()

        for index, value in enumerate(stats, start=0):
            details_list.append({'label': labels[index], 'value': value})

        return details_list
