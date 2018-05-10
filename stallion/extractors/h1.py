from stallion.extractors import BaseExtractor


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
