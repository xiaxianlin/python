import MySQLdb

class MysqlCline(object):
    def __new__(cls, *args, **kw):  
        if not hasattr(cls, '_instance'):  
            orig = super(Singleton, cls)  
            cls._instance = orig.__new__(cls, *args, **kw)  
        return cls._instance 
    def connection():
        try:
            conn = MySQLdb.connect(host='localhost',user='root',passwd='root',port=3306)
            cur = conn.cursor()
            conn.select_db('rong')
            cur.close()
            conn.close()
        except MySQLdb.Error,msg:
            print "MySQL Error %d: %s" %(msg.args[0],msg.args[1])
        return conn;
