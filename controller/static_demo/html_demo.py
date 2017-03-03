# coding:utf-8
"""
Created on 2017-02-23

@author: ysw
"""

import web
from module import base, tools

session = web.config._session
render = base.render(__file__, "static_demo")


class PluginsByOthers:
    """
    PluginsByOthers
    GET()

    """

    def GET(self):
        return render.plugins_by_other_demo()


class PluginsByMe:
    """
    PluginsByMe
    GET()

    """

    def GET(self):
        return render.plugins_by_me_demo()