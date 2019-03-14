import requests

def start():
    url = 'https://s.weibo.com/weibo?q=神州优车&Refer=user_weibo'
    response = requests.get(url)
    print(response.text)
def main():
    start()

if __name__ == '__main__':
    main()

