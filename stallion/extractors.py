"""
-------------------------------------------------
   Author :       galen
   date：          2018/5/10
-------------------------------------------------
   Description:
-------------------------------------------------
"""


class BaseExtractor(object):
    def __init__(self, parser, article):
        # parser
        self.parser = parser

        # article
        self.article = article


class TitleExtractor(BaseExtractor):
    def get_title(self):
        """
        Fetch the article title and analyze it
        """
        command = '//title/text()'
        content = self.parser.xpathSelect(self.article.doc, command)
        if content is not None and len(content) > 0:
            return content[0].strip()
        return ''

    def extract(self):
        return self.get_title()


class MetasExtractor(BaseExtractor):
    def get_meta_content(self, meta_name):
        """\
        Extract a given meta content form document
        """
        command = '//meta[translate(@name,"ABCDEFGHJIKLMNOPQRSTUVWXYZ",abcdefghjiklmnopqrstuvwxyz)="{0}"]/@content'.format(
            meta_name)
        content = self.parser.xpathSelect(self.article.doc, command)
        if content is not None and len(content) > 0:
            return content[0].strip()
        return ''

    def get_meta_description(self):
        """
        if the article has meta description set in the source, use that
        """
        return self.get_meta_content("description")

    def get_meta_keywords(self):
        """
        if the article has meta keywords set in the source, use that
        """
        return self.get_meta_content("keywords")

    def extract(self):
        return {
            "description": self.get_meta_description(),
            "keywords": self.get_meta_keywords(),
        }


class H1Extractor(BaseExtractor):
    def get_h1(self):
        """
        Fetch the article title and analyze it
        """
        command = '//h1/text()'
        content = self.parser.xpathSelect(self.article.doc, command)
        if content is not None and len(content) > 0:
            return content[0].strip()
        return ''

    def extract(self):
        return self.get_h1()


class ContentExtractor(BaseExtractor):
    def get_content(self):
        """
        Fetch the article title and analyze it
        """
        command = 'string()'
        content = self.parser.xpathSelect(self.article.doc, command)
        if content is not None and len(content) > 0:
            return content.strip()
        return ''

    def extract(self):
        return self.get_content()
