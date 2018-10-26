"""
-------------------------------------------------
   Author :       galen
   date：          2018/5/9
-------------------------------------------------
   Description:
-------------------------------------------------
"""
from stallions import Stallion
from urllib.parse import urljoin


def page_code():
    # GBK
    url_gbk = "http://sh.news.163.com/18/0814/12/DP5U749G04188CSJ.html"


def main():
    s = Stallion()
    # a = s.extract("https://www.rtbasia.com/")
    # a = s.extract("http://www.dytt8.net/")
    a = s.extract("https://www.163.com/")
    # a = s.extract("https://blog.csdn.net/skiof007/article/details/55195434")
    # a = s.extract("http://sh.news.163.com/18/0814/12/DP5U749G04188CSJ.html")
    # # print(a.content)
    print("title", a.title)
    print("h1", a.h1)
    print("meta_keywords", a.meta_keywords)
    print("meta_description", a.meta_description)
    print(a.content)
    # print(a.url_list)
    # for url in a.url_list:
    #     print(url)


def test_urljoin():
    url = "http://www.dytt8.net/"
    url_sun = "http://www.dytt8.net/html/gndy/rihan/index.html"
    print(urljoin(url, "/html/gndy/jddy/20180503/56783.html"))


def test_duplicate():
    a = [1, 2, 2, 2, 3, 4, 5, 6, 6, 6, 6]
    a = list(set(a))
    print(a)


if __name__ == "__main__":
    main()
