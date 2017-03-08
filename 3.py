# -*- coding: utf-8 -*-
import urllib
import urllib.request
import re
import os

class TiebaSpider:
    def __init__(self):
        self.siteURL = 'https://tieba.baidu.com/p/1181591427'
        self.imageNumber = 8

    def getHtml(self):
        request = urllib.request.Request(self.siteURL)
        response = urllib.request.urlopen(request)

        html = response.read()
        return html


    def saveImages(self, imglist, name):
        for imageURL in imglist:
            self.imageNumber += 1
            splitPath = imageURL.split('.')
            fTail = splitPath.pop()
            if len(fTail) > 3:
                fTail = 'jpg'
            fileName = name + "/" + str(self.imageNumber) + "." + fTail
            # 对于每张图片地址，进行保存
            try:
                u = urllib.request.urlopen(imageURL)
                data = u.read()
                f = open(fileName, 'wb+')
                f.write(data)
                print
                u'正在保存的一张图片为', fileName
                f.close()
            except urllib.request.URLError as e:
                print(e.reason)

    def getAllImg(self,response):
        regx = r'src="(https://img.*?\.jpg)"'
        pattern1 = re.compile(regx)
        imglist = re.findall(pattern1,repr(response))
        return imglist

    def getPageNumber(self, html):
        # 利用正则表达式来从网页源代码中分析得到页面数
        reg = '<span class="red">(.*?)</span>'  # 根据正则表达式找到该网址下共有多少个页面
        numre = re.compile(reg)
        number = re.findall(numre,repr(html))
        return int(number[0])  # 可能会找到好几个这个数字，只需取出第一个，并转为整型

    #  获取网址下所有页面
    def getAllPages(self, number):
        # 获取主网址下的共number个页面的源代码，放在pagesHtml中
        pagesHtml = []
        for pageIndex in range(1, number + 1):
            url = self.siteURL + '?pn=' + str(pageIndex)
            pageHtml = urllib.request.urlopen(url).read()
            pagesHtml.append(pageHtml)
        return pagesHtml

        # 从该网址下所有页面中获取图片

    def saveImgAllPages(self):
        # 新建本地文件夹保存图片
        path = u'图片'
        self.mkdir(path)
        # 获取所要爬虫的网址网页详细信息，得到的html就是网页的源代码
        html = self.getHtml()
        # 得到该贴吧网址下共有多少个页面
        pageNumber = self.getPageNumber(html)
        # 获取所有的页面的源代码，从中分析出图片
        pagesHtml = self.getAllPages(pageNumber)
        x = 1
        for pageHtml in pagesHtml:
            # 获取每个页面下的所有图片地址列表
            imglist = self.getAllImg(pageHtml)  # 获取图片的地址列表
            self.saveImages(imglist, path)  # 保存图片
            print
            u'已经保存了第', x, u'页的所有图片'
            x += 1



            # 创建本地保存文件夹，并下载保存图片


if __name__ == '__main__':
    spider = TiebaSpider()
    spider.saveImgAllPages()
    print
    u'图片下载保存结束，共抓取了', spider.imageNumber, u'张图片'
    # path = u'图片'
    # mkdir(path) #创建本地文件夹
    # imglist = getAllImg(html)
    # saveImages(imglist,path)