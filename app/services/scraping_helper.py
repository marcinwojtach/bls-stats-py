class ScrapingHelper:
    @staticmethod
    def get_href_id(href_text, id):
        return href_text.split(id)[1].split('=')[1]
