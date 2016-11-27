import MySQLdb as mdb;
#from django.db import models

def getConnect(query):
    connect = mdb.connect(host = '127.0.0.1', user = 'root', passwd = '12345678', db = 'shop')
    cursor  = connect.cursor()
    cursor.execute('SET NAMES `utf8`')
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    return result

class Db():
    """description of class"""
    @staticmethod

    def getListUsers():
        return getConnect('select * from app_clients;')

    def getListProducts():
        return getConnect('select id, name, title from app_products;')

    def getListProduct(id):
        return getConnect('select id, name, title from app_products;' + 'where id=' + id)