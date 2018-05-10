"""
-------------------------------------------------
   Author :       galen
   date：          2018/5/9
-------------------------------------------------
   Description:
-------------------------------------------------
"""
from stallion import Stallion

s = Stallion()
# a = s.extract("https://www.rtbasia.com/")
a = s.extract("http://www.taoche.com/buycar/b-dealerkcw5385818t.html")
print(a)
print(a.content)
print(a.title)
print(a.h1)
print(a.meta_keywords)
print(a.meta_description)
