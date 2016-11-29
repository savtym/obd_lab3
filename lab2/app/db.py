import MySQLdb as mdb;

def getConnect(query):
    connect = mdb.connect(host = '127.0.0.1', user = 'root', passwd = '12345678', db = 'shop')
    cursor  = connect.cursor()
    cursor.execute('SET NAMES `utf8`')
    cursor.execute(query)
    result = dictfetchall(cursor)
    cursor.close()
    return result

def dictfetchall(cursor): 
    "Returns all rows from a cursor as a dict" 
    desc = cursor.description 
    return [
            dict(zip([col[0] for col in desc], row)) 
            for row in cursor.fetchall() 
    ]

class Db():
    """description of class"""
    @staticmethod

    def getListUsers():
        return getConnect('select * from app_clients;')

    def getListProducts():
        return getConnect('select id, name, title from app_products;')

    def getListManufactories():
        return getConnect('select * from app_manufactories;')

    def getListCategories():
        return getConnect('select * from app_categories;')

    def getProduct(id):
        return getConnect('select p.id, p.name, p.title, c.name nameCategory, m.name nameManufactory from app_products p join app_categories c on p.category_id = c.id join app_manufactories m on p.manufactory_id = m.id where p.id = %s' % id)[0]

    def addProduct(name, title, categoryId, manufactoryId):
        return getConnect("insert into app_products (name, title, category_id, manufactory_id) values(%s, %s, %s, %s);" % (name, title, categoryId, manufactoryId))