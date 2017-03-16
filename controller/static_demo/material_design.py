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
        data = web.input()
        type = data.get("type", "1")
        dist_render = {
            "1": render.dash_board(),
            "2": render.dash_board_advanced()
        }
        return dist_render[type]