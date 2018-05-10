from stallion.extractors import BaseExtractor


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
