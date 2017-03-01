# coding:utf-8
"""
Created on 2017-02-16

@author: ysw
"""

import os
import yaml

os_path = os.path.split(__file__)[0]
abs_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/db_sqlite"

run_mode = os.environ.get("RUN_ENV", "local")

db_filename = {
    "local": os.path.join(abs_path, "db_local.sqlite3"),
    "test": os.path.join(abs_path, "db_test.sqlite3"),
    "deploy": os.path.join(abs_path, "db_deploy.sqlite3"),
}[run_mode]

cfg = yaml.load(file(os_path + "/cfg.yml", "r"))[run_mode]

srv = yaml.load(file(os_path + "/srv.yml", "r"))[run_mode]

error = yaml.load(file(os_path + "/error.yml", "r"))

vesion = "0.0.3"