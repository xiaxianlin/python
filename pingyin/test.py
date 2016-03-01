#-*- coding : utf-8 -*-
import sys, time, uuid
from image import createImage
import httplib
reload(sys)
sys.setdefaultencoding('utf-8')

def createImageByWord(word):
    targetDir = '/Users/xiaxianlin1/Download/'
    createImage(word, targetDir)

ctime = int(time.time() * 1000)
print uuid.uuid4()