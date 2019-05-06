# -*- coding: utf-8 -*-#
"""
@author:Galen
@file: stallion.py
@time: 2019/05/06
@description:
爬虫
url => 文字和图片

环境要求
```
pillow
tldextract
fake-useragent
readability-lxml
```
"""
import base64
import hashlib
import os
import random
import re
import shutil
from io import BytesIO
from urllib.parse import urljoin

import requests
import tldextract
from PIL import Image
from fake_useragent import UserAgent
from lxml import etree
from readability import Document

# fake ua
ua = UserAgent()
ua_default = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36"

MOBILE_USER_AGENT = [
    # # phone
    "Mozilla/5.0 (Linux; Android 8.1.0; ALP-AL00 Build/HUAWEIALP-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.36 T7/10.13 baiduboxapp/10.13.0.11 (Baidu; P1 8.1.0)",
    "Mozilla/5.0 (Linux; Android 8.1; EML-AL00 Build/HUAWEIEML-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.143 Crosswalk/24.53.595.0 XWEB/358 MMWEBSDK/23 Mobile Safari/537.36 MicroMessenger/6.7.2.1340(0x2607023A) NetType/4G Language/zh_CN",
    "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.9.4.974 UWS/2.13.1.48 Mobile Safari/537.36 AliApp(DingTalk/4.5.11)",
]
HTTP_DEFAULT_TIMEOUT = 4
IMAGE_TMP_SAVE = '/tmp'


class Article:
    def __init__(self, org_url):
        # 基础属性
        self.org_url = org_url
        # 页面属性
        self.status = 0
        self.meta_description = ""
        self.meta_keywords = ""
        self.title = ""
        self.h1 = ""
        self.content = ""
        # 文章主要内容提取
        self.summary = ""
        self.raw_html = ""
        # 图片
        self.img_list = []
        self.img_dir = None

        # the lxml Document object
        self.doc = None

    @property
    def info(self):
        data = {
            "meta_description": self.meta_description,
            "meta_keywords": self.meta_keywords,
            "title": self.title,
            "h1": self.h1,
            "content": self.content,
            "img_dir": self.img_dir
        }
        return data


# 删除标签 <!--done-->  style script
def delete_tags(html_raw, tags):
    html_list = html_raw.split("<{0}".format(tags))
    fresh_html = ""
    if html_raw.startswith("<{0}".format(tags)):
        for i, htm in enumerate(html_list):
            if "</{0}>".format(tags) not in htm:
                continue
            fresh_html += htm.split("</{0}>".format(tags))[-1]
    else:
        for i, htm in enumerate(html_list):
            if i == 0:
                fresh_html += htm
                continue
            if "</{0}>".format(tags) not in htm:
                continue
            fresh_html += htm.split("</{0}>".format(tags))[-1]
    return fresh_html


def delete_notes(html_raw):
    # delete note
    html_list = html_raw.split("<!--")
    fresh_html = ""
    if html_raw.startswith("<!--"):
        for i, htm in enumerate(html_list):
            if "-->" not in htm:
                continue
            fresh_html += htm.split("-->")[-1]
    else:
        for i, htm in enumerate(html_list):
            if i == 0:
                fresh_html += htm
                continue
            if "-->" not in htm:
                continue
            fresh_html += htm.split("-->")[-1]
    return fresh_html


def delete_all_tag(html_raw):
    # <!--done-->  style script
    html_raw = delete_notes(html_raw)
    html_raw = delete_tags(html_raw, "STYLE")
    html_raw = delete_tags(html_raw, "SCRIPT")
    html_raw = delete_tags(html_raw, "style")
    return delete_tags(html_raw, "script")


# os 操作
def get_md5(data_str):
    # 字符串转 md5
    if isinstance(data_str, str):
        data_str = data_str.encode("utf-8")
    m = hashlib.md5()
    m.update(data_str)
    return m.hexdigest()


def get_domain(url):
    # 获得域名的主域
    ext = tldextract.extract(url)
    if ext.subdomain == "www":
        return ext.registered_domain
    else:
        domain_info = [ext.subdomain, ext.registered_domain]
        domain_info = [x for x in domain_info if len(x) > 0]
        return ".".join(domain_info)


def get_img_path(save_dir, url):
    # 创建图片路径
    return os.path.join(save_dir, get_md5(url))


def get_img_dir(save_dir, url):
    # 创建图片存储目录
    if save_dir is None:
        save_dir = IMAGE_TMP_SAVE
    save_path = get_img_path(save_dir, url)
    os.makedirs(save_path, exist_ok=True)
    return save_path


