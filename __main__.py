# -*- codeing:utf-8 -*-
# __author__ = 'Buguin'
import os

from toolkits.common.control import Control

if __name__ == '__main__':
    configpath = os.getcwd() + "\scripts\config.xml"
    control = Control(configpath)
    control.run()
