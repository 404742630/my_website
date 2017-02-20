# coding:utf-8
"""
Created on 2017-02-16

@author: ysw
"""

import time
import string
import random
import requests
import urllib
import json
import config
import web
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

def int2hex(num):
    """
    整数转16进制
    :param num:
    :return:
    """
    return str(hex(int(num))).replace('0x', '').replace('L', '')

def hex2int(shex):
    """
    16进制转整数
    :param shex:
    :return:
    """
    return int('0x' + shex, 16)

def str2intList(strList):
    """
    字符串转List(int)
    :param strList:
    :return:
    """
    intList = [int(s) for s in strList]
    return intList

def str2ts(dts, format='%Y-%m-%d %H:%M'):
    """
    字符串转时间戳（带格式）
    :param dts:
    :param format:
    :return:
    """
    return time.mktime(time.strptime(dts, format))

def ts2str(ts, format='%Y-%m-%d %H:%M'):
    """
    时间戳转字符串（带格式）
    :param ts:
    :param format:
    :return:
    """
    return time.strftime(format, time.localtime(ts))

def sxml2dict(sxml):
    """
    xml转数据字典dict{}
    :param sxml:
    :return:
    """
    redict = {}
    root = ET.fromstring(sxml)
    # print root.find("Content").text
    for child in root:
        value = child.text
        redict[child.tag] = value
    return redict

def dict2sxml(obj):
    """
    字典转xml
    :param obj:
    :return:
    """
    xml = ["<xml>"]
    for k, v in obj.iteritems():
        if v.isdigit():
            xml.append("<{0}>{1}</{0}>".format(k, v))
        else:
            xml.append("<{0}><![CDATA[{1}]]></{0}>".format(k, v))
    xml.append("</xml>")
    return "".join(xml)

def group(lst, block):
    """
    list分组
    :param lst:list
    :param block:步进
    :return:
    """
    return [lst[i:i + block] for i in range(0, len(lst), block)]

def importName(modulename, name):
    """
    加载包
    :param modulename:
    :param name:
    :return:
    """
    try:
        module = __import__(modulename, fromlist=[name])
    except ImportError, e:
        print 'import', modulename, name, e
    return getattr(module, name)

def randomList(num, docs):
    """
    list乱序
    :param num:
    :param docs:
    :return:
    """
    rid = []
    for i in range(len(docs)):
        r = random.randrange(0, len(docs))
        if r not in rid:
            rid.append(r)
    return [docs[j] for j in rid[:num]]

def createNoncestr(length=8, chars=string.letters + string.digits):
    """
    生成字母数字随机字符串
    :param length:
    :param chars: 默认26个大小写字母以及数字
    :return:
    """
    return ''.join(random.choice(chars) for _ in range(length))


def createLinkString(parameter):
    """
    生成url参数字符串(不带url转义）
    :param parameter:
    :return:
    """
    parameter = parameter.items()
    parameter.sort()
    return '&'.join(["%s=%s" % (k, str(v)) for k, v in parameter])

def createLinkstringUrlencode(parameter):
    """
    生成url参数字符串(带url转义）
    :param parameter:
    :return:
    """
    parameter = parameter.items()
    parameter.sort()
    kvList = [(k, urllib.quote(str(v).encode('utf-8'))) for k, v in parameter]
    return '&'.join(["%s=%s" % (k, str(v)) for k, v in kvList])

def httpGet(url, param):
    """
    request get
    :param url:
    :param param:
    :return:json
    """
    resp = requests.get(url, param)
    return resp.json()

def httpPost(url, param):
    """
    request post
    :param url:
    :param param:
    :return:json
    """
    resp = requests.post(url, param)
    return resp.json()

def multiGetLetter(str_input):
    """
    获取字符串首字母
    :param str_input:
    :return:
    """
    # 判断str_input是否是unicode类型的
    if isinstance(str_input, unicode):
        unicode_str = str_input
    else:
        # 转化成unicode类型的
        try:
            unicode_str = str_input.decode('utf8')
        except:
            try:
                unicode_str = str_input.decode('gbk')
            except:
                print 'unknown coding'
                return ""

    return_list = ""
    for one_unicode in unicode_str:
        return_list += (singleGetFirst(one_unicode))
    return return_list

def singleGetFirst(one_unicode):
    """
    获取字符首字母
    :param one_unicode:
    :return:
    """
    str1 = one_unicode.encode('gbk')
    try:
        # 将字符或布尔类型转成ascll码 如果转化出错则是中文 否则就是字母 直接输出
        ord(str1)
        return str1
    except:
        print str1[0]
        asc = ord(str1[0]) * 256 + ord(str1[1]) - 65536
        if asc >= -20319 and asc <= -20284:
            return 'a'
        if asc >= -20283 and asc <= -19776:
            return 'b'
        if asc >= -19775 and asc <= -19219:
            return 'c'
        if asc >= -19218 and asc <= -18711:
            return 'd'
        if asc >= -18710 and asc <= -18527:
            return 'e'
        if asc >= -18526 and asc <= -18240:
            return 'f'
        if asc >= -18239 and asc <= -17923:
            return 'g'
        if asc >= -17922 and asc <= -17418:
            return 'h'
        if asc >= -17417 and asc <= -16475:
            return 'j'
        if asc >= -16474 and asc <= -16213:
            return 'k'
        if asc >= -16212 and asc <= -15641:
            return 'l'
        if asc >= -15640 and asc <= -15166:
            return 'm'
        if asc >= -15165 and asc <= -14923:
            return 'n'
        if asc >= -14922 and asc <= -14915:
            return 'o'
        if asc >= -14914 and asc <= -14631:
            return 'p'
        if asc >= -14630 and asc <= -14150:
            return 'q'
        if asc >= -14149 and asc <= -14091:
            return 'r'
        if asc >= -14090 and asc <= -13119:
            return 's'
        if asc >= -13118 and asc <= -12839:
            return 't'
        if asc >= -12838 and asc <= -12557:
            return 'w'
        if asc >= -12556 and asc <= -11848:
            return 'x'
        if asc >= -11847 and asc <= -11056:
            return 'y'
        if asc >= -11055 and asc <= -10247:
            return 'z'
        return ''

def uriEncode(url):
    """
    uri encode
    :param url:
    :return:
    """
    return urllib.quote(url)

def uriDecode(url):
    """
    uri decode
    :param url:
    :return:
    """
    return urllib.unquote(url)