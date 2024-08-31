import requests


class HttpService:
    def get(self, url):
        response = requests.get(
            url,
            stream=False
        )

        if response.status_code == 200:
            return response.text
        else:
            return None

    def post(self, url, data):
        response = requests.post(
            url,
            headers={
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': '*/*',
            },
            data=data,
            stream=False,
        )

        if response.status_code == 200:
            return response.text
        else:
            return None
