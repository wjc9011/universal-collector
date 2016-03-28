# -*- coding: utf-8 -*-
# jw范采集
# coded by Junchao
# www.junchaowang.com
import urllib2, re
from bs4 import BeautifulSoup
import jieba
import jieba.analyse
import random

def jwfcj(target_url):

    html_doc = urllib2.urlopen(target_url).read()
    soup = BeautifulSoup(html_doc, "html5lib")
    pre_title = unicode(soup.title.string)

    if pre_title.find('|') != -1:
        pre_title = pre_title.split('|')
    elif pre_title.find('_') != -1:
        pre_title = pre_title.split('_')
    else:
        pre_title = pre_title.split('-')

    title_length = 0
    for each_pre_title in pre_title:
        if len(each_pre_title) > title_length:
            pre_title = each_pre_title
            title_length = len(each_pre_title)
        else:
            pass
                
    pre_content = soup.get_text()
    pre_content = re.findall(u"[\u4e00-\u9fa5]+[\u3000-\u303f\ufb00-\ufffd]+", pre_content)
    pre_content_full = ''
    for each_pre_content in pre_content:

        if len(each_pre_content) > 5:
            if random.random() > 0.9:
                pre_content_full = pre_content_full + '<br />' + each_pre_content
            else:
                pre_content_full = pre_content_full + each_pre_content


    return [pre_title, pre_keywords, pre_content_full]


