from bs4 import BeautifulSoup


from app.models.player import Player
from app.services.soup_provider import SoupProvider


class PlayersPage:
    def __init__(self, html_text: str):
        self.html_text: str = html_text
        self.soup: BeautifulSoup = SoupProvider.html_parser(html_text)