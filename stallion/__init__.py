"""
Extract the content of the web page
"""

from stallion.crawler import Crawler


class Stallion(object):
    """
    Main class
    """

    @staticmethod
    def extract(url=None):
        """
        Main method to extract an article object from a URL,
        pass in a url and get back a Article
        """
        cr = Crawler()
        article = cr.crawl(url)
        # try:
        #     cr = Crawler()
        #     article = cr.crawl(url)
        # except Exception as e:
        #     print(e)
        #     return None
        return article

    def shutdown_network(self):
        pass
