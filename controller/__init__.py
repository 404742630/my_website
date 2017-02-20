# coding:utf-8
"""
Created on 2017-02-16

@author: ysw
"""

import os

urls = []

for f in os.listdir(os.path.split(__file__)[0]):
    module_name, ext = os.path.splitext(f)
    if ext == '':
        module = __import__(__name__ + '.' + module_name, fromlist=module_name)
        urls.append("/" + module_name)
        urls.append(module.app)

