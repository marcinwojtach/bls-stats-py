from bs4 import BeautifulSoup


class SoupProvider:
    @staticmethod
    def html_parser(html_text):
        return BeautifulSoup(html_text, 'html.parser')
