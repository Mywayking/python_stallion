class Article(object):
    def __init__(self):
        self.meta_description = ""
        self.meta_keywords = ""
        self.title = ""
        self.h1 = ""
        self.content = ""

    @property
    def infos(self):
        data = {
            "meta_description": self.meta_description,
            "meta_keywords": self.meta_keywords,
            "title": self.title,
            "h1": self.h1,
            "content": self.content,
        }
        return data
