class BaseExtractor(object):
    def __init__(self, parser, article):
        # parser
        self.parser = parser

        # article
        self.article = article

        # stopwords class
        # self.stopwords_class = stopwords_classconfig.
