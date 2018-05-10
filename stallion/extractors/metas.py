from stallion.extractors import BaseExtractor


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
