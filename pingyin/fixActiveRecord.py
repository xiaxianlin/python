#-*- coding : utf-8 -*-
import sys
import web
from runable import *
from db import DB
from image import createImage
import httplib
reload(sys)
sys.setdefaultencoding('utf-8')

devConfig = {
    'url': '121.40.225.104',
    'user': 'uwelian',
    'pwd': 'welian!@#$',
    'db': 'welian_new'
}
# devConfig = {
#     'url': '192.168.48.212',
#     'user': 'welian',
#     'pwd': 'welian',
#     'db': 'welian'
# }

def searchActiveRecordCount():
    db = DB(devConfig)
    sql = "select count(*) from active_record where deleted = 0 and (uid = 0 or uid is null)"
    result = db.get(sql)
    return result[0]

def searchActiveRecord(begin, limit):
    db = DB(devConfig)
    sql = "select id,username from active_record where deleted = 0 and (uid = 0 or uid is null) order by id desc limit %d,%d" % (
        begin, limit)
    return db.findAll(sql)

def excuteThread():
    global step
    global size
    global count
    begin = step * size
    print 'step: %d\tsize:%d\tcount:%d' % (step, size, count)
    if begin <= count:
        records = searchActiveRecord(begin, size)
        pool = ThreadPool(excuteThread)
        for i in xrange(0, len(records)):
            thread = UploadThread(records[i])
            pool.add(thread)
        pool.execute()
    step = step + 1


class UploadThread(ExcuteThread):
    def __init__(self, record):
        super(UploadThread, self).__init__()
        self.record = record

    def run(self):
        db = DB(devConfig)
        id, name = self.record
        word = name[-1].encode('utf-8').strip()
        word = word.upper()
        url = '/avatar/%s.png' % self.encty(word)
        avatar = 'http://image.welian.com%s' % url
        try:
            conn = httplib.HTTPConnection('image.welian.com')
            conn.request("GET", url)
            res = conn.getresponse()
            if res.status != 200:
                avatar = 'http://image.welian.com/avatar/avatar.png'
        except Exception, e:
                pass
        ctime = int(time.time() * 1000)
        sql = "update active_record set avatar='%s', modify_time='%d' where id = %d" % (avatar, ctime, id)
        rows = db.crud(sql)
        print 'id:%d\tname:%s\tstatus:%d\t\n' % (id, name, rows)

    def encty(self, word):
        m1 = md5.new()
        m1.update(word)
        return m1.hexdigest()


count = searchActiveRecordCount()
pools = []
step = 0
size = 2000