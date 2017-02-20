# coding:utf-8
"""
Created on 2017-02-16

@author: ysw
"""

import web
import urls

app = web.application(urls.urls, locals())