import requests


class BlsPageHttp:
    @staticmethod
    def get_profile_information(user_id: int):
        return requests.get(
            'https://blssiatkowka.ligspace.pl/index.php?mod=Players&ac=Profile&lp_id=' + str(user_id),
            stream=False
        )

    def get_profile_career(user_id: int):
        return requests.get(
            'https://blssiatkowka.ligspace.pl/index.php?mod=Players&ac=Records&lp_id=' + str(user_id),
            stream=False
        )

    @staticmethod
    def get_team_players(team_id: int):
        return requests.get(
            'https://blssiatkowka.ligspace.pl/index.php?mod=Teams&ac=TeamPlayers&t_id=' + str(team_id),
            stream=False
        )
