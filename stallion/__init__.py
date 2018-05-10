"""
Extract the content of the web page
"""

from stallion.crawler import Crawler


class Stallion(object):
    """
    Main class
    """

    def __init__(self, enable_urls=False):
        self.enable_urls = enable_urls

    def extract(self, url=None):
        """
        Main method to extract an article object from a URL,
        pass in a url and get back a Article
        """
        cr = Crawler(self.enable_urls)
        try:
            article = cr.crawl(url)
        except Exception as e:
            print(e)
            return cr.article
        return article

    def shutdown_network(self):
        pass
