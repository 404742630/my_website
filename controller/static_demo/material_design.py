# coding:utf-8
"""
Created on 2017-03-02

@author: ysw
"""

import web
from module import base, tools

session = web.config._session
render = base.render(__file__, "static_demo")


class DashBoard:
    """
    仪表盘
    GET()

    """

    def GET(self):
        return render.dash_board()