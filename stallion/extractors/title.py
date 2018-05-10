from stallion.extractors import BaseExtractor


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
