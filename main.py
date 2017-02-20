# coding:utf-8
"""
Created on 2017-02-16

@author: ysw
"""

import web

web.config.debug = True
web.config.session_parameters.timeout = 6000

import controller as ctrl

urls = ctrl.urls

app = web.application(urls, globals())

if web.config.get("_session") is None:
    web.config._session = web.session.Session(app, web.session.DiskStore("sessions"), {"count": 0})

if __name__ == "__main__":
    app.run()
