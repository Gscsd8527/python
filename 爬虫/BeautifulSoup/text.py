html = """
<div class='panel'>
    <div class='panel-heading'>
    <h4>Hello</h4>
    </div>
    <div class='panel-body'>
      <ul class='list' id='list-1'>
        <ll class='enement'>Foo</ll>
        <ll class='enement'>Bar</ll>
        <ll class='enement'>Jay</ll>
        </ul>
      <ul class='list list-small' id='list-2'>
        <ll class='enement'>Foo</ll>
        <ll class='enement'>Bar</ll>
        </ul>
    </div>
</div>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(soup.find_all(text='Foo'))