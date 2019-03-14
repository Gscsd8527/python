html = """
<div class='panel'>
    <div class='panel-heading'>
    <h4>Hello</h4>
    </div>
    <div class='panel-body'>
      <ul class='list' id='list-1' name='elements'>
        <ll class='element'>Foo</ll>
        <ll class='element'>Bar</ll>
        <ll class='element'>Jay</ll>
        </ul>
      <ul class='list list-small' id='list-2'>
        <ll class='element'>Foo</ll>
        <ll class='element'>Bar</ll>
        </ul>
    </div>
</div>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(soup.find_all(attrs={'id':'list-1'}))
print(soup.find_all(attrs={'name':'elements'}))

# 也可用下面这种方式
print(soup.find_all(id='list-1'))
print(soup.find_all(class_='element'))