import base64
from app.repositories import PlayerRepository
from app.services import PlayerHighestScores, FileHelper
from app.shared import state


class PlayerController:
    @staticmethod
    def serialize_params(params_dict):
        params = []
        for key, value in params_dict.items():
            if value is not None and value == 'on':
                params.append(key)
        return params

    def __init__(self, player_id):
        self.player_id = player_id
        self._repository = PlayerRepository(player_id)
        self._highest_scores_service = PlayerHighestScores()
        self.headers = state['headers']

    def index(self):
        return {
            'player': self._repository.get_player(),
            'latest_stats': self._repository.get_latest_stats(),
            'all_seasons_stats': self._repository.get_all_seasons_stats(),
            'form_options': self.headers.labels()
        }

    def highest_scores_chart_base64(self, params):
        all_time_stats = self._repository.get_all_time_best_stats()
        latest_match_stats = self._repository.get_latest_stats()[0]['details']
        buffer = FileHelper.create_buffer(self._highest_scores_service.get_chart(all_time_stats, latest_match_stats, params))
        return base64.b64encode(buffer.getvalue()).decode('utf-8')
