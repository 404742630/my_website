# coding:utf-8
"""
Created on 2017-02-16

@author: ysw
"""

import web
from module import base, tools

session = web.config._session
render = base.render(__file__, "curriculum_vitae")


class Index:
    """
    简历主页
    GET()

    """

    def GET(self):
        return render.index()