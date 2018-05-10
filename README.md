## stallion
Parsing ang page context.

**Use**
```
from stallion import Stallion
url = 'http://edition.cnn.com/2012/02/22/world/europe/uk-occupy-london/index.html?hpt=ieu_c2'
g = stallion()
article = g.extract(url=url)
article.title
```

Galen _@20180510_