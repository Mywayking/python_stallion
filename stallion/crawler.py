from stallion.article import Article
from stallion.extractors import TitleExtractor, H1Extractor, ContentExtractor, MetasExtractor
from stallion.outputformat import OutputFormatter

from stallion.network import HtmlFetcher
from lxml.html.clean import Cleaner
from stallion.parsers import Parser

get_parser = Parser()

cleaner = Cleaner(meta=False, page_structure=False, safe_attrs_only=False)


class Crawler(object):
    def __init__(self):
        # config
        # parser
        self.parser = get_parser
        # article
        self.article = Article()

        # metas extractor
        self.metas_extractor = self.get_metas_extractor()

        # title extractor
        self.title_extractor = self.get_title_extractor()

        # h1 extractor
        self.h1_extractor = self.get_h1_extractor()

        # content extractor
        self.content_extractor = self.get_content_extractor()

        # html fetcher
        self.html_fetcher = HtmlFetcher()

    def crawl(self, url):
        raw_html = self.html_fetcher.get_html(url)
        if raw_html is None:
            return self.article
        # filter js script
        raw_html = cleaner.clean_html(raw_html)
        doc = self.parser.raw_to_document(raw_html)
        self.article.raw_html = raw_html
        self.article.doc = doc
        metas = self.metas_extractor.extract()
        self.article.meta_description = OutputFormatter.clean_content(metas['description'])
        self.article.meta_keywords = OutputFormatter.clean_content(metas['keywords'])
        self.article.title = OutputFormatter.clean_content(self.title_extractor.extract())
        self.article.h1 = OutputFormatter.clean_content(self.h1_extractor.extract())
        self.article.content = OutputFormatter.clean_content(self.content_extractor.extract())

        return self.article

    def get_metas_extractor(self):
        return MetasExtractor(self.parser, self.article)

    def get_title_extractor(self):
        return TitleExtractor(self.parser, self.article)

    def get_h1_extractor(self):
        return H1Extractor(self.parser, self.article)

    def get_content_extractor(self):
        return ContentExtractor(self.parser, self.article)
