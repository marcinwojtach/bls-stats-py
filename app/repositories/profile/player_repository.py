import requests
from app.services import SoupProvider
from app.models import Player
from app.shared import state


class PlayerRepository:
    @staticmethod
    def player_profile_url(player_id):
        return requests.get(
            'https://blssiatkowka.ligspace.pl/index.php?mod=Players&ac=Profile&lp_id=' + str(player_id),
            stream=False
        )

    @staticmethod
    def player_stats_url(player_id):
        return requests.get(
            'https://blssiatkowka.ligspace.pl/index.php?mod=Players&ac=Stats&lp_id=' + str(player_id),
            stream=False
        )

    @staticmethod
    def player_all_time_best_url(player_id):
        return requests.get(
            'https://blssiatkowka.ligspace.pl/index.php?mod=Players&ac=Records&lp_id=' + str(player_id),
            stream=False
        )

    def __init__(self, player_id):
        self.player_id = player_id
        self.headers = state['headers']
        self.player_html = ''
        self.seasons_html = ''
        self.highest_scores_html = ''

    def get_player(self):
        soup = SoupProvider.html_parser(self.__get_player_html())
        profile_lead = soup.find('div', class_='profile-lead')
        profile_meta = soup.find('div', class_='aside')
        if not profile_lead or not profile_meta:
            return None
        position = profile_meta.find_all('td')[3].text
        name = profile_lead.find('h2').text
        return Player(self.player_id, name, position)

    def get_latest_stats(self):
        stats = []
        soup = SoupProvider.html_parser(self.__get_player_html())
        table = soup.find('table', class_='t2')
        trs = table.find_all('tr')
        for tr in trs:
            tds = tr.find_all('td')
            if tds:
                match_title = tds[0].text
                stats.append({'title': match_title.split(')')[0] + ')', 'date': match_title.split(')')[1], 'details': self.__get_row_stats(tds[1:])})

        return stats

    def get_all_seasons_stats(self):
        stats = []
        soup = SoupProvider.html_parser(self.__get_all_seasons_stats_html())
        table = soup.find('table', class_='t2')
        trs = table.find_all('tr')
        for tr in trs[2:]:
            tds = tr.find_all('td')
            if tds:
                matches_played = tds[1].text
                season_title_text = tds[0].text

                if season_title_text == 'Razem':
                    season_title = season_title_text
                    details = self.__get_row_stats(tds[2:])
                else:
                    season_title = season_title_text.split('(')[1].split(')')[0]
                    details = self.__get_row_stats(tds[1:])

                stats.append({'title': season_title, 'played': matches_played, 'details': details})

        return stats

    def get_all_time_best_stats(self):
        stats = []
        soup = SoupProvider.html_parser(self.__get_all_times_best_html())
        table = soup.find('table', class_='teamsstats')
        trs = table.find_all('tr')
        for tr in trs[1:]:
            tds = tr.find_all('td')
            title_text = tds[0].text
            score = self.__parse_text_to_float(tds[1].text)
            stats.append({'label': title_text, 'value': score})
        return stats

    def __get_row_stats(self, tds):
        labels = self.headers.labels()
        stats_values = [self.__parse_text_to_float(td.text) for td in tds]
        stats_per_row = []
        for index, value in enumerate(stats_values, start=0):
            try:
                stats_per_row.append({'label': labels[index], 'value': value})
            except IndexError:
                print('Something went wrong while assigning correct value key pairs')

        return stats_per_row

    def __parse_text_to_float(self, text):
        value = text.strip()
        if value:
            try:
                if value == '-':
                    return 0.0
                else:
                    return float(value.replace(',', '.'))
            except ValueError:
                print('Something went wrong while parsing values: ', value)

    def __get_player_html(self):
        if self.player_html:
            return self.player_html
        else:
            self.player_html = PlayerRepository.player_profile_url(self.player_id).text
            return self.player_html

    def __get_all_seasons_stats_html(self):
        if self.seasons_html:
            return self.seasons_html
        else:
            self.seasons_html = PlayerRepository.player_stats_url(self.player_id).text
            return self.seasons_html

    def __get_all_times_best_html(self):
        if self.highest_scores_html:
            return self.highest_scores_html
        else:
            self.highest_scores_html = PlayerRepository.player_all_time_best_url(self.player_id).text
            return self.highest_scores_html
