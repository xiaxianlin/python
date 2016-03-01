# coding=utf-8 
import urllib
import urllib2
import re
from word import Word

def getWord(page):
    url = "http://hanyu.iciba.com/hanzi/%d.shtml" % page
    word = Word()
    try:
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        html = response.read().decode('utf-8')
        #hanzi
        hzPattern = re.compile('<div class="hanzi01">(.*?)</div>')
        hzResults = re.findall(hzPattern, html);
        word.hanzi = hzResults[0]
        #抓取繁体，笔画，部首，五笔
        sxPattern = re.compile('<div class="hanzi022">(.*?)</div>')
        sxResults = re.findall(sxPattern, html);
        word.fanti = sxResults[0]
        word.bihua = sxResults[1]
        word.bushou = sxResults[2]
        word.wubi = sxResults[3]
    except urllib2.URLError, e:
        if hasattr(e, "code"):
            print e.code
        if hasattr(e, "reason"):
            print e.reason
    except Exception, e:
        pass
    return word
