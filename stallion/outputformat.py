import re


class OutputFormatter(object):
    @staticmethod
    def clean_content(content):
        """streamline \r\n\ space"""
        return re.sub('[\r\n\t ]+', ' ', content)


class StandardOutputFormatter(OutputFormatter):
    pass
