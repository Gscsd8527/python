import requests
import re
from bs4 import BeautifulSoup

def parse(url):
    fromname = '广场出口'
    fromaddr = '天安门'
    toname = '清华大学南门'
    toaddr = '清华大学'
    params = {
        'fromname':fromname,
        'fromaddr':fromaddr,
        'toname':toname,
        'toaddr':toaddr
    }
    http = requests.get(url,params=params)
    print(http.status_code)
if __name__ == "__main__":

    url = 'https://apigate/v1/estimates/price'
    parse(url)