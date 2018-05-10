import re


class OutputFormatter(object):
    @staticmethod
    def clean_content(content):
        """streamline \r\n\ space"""
        return re.sub('[\r\n\t ]+', ' ', content).replace('\xa0', '').strip()


class StandardOutputFormatter(OutputFormatter):
    pass
