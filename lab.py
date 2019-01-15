# -*- coding: utf-8 -*-#
"""
@author:Galen
@file: lab.py
@time: 2019/01/11
@description:
https://github.com/Mywayking/python-readability
"""

import requests
from readability import Document
import html2text
from stallions import Stallion, extract


def clean_html():
    s = Stallion()
    # a = s.extract("https://www.rtbasia.com/")
    # a = s.extract("http://www.dytt8.net/")
    a = s.extract("http://v.pptv.com/show/fbGeHITqWpj7eeE.html")
    # response = requests.get('http://lady.163.com/19/0111/10/E57V9GIV00267VA9.html')
    # response = requests.get('http://www.rtbchina.com/')
    # response = requests.get('http://guba.eastmoney.com/news,000611,173895506.html')
    doc = Document(a.raw_html)
    # doc = Document(response.text)
    # print(doc.content())
    print(doc.short_title())
    # print(doc.title())
    # print(doc.summary())
    h = html2text.HTML2Text()
    h.ignore_links = True
    print(h.handle(doc.summary()))


if __name__ == "__main__":
    clean_html()
