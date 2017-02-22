# coding:utf-8
"""
Created on 2017-02-22

@author: ysw
"""

class MultiDimension:
    """
    多维模型
    @length: 长
    @width: 宽
    @height: 高
    @obj: 存入的数据
    """

    def __init__(self, length, width, height, obj=None):
        self.length = length
        self.width = width
        self.height = height
        self.set_dict(obj)

    def set_dict(self, obj=None):
        for l in xrange(self.length):
            dict_temp = {}
            for w in xrange(self.width):
                dict_temp_ = {}
                for h in xrange(self.height):
                    dict_temp_[h] = obj
                dict_temp[w] = dict_temp_
            self.multi_d[l] = dict_temp

    def get_dict(self):
        return self.multi_d


class Cube(MultiDimension):
    """
    方块
    @color: 方块各个面的颜色
    """

    def __init__(self, color={}, length=1, width=1, height=1):
        self.color = {
            'U': '',
            'D': '',
            'R': '',
            'L': '',
            'F': '',
            'B': ''
        }
        self.set_color(color)
        MultiDimension.__init__(length, width, height, self.color)

    def set_color(self, color):
        for c in color:
            self.color[c] = color[c]

    def get_color(self):
        return self.color