# coding:utf-8
"""
Created on 2017-02-22

@author: ysw
"""

import web
from module import base, tools

session = web.config._session
render = base.render(__file__, "magic_cube")


class Index:
    """
    魔方主页
    GET()

    """

    def GET(self):
        pass


class MagicCubeModel:
    """
    魔方模型
    GET()

    """

    def GET(self):
        pass