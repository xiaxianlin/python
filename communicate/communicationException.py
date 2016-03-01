#-*- coding=utf-8 -*-


class ThreadTypeErrorException(Exception):
    def __init__(self, value="Your thread is not normal ExcuteThread!"):
        self.value = value

    def __str__(slef):
        return repr(self.value)


class ThreadTooMuchException(Exception):
    def __init__(self, value="You add a lot of threads, the pool is full!"):
        self.value = value

    def __str__(slef):
        return repr(self.value)
