from collections import deque

d = deque('ghi')
d.append('j')
d.appendleft('f')
d.remove('g')
for x in list(d):
    print x