# coding:utf-8
"""
Created on 2017-02-16

@author: ysw
"""

import re
import web
from model import interceptor

def interceptorHook(interceptor_stack):
    """
    拦截器钩子hook
    :param interceptor_stack:
    :return:
    """
    path = web.ctx.path
    interceptors = interceptor_stack.get(path)
    if interceptors is None:
        for k in interceptor_stack:
            if re.match('^' + k + '$', path):
                interceptors = interceptor_stack[k]
                break

    if interceptors is None:
        raise web.notfound()
    else:
        chain = interceptor.InterceptorChain(interceptors[:])
    result = chain.do()
    return result