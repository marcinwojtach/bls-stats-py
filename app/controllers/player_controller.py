import base64
from app.repositories import PlayerRepository
from app.services import PlayerHighestScores, FileHelper


class PlayerController:
    def __init__(self, player_id):
        self.player_id = player_id
        self._repository = PlayerRepository(player_id)
        self._highest_scores_service = PlayerHighestScores()

    def index(self):
        return {
            'player': self._repository.get_player(),
            'latest_stats': self._repository.get_latest_stats(),
            'all_seasons_stats': self._repository.get_all_seasons_stats(),
        }

    def highest_scores_chart_base64(self):
        all_time_stats = self._repository.get_all_time_best_stats()
        latest_match_stats = self._repository.get_latest_stats()[0]['details']
        buffer = FileHelper.create_buffer(self._highest_scores_service.get_chart(all_time_stats, latest_match_stats))
        return base64.b64encode(buffer.getvalue()).decode('utf-8')


