import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException


# 获取页面源码函数
def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/58.0.3029.110 Safari/537.36 '
    }
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            print('ok')
            return r.text
        return None
    except RequestException:
        return None


# 解析页面获得所有职位信息的函数
def parse_index():
    url = 'https://www.lagou.com/'
    soup = BeautifulSoup(get_html(url), 'lxml')
    # CSS 选择器
    all_positions = soup.select('div.menu_sub.dn > dl > dd > a')
    joburls = [i['href'] for i in all_positions]
    jobnames = [i.get_text() for i in all_positions]

    for joburl, jobname in zip(joburls, jobnames):
        data = {
            'url': joburl,
            'name': jobname
        }

        yield data