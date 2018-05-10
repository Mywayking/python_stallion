import requests
import random


class HtmlFetcher(object):
    def __init__(self, config):
        self.config = config
        # set header
        self.headers = {'User-agent': random.choice(self.config.browser_user_agent)}

    def get_html(self, url):
        # do request
        try:
            response = requests.get(
                url,
                headers=self.headers, timeout=self.config.http_timeout)
            response.encoding = response.apparent_encoding
            response.keep_alive = False
            html = response.text
        except Exception as e:
            print(e)
            html = None
        # read the result content
        if html is not None:
            return html
        return None
