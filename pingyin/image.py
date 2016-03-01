# coding=utf-8
import sys, os, md5
from PIL import Image, ImageDraw, ImageFont


def createImage(word, target):
    root = cur_file_dir()
    bg = "%s/resource/avatar.png" % root
    ttf = "%s/resource/simyou.ttf" % root
    image = Image.open(bg)
    # 创建Font对象:
    font = ImageFont.truetype(ttf, 36, encoding='unic')
    # 创建Draw对象:
    draw = ImageDraw.Draw(image)
    # 输出文字:
    if word.isalpha(): 
        draw.text((30, 22), unicode(word, 'UTF-8'), font=font, fill='#000')
    else:
        draw.text((22, 22), unicode(word, 'UTF-8'), font=font, fill='#000')
    filePath = target + createMd5(word) + '.png'
    if os.path.isfile(filePath):
        os.remove(filePath)
    image.save(filePath)


#获取脚本文件的当前路径
def cur_file_dir():
    #获取脚本路径
    path = sys.path[0]
    #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)


def createMd5(word):
    m1 = md5.new()
    m1.update(word)
    return m1.hexdigest()

def createBasicWord(target):
    words = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for word in words:
        createImage(word.upper(), target)
