# coding:utf-8
"""
Created on 2017-02-16

@author: ysw
"""

import os

urls = []
INTERCEPTOR = 'interceptor:'
global_interceptors = []
interceptors = {}

for f in os.listdir(os.path.split(__file__)[0]):
    module_name, ext = os.path.splitext(f)
    if module_name.startswith('url_') and ext == '.py':
        module = __import__(__name__ + '.' + module_name, fromlist=module_name)
        for i, url in enumerate(module.urls):
            if url.startswith(INTERCEPTOR):
                # 如果是拦截器 则把拦截器添加到对应位置的拦截器列表
                interceptors[module.urls[i - 2]] = interceptors[module.urls[i - 2]] + url.replace(INTERCEPTOR, '').split(',')
            else:
                # 如不是拦截器配置，则加进urls
                urls.append(url)
                if url.startswith('/'):
                    interceptors[url] = global_interceptors + module.local_interceptor