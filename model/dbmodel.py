# coding:utf-8
"""
Created on 2017-02-16

@author: ysw
"""

from pony.orm import *
import config

db = Database()



db.bind('sqlite', config.db_filename, create_db=True)

if __name__ == "__main__":
    db.generate_mapping(check_tables=True, create_tables=True)
else:
    db.generate_mapping(check_tables=True, create_tables=False)