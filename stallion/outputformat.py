import re


class OutputFormatter(object):
    @staticmethod
    def clean_content(content):
        """精简空格，剔除非中文字符"""
        # content = ''.join(content)
        # 去除\r\n\t字符
        content = re.sub('[\r\n\t]', '', content)
        # 剔除中文
        return re.sub(' +', ' ', content)


class StandardOutputFormatter(OutputFormatter):
    pass
