import os

from dbdb.interface import DBDB


__all__ = ['DBDB', 'connect']

#打开或创建一个数据库,然后返回一个叫DBDB的实例
def connect(dbname):
    try:
        f = open(dbname, 'r+b')
    except IOError:
        fd = os.open(dbname, os.O_RDWR | os.O_CREAT)
        f = os.fdopen(fd, 'r+b')
    return DBDB(f)
