## Stallion
Parsing any web page context.

**Use**
```
from stallions import Stallion
url = "https://www.rtbasia.com/"
g = Stallion()
article = g.extract(url=url)
article.title
print("title", article.title)
print("h1", article.h1)
print("meta_keywords", article.meta_keywords)
print("meta_description", article.meta_description)
print(article.content)
```

Galen _@20180510_