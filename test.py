"""
-------------------------------------------------
   Author :       galen
   date：          2018/5/9
-------------------------------------------------
   Description:
-------------------------------------------------
"""
from stallion import Stallion
from urllib.parse import urljoin


def main():
    s = Stallion(enable_urls=False)
    # a = s.extract("https://www.rtbasia.com/")
    a = s.extract("http://www.dytt8.net/")
    # print(a.content)
    print(a.title)
    print(a.h1)
    print(a.meta_keywords)
    print(a.meta_description)
    # print(a.url_list)
    for url in a.url_list:
        print(url)


def test_urljoin():
    url = "http://www.dytt8.net/"
    url_sun = "http://www.dytt8.net/html/gndy/rihan/index.html"
    print(urljoin(url, "/html/gndy/jddy/20180503/56783.html"))


if __name__ == "__main__":
    main()
