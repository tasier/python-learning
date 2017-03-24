# -*- coding: UTF-8 -*-

import requests
import random
from time import sleep

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


def counter(start_at=0):
    count = [start_at]

    def incr():
        count[0] += 1
        return count
    return incr


x = 10
def foo():
    y = 2
    bar = lambda :x+y
    print bar()

if __name__ == '__main__':
    #print '你好'
    #    demo_list()
    #print isinstance('123', str)


    #闭包实验
    #对装饰器的理解有重要作用
    # print counter(3)()

    # foo()

    random_time = random.random()
    print random_time
    sleep(random_time+1)
