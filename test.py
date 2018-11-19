"""
-------------------------------------------------
   Author :       galen
   date：          2018/5/9
-------------------------------------------------
   Description:
-------------------------------------------------
"""
from stallions import Stallion, extract
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


def spider_url():
    """
    """
    url_list = [
        # "http://www.liuxiaoer.com/lh/29192_2.html",  # ISO-8859-1 UTF-8-SIG []
        # "https://www.iqiyi.com/v_19rrjepf9k.html",  # UTF-8 utf-8 ['utf-8']
        # "http://so.sccnn.com/search/%E8%83%8C%E6%99%AF/29.html",  # ISO-8859-1 ISO-8859-1 ['Gb2312']
        # "https://www.diyifanwen.com/tool/xingshiduilian/1132716293727642.htm",  # ISO-8859-1 GB2312 ['gb2312']
        # "http://fun.youth.cn/gnzx/201811/t20181101_11770610_3.htm",  # ISO-8859-1 Windows-1254 ['UTF-8']
        # "http://www.64365.com/ask/5366780.aspx", #utf-8 utf-8 ['utf-8']
        # "http://www.kanshuge.la/",  # utf-8 utf-8 ['utf-8']
        # "http://www.xbiquge.cc/book/15048/10632298.html&rx=0&eae=0&fc=656&docm=11&brdim=0,86,-8,-8,1366,,1382,744,1366,642&vis=1&rsz=",  # utf-8 utf-8 ['utf-8']
        # "http://gooyooo.cn/default.php",  # utf-8 utf-8 ['utf-8'] # 动态加载页面
        # "http://mini2.eastday.com/",  # utf-8 utf-8 ['utf-8']
        # "http://www.shuaijiao.com/",  # utf-8 utf-8 ['utf-8']
        # "http://wx.xiaoziling.xyz/",  # utf-8 utf-8 ['utf-8']
        # "http://www.zshonghai.com.cn/",  # utf-8 utf-8 ['utf-8']
        "https://www.sogou.com/link?url=TdXYaTdl0k6lQf0X3CwABpXSWeLyrmojVc4H97C172o.&rx=0&eae=0&fc=1936&brdim=0,109,0,109,1920,0,1920,911,1920,911&vis=1&rsz=d||eE|&abl=CS&ppjl=f&pfx=0&fu=8&bc=13&ifi=1&uci=1.ud8sh1wu23z3&xpc=fljDE0SUi6&p=http://www.unjs.com&dtd=159",  # utf-8 utf-8 ['utf-8']
    ]
    for url in url_list:
        article = extract(url=url, coding=True)
        print(url)
        # 提取 title
        print("title", article.title)
        # 提取 h1
        print("h1", article.h1)
        # 提取 meta_keywords
        print("meta_keywords", article.meta_keywords)
        # 提取 meta_description
        print("meta_description", article.meta_description)
        # 提取网页的整个页面内容
        # print(article.content)


if __name__ == "__main__":
    spider_url()
