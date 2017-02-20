# coding:utf-8
"""
Created on 2017-02-16

@author: ysw
"""

import os
import web

import json
import time
import config
import filter
from web.contrib.template import render_jinja

error_disc = config.error


def rtJson(code=200, **args):
    """
    return json
    :param code: 错误码
    :param args: 其他参数
    :return:
    """
    return json.dumps({
        'status': code,
        'message': error_disc.get(code),
        'data': args
    })

def rtStr(code=200, _str=""):
    """
    return _str
    :param code:
    :return:
    """
    return _str if code == 200 else ("error|" + error_disc.get(code))

def page(total_num, page_num=1, page_size=20):
    """
    分页
    :param total_num: 记录总数
    :param page_num: 请求页码
    :param page_size: 每页的记录数
    :return: pager 分页数据包
    """
    total_page = (total_num / page_size + 1) if total_num % page_size != 0 else (total_num / page_size)
    pager = {
        'total_num': total_num,
        'page_num': page_num,
        'page_size': page_size,
        'total_page': total_page,  # 总页数
        'start': (page_num - 1) * page_size,
        'end': page_num * page_size - 1
    }
    return pager

def pageForList(data, page_num=1, page_size=20):
    """
    列表数据分页
    :param data:
    :param page_num:
    :param page_size:
    :return:
    """
    pager = page(len(data), page_num, page_size)
    lis_data = data[pager['start']:pager['end'] + 1]
    return lis_data, pager

def notFound():
    """
    404错误处理
    :return:
    """
    return web.notfound(render('framework').notfound())

def internalError():
    """
    500内部错误处理
    :return:
    """
    return web.internalerror(render('framework').internalerror())

def render(module_path, parent=''):
    """
    自定义渲染渲染
    :param module_path: 当前的文件名
    :param parent: 当前文件的父文件名
    :return:
    """
    cfg = config.cfg
    cfg['debug'] = 1 if web.config.debug else 0
    cfg['vt'] = config.vesion if config.run_mode in ["deploy"] else int(time.time())

    tempath = os.path.split(module_path)[1].replace('.pyc', '').replace('.py', '')
    render = render_jinja(['view/', 'view/' + parent + "/" + tempath], encoding='utf-8')
    render._lookup.globals.update(session=web.config._session, cfg=cfg)
    render._lookup.filters.update(filter.filters)

    return render