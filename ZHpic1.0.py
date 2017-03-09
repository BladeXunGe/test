# -*- coding: utf-8 -*-
import urllib
import urllib.request
import re
import os

def download_page(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = response.read()
    return data

path = input('please enter your place like D:/imags/')
if os.path.exists(path) == False:
    os.mkdir(path)


def get_image(html):
    regx = r'img src="(http.*?)"'
    pattern = re.compile(regx)
    imlist = re.findall(pattern,repr(html))
    num = 1
    for img in imlist:
        image = download_page(img)
        name = '%s.jpg ' % num
        with open(path + name,'wb') as fp:
            fp.write(image)
            num += 1
            print('downloding pic%s'%num)
    return

url = 'https://www.zhihu.com/question/34378366'
html = download_page(url)
get_image(html)