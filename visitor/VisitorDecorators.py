# -*- coding: UTF-8 -*-

from time import ctime


def console_log(func):
    '''
    这是一个有关控制台的日志装饰器
    '''
    def wrapper(*args, **kwargs):
        print '[%s] before  %s() called' % (ctime(),func.__name__)
        func(*args, **kwargs)
        print '[%s] after  %s() called' % (ctime(), func.__name__)
        return func
    return wrapper


def console_log_args(decorator_arg):
    '''
    实验性质的带参数的装饰器
    '''
    def real_decorator(func):
        def wrapper(*args, **kwargs):
            print 'before '+decorator_arg
            func(*args, **kwargs)
            print 'after '+decorator_arg
            return func
        return wrapper
    return real_decorator