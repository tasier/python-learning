# -*- coding: UTF-8 -*-

import requests

# content = requests.get('http://www.qiushibaike.com').content
# print 'hello'


def demo_list():
    lista = [1, 2, 3]
    print lista
    print len(lista)

    print 1 in lista

    listb = [23,'abc',1.34]
    print lista+listb
    print listb

if __name__ == '__main__':
    #print '你好'
    #    demo_list()
    #print isinstance('123', str)

    visit_file = open('visit-has-new-visitor.log', 'r+')
    try:
        print visit_file.readline()
        visit_file.seek(0)
        visit_file.write('33')

    finally:
        visit_file.close()


