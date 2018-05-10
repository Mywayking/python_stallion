from stallion.extractors import BaseExtractor


class LinksExtractor(BaseExtractor):
    def extract(self):
        links = []
        # items = self.parser.getElementsByTag(self.article.top_node, 'a')
        # for i in items:
        #     attr = self.parser.getAttribute(i, 'href')
        #     if attr:
        #         links.append(attr)
        return links
