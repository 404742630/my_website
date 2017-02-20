# coding:utf-8
"""
Created on 2017-02-16

@author: ysw
"""

from module import tools


class InterceptorChain:

    def __init__(self, interceptors=[]):
        self.interceptors = interceptors
        self.interceptors.reverse()

    def do(self):
        if len(self.interceptors):
            interceptor = self.interceptors.pop()
            # 拦截器的地址
            module_name = 'module.interceptors.'
            name = interceptor
            # 加载拦截器
            handler_class = tools.importName(module_name, name)
            # 执行
            handler_class(self.do)