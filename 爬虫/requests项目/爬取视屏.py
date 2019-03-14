import requests
from bs4 import BeautifulSoup

# print('开始下载')
# with open('G:/video.swf','wb') as mp4:
#     for chunk in r.iter_content(chunk_size=1024*1024):
#         print(chunk)
#         if chunk:
#             mp4.write(chunk)
# print('下载完成')
def main(url):
    html = requests.get(url)
    html = html.text
    soup = BeautifulSoup(html, 'lxml')
    video = soup.select('ul.listvideo-list.clearfix li')
    for i in video:
        video_url = i.select('div.vervideo-bd a')[0]
        video_url = video_url.get('href')
        video_url = 'http://www.pearvideo.com/' + video_url
        print(video_url)
        parss_url(video_url)

def parss_url(video_url):
    html = requests.get(video_url)
    html = html.text
    soup = BeautifulSoup(html, 'lxml')
    src = soup.select('div.video-main')
    # src = src.get('src')
    print(src)


if __name__ == '__main__':
    url = 'http://www.pearvideo.com/category_9'
    main(url)