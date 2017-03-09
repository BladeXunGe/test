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

if os.path.exists("D:/imags") == False:
    os.mkdir("D:/imags")

def get_image(html,x):
    regx = r'src="(https://img.*?\.jpg)"'
    pattern = re.compile(regx)
    imlist = re.findall(pattern,repr(html))

    print(imlist)

    for img in imlist:
        image = download_page(img)
        name = '%s.jpg '% x
        with open('D:/imags/'+ name, 'wb') as fp:
            fp.write(image)
            x += 1
            print('downloding pic%s' % x)

    return x

x = 1
url = 'https://tieba.baidu.com/p/1181591427?pn='

for k in range(1,28):
    ul = url + str(k)
    print(ul)
    html = download_page(url)
    get_image(html,x)
    x = get_image(html,x)