def delete_file(path):
    if os.path.exists(path):  # 如果文件存在
        shutil.rmtree(path)
    else:
        print('no such file:%s' % path)  # 则返回文件不存在


# 清理非中文
def clean_content(content):
    """streamline \r\n\ space"""
    # content = re.sub(r'[^\u4e00-\u9fa5]+', ' ', content) # Eliminate Chinese characters
    return re.sub('[\r\n\t ]+', ' ', content).replace('\xa0', '').strip()


def clean_img_link(page_url, url_list, is_base):
    """
    提取页面图片链接
    :param page_url:
    :param url_list:
    :param is_base:
    :return:
    """
    img_list = []
    base_list = []
    if page_url in url_list:
        url_list.remove(page_url)
    for url in url_list:
        if url in img_list or url in base_list:
            continue
        if not url.startswith("http") and not url.startswith("data:"):
            full_url = urljoin(page_url, url)
            img_list.append(full_url)
        if url.startswith("http"):
            img_list.append(url)
        if is_base:
            if url.startswith("data:"):
                base_list.append(url)
    return img_list, base_list


# 提取标签内容
def get_meta_content(selector, meta_name):
    """
    Extract a given meta content form document
    """
    result = ''
    command = '//meta[translate(@name,"ABCDEFGHJIKLMNOPQRSTUVWXYZ",abcdefghjiklmnopqrstuvwxyz)="{0}"]/@content'.format(
        meta_name)
    content = selector.xpath(command)
    if content is not None and len(content) > 0:
        result = content[0].strip()
    return clean_content(result)


def get_text_by_xpath(selector, command):
    result = ''
    content = selector.xpath(command)
    if content is not None and len(content) > 0:
        result = content[0].strip()
    return clean_content(result)


def get_content_by_xpath(selector, command):
    result = ''
    content = selector.xpath(command)
    if content is not None and len(content) > 0:
        result = content.strip()
    return clean_content(result)


def get_summary_by_xpath(raw_html, command):
    result = ''
    doc = Document(raw_html)
    summary_html = doc.summary()
    # print(summary_html)
    selector = etree.HTML(summary_html)
    content = selector.xpath(command)
    if content is not None and len(content) > 0:
        result = content.strip()
    return clean_content(result)


# 图片操作
def image_bytes_shape_filter(img_content, threshold=100):
    """
    过滤掉图片长、宽小于 280, 过滤背景图片1920
    :param img_content:
    :param threshold:
    :return:
    """
    try:
        im = Image.open(BytesIO(img_content))
        w, h = im.size
        # print(w, h)
        if w < threshold or h < threshold or w > 1900:
            return True
        return False
    except:
        return True


def base64_to_img(image_str, save_path='demo.jpg', filter_size=100):
    """
    base64 字符串转 image
    data:image/png;base64,iVBOR

    :param image_str:
    :param save_path:
    :return:
    """
    try:
        base_64_list = image_str.split(';')
        # 获得数据字符
        data = base_64_list[-1].split(',')[-1]
        # 获得后缀
        sub_str = base_64_list[0].split('/')[-1]
    except Exception as e:
        print(e)
        data, sub_str = image_str, "jpg"
    content = base64.b64decode(data)
    if filter_size is not None:
        if not image_bytes_shape_filter(content, filter_size):
            return
    with open('{0}.{1}'.format(save_path, sub_str), "wb") as fh:
        fh.write(content)


def request_download(url_img, save_path, referrer, user_agent, filter_size):
    headers = {
        "HOST": get_domain(referrer),
        "Referer": referrer,
        'User-Agent': user_agent,
    }
    r = requests.get(url_img, headers=headers)
    if r.status_code != 200:
        return
    save_file = '{0}.jpg'.format(save_path)
    if filter_size is not None:
        if image_bytes_shape_filter(r.content, filter_size):
            return
    # print(save_file)
    with open(save_file, 'wb') as f:
        f.write(r.content)


def get_img_by_xpath(url, selector, command, user_agent, is_base, img_num, img_dir, filter_size):
    img_list_org = selector.xpath(command)
    img_list, base_list = clean_img_link(url, img_list_org, is_base)
    if len(img_list) > img_num:
        img_list = img_list[0:img_num]
    for p in img_list:
        save_path = get_img_path(img_dir, p)
        try:
            request_download(p, save_path, url, user_agent, filter_size)
        except Exception as e:
            print(e, p)
    if is_base:
        for d in base_list:
            save_path = get_img_path(img_dir, d)
            base64_to_img(d, save_path)
    return img_list, base_list


