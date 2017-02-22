# coding:utf-8
"""
Created on 2017-02-22

@author: ysw
"""

pre = __name__[:__name__.find('.', 11, -1) + 1]

urls = [
    "/index",           pre + "cube.Index",
    "/magicCubeModel",  pre + "cube.MagicCubeModel"
]