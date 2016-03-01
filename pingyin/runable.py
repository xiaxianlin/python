# coding=utf-8
import time, string, md5, math, uuid
import threading


#线程池
class ThreadPool():
    threads = dict()
    executeTreads = dict()

    def __init__(self, callback, minNum=5, maxNum=20):
        self.listener = ListenerThread(self)
        self.callback = callback
        self.minNum = minNum
        self.maxNum = maxNum

    #添加线程
    def add(self, thread):
        if isinstance(thread, ExcuteThread):
            self.threads[thread.hashKey] = thread

    #移除线程
    def remove(self, key):
        count = len(self.threads)
        if key in self.executeTreads.keys():
            try:
                self.executeTreads.pop(key)
                #如果待命线程还有的话就加入
                if count > 0:
                    thread = self.addExcuteThread()
                    if thread != None:
                        thread.start()
            except Exception, e:
                pass
        #所有线程都结束后回掉
        if count == 0:
            print 'threads excute over, callback something'
            self.callback()

    #开始执行
    def execute(self):
        self.dealExcuteThread()
        self.listener.start()

    def addExcuteThread(self):
        key = ''
        currentThread = None
        if len(self.threads) > 0:
            try:
                key, currentThread = self.threads.items()[0]
                self.executeTreads[key] = currentThread
                self.threads.pop(key)
            except Exception, e:
                pass
        return currentThread

    def dealExcuteThread(self):
        count = len(self.executeTreads)
        for x in xrange(count, self.maxNum):
            self.addExcuteThread()
        for key, thread in self.executeTreads.iteritems():
            try:
                thread.start()
            except Exception, e:
                pass


# 监听现场
# 负责监听线程是否结束
class ListenerThread(threading.Thread):
    def __init__(self, pool):
        super(ListenerThread, self).__init__()
        self.pool = pool

    def run(self):
        while True:
            for (key, thread) in self.pool.executeTreads.items():
                if thread.isAlive() == False:
                    self.pool.remove(key)
            if len(self.pool.threads) == 0:
                break
            time.sleep(0.1)


#执行线程
class ExcuteThread(threading.Thread):
    hashKey = ''

    def __init__(self):
        super(ExcuteThread, self).__init__()
        ruid = uuid.uuid4()
        ctime = int(time.time() * 1000)
        self.hashKey = '%s-%d' % (ruid, ctime)

    def run(self):
        print 'thread %s is running' % self.hashKey
