# -*- coding: utf-8 -*- 
# @Time : 2022/2/22 4:16 下午 
# @Author : wwh
# @File : settings.py

class BaseConfiguration:
    DEBUG = False


class DevelopConfiguration:
    DEBUG = True
    DATABASE = {
        'MYSQL_HOST': '127.0.0.1',
        'MYSQL_PORT': '3306',
        'MYSQL_USER': 'root',
        'MYSQL_PASSWORD': '123456',
        'MYSQL_DATABASE': 'store',
    }


class ProductConfiguration:
    DATABASE = {
        'MYSQL_HOST': '127.0.0.1',
        'MYSQL_PORT': '3306',
        'MYSQL_USER': 'root',
        'MYSQL_PASSWORD': '123456',
        'MYSQL_DATABASE': 'test',
    }