# 解决网页编码问题
def get_encoding_type(apparent_encoding, html_encoding_list):
    #  utf-8 < GB2312、BIG5、GBK、GB18030
    html_encoding = ''
    if len(html_encoding_list) > 0:
        html_encoding = html_encoding_list[0]
    data_list = [apparent_encoding, html_encoding]
    gbk_list = [x for x in data_list if "GB" in x.upper()]
    if len(gbk_list) > 0:
        return gbk_list[0]
    utf_list = [x for x in data_list if "UTF" in x.upper()]
    if len(utf_list) > 0:
        return utf_list[0]
    return 'UTF-8'


def get_user_agent(ua_type=0):
    if ua_type == 0:
        # pc user_agent 库
        try:
            user_agent = ua.random
        except:
            user_agent = ua_default
        return user_agent
    else:
        # 移动 user_agent 库
        return random.choice(MOBILE_USER_AGENT)


def get_html(url, user_agent):
    # do request
    html = ''
    status = 0
    headers = {'User-agent': user_agent}
    try:
        req = requests.get(url, headers=headers, timeout=HTTP_DEFAULT_TIMEOUT)
        header = req.headers
        # 剔除二进制
        content_type = header.get('Content-type', None)
        if content_type == 'application/octet-stream':
            return html, status
        response_encoding_list = requests.utils.get_encodings_from_content(req.text)
        if req.status_code >= 400:
            return html, 0
        status = 1
        # print(req.encoding, req.apparent_encoding, response_encoding_list)
        if req.encoding == "ISO-8859-1":
            req.encoding = get_encoding_type(req.apparent_encoding, response_encoding_list)
        req.keep_alive = False
        # print(html)
        html = req.text
    except Exception as e:
        print(e, "encoding error")
    # print(html, 'html')
    return html, status


def extract(url, ua_type=0, is_summary=False, is_img=False, img_num=10, is_base=False, filter_size=300, save_dir=None,
            is_keep=False):
    """

    :param url:
    :param ua_type:取值0 -> pc,1 -> mobile
    :param is_summary: 提取文章
    :param is_img: 提取图片
    :param img_num: 提取最大图片数据
    :param is_base: 是否提取 base64图片
    :param filter_size:过滤最小尺寸
    :param save_dir:图片保存路径
    :param is_keep:True 保存下载图片，Fasle 删除保存图片
    :return:
    """
    article = Article(url)
    user_agent = get_user_agent(ua_type)
    html, status = get_html(url, user_agent)
    if status == 0 or html == '':
        return article
    article.status = 1
    raw_html = delete_all_tag(html)
    selector = etree.HTML(raw_html)
    article.meta_description = get_meta_content(selector, 'description')
    article.meta_keywords = get_meta_content(selector, "keywords")
    article.title = get_text_by_xpath(selector, '//title/text()')
    article.h1 = get_text_by_xpath(selector, '//h1/text()')
    article.content = get_content_by_xpath(selector, 'string()')
    if is_summary:
        article.summary = get_summary_by_xpath(raw_html, 'string()')
    if is_img:
        article.img_dir = get_img_dir(save_dir, url)
        article.img_list, _ = get_img_by_xpath(url, selector, '//img/@src', user_agent, is_base,
                                               img_num, article.img_dir, filter_size)
        if not is_keep:
            delete_file(article.img_dir)
    return article


if __name__ == "__main__":
    # raw_url = "http://www.le.com/ptv/vplay/26335580.html"
    # raw_url = "https://rtbasia.com/"
    # raw_url = "https://www.163.com/"
    raw_url = "https://ent.163.com/19/0506/16/EEGN1F5Q00038FO9.html"
    page = extract(url=raw_url, is_summary=True, is_img=True, is_keep=True,
                   save_dir='/Users/wangchun/PycharmProjects/thanos/resources/tmp_image')
    print(page.org_url)
    print(page.status)
    # 提取 title
    print("title", page.title)
    # 提取 h1
    print("h1", page.h1)
    # 提取 meta_keywords
    print("meta_keywords", page.meta_keywords)
    # 提取 meta_description
    print("meta_description", page.meta_description)
    # 提取网页的主要内容
    print('summary', page.summary)
    # 提取网页的整个页面内容
    print('content', page.content)
    print([page.status, page.title, page.h1, page.meta_keywords, page.meta_description,
           page.summary,
           page.content])
