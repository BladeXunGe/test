# -*- coding: utf-8 -*-
import urllib
import urllib.request
import re

def download_page(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = response.read()
    return data


def get_image(html):
    regx = r'src="(https://img.*?\.jpg)"'
    pattern = re.compile(regx)
    get_img = re.findall(pattern,repr(html))
    num = 1
    for img in get_img:
        image = download_page(img)
        with open('%s.jpg '%num,'wb') as fp:
            fp.write(image)
            num += 1
            print('downloding pic%s'%num)
    return

url = 'https://tieba.baidu.com/p/1181591427'
html = download_page(url)
get_image(html)