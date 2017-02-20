# coding:utf-8
"""
Created on 2017-02-16

@author: ysw
"""

import os

urls = []

for f in os.listdir(os.path.split(__file__)[0]):
    module_name, ext = os.path.splitext(f)
    if module_name.startswith('url_') and ext == '.py':
        module = __import__(__name__ + '.' + module_name, fromlist=module_name)
        for i, url in enumerate(module.urls):
            urls.append(url)