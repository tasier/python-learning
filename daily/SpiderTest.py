# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup

if __name__ == '__main__':
    html_doc = ''
    with open('html_doc') as htmlfile:
        for line in htmlfile:
            html_doc += line

    soup = BeautifulSoup(html_doc, "lxml")
    #构造器可以是文件对象
    # soup = BeautifulSoup(open('html_doc'), 'lxml')
    # print soup.prettify()

    #直接访问某个标签
    # print soup.title
    # print soup.title.name
    # print soup.title.string

    #访问标签的父标签
    # print soup.title.parent

    #访问标签的属性
    # print soup.p, type(soup.p)
    # print soup.p['class']

    #获取某一类的所有标签
    # for line in soup.find_all('a'):
    #     print line, line['class'], line['href']
    #     print line.get('href')

    #获取id为link1的标签
    # print soup.find(id='link1')

    #从文档中获取所有文字内容
    # print soup.get_text()

    print len(list(soup.children))
    print len(list(soup.descendants))