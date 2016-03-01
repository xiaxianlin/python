# coding=utf-8
import time, string, md5, math, uuid, threading
from collections import deque
import communicationException


class ThreadPool():
    # statues
    __readingStatus = 10000
    __waitingStatus = 10001
    __runningStatus = 10002
    __overingStatus = 10003
    # status list
    __statusList = []
    # pool status in current
    __status = 0
    # run thread maximum
    __maxRunningThreadNum = 0
    # wait thread maximum
    __maxWaitingThreadNum = 2000
    # run thread number in current
    __currentRunningThreadNum = 0
    # wait thread number in current
    __currentWaitingThreadNum = 0
    # the thread use to listen the pool's thread
    __listener = None
    # waiting thread list
    __waitingThreadQueue = deque()
    # running thread list
    __runningThreadQueue = deque()
    # error thread list
    __errorThreadQueue = deque()

    def __init__(self, maxNum=20):
        # regsiter the listener to listen the pool running status
        self.__listener = PoolListener(self)
        #self.__listener.setDaemon(True)
        # the max running thread number
        self.__maxRunningThreadNum = maxNum
        self.__status = self.__readingStatus
        # add status into list
        self.__statusList.append(self.__readingStatus)
        self.__statusList.append(self.__waitingStatus)
        self.__statusList.append(self.__runningStatus)
        self.__statusList.append(self.__overingStatus)

    # add wait thread
    def add(self, thread):
        if isinstance(thread, ExcuteThread):
            if self.__currentWaitingThreadNum > self.__maxWaitingThreadNum:
                raise ThreadTooMuchException()
            else:
                self.__waitingThreadQueue.append(thread)
                self.__currentWaitingThreadNum += 1
        else:
            raise ThreadTypeErrorException()

    # run the thread pool
    def execute(self):
        self.__listener.start()

    # move thread from waiting queue to running queue, then start the thread
    def moveAndRunTheThread(self):
        # get the newest thread
        thread = self.__waitingThreadQueue.popleft()
        # insert into the running queue
        self.__runningThreadQueue.append(thread)
        self.__currentRunningThreadNum += 1
        # remove the thread from the waiting queue
        self.__currentWaitingThreadNum -= 1
        # run the thread
        thread.start()

    def validataRunningThread(self):
        for thread in list(self.__runningThreadQueue):
            if thread.is_alive() != True:
                print "thread %s is finished" % thread.hashKey
                self.__runningThreadQueue.remove(thread)
                self.__currentRunningThreadNum -= 1

    # get current run thread number
    def getCurrentRunningThreadNum(self):
        return self.__currentRunningThreadNum

    # get current wait thread number
    def getCurrentWaitingThreadNum(self):
        return self.__currentWaitingThreadNum

    # the run thread maximum
    def getMaxRunningThreadNum(self):
        return self.__maxRunningThreadNum

    # pause the pool
    def pause(self):
        self.__status = self.__waitingStatus

    # run the pool
    def run(self):
        self.__status = self.__runningStatus

    # destory the pool
    def destory(self):
        self.__listener.finish()
        self.__status = self.__overingStatus

    # check pool is ready or not
    def isReady(self):
        return self.__status == self.__readingStatus
    # check pool is wait or not
    def isPause(self):
        return self.__status == self.__waitingStatus

    # check pool is run or not
    def isRunning(self):
        return self.__status == self.__runningStatus

    # check pool is finish or not
    def isFinished(self):
        return self.__status == self.__overingStatus


# PoolListener
# listen the pool how to run, check the pool's threads is alive or not
class PoolListener(threading.Thread):
    __pool = None
    __running = True

    def __init__(self, pool):
        super(PoolListener, self).__init__()
        self.__pool = pool

    def run(self):
        pool = self.__pool
        while True:
            # if the pool is excetue over and the listener is not run, interupt the lister thread
            if self.__running == False:
                break

            # the pool is in the ready status, change the status to running
            if pool.isReady():
                print 'pool is ready'
                pool.moveAndRunTheThread()
                pool.run()
            # the pool is pause by someone
            elif pool.isPause():
                print 'pool is pasued'
                pass
            # the pool is running
            elif pool.isRunning():
                print 'pool is running'
                # check run thread is alive or not
                pool.validataRunningThread()
                if pool.getCurrentWaitingThreadNum() > 0:
                    # if current running thread is not enough, move the thread from waiting and run it
                    if pool.getCurrentRunningThreadNum() < pool.getMaxRunningThreadNum():
                        pool.moveAndRunTheThread()
            # the pool is finished, if the listener's status is not change, here can finish the listener
            elif pool.isFinished():
                print 'pool is finished'
                break
            # pause 100ms
            time.sleep(0.1)

    def finish(self):
        self.__running = False


# excute thread
# every thread must extend this thread
class ExcuteThread(threading.Thread):
    hashKey = ''

    def __init__(self):
        super(ExcuteThread, self).__init__()
        ruid = uuid.uuid4()
        ctime = int(time.time() * 1000)
        self.hashKey = '%s-%d' % (ruid, ctime)

    def run(self):
        time.sleep(1.5)
        print 'thread %s is running' % self.hashKey


if __name__ == '__main__':
    pool = ThreadPool()
    for x in xrange(0, 1000):
        thread = ExcuteThread()
        pool.add(thread)
    pool.execute()
