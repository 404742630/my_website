# coding:utf-8
"""
Created on 2017-02-16

@author: ysw
"""

import web
import urls
from module import interceptors


def interceptor():
    interceptors.interceptorHook(urls.interceptors)

app = web.application(urls.urls, locals())
app.add_processor(web.loadhook(interceptor))