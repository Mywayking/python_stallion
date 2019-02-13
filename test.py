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
        # "http://www.unjs.com/Special/yubeidangyuan/",  # utf-8 utf-8 ['utf-8']
        # "http://api.mobile.meituan.com/appupdate/download/simple/waimai?channel=8103&scheme=https",
        # "http://www.wo99.net/",
        # "https://www.jikexueyuan.com/",
        # " https://m.toutiaocdn.cn/group/6592553741415612941/?iid=47687443492&app=news_article&timestamp=1540821841&group_id=6592553741415612941&tt_from=copy_link&utm_source=copy_link&utm_medium=t",
        # "https://finance.sina.com.cn/stock/jsy/2019-01-17/doc-ihqhqcis7016473.shtml",
        # "https://baike.baidu.com/item/HTTP%E7%8A%B6%E6%80%81%E7%A0%81/5053660?fr=aladdin",
        # "https://v.qq.com/x/cover/c949qjcugx9a7gh.html",
        # "http://auto.sina.com.cn/news/hy/2019-01-17/detail-ihqhqcis6939835.shtml",
        # "https://v.youku.com/v_show/id_XNzA3MDk4Mjg0.html",
        # "https://www.zhihu.com/appview/v2/answer/507901751",
        # "https://www.sohu.com/a/164810876_208076",
        # "http://www.sohu.com/a/200229311_220283",
        # "http://weitushe.com/xjmg/shot_spage_weitushe/get?tid=47354268",
        # "https://baijiahao.baidu.com/s?id=1623231191866727173&wfr=spider&for=pc",
        # "http://www.mm131.com/qingchun/4182.html",
        "http://www.mm131.com/chemo/",
    ]
    for url in url_list:
        article = extract(url=url, coding=True, is_summary=True)
        print(url)
        print(article.status)
        # 提取 title
        print("title", article.title)
        # 提取 h1
        print("h1", article.h1)
        # 提取 meta_keywords
        print("meta_keywords", article.meta_keywords)
        # 提取 meta_description
        print("meta_description", article.meta_description)
        # 提取网页的主要内容
        print('summary', article.summary)
        # 提取网页的整个页面内容
        print('content', article.content)


if __name__ == "__main__":
    spider_url()
