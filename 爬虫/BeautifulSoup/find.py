# find是查找单个元素，而find_all返回所有元素
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
print(soup.find('ul'))
print(type(soup.find('ul')))
print(soup.find('page'))