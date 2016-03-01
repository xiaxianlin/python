#-*- coding : utf-8 -*-
import sys, random, time
from db import DB
reload(sys)
sys.setdefaultencoding('utf-8')

devConfig = {
    'url': '121.40.225.104',
    'user': 'uwelian',
    'pwd': 'welian!@#$',
    'db': 'welian_new'
}

def searchActiveCount():
    db = DB(devConfig)
    sql = "select count(*) from active where (auth_password is null or auth_password = '') and deleted = 0"
    result = db.get(sql)
    return result[0]

def searchActive():
    db = DB(devConfig)
    sql = "select id from active where (auth_password is null or auth_password = '') and deleted = 0"
    return db.findAll(sql)

list = searchActive()
for active in list:
    db = DB(devConfig)
    id = active[0]
    pwd =  random.randint(10000, 99999)
    ctime = int(time.time() * 1000)
    sql = "update active set auth_password='%d', modify_time='%d' where id = %d" % (pwd, ctime, id)
    rows = db.crud(sql)
    print rows,id, pwd, sql