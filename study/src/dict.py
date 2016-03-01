d = {
    'adam': 95,
    'lisa': 85,
    'bart': 59
}

print len(d)

if('paul' in d):
    print d['paul']

print d.get('lisa')

d['paul'] = 72

print d.keys()

print d