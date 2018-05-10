"""
Extract the content of the web page
"""

from stallion.version import version_info, __version__
from stallion.configuration import Configuration
from stallion.crawler import Crawler


class Stallion(object):
    """
    Main class
    """

    def __init__(self, config=None):
        self.config = config or Configuration()
        self.extend_config()

    def extend_config(self):
        if isinstance(self.config, dict):
            config = Configuration()
            for k, v in self.config.items():
                if hasattr(config, k):
                    setattr(config, k, v)
            self.config = config

    def extract(self, url=None):
        """
        Main method to extract an article object from a URL,
        pass in a url and get back a Article
        """
        try:
            cr = Crawler(self.config)
            article = cr.crawl(url)
        except Exception as e:
            print(e)
            return None
        return article

    def shutdown_network(self):
        pass
