# coding:utf-8
"""
Created on 2017-02-23

@author: ysw
"""

import web
from module import base, tools

session = web.config._session
render = base.render(__file__, "static_demo")


class Bootstrap:
    """
    Bootstrap
    GET()

    """

    def GET(self):
        return render.plugins_by_other_demo()