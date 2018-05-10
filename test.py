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
a = s.extract("https://www.rtbasia.com/")
print(a.content)
