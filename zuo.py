# coding:utf-8
import requests
from lxml import html

def header(referer):
    headers = {
        'Host': 'i.meizitu.net',
        'Pragma': 'no-cache',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/59.0.3071.115 Safari/537.36',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Referer': '{}'.format(referer),
    }
    return headers

def getPage(url):

    selector = html.fromstring(requests.get(url).content)
    urls = []
    for i in selector.xpath('//h2[@class="block-title"]/a/@href'):
        urls.append(i)
        print(i)
    return urls

def getTxt(urll):
    sel = html.fromstring(requests.get(urll).content.decode(encoding='utf-8'))
    title = sel.xpath('normalize-space(//h2[@class="block-title"]/text())').replace('?', ' ')
    txt1 = sel.xpath('//div[@class="grap"]//li/text()')

    for t in txt1:
        txt = t

        fpath = 'D:/1/%s.txt' % title
        with open(fpath, 'a', encoding='utf-8') as f:
            f.write(str(txt) + '\n')
            f.write('*' * 50 + '\n')
            f.close()






def getOnePage(url):

    p = getPage(url)
    for e in p:
        print(e)
        getTxt(e)

def main():
    pageNum = input(u'请输入页码：')


    url = 'http://www.zreading.cn/archives/tag/一语惊人/page/'
    for i in range(eval(pageNum)):
        i = i + 1
        ul = url + str(i)
        print(ul)
        getOnePage(ul)

main()