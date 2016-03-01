# coding=utf-8
import MySQLdb

class DB():
    def __init__(self, config):
        try:
            self.conn = MySQLdb.connect(host=config['url'],
                                        user=config['user'],
                                        passwd=config['pwd'],
                                        db=config['db'],
                                        port=3306,
                                        charset="utf8")
            self.cur = self.conn.cursor()
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])

    def crud(self, sql):
        rows = 0
        try:
            rows = self.cur.execute(sql)
            self.conn.commit()
            self.cur.close()
            self.conn.close()
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return rows

    def findAll(self, sql):
        result = []
        try:
            self.cur.execute(sql)
            result = self.cur.fetchall()
            self.cur.close()
            self.conn.close()
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return result

    def find(self, sql, size):
        result = []
        try:
            self.cur.execute(sql)
            result = self.cur.fetchmany(size)
            self.cur.close()
            self.conn.close()
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return result

    def get(self, sql):
        result = []
        try:
            self.cur.execute(sql)
            result = self.cur.fetchone()
            self.cur.close()
            self.conn.close()
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return result
