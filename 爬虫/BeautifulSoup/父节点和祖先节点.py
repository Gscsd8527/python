html = """
<html>
   <head>
      <title>The Dormouse's story</title>
   </head>
<body>
  <p class="story">
   Once upon a time there were three little sisters; and their names were
   <a href="http://example.com/elsie" class="sister" id="link1">
      <span>Elsle</span>
   </a>
   <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    and they lived at the bottom of a well.
    </p>
<p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
# 获取父节点
print(soup.a.parent)
# 获取父节点和祖先节点一起获取
print(list(enumerate(soup.a.parents)))
