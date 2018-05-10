import re


class OutputFormatter(object):
    @staticmethod
    def clean_content(content):
        """streamline space and \r\n\ """
        return re.sub('[\r\n\t ]+', ' ', content)


class StandardOutputFormatter(OutputFormatter):
    pass
