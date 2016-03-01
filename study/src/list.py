# -*- coding: utf-8 -*-
mates = ['Adam', 95.5, 'Lisa', 85, 'Bart', 59]

"""
print mates[0]
print mates[1]
print mates[2]
print mates[3]

print mates[-1]
print mates[-2]
print mates[-3]
"""

mates.append('Paul')
mates.insert(7,80)

score = mates.pop(7);
#print score

name = mates.pop(6);
#print name
print mates
#索引0到3
print 1,mates[0:3]
print 2,mates[:3]
#索引1到3
print 3,mates[1:3]
#全部
print 4,mates[:]
#从2开始每2个取1个
print 5,mates[2::2]
#倒数第二个开始
print 6,mates[-2:]
#取到倒数第二个
print 7,mates[:-2]
#倒数第三个到倒数第二个
print 8,mates[-3:-1]
#从倒数第四个到倒数第一个每2个取1个
print 9,mates[-4:-1:2]