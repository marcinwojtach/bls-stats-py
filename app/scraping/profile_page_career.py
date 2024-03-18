from bs4 import BeautifulSoup


from app.services.soup_provider import SoupProvider
from app.shared import state


class ProfilePageCareer:
    def __init__(self, career_html_text: str):
        self.career_html_text: str = career_html_text
        self.career_soup: BeautifulSoup = SoupProvider.html_parser(career_html_text)
        self.headers = state['headers']

    def call(self):
        career_stats =  self.__get_career_stats()
        return {
            'career_details': self.__get_career_details(career_stats)
        }

    def __get_career_stats(self) -> list[float]:
        table_soup = self.career_soup.find('table', class_='teamsstats')
        stats: list[float] = []
        tds_rows = table_soup.find_all('tr')

        for tr in tds_rows:
            # TODO: can't access by index, wonder why..
            stat_tds = tr.find_all('td', limit=2)
            for index, stat in enumerate(stat_tds, start=0):
                if index == 1:
                    stats.append(float(stat.text.replace(',', '.')))

        return stats

    def __get_career_details(self, stats):
        details_list = []
        labels = self.headers.labels()

        for index, value in enumerate(stats, start=0):
            details_list.append({'label': labels[index], 'value': value})

        return details_list